#!/usr/bin/env python3
"""
BigQuery Bridge — Expõe dados do BigQuery como API HTTP
Roda no PC, Hermes (VPS) acessa via HTTP
"""

from flask import Flask, jsonify, request
from google.cloud import bigquery
import logging
import os
from datetime import datetime

# Config
PORT = int(os.getenv("BRIDGE_PORT", "5000"))
PROJECT_ID = os.getenv("GCP_PROJECT_ID", "aloud-rox")
DATASET_ID = os.getenv("GCP_DATASET_ID", "alouddatamarket")

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Inicializa BigQuery client
try:
    client = bigquery.Client(project=PROJECT_ID)
    logger.info(f"✅ BigQuery conectado: {PROJECT_ID}")
except Exception as e:
    logger.error(f"❌ Erro ao conectar BigQuery: {str(e)}")
    client = None

# ============================================================================
# ENDPOINTS
# ============================================================================

@app.route("/health", methods=["GET"])
def health():
    """Health check"""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "project": PROJECT_ID,
        "dataset": DATASET_ID
    })

@app.route("/krakens/hoje", methods=["GET"])
def krakens_hoje():
    """
    Relatório do time de hoje
    Retorna: GBV, Meta%, Ticket, FTR, Ligações, Meetings por vendedor
    """
    if not client:
        return jsonify({"error": "BigQuery não conectado"}), 500
    
    query = f"""
    SELECT
        vendedor,
        COUNT(DISTINCT lead_id) as leads,
        SUM(gbv) as gbv,
        AVG(ticket) as ticket_medio,
        AVG(ftr_minutos) as ftr_medio,
        COUNT(DISTINCT CASE WHEN tipo='ligacao' THEN 1 END) as ligacoes,
        COUNT(DISTINCT CASE WHEN tipo='meeting' THEN 1 END) as meetings,
        COUNT(DISTINCT CASE WHEN status='fechado' THEN 1 END) as fechamentos,
        ROUND(100.0 * COUNT(DISTINCT CASE WHEN status='fechado' THEN 1 END) / 
              NULLIF(COUNT(DISTINCT lead_id), 0), 2) as taxa_conversao_pct
    FROM `{PROJECT_ID}.{DATASET_ID}.krakens_leads`
    WHERE DATE(data_criacao) = CURRENT_DATE()
    GROUP BY vendedor
    ORDER BY gbv DESC
    """
    
    try:
        query_job = client.query(query)
        results = query_job.result()
        
        data = []
        for row in results:
            data.append({
                "vendedor": row.vendedor,
                "leads": int(row.leads),
                "gbv": float(row.gbv or 0),
                "ticket_medio": float(row.ticket_medio or 0),
                "ftr_minutos": float(row.ftr_medio or 0),
                "ligacoes": int(row.ligacoes or 0),
                "meetings": int(row.meetings or 0),
                "fechamentos": int(row.fechamentos or 0),
                "taxa_conversao_pct": float(row.taxa_conversao_pct or 0)
            })
        
        logger.info(f"✅ Query /krakens/hoje: {len(data)} vendedores")
        return jsonify({
            "timestamp": datetime.now().isoformat(),
            "data": data,
            "total_gbv": sum(d["gbv"] for d in data)
        })
        
    except Exception as e:
        logger.error(f"Erro em /krakens/hoje: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/krakens/funil", methods=["GET"])
def krakens_funil():
    """
    Distribuição do funil por etapa
    S1=Abertura, S2-S5=Conversão, S6-S7=Fechamento, S8-S9=Encerrado
    """
    if not client:
        return jsonify({"error": "BigQuery não conectado"}), 500
    
    query = f"""
    SELECT
        stage,
        COUNT(*) as quantidade,
        ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) as percentual
    FROM `{PROJECT_ID}.{DATASET_ID}.krakens_leads`
    WHERE DATE(data_atualizacao) >= CURRENT_DATE() - 1
    GROUP BY stage
    ORDER BY stage
    """
    
    try:
        query_job = client.query(query)
        results = query_job.result()
        
        data = []
        for row in results:
            data.append({
                "etapa": row.stage,
                "quantidade": int(row.quantidade),
                "percentual": float(row.percentual)
            })
        
        logger.info(f"✅ Query /krakens/funil: {len(data)} etapas")
        return jsonify({"data": data})
        
    except Exception as e:
        logger.error(f"Erro em /krakens/funil: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/krakens/vendedor/<vendedor>", methods=["GET"])
def krakens_vendedor(vendedor):
    """
    Performance individual de um vendedor
    """
    if not client:
        return jsonify({"error": "BigQuery não conectado"}), 500
    
    query = f"""
    SELECT
        vendedor,
        COUNT(DISTINCT lead_id) as leads,
        SUM(gbv) as gbv,
        AVG(ticket) as ticket_medio,
        AVG(ftr_minutos) as ftr_medio,
        COUNT(DISTINCT CASE WHEN tipo='ligacao' THEN 1 END) as ligacoes,
        COUNT(DISTINCT CASE WHEN status='fechado' THEN 1 END) as fechamentos
    FROM `{PROJECT_ID}.{DATASET_ID}.krakens_leads`
    WHERE vendedor = @vendedor AND DATE(data_criacao) >= CURRENT_DATE() - 7
    GROUP BY vendedor
    """
    
    try:
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("vendedor", "STRING", vendedor)
            ]
        )
        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        
        row = list(results)[0] if results.total_rows > 0 else None
        
        if not row:
            return jsonify({"error": f"Vendedor {vendedor} não encontrado"}), 404
        
        data = {
            "vendedor": row.vendedor,
            "leads_7dias": int(row.leads),
            "gbv_7dias": float(row.gbv or 0),
            "ticket_medio": float(row.ticket_medio or 0),
            "ftr_minutos": float(row.ftr_medio or 0),
            "ligacoes": int(row.ligacoes or 0),
            "fechamentos": int(row.fechamentos or 0)
        }
        
        logger.info(f"✅ Query /krakens/vendedor/{vendedor}")
        return jsonify(data)
        
    except Exception as e:
        logger.error(f"Erro em /krakens/vendedor/{vendedor}: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/krakens/conversas", methods=["GET"])
def krakens_conversas():
    """
    Últimas conversas (pra análise qualitativa SCOPE CODEX)
    """
    if not client:
        return jsonify({"error": "BigQuery não conectado"}), 500
    
    limit = request.args.get("limit", default=10, type=int)
    
    query = f"""
    SELECT
        lead_id,
        vendedor,
        timestamp,
        tipo_mensagem,
        conteudo,
        duracao_audio_seg
    FROM `{PROJECT_ID}.{DATASET_ID}.krakens_conversas`
    ORDER BY timestamp DESC
    LIMIT @limit
    """
    
    try:
        job_config = bigquery.QueryJobConfig(
            query_parameters=[
                bigquery.ScalarQueryParameter("limit", "INT64", limit)
            ]
        )
        query_job = client.query(query, job_config=job_config)
        results = query_job.result()
        
        data = []
        for row in results:
            data.append({
                "lead_id": row.lead_id,
                "vendedor": row.vendedor,
                "timestamp": str(row.timestamp),
                "tipo": row.tipo_mensagem,
                "conteudo": row.conteudo,
                "duracao_audio_seg": int(row.duracao_audio_seg or 0)
            })
        
        logger.info(f"✅ Query /krakens/conversas: {len(data)} registros")
        return jsonify({"data": data})
        
    except Exception as e:
        logger.error(f"Erro em /krakens/conversas: {str(e)}")
        return jsonify({"error": str(e)}), 500

# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    logger.info(f"🚀 BigQuery Bridge iniciado")
    logger.info(f"   Projeto: {PROJECT_ID}")
    logger.info(f"   Dataset: {DATASET_ID}")
    logger.info(f"   Porta: {PORT}")
    logger.info(f"   URL: http://localhost:{PORT}")
    logger.info(f"\n   Endpoints:")
    logger.info(f"   - GET /health")
    logger.info(f"   - GET /krakens/hoje")
    logger.info(f"   - GET /krakens/funil")
    logger.info(f"   - GET /krakens/vendedor/<nome>")
    logger.info(f"   - GET /krakens/conversas?limit=10")
    
    app.run(host="0.0.0.0", port=PORT, debug=False)


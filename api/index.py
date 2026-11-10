"""
Ponto de entrada da função Python na Vercel.

Reaproveita o app Flask de HDR/app.py (o mesmo usado localmente com
`python HDR/app.py`). O vercel.json redireciona POST /process para cá.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "HDR"))

from app import app, process  # noqa: E402

# Garante que a rota responda qualquer que seja o caminho repassado pela Vercel.
app.add_url_rule("/api", "process_api_root", process, methods=["POST"])
app.add_url_rule("/api/index", "process_api_index", process, methods=["POST"])
app.add_url_rule("/api/process", "process_api", process, methods=["POST"])


@app.route("/api/health")
def health():
    return {"status": "ok"}

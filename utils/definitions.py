import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

ROOT_PATH = "/api"
ENV_PATH = os.path.join(ROOT_DIR, ".env")

OK_RESP = {"code": 0, "msg": "Successful response"}

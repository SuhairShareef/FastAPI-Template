from fastapi import FastAPI

from utils.definitions import ROOT_PATH
from settings import APP_NAME

app = FastAPI(
    title=f"{APP_NAME.capitalize()} API",
    openapi_url=ROOT_PATH + "/openapi.json",
    redoc_url=ROOT_PATH + "/redoc",
    docs_url=ROOT_PATH + "/docs",
    swagger_ui_oauth2_redirect_url=ROOT_PATH + "/docs/oauth2-redirect",
)

# Add your routes here
# using app.include_router()

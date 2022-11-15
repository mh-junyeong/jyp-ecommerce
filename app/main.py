from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/index.html")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("index.html", context)


@app.get("/login.html")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("login.html", context)


@app.get("/product-details.html")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("product-details.html", context)


@app.get("/shop.html")
def index(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("shop.html", context)


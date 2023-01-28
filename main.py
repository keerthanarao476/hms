from fastapi.params import Form
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import starlette.status as status
from starlette.responses import RedirectResponse, Response  
from dbcontroller import DBController

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),"static")

templates = Jinja2Templates("templates")

db = DBController("app.db")

@app.get("/", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})

@app.post("/",response_class=HTMLResponse)
def index_post(request:Request, email:str = Form(...), password:str=Form(...)):
    row = db.executeQueryWithParams("select * from login where email = ? and password = ?",[email,password])
    if(len(row)==0):
        return templates.TemplateResponse ("login.html",{"request":request, "msg":"invalid email and password" })
    return RedirectResponse("/appointment",status_code=status.HTTP_302_FOUND)
    
@app.get("/login", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})


@app.get("/dashboard", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("dashboard.html",{"request":request})
    
@app.get("/appointment", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("appointment.html",{"request":request})

@app.get("/contact", response_class=HTMLResponse)
def index(request:Request):
    return templates.TemplateResponse("contact.html",{"request":request})
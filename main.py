from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routes import auth, users, medicine, patient, industry, progress_note,qrcode
from dotenv import dotenv_values
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
config = dotenv_values(".env")

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.get("/patient-info", response_class=HTMLResponse)
async def user_profile(request: Request):
    return templates.TemplateResponse("patient_info.html", {"request": request})

@app.get("/user", response_class=HTMLResponse)
async def user_profile(request: Request):
    
    return templates.TemplateResponse("user.html", {"request": request})

@app.get("/medical-summary", response_class=HTMLResponse)
async def medical_summary(request: Request):
    return templates.TemplateResponse("medical_summary.html", {"request": request})

@app.get("/search-patient", response_class=HTMLResponse)
async def search_patient(request: Request):
    return templates.TemplateResponse("search_patient.html", {"request": request})

@app.get("/prescriptions", response_class=HTMLResponse)
async def medical_summary(request: Request):
    return templates.TemplateResponse("prescriptions.html", {"request": request})


@app.get("/vaccinations", response_class=HTMLResponse)
async def medical_summary(request: Request):
    return templates.TemplateResponse("vaccination.html", {"request": request})


@app.get("/doc_notes", response_class=HTMLResponse)
async def medical_summary(request: Request):
    return templates.TemplateResponse("doc_notes.html", {"request": request})


@app.get("/usershare/{uid}", response_class=HTMLResponse)
async def medical_summary(uid:str,request:Request):
    return templates.TemplateResponse("uid_profile.html", {"request": request,"uid":uid})





#Connecting to patient Database
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["DATABASE_URL"])
    app.database = app.mongodb_client[config["MONGO_INITDB_DATABASE"]]

app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(users.router, tags=['Users'], prefix='/api/users')
app.include_router(patient.router, tags=["patient"], prefix="/api/patient")
app.include_router(medicine.router, tags=["medicine"], prefix="/api/medicine")
app.include_router(industry.router, tags=["industry"], prefix="/api/industry")
app.include_router(progress_note.router, tags=["progress-note"], prefix="/api/progress-note")
app.include_router(qrcode.router, tags=["qrcode"], prefix="/api/qrcode")
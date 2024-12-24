from fastapi import FastAPI, status, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from util.config import settings

print("Loading DataBase ...")
from util.db import start_db_data
start_db_data()
print("DataBase loaded!")

security = HTTPBasic()
def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != settings.API2_USERNAME or credentials.password != settings.API2_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

def verify_basic_auth_admin(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != settings.API2_USERNAME or credentials.password != settings.API2_ADM_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

app = FastAPI(
    title=settings.API2_NAME,
    version=settings.API2_VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK, tags=['root'])
def read_root():
    return {"apiName": settings.API2_NAME, "version": settings.API2_VERSION}

from endpoints import air_route, admin

app.include_router(air_route.router, prefix="/air-route", tags=['air-route'], dependencies=[Depends(verify_basic_auth)])
app.include_router(admin.router, prefix="/admin", tags=['admin'], dependencies=[Depends(verify_basic_auth_admin)])

import os
from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

templates = Jinja2Templates(directory="client/public")
templates.env.globals["STATIC_URL"] = "/client/public"

class Login(BaseModel):
    clientId: str
    passcode: any
class CustomFastAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super(CustomFastAPI, self).__init__(*agrs, **kwargs)
        self.base_url = None
        self.resource_url = None
    def load_yaml(self):
        with open('application.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

app = CustomFastAPI()
app.mount("/client/public", StaticFiles(directory=os.path.join(BASE_DIR, "client/public")), 
name="client/pulbic")

@app.get("/")
async def root(request : Request):
    return templates.TemplateResponse('index.html', context={"request":request})

@app.post("/api/new/auth/client/login")
async def login(login: Login):
    print(f"{login.clientId}")
    params = login.dict()
    print(f"clientId: {params['clientId']}, passcode: {params['passcode']}")
    return login


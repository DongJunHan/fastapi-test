import os
from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import yaml
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
class Login(BaseModel):
    clientId: str
    passcode: str
class CustomFastAPI(FastAPI):
    def __init__(self, *args, **kwargs):
        super(CustomFastAPI, self).__init__(*args, **kwargs)
        self.base_url = None
        self.resource_path = None
        self.get_yaml_data()
    def load_yaml(self):
        with open('application.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_yaml_data(self):
        yaml_data = self.load_yaml()
        self.base_url = yaml_data['base_url']
        self.resource_path = yaml_data['resource_path']

app = CustomFastAPI()

templates = Jinja2Templates(directory=app.resource_path)
templates.env.globals["STATIC_URL"] = "/"+app.resource_path

app.mount("/"+app.resource_path, StaticFiles(directory=os.path.join(BASE_DIR, app.resource_path)), 
name=app.resource_path)

@app.get("/")
async def root(request : Request):
    return templates.TemplateResponse('index.html', context={"request":request})

@app.post("/api/new/auth/client/login")
async def login(login: Login):
    print(f"{login.clientId}")
    params = login.dict()
    print(f"clientId: {params['clientId']}, passcode: {params['passcode']}")
    return login


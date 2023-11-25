from fastapi import FastAPI

app = FastAPI()


@app.post('/login')
async def login(login_schema: dict):
    return login_schema['id']

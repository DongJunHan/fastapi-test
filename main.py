from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException

from pydantic import BaseModel

app = FastAPI()


class LoginSchema(BaseModel):
    id: str
    password: str


@app.post('/login', status_code=status.HTTP_200_OK)
async def login(login_schema: LoginSchema):
    if not (login_schema.id == 'asdf' and login_schema.password == 'zxcv'):
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            detail="please right id or password")
    return login_schema.id

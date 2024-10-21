from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrapping.script_abes import update_data_abes

app = FastAPI()

class PasswordRequest(BaseModel):
    password: str

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.post('/ingest')
def update_data(password_request: PasswordRequest):
    if password_request.password == "s3cr3t":  # Verifique a senha
        update_data_abes()
        return {'message': 'Data updated successfully'}
    else:
        raise HTTPException(status_code=403, detail="Forbidden: Incorrect password")
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrapping.script_abes import update_data_abes
from database_utils.db import get_dict_abes_scrapping, get_dict_br_versus_la

app = FastAPI()


class PasswordRequest(BaseModel):
    password: str


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/abes/table')
def get_table_abes_scrapping():
    return get_dict_abes_scrapping()


@app.get('/abes/pizza/br_la')
def get_pizza_br_x_la():
    return get_dict_br_versus_la()


@app.post('/abes/ingest')
def update_abes_data(password_request: PasswordRequest):
    if password_request.password == 's3cr3t':  # Verifique a senha
        update_data_abes()
        return {'message': 'Data updated successfully'}
    else:
        raise HTTPException(
            status_code=403, detail='Forbidden: Incorrect password'
        )

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrapping.script_abes import update_data_abes
from database_utils.db import (
    get_dict_abes_scrapping,
    get_dict_br_versus_la,
    get_dict_br_positions,
    get_dict_br_versus_world,
)
from services.abes_service import (
    format_pizza_br_x_la,
    format_bars_br_x_world,
    format_lines_br_position,
)

app = FastAPI()


class PasswordRequest(BaseModel):
    password: str


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/abes/table')
def get_table_abes_scrapping():
    """
    Get all data from abes scrapping in the formate of HTML Table
    """
    return get_dict_abes_scrapping()


@app.get('/abes/pizza/br_la')
def get_pizza_br_x_la():
    """
    Get Brazil and Latin America's investment values along the years in the format of Pizza Graph in ChartJS
    """
    db_response = get_dict_br_versus_la()
    return format_pizza_br_x_la(db_response)


@app.get('/abes/bars/br_world')
def get_bars_br_x_world():
    """
    Get Brazil and World's investment values along the years in the format of Bars Graph in ChartJS
    """
    db_response = get_dict_br_versus_world()
    return format_bars_br_x_world(db_response)


@app.get('/abes/line/br_position')
def get_line_br_position():
    """
    Get Brazil positions along the years in the format of Line Graph in ChartJS
    """
    db_response = get_dict_br_positions()
    return format_lines_br_position(db_response)


@app.post('/abes/ingest')
def update_abes_data(password_request: PasswordRequest):
    """
    Ingest abes webscrapping and data
    """
    if password_request.password == 's3cr3t':  # Verifique a senha
        update_data_abes()
        return {'message': 'Data updated successfully'}
    else:
        raise HTTPException(
            status_code=403, detail='Forbidden: Incorrect password'
        )

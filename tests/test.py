import pytest
from fastapi.testclient import TestClient

from llm.utils import create_dict_analise_investimento_ti
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'Hello': 'World'}


def test_get_table_abes_scrapping():
    response = client.get('/abes/table')
    assert response.status_code == 200

    data = response.json()

    assert data[0] == {
        'brazil_movement': '$45.2B',
        'brazil_position': '12',
        'latin_america_investment': '$124B',
        'global_investment': '$3.11T',
        'study_year': '2022',
        'investment_sectors': '5G, Cibersegurança, IoT',
        'created_at': '2024-10-21T14:10:55.957000',
    }

    assert data[-1] == {
        'brazil_movement': '$5.98B',
        'brazil_position': '15',
        'latin_america_investment': 'Not Informed',
        'global_investment': '$1T',
        'study_year': '2004',
        'investment_sectors': 'software, services',
        'created_at': '2024-10-21T14:10:55.957000',
    }


def test_llm_resume():
    string_text = """
    Mercado Brasileiro de Software – Panorama e Tendências / edição 2008
    Dados consolidados de 2007

    Em 2007, o mercado nacional de software e serviços voltou à posição que ocupava 2005 no cenário mundial, a 12ª. O setor movimentou cerca de US$ 11,12 bilhões, um aumento de 22,3% em relação ao ano anterior. Desse total, US$ 4,19 bilhões referem-se a softwares, o que representa 1,6% do mercado mundial, e US$ 6,93 bilhões dizem respeito a serviços.

    O mercado mundial de Tecnologia da Informação movimentou cerca de US$ 1,3 trilhão e o latino-americano US$ 47,7 bilhões. Nesse contexto, o Brasil correspondeu a 43,4%.

    """
    data = create_dict_analise_investimento_ti(string_text)

    assert data['brazil_movement'] == '$11.12B'
    assert data['brazil_position'] == '12'
    assert data['latin_america_investment'] == '$47.7B'
    assert data['global_investment'] == '$1.3T'
    assert data['study_year'] == '2007'

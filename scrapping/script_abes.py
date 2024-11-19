from llm.utils import create_dict_analise_investimento_ti
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import database_utils.db as db

url_abes = 'https://abes.com.br/dados-do-setor/'
root_str = 'et_pb_toggle_'
not_formatted = [9, 10, 11, 18]


def get_text_abes_website():
    return requests.get(url_abes).text


def update_data_abes():
    soup = BeautifulSoup(get_text_abes_website(), 'html.parser')
    estudos = soup.find('div', {'class': 'et_pb_column_4'})
    time_now = datetime.now()
    list_dict = []

    for i in range(6, 25):
        if i in not_formatted:
            continue

        string_final = ''
        for tag in estudos.find(
            'div', {'class': root_str + str(i)}
        ).descendants:
            if tag.name != 'p':
                continue
            if not tag.get_text().strip():
                continue

            string_final += ' ' + tag.get_text()
        dict_data = create_dict_analise_investimento_ti(string_final)
        dict_data['created_at'] = time_now
        list_dict.append(dict_data)

    for item in not_formatted:
        string_final = ''
        for tag in estudos.find(
            'div', {'class': root_str + str(item)}
        ).descendants:
            if not tag.name:
                continue
            if not tag.get_text().strip():
                continue

            string_final += ' ' + tag.get_text()
        dict_data = create_dict_analise_investimento_ti(string_final)
        dict_data['created_at'] = time_now
        list_dict.append(dict_data)

    db.insert_many_data_abes(list_dict)

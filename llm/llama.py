import json
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = ChatGroq(model='llama3-70b-8192')

system_template = """
Você receberá um parágrafo contendo informações sobre investimentos em inteligência artificial (IA) por diferentes regiões e países. Seu objetivo é identificar os seguintes cinco dados e retornar no formato 'chave: valor':

1. Investimento do Brasil em TI (em dólares).
2. Posição do Brasil no Ranking Mundial de Investimentos de TI
3. Investimento da América Latina em TI (total).
4. Investimento global em TI.
5. Ano do estudo.
6. Setores de investimento

Exemplo de saída esperada:

{{
     "investimento_brasil": "$500M",
     "posicao_brasil": "12",
    "investimento_am_latina": "$1.2B",
    "investimento_global": "$150B",
    "ano_estudo": "2024",
    "setores_investimento": "5G, IOT, Cibersegurança"
}}

Se algum dado não estiver presente no parágrafo, devolva o valor como "Não Informado".
Você DEVE somente mostrar o dicionario sem nenhuma outra coisa.
Lembre-se 1 Milhão = 1M, 14 Bilhões = 14B, 13 Trilhões = 13T e da mesma forma para os outros números
Lembre-se você está analisando estudos do “Mercado Brasileiro de Software – Panorama e Tendências”, se o nome do estudo for “Mercado Brasileiro de Software – Panorama e Tendências 2020”, seu ano do estudo é um a menos, ou seja, 2019 nesse caso.
Parágrafo:
"""

prompt_template = ChatPromptTemplate.from_messages(
    [('system', system_template), ('user', '{text}')]
)

chain = prompt_template | model | StrOutputParser()


def create_dict_data(texto: str):
    resultado = chain.invoke({'text': texto})
    print(resultado)
    dict_obj = json.loads(resultado)

    return dict_obj

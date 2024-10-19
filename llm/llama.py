import json
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

system_template = """
Você receberá um parágrafo contendo informações sobre investimentos em inteligência artificial (IA) por diferentes regiões e países. Seu objetivo é identificar os seguintes cinco dados e retornar no formato 'chave: valor':

1. Investimento do Brasil em IA (em dólares).
2. Investimento da América Latina em IA (total).
3. Investimento global em IA.
4. Ano do investimento.

Exemplo de saída esperada:

{{
     "investimento_brasil": "$500M",
    "investimento_am_latina": "$1.2B",
    "investimento_global": "$150B",
    "ano_investimento": "2024"
}}

Se algum dado não estiver presente no parágrafo, devolva o valor como 'não informado'.
Você DEVE somente mostrar o dicionario sem nenhuma outra coisa.

Parágrafo:
"""

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template),
     ("user", "{text}")]
)

model = ChatGroq(model="llama3-70b-8192")

chain = prompt_template | model | StrOutputParser()

texto = """
A ABES – Associação Brasileira das Empresas de Software e a International Data Corporation (IDC) apresentam o Estudo Mercado Brasileiro de Software – Panorama e Tendências 2023. De acordo com dados da International Data Corporation (IDC) analisados pela ABES, o Brasil hoje manteve 1,65% dos investimentos em tecnologia em nível global, e 36% dos investimentos em toda a América Latina (contra 40% na pesquisa anterior). Considerando o total de investimentos globais em tecnologia da informação (software, hardware e serviços) durante o ano de 2022 – que foi de US＄ 3,11 trilhões, contra US＄ 2,79 trilhões –, o Brasil caiu duas posições, figurando agora em décimo-segundo lugar neste ranking de investimentos, com US＄ 45,2 bilhões aplicados e lidera na América Latina, cujo total de investimentos alcançou US＄ 124 bilhões (contra US＄ 115 bilhões em 2021). A IDC destacou as tendências para 2023-2024, a partir de uma perspectiva pragmática e focou temas como 5G, Cibersegurança e IoT, faça o download gratuito.
"""
resultado = chain.invoke({"text": texto})

dict_obj = json.loads(resultado)

print(dict_obj['investimento_brasil'])
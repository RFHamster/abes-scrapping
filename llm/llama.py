import json
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = ChatGroq(model='llama3-70b-8192')

system_template = """
You will receive a paragraph containing information about a study in information technology (IT) that analise the brazilian market of software. 

Your goal is to identify the following six data points and return them in the format 'key: value':

1. Brazil's investment/movement in IT (in dollars).
2. Brazil's position in the Global IT Investment Ranking.
3. Latin America's total investment in IT.
4. Global investment in IT.
5. Year of the study.
6. Investment sectors.

Example of expected output:

{{ "brazil_movement": "$500M", "brazil_position": "12", "latin_america_investment": "$1.2B", "global_investment": "$150B", "study_year": "2024", "investment_sectors": "5G, IoT, Cybersecurity" }}

If any data is not present in the paragraph, return the value as "Not Informed".

You MUST only show the dictionary without anything else.

USE the following annotation Million = M, Billion = B, Trillion = T.

Keep in mind that Brazil's position in Latin America is irrelevant; we only want the global position.

Remember that you are analyzing studies from "Brazilian Software Market – Overview and Trends." If the study name is "Brazilian Software Market – Overview and Trends 2020," the year of the study is one year less, meaning 2019 in this case.

In many cases we only have the Brazil quantity of investment/movement, and to deduce the other we need to analise the percent (%) from Brazil. For example: Brazil quantity is 50 Million and represents 48% of Latin America, so the quantity of Latin America is 50 Million times 100 dividide by 48, equal to 104,16 Million
"""

prompt_template = ChatPromptTemplate.from_messages(
    [('system', system_template), ('user', '{text}')]
)

chain = prompt_template | model | StrOutputParser()


def create_dict_analise_investimento_ti(texto: str):
    resultado = chain.invoke({'text': texto})
    print(resultado)
    dict_obj = json.loads(resultado)

    return dict_obj

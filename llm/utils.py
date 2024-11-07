import json
from langchain_core.output_parsers import StrOutputParser
from llm.prompt_factory import get_prompt
from llm.model_factory import get_model

model = get_model('llama3-70b', 'groq')

prompt_template = get_prompt('abes-scrapping')

chain_dict = prompt_template | model | StrOutputParser()


def create_dict_analise_investimento_ti(texto: str):
    resultado = chain_dict.invoke({'text': texto})
    print(resultado)
    dict_obj = json.loads(resultado)

    dict_obj['origin'] = 'scrap_abes_dados_setor'

    return dict_obj

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

## Eh necessário sua API KEY estar cadastrada nos .env
## Também é preciso ter créditos para usar a LLM
def get_model(model, enterprise):
    enterprise = enterprise.lower()
    if enterprise == 'groq':
        if model == 'llamma3-70b':
            return ChatGroq(model='llama3-70b-8192')
        if model == 'llamma3.1-70b':
            return ChatGroq(model='llama-3.1-70b-versatile')

    if enterprise == 'openai':
        if model == 'gpt-4':
            return ChatOpenAI(model='gpt-4')
        if model == 'gpt-3.5':
            return ChatOpenAI(model='gpt-3.5')

    return ChatGroq(model='llama3-70b-8192')

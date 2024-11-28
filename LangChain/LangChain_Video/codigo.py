from dotenv import load_dotenv
import os 
from langchain.schema import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()
key_API = os.getenv('OPENAI_API_KEY')

messages = [
    SystemMessage(content="Traduza o texto a seguir para o inglês"),
    HumanMessage(content="Eae tudo bom")
]

model = ChatOpenAI(model='gpt-3.5')

resposta = model.invoke(messages)
print(resposta)
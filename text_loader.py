from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Extract the main points from the following text:\n\n{text}",
    input_variables=["text"],   
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")

documents = loader.load()

print(type(documents))

chain = prompt | model | parser
result = chain.invoke({"text": documents[0].page_content})
print(result)

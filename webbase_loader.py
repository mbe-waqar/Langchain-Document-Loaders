from langchain_community.document_loaders import WebBaseLoader

url = "https://www.example.com/some-webpage"
loader = WebBaseLoader(url)

documents = loader.load()

print(len(documents))
print(documents[0].page_content)
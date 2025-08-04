from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

embeddings = OllamaEmbeddings(model="llama3.2:1b")

file_path = "C:/Users/CSESTUDENT/Desktop/Explore maker/EXPLORE MAKER.pdf"
loader = PyPDFLoader(file_path)
data = loader.load_and_split()
print(data)
url ="https://a91bbc31-2855-4d6a-921e-c0c8e13eb7da.us-west-1-0.aws.cloud.qdrant.io"
api_key ="<api>"

qdrant = QdrantVectorStore.from_documents(
    data,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="Explore maker",
)
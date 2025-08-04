from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from llm import *

embeddings = OllamaEmbeddings(model="llama3.2:1b")

url ="https://a91bbc31-2855-4d6a-921e-c0c8e13eb7da.us-west-1-0.aws.cloud.qdrant.io"
api_key ="<api>"

question = input("Enter your question: ")

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url=url,
    api_key=api_key,
    collection_name="Explore maker",
)

response =  qdrant.similarity_search(
    question,
    k=1)


prompt = f"""

Question: {question},
context: {response}
Only return the summary based on the provided content.
"""

print(completion_llm(prompt))

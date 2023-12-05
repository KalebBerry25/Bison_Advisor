import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
import pyrebase
from flask import *

app = Flask(__name__)
config = {
"apiKey": "AIzaSyBurNMdpk2CxK8fo6Q4HDrEkE3liRy85H4",
"authDomain": "bison-advisor-group-n.firebaseapp.com",
"projectId": "bison-advisor-group-n",
"storageBucket": "bison-advisor-group-n.appspot.com",
"messagingSenderId": "69696678672",
"appId": "1:69696678672:web:eec07336c9c210d45d9395",
"measurementId": "G-SLY1NJN3JX",
"databaseURL": "https://console.firebase.google.com/u/0/project/bison-advisor-group-n/database/bison-advisor-group-n-default-rtdb/data/~2F"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

os.environ["OPENAI_API_KEY"] = "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"

directory = 'bison_adv/ChatAI/docs'

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)
len(documents)


def split_docs(documents,chunk_size=1000,chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)
print(len(docs))

query = "How many credits is CHEM 003?"

embeddings = OpenAIEmbeddings()

query_result = embeddings.embed_query("Hello world")
len(query_result)

pinecone.init(
  api_key="3050022e-9d8b-4963-96bc-854f8062c492",
  environment="gcp-starter"
)

index_name = "bison-adv"

index = Pinecone.from_documents(docs, embeddings, index_name=index_name)

def get_similiar_docs(query, k=2, score=False):
  if score:
   similar_docs = index.similarity_search_with_score(query, k=k)
  else:
    similar_docs = index.similarity_search(query, k=k)
  return similar_docs

llm = ChatOpenAI(model_name="gpt-4")

chain = load_qa_chain(llm, chain_type="stuff")

def get_answer(query):
  similar_docs = get_similiar_docs(query)
  answer =  chain.run(input_documents=similar_docs, question=query)
  return answer

print(get_answer(query))


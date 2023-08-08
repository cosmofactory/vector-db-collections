import os

import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

load_dotenv()

client = chromadb.PersistentClient(path='./db_2/')
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv('OPEN_API_KEY'),
    model_name="text-embedding-ada-002"
)
collection = client.get_collection(
    'umbrella_chats',
    embedding_function=openai_ef
)


def list_collections():
    return client.list_collections()


def get_messages():
    messages = collection.get(
        limit=10,
        include=['documents']
    )
    return messages['documents']


def get_query():

    search = collection.query(
        query_texts=['бота'],
        n_results=10,
        include=['documents']
    )
    return search


if __name__ == '__main__':
    print(list_collections())
    print(get_messages())
    print(get_query())

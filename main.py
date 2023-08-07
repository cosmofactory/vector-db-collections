import chromadb
from chromadb.utils import embedding_functions
import openai



client = chromadb.PersistentClient(path='./db_2/')
# openai_ef = embedding_functions.OpenAIEmbeddingFunction(
#                 model_name="text-embedding-ada-002"
#             )

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_base='https://api.aiguoguo199.com/v1',
                api_type="azure",
                model_name="text-embedding-ada-002"
            )

print(client.list_collections())

collection = client.get_collection('umbrella_chats', embedding_function=openai_ef)
messages = collection.get(
    limit=10,
    include=['documents', 'metadatas']
    )
print(messages['documents'])

print(collection.query(
    query_texts='бота',
    where={'date': '2023-06-01T00:00:00'},
    include=['documents', 'metadatas']
))
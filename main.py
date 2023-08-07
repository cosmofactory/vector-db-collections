import chromadb

client = chromadb.PersistentClient(path='./db/')

print(client.list_collections())
# # print(client.get_collection('umbrella_chats'))

collection = client.get_collection('umbrella_chats')
# messages = collection.get(
#     limit=10,
#     include=['documents', 'metadatas']
#     )


print(collection.query(
    query_texts='бота',
    where={'date': '2023-06-01T00:00:00'},
    include=['documents', 'metadatas']
))

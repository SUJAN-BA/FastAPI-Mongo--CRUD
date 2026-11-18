from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import  certifi
 
uri  =  "mongodb+srv://sujan:spash123@cluster0.gjqmfc7.mongodb.net/"
client  =  MongoClient(uri, tlsCAFile=certifi.where())
 
db  =  client.todo_db 
collection  =  db["todo_data"] 
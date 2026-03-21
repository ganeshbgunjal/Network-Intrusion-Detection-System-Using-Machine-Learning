import pymongo
from pymongo.mongo_client import MongoClient
import certifi

# 1. Get your CA bundle path
ca = certifi.where()

# 2. Replace with your actual connection string from Atlas
# uri = "mongodb+srv://<username>:<password>@ac-gareppd-shard-00-00.rwkvxvz.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://ganeshgunjal118_db_user:Admin123@ac-gareppd-shard-00-00.rwkvxvz.mongodb.net/?retryWrites=true&w=majority"

# 3. Create the client with SSL fixes
client = MongoClient(
    uri,
    tlsCAFile=ca,                    # Uses certifi to find valid root certificates
    tlsAllowInvalidCertificates=True # Bypasses the 'Internal Error' handshake alert
)

# 4. Test the connection
try:
    client.admin.command('ping')
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
    
    # Check existing databases
    print(f"Available Databases: {client.list_database_names()}")
    
except Exception as e:
    print(f"❌ Connection failed: {e}")


# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://ganeshgunjal118_db_user:Admin123@cluster01.rwkvxvz.mongodb.net/?appName=Cluster01"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
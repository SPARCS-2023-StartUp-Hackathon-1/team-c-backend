from pymongo import MongoClient

def get_database():
     
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://jun916:110958yjy@db-cluster.bkfftpf.mongodb.net/?retryWrites=true&w=majority"
 
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
 
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['clothes_details']
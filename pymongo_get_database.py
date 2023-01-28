from pymongo import MongoClient

def get_database():
    
    CONNECTION_STRING = "mongodb+srv://jun916:110958yjy@db-cluster.bkfftpf.mongodb.net/?retryWrites=true&w=majority"
 
    client = MongoClient(CONNECTION_STRING)
 
    return client['clothes_details']

if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
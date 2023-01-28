from pymongo import MongoClient
import certifi

def get_database():
    
    ca = certifi.where()
    
    CONNECTION_STRING = "mongodb+srv://jun916:110958yjy@db-cluster.bkfftpf.mongodb.net/?retryWrites=true&w=majority"
 
    client = MongoClient(CONNECTION_STRING, tlsCAFile=ca)
 
    return client['clothes_details']

if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
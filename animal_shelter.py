from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host='nv-desktop-services.apporto.com', port=32308, db='AAC', col='animals'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'Ελλινηκα'
        USER = user
        PASS = password
        HOST = host
        PORT = port
        DB = db
        COL = col
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Test connection to MongoDB
    def testConnection(self):
        try:
            # find one document to test the connection and return True if successful
            self.database.animals.find_one()
            return True
        except Exception as e:
            # if an error is thrown while trying to use find_one(), return False
            return False
        
    # 'Create' method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # 'Read' method to implement the R in CRUD.
    def read(self, data):
        if data is None:
            data = {}
        return self.collection.find(data)
    
    # 'Update' method to implement the U in CRUD
    def update(self, criteria, update_data):
        if criteria is not None and update_data is not None:
            result = self.collection.update_many(criteria, {'$set': update_data})
            return result.modified_count
        else:
            raise Exception("Criteria and update data parameters cannot be empty")

    # 'Delete' method to implement the D in CRUD
    def delete(self, criteria):
        if criteria is not None:
            result = self.collection.delete_many(criteria)
            return result.deleted_count
        else:
            raise Exception("Criteria parameter cannot be empty")
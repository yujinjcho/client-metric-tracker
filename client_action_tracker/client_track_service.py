class ClientTrackService:
    def __init__(self, datastore):
        self.datastore = datastore

    def hello_world(self):
        print("Handling hello_world")
        return 'Hello, World'


    def create_test(self):
        self.datastore.insert_test()
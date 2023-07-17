import logging
class ClientTrackService:
    def __init__(self, datastore):
        self.datastore = datastore

    def hello_world(self):
        logging.info("Handling hello_world")
        return 'Hello, World'

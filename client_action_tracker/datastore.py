
class Datastore:

    def __init__(self, conn):
        self.conn = conn

    def insert_test(self):
        query = 'INSERT INTO test (id) VALUES (%s)'
        print('Datastore - insert_test')

        with self.conn.cursor() as cur:
            cur.execute(query, ('123',))
        self.conn.commit()

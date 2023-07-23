import json

import psycopg2
import psycopg2.extras

class Datastore:
    def __init__(self, conn):
        self.conn = conn

    def insert_events(self, events):
        try:
            with self.conn.cursor() as cur:
                print(events)
                events_tuples = [
                    (
                        event['event_id'],
                        event['name'],
                        event['event_type'],
                        event['event_status'],
                        event['client_created_at'],
                        event['client_completed_at'],
                        event['client_user_id'],
                        event['project_id'],
                        json.dumps(event.get('properties', {}))  # Convert the properties to JSON string
                    )
                    for event in events
                ]
                psycopg2.extras.execute_values(
                    cur,
                    """
                    INSERT INTO events_v2 (event_id, name, event_type, event_status, client_created_at, client_completed_at, client_user_id, project_id, properties)
                    VALUES %s
                    """,
                    events_tuples,
                    # template="(%(event_id)s, %(name)s, %(event_type)s, %(event_status)s, %(client_created_at)s, %(client_completed_at)s, %(client_user_id)s, %(project_id)s, %(properties)s)",
                    page_size=1000
                )
                self.conn.commit()
        except psycopg2.Error as e:
            self.conn.rollback()
            raise e
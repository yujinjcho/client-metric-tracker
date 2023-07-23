import os
import datetime
from uuid import UUID
from jsonschema import validate, ValidationError
from werkzeug.exceptions import BadRequest

def is_uuid(uuid_string):
    try:
        UUID(uuid_string)
        return True
    except ValueError:
        return False

def is_timestamp(timestamp):
    try:
        datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
        return True
    except ValueError:
        return False

event_schema = {
        "type": "object",
        "properties": {
            "event_id": {"type": "string", "validator": is_uuid},
            "name": {"type": "string"},
            "event_type": {"type": "string"},
            "event_status": {"type": "string"},
            "client_created_at": {"type": "string", "validator": is_timestamp},
            "client_completed_at": {"type": "string", "validator": is_timestamp},
            "client_user_id": {"type": "string"},
            "properties": {"type": "object"}
        },
        "required": ["event_id", "name", "event_type", "event_status", "client_created_at", "client_completed_at", "client_user_id", "properties"]
    }
class ClientTrackService:
    def __init__(self, datastore):
        self.datastore = datastore

    def hello_world(self):
        print("Handling hello_world")
        return 'Hello, World'

    def validate_event(self, data):
        try:
            validate(instance=data, schema=event_schema)
            return True
        except ValidationError as v:
            return False

    def create_events(self, events, api_key):
        project_id = get_project_id(api_key)
        if not project_id:
            raise BadRequest(f'No project associated with api key')

        for event in events:
            event['project_id'] = project_id

        self.datastore.insert_events(events)
        return

# TODO: for now just use environ variable
def get_project_id(api_key):
    keys_to_project_id_raw = os.environ.get('KEYS_TO_PROJECT_ID', None)
    print(keys_to_project_id_raw)
    if not keys_to_project_id_raw:
        return None

    keys_to_projects = dict(entry.split(":") for entry in keys_to_project_id_raw.split(","))
    return keys_to_projects.get(api_key, None)
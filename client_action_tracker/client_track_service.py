
from client_action_tracker.utils import get_project_id
from client_action_tracker.models import parse_event_dict

class ClientTrackService:
    def __init__(self, datastore):
        self.datastore = datastore

    def hello_world(self):
        # TODO: try real logger
        print("Handling hello_world")
        return 'Hello, World'

    def create_events(self, events_raw, api_key):
        project_id = get_project_id(api_key)
        if not project_id:
            raise ValueError("No project associated with api key")

        if not events_raw:
            return

        events = []
        for event_raw in events_raw:
            events.append(parse_event_dict(event_raw, project_id))

        self.datastore.insert_events(events)
        return

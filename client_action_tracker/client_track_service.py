import logging
from typing import List, Callable

from client_action_tracker.datastore import Datastore
from client_action_tracker.models import parse_event_dict, Event


class ClientTrackService:
    def __init__(self, datastore: Datastore, get_project_id: Callable[[str], str]) -> None:
        self.datastore = datastore
        self.get_project_id = get_project_id

    def hello_world(self) -> str:
        logging.info("Handling hello_world")
        return 'Hello, World'

    def create_events(self, events_raw: List[dict], api_key: str) -> None:
        project_id = self.get_project_id(api_key)
        if not project_id:
            raise ValueError("No project associated with api key")

        if not events_raw:
            return

        events: List[Event] = []
        for event_raw in events_raw:
            events.append(parse_event_dict(event_raw, project_id))

        self.datastore.insert_events(events)
        return

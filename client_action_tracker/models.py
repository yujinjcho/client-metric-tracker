from dataclasses import dataclass
import json
from typing import Dict, Any, Optional, List
from uuid import UUID
from enum import Enum
from datetime import datetime


class EventType(Enum):
    """Do not change the string values otherwise will lose
    compatibility with how it's stored in the database"""
    ONE_TIME = 'one_time'
    COMPLETION = 'completion'

class EventStatus(Enum):
    """Do not change the string values otherwise will lose
    compatibility with how it's stored in the database"""
    SUCCESS = "success"
    FAIL = "fail"

@dataclass
class Event:
    event_id: UUID
    # TODO: rename this to event_name
    name: str
    project_id: UUID
    event_type: EventType
    event_status: EventStatus
    client_created_at: datetime
    client_completed_at: datetime
    client_user_id: Optional[str]
    properties: Dict[str, Any]

def parse_event_dict(event_dict: dict, project_id: str) -> Event:
    try:
        event_id = UUID(event_dict["event_id"])
        project_id = UUID(project_id)
        name = event_dict["name"]
        event_type = EventType(event_dict["event_type"])
        event_status = EventStatus(event_dict["event_status"])
        client_created_at = datetime.fromisoformat(event_dict["client_created_at"].replace("Z", "+00:00"))
        client_completed_at = datetime.fromisoformat(event_dict["client_completed_at"].replace("Z", "+00:00"))
        client_user_id = event_dict.get("client_user_id")  # Returns None if "client_user_id" is not in the dictionary
        properties = event_dict["properties"]

        return Event(event_id, name, project_id, event_type, event_status, client_created_at, client_completed_at, client_user_id, properties)

    except (ValueError, KeyError, TypeError) as e:
        raise ValueError(f"Invalid event dict: {event_dict}") from e
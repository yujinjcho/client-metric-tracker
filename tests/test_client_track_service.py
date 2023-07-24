import unittest
from unittest.mock import Mock

from client_action_tracker.client_track_service import ClientTrackService


class TestClientTrackService(unittest.TestCase):
    def test_hello_world(self):
        datastore = Mock()
        get_project_id = Mock()
        client_track_service = ClientTrackService(datastore, get_project_id)
        self.assertEqual(client_track_service.hello_world(), 'Hello, World')

    def test_create_events_no_events(self):
        datastore = Mock()
        get_project_id = Mock()
        get_project_id.return_value = 'project_id'
        client_track_service = ClientTrackService(datastore, get_project_id)
        client_track_service.create_events([], 'api_key')
        datastore.insert_events.assert_not_called()

    def test_create_events_with_events(self):
        datastore = Mock()
        get_project_id = Mock()
        get_project_id.return_value = '00000000-0000-0000-0000-000000000001'
        client_track_service = ClientTrackService(datastore, get_project_id)

        event = {
            "event_id": "00000000-0000-0000-0000-000000000002",
            "event_name": "some name",
            "event_type": "completion",
            "event_status": "success",
            "client_created_at": "2023-07-19T17:23:42.000Z",
            "client_completed_at": "2023-07-19T18:23:42.000Z",
            "client_user_id": "TestUser",
            "properties": {}
        }

        client_track_service.create_events([event], 'api_key')
        datastore.insert_events.assert_called_once()


if __name__ == '__main__':
    unittest.main()

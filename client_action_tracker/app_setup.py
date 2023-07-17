from flask import Flask

from client_action_tracker.client_track_service import ClientTrackService
from client_action_tracker.datastore import Datastore


def create_app():
    app = Flask(__name__)
    datastore = Datastore()
    service = ClientTrackService(datastore)
    return app, service


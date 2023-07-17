from flask import Flask

from client_action_tracker.client_track_service import ClientTrackService


def create_app():
    app = Flask(__name__)
    service = ClientTrackService()
    return app, service


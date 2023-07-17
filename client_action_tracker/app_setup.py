import logging
from flask import Flask

from client_action_tracker.client_track_service import ClientTrackService
from client_action_tracker.datastore import Datastore


def create_app():
    logging.basicConfig(
        level=logging.INFO,
        format=f'%(asctime)s - %(levelname)s - %(message)s'
    )

    logging.info("Creating app")

    app = Flask(__name__)
    datastore = Datastore()
    service = ClientTrackService(datastore)

    return app, service


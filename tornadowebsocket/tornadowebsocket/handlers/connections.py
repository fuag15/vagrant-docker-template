"""
Request Handler for server statistics
"""

from json import dumps
from datetime import datetime

from tornado.web import RequestHandler

class ConnectionsHandler(RequestHandler):
    """
    Normal request handler to send statistics
    about server
    """

    async def get(self):
        """
        display statistics on all clients
        """
        current_time = datetime.now()
        self.write(
            dumps([{'uptime_ms': (handler_instance.start_time - current_time
                                 ).microseconds / 1000, 
                    'messages': handler_instance.valid_messages_recieved}
                   for handler_instance 
                   in self.settings['active_mongo_websocket_handlers']]
                 ))

        self.finish()

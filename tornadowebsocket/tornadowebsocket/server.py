"""
Tornado Server
"""

from weakref import WeakSet

from motor.motor_tornado import MotorClient

from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line

from .handlers.mongowebsocket import MongoWebsocketHandler
from .handlers.connections import ConnectionsHandler

def main():
    """
    Launch the server
    """
    parse_command_line()
    application = Application(
        [('/connect', MongoWebsocketHandler),
         ('/connections', ConnectionsHandler)],
         database=MotorClient('mongodb://database:27017'
                             ).tornado_websocket.tornado_websocket,
         active_mongo_websocket_handlers=WeakSet())

    application.listen(80)
    IOLoop.instance().start()

if __name__ == '__main__':
    """
    Script entrypoint
    """
    main()

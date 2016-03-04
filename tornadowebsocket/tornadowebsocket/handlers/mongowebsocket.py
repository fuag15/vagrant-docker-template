"""
Tornado Server
"""

from datetime import datetime

from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop

from ..asyncmotor import find_one, insert

class MongoWebsocketHandler(WebSocketHandler):
    """
    Instance of the tornado websocket handler
    that acts as entrypoint into mongo
    """
    
    def __init__(self, application, request, **kwargs):
        """
        initialize some state used to determine
        global connection state on connections route

        :param application:
            the whole application object
        :type application:
            :class:`tornado.web.Application`
        
        :param request:
            the request object
        :type request:
            :class:`HTTPServerRequest`
        """
        self.start_time = datetime.now()
        self.valid_messages_recieved = 0
        super().__init__(application, request, **kwargs)

    def open(self):
        """
        Called whenever a new websocket is
        opened. Writes a hello back to the client
        and adds instance to the global contexts
        WeakrefSet.
        """
        self.settings['active_mongo_websocket_handlers'].add(self)
        self.write_message("hello")

    def on_message(self, message):
        """
        Called whenever we get a message
        parses the message for either

        get {key}

        or

        set {key} {value}

        and performs the relevant operation
        on the mongo collection this app uses.
        sends the result back over the websocket
        
        :param message:
            the text recieved over the websocket
        :type message:
            str
        """
        command_parts = message.split()
        if command_parts[0] == 'get' and len(command_parts) == 2:
            self.valid_messages_recieved += 1
            IOLoop.current().spawn_callback(
                find_one,
                self.settings['database'],
                {command_parts[1]: {'$exists': True}
                },
                lambda document: self.write_message(document.get(command_parts[1])
                                                    if document 
                                                    else 'null'),
                lambda motor_error: self.write_message(repr(motor_error)
                                                      )
               )

        elif command_parts[0] == 'set' and len(command_parts) > 2:
            self.valid_messages_recieved += 1
            IOLoop.current().spawn_callback(
                insert,
                self.settings['database'],
                {command_parts[1]: message.lstrip(' '.join(command_parts[:2])
                                                 )
                },
                lambda _: self.write_message('ok'),
                lambda motor_error: self.write_message(repr(motor_error)
                                                      )
               )

    def on_close(self):
        """
        Called when the websocket closes
        we remove ourselves from the global contexts
        WeakrefSet.
        """
        self.settings['active_mongo_websocket_handlers'].discard(self)

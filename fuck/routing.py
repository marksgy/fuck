from channels.routing import route
from ffff.consumers import ws_usualconnect,ws_message, ws_disconnect,msg_consumer

channel_routing = [
    route("websocket.connect", ws_usualconnect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    route("chat-messages", msg_consumer),
]
import socketio
from socketio import Client

sio = None
try:
    MAIN_HOST = 'http://38.242.196.170'
    sio: Client = socketio.Client()
    sio.connect(MAIN_HOST, namespaces=['/robot'])
    print('Connected to {}'.format(MAIN_HOST))
except Exception as ex:
    print(ex)
    # TODO: handle exception with speaker beeps


@sio.on('move', namespace='/robot')
def completeOrder(data):
    # TODO: Implement robot movement
    d = data["data"]
    station = d["station"]
    print("moving to station {}".format(station))


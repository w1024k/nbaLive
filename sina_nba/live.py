import websocket
import requests, time, json
import settings


class Live(object):
    def __init__(self, match_id):
        params = dict(match_id=match_id)
        self.roomnum = requests.get(url=settings.ROOMNUM_URL, params=params).json()['result']['data']['room_num']
        self.title = requests.get(url=settings.ROOMNUM_URL, params=params).json()['result']['data']['name']

    def on_message(self, ws, message):
        rsp = json.loads(message)
        detail = rsp.get("c") or rsp.get("b")
        match = detail.get("match")
        # print detail
        if match:
            print "%s, %s [%s : %s]" % (self.title, match["phase"], match["score2"], match["score1"])

        print "%s: %s" % (detail["liver"]["nickname"], detail.get("text"))

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def get_verify(self):
        params = {
            "roomnum": "sports:%s" % self.roomnum,
            "_": str(int(time.time() * 1000))
        }
        print params
        verify = requests.get(url=settings.VERIFY_URL, params=params).json()
        print verify
        return verify['result']['data']

    def run(self):
        websocket.WebSocket()
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(
            settings.LIVE_WS + self.get_verify(),
            header=settings.WS_HEADERS,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        print self.title
        ws.run_forever()

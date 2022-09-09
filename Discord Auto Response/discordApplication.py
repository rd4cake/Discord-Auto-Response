from urllib import response
import websocket
import json
import threading
import time
import requests
import openaiTEXT

def send_json_request(ws, request):
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response =ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval, ws):
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)

ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
event = recieve_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval'] / 1000
threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

token = "YOUR DISCOD TOKEN"

payload = {
    'op' : 2,
    'd' : {
        "token": token,
        "properties": {
            "$os" : "windows",
            "$browser": "chrome",
            "$device" : "pc"
        }
    }
}


send_json_request(ws, payload)
text = ""
while True:
    event = recieve_json_response(ws)

    try:
        if event['d']['author']['username'] == "USERNAME OF OTHER PERSON":
            text+="You: " + event['d']['content']+'\n'
            respond = openaiTEXT.respond(text)
            respond = respond.replace("Friend:", "")
            payload = {
                'content' : respond
            }
            text+="Friend: "+respond+'\n'
            header = {
                'authorization' : "AUTH KEY"
            }
            print(text)
            r = requests.post("DISCORD CHANNEL API", data=payload, headers=header)

        op_code = event('op')
        if op_code == 11:
            print("hearbeat recieved")
    except Exception as e:
        print(e)

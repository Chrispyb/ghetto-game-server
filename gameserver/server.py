from worlds import *
from flask import Flask, escape, request
import _thread
import threading
import time
from game import Game
app = Flask(__name__)

lock = threading.Lock()
game = Game()


@app.route('/get_world', methods=['GET'])
def get_world():
    global game
    return game.get_game()

@app.route('/update_world', methods=['POST'])
def update_world():
    global lock
    global game

    world = {}

    with lock:
        if request.method == 'POST':
            data = request.form
            game.update_with_action(data)
    return 'Success'

@app.route('/new_player')
def new_player():
    global game
    
    response = ''
    with lock:
        response = game.add_player()
        print(response)
    return response

def game_thread():
    global game
    global lock
    
    while(True):
        time.sleep(1/60)
        with lock:
            game.update_game()


try:
    _thread.start_new_thread(game_thread, ())
    app.run(host="127.0.0.1", port=5000, threaded=True)
except:
    print ("Error: unable to start thread")




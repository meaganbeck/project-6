"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""
import requests

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations

app = flask.Flask(__name__)
app.debug = True
app.logger.setLevel(logging.DEBUG)

api_host = os.environ["API_ADDR"]
api_port = os.environ["API_PORT"]

api_url = f"http://{api_host}:{api_port}/api/}"

import logging

def insert_brevet(brevet_dist, start_time, controls):
    brevet = {"brevet_dist":brevet_dist,
              "start_time": start_time,
              "controls": controls}
    controls = requests.post(f"{api_url}/brevets", json=brevet).json()
    
    return ""



def get_brevet():
    #idk if controls
    controls = requests.get(f"{api_url}/brevets").json()
    for control in controls:
        #controls wrong
        return control["brevet_dist"], control["start_time"], control["controls"]
###
# Globals
###
app = flask.Flask(__name__)
#CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
#    return flask.render_template('calc.html')

###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    brevet_distance = request.args.get('brevet_distance', 999, type=float)#dded
    start_time = request.args.get('start_time', type=str) #added. passes to acp times. convert to arrow object before passing below in open/close times. 
    app.logger.debug("km={}".format(km))
    app.logger.debug("brev_dist={}".format(brevet_distance))
    app.logger.debug("start_time={}".format(start_time))
    app.logger.debug("request.args: {}".format(request.args))
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!
    open_time = acp_times.open_time(km, brevet_distance, arrow.get(start_time, 'YYYY-MM-DDTHH:mm'))
    close_time = acp_times.close_time(km, brevet_distance, arrow.get(start_time, 'YYYY-MM-DDTHH:mm')) #maybe end_time...
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route('/insert/', method=['POST']) #where is this shit coming from?
def insert_brevet(brevet_dist, start_time, controls):
    output = collection.insert_one({"controls": controls, "brevet_dist":brevet_dist, "start_time":start_time})
    #_id = output.inserted_id
    return output
    open_time = request.json['open_time'],
    close_time = request.json['close_time'],
    km = request.json['km']

    controls_id = set_control(brevet_dist, start_time, controls)
    #db.insert_one(brevet_dist, start_time, controls)
        return flask.jsonify(
            result = {},
            status = 1,
            message = "inserted",
            mongo_id = controls_id)
    except:
        return flask.jsonify(
            result = {},
            status = 0,
            message = "naur. bad",
            mongo_id = 'None')
    

@app.route('/fetch')
def get_brevet():
    try:
        controls, brevet_dist, start_time = get_control()
    #brevet_dist, start_time, items = db.find(item_doc)
    
        return flask.jsonify(
            result = {'brevet_dist' : brevet_dist, 'start_time' : start_time, 'controls' : controls},
            status = 1,
            message = "got the data"
            )
    except:
        return flask.jsonify(result = {"brevet_dist": 200, "start_time": arrow.now().format("YYY-MM-DDTHH:mm"), "controls": []}, status = 0)

app.debug = os.environ["DEBUG"]
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.run(port = os.environ["PORT"], host='0.0.0.0') #maybe add port?

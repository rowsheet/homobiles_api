from flask import Flask, request, jsonify
import json
import os
import requests
import sys
app = Flask(__name__)

def log_stdout(msg):
    sys.stdout.write(str(msg) + "\n")
    sys.stdout.flush()

if "PORT" not in os.environ:
    raise Exception(
        "Invalid deployment: Missing env var '%s'" % "PORT")
PORT= os.environ["PORT"]

if "ROWSHEET_EMAILER_KEY" not in os.environ:
    raise Exception(
        "Invalid deployment: Missing env var '%s'" % "ROWSHEET_EMAILER_KEY")
ROWSHEET_EMAILER_KEY = os.environ["ROWSHEET_EMAILER_KEY"]

if "RECAPTCHA_SECRET" not in os.environ:
    raise Exception(
        "Invalid deployment: Missing env var '%s'" % "RECAPTCHA_SECRET")
RECAPTCHA_SECRET = os.environ["RECAPTCHA_SECRET"]

if "RECAPTCHA_MIN_SCORE" not in os.environ:
    raise Exception(
        "Invalid deployment: Missing env var '%s'" % "RECAPTCHA_MIN_SCORE")
RECAPTCHA_MIN_SCORE = os.environ["RECAPTCHA_MIN_SCORE"]

EMAIL_TO_LIST = [
    "alex@rowsheet.com",
    "k@metrctensor.com",
    "4155745023@tmomail.net",
    "rcbrown@gmail.com",
    " j7f3c6z1t3f0t3q8@homobiles.slack.com",
]

def validate_recaptcha(secret, token, min_score):
    url = (
        "https://www.google.com/" +
        "recaptcha/api/siteverify" +
        "?secret=%s&response=%s" % (
            secret,
            token,
        )
    )
    response = requests.post(url)
    if response.status_code != 200:
        return False
    response_data = json.loads(response.text)
    if response_data["success"] != True:
        return False
    if response_data["success"] == False:
        return False
    if response_data["score"] < min_score:
        return False
    return True

def send_email(email_to, body):
    log_stdout("Calling sending_email()")
    log_stdout("email_to:")
    log_stdout(email_to)
    log_stdout("body:")
    log_stdout(body)
    r = requests.post(
        "https://emailer.rowsheet.com/",
        data=json.dumps({
            "api_key": ROWSHEET_EMAILER_KEY,
            "to": email_to,
            "subject": "Ride Request",
            "body": body,
        }),
        headers={'content-type': 'application/json'}
    )
    return r

def request_a_ride(data):
    log_stdout("Calling request_a_ride()")
    if "name" not in data:
        return "Invalid request.", 400
    name = data["name"]
    if "pickup_time" not in data:
        return "Invalid request.", 400
    pickup_time = data["pickup_time"]
    if "phone_number" not in data:
        return "Invalid request.", 400
    phone_number = data["phone_number"]
    if "pronoun" not in data:
        return "Invalid request.", 400
    pronoun = data["pronoun"]
    if "start_location" not in data:
        return "Invalid request.", 400
    start_location = data["start_location"]
    if "end_location" not in data:
        return "Invalid request.", 400
    end_location = data["end_location"]
    if "passenger_count" not in data:
        return "Invalid request.", 400
    passenger_count = data["passenger_count"]
    if "num_bags" not in data:
        return "Invalid request.", 400
    num_bags = data["num_bags"]
    if "special_req" not in data:
        return "Invalid request.", 400
    special_req = data["special_req"]
    body = """
Name: %s
Pickup Time: %s
Phone Number: %s
Pronoun: %s
Start Location: %s
End Location: %s
Passenger Count: %s
Num Bags: %s
Special Requests: %s
    """ % (
        name,
        pickup_time,
        phone_number,
        pronoun,
        start_location,
        end_location,
        passenger_count,
        num_bags,
        special_req
    )
    for email_to in EMAIL_TO_LIST:
        r = send_email(email_to, body)
        if r.status_code != 200:
            log_stdout("Non 200 response code from emailer service:")
            log_stdout(r.text)
            return "Unknown error occurred.", 500
    return "Ride request submited!"

def driver_signup(data):
    """
    if "username" not in data:
        return "Invalid request.", 400
    username = data["username"]
    """
    if "first_name" not in data:
        return "Invalid request.", 400
    first_name = data["first_name"]
    if "last_name" not in data:
        return "Invalid request.", 400
    last_name = data["last_name"]
    if "pronoun" not in data:
        return "Invalid request.", 400
    pronoun = data["pronoun"]
    """
    if "password" not in data:
        return "Invalid request.", 400
    password = data["password"]
    if "repeat_password" not in data:
        return "Invalid request.", 400
    repeat_password = data["repeat_password"]
    """
    if "smartphone_type" not in data:
        return "Invalid request.", 400
    smartphone_type = data["smartphone_type"]
    if "vehicle_year" not in data:
        return "Invalid request.", 400
    vehicle_year = data["vehicle_year"]
    if "vehicle_make" not in data:
        return "Invalid request.", 400
    vehicle_make = data["vehicle_make"]
    if "vehicle_model" not in data:
        return "Invalid request.", 400
    vehicle_model = data["vehicle_model"]
    if "vehicle_doors" not in data:
        return "Invalid request.", 400
    vehicle_doors = data["vehicle_doors"]
    if "yes_no_square" not in data:
        return "Invalid request.", 400
    yes_no_square = data["yes_no_square"]
    if "yes_no_insurance" not in data:
        return "Invalid request.", 400
    yes_no_insurance = data["yes_no_insurance"]
    if "yes_no_criminal_history" not in data:
        return "Invalid request.", 400
    yes_no_criminal_history = data["yes_no_criminal_history"]
    if "comments" not in data:
        return "Invalid request.", 400
    comments = data["comments"]
    body = """
Pronoun: %s
First Name: %s
Last Name: %s
Smartphone Type: %s
Vehicle Year: %s
Vehicle Make: %s
Vehicle Model: %s
Vehicle Doors: %s
Yes No Square: %s
Yes No Insurance: %s
Yes No Criminal History: %s
Comments: %s
    """ % (
        pronoun,
        first_name,
        last_name,
        smartphone_type,
        vehicle_year,
        vehicle_make,
        vehicle_model,
        vehicle_doors,
        yes_no_square,
        yes_no_insurance,
        yes_no_criminal_history,
        comments,
    )
    log_stdout(body)
    r = requests.post(
        "https://emailer.rowsheet.com/",
        data=json.dumps({
            "api_key": ROWSHEET_EMAILER_KEY,
            "to": "homobiles@gmail.com",
            # "to": "alex@rowsheet.com",
            "subject": "Driver Signup",
            "body": body,
        }),
        headers={'content-type': 'application/json'}
    )
    if r.status_code != 200:
        return "Unknown error occurred.", 500
    return "Your application has been submited!"

@app.route('/', methods=['POST', 'GET'])
def index():
    data = request.json
    log_stdout("got request: ")
    log_stdout(data)
    if data is None:
        return "Invalid request, missing request data.", 400
    if "command" not in data:
        return "Invalid request, missing command.", 400
    if "_grecaptcha_token" not in data:
        return "Invalid request, missing reCAPTCHA token.", 400
    #---------------------------------------------------------------------------
    # Validate reCAPTCHA token.
    #---------------------------------------------------------------------------
    secret = RECAPTCHA_SECRET
    token = data["_grecaptcha_token"]
    min_score = float(RECAPTCHA_MIN_SCORE)
    if validate_recaptcha(secret, token, min_score) == False:
        return "Invalid reCAPTCHA token. Are you a bot?", 400
    #---------------------------------------------------------------------------
    # Test routes.
    #---------------------------------------------------------------------------
    elif data["command"] == "test_500":
        return "test_500", 500
    elif data["command"] == "test_400":
        return "test_400", 400 
    elif data["command"] == "test_401":
        return "test_401", 401 
    #---------------------------------------------------------------------------
    # API routes.
    #---------------------------------------------------------------------------
    elif data["command"] == "request_a_ride":
        return request_a_ride(data)
    elif data["command"] == "driver_signup":
        return driver_signup(data)
    elif data["command"] == "driver_login":
        # return "OK rider_signup"
        return "This service hasn't been implemented yet.", 503
    elif data["command"] == "rider_signup":
        # return "OK rider_signup"
        return "This service hasn't been implemented yet.", 503
    elif data["command"] == "rider_login":
        # return "OK rider_login"
        return "This service hasn't been implemented yet.", 503
    elif data["command"] == "rider_login":
        # return "OK rider_login"
        return "This service hasn't been implemented yet.", 503
    else:
        return "Invalid request.", 400

@app.route('/ping', methods=['POST', 'GET'])
def ping():
    log_stdout("got ping")
    return "pong"

if __name__ == '__main__':
    app.run(
        host= '0.0.0.0',
        port=PORT,
        debug=True
    )

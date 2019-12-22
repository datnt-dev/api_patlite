import json
import decimal
from flask import Flask, request, jsonify
# from flask_restful import marshal
from database import get_connection
# from flask_marshmallow import Marshmallow


app = Flask(__name__)


def json_encode_decimal(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError(repr(obj) + " is not JSON serializable")


@app.route('/api/state/<mac_address>', methods=['GET', ])
def get_state(mac_address):
    connect = get_connection()
    with app.app_context():
        cursor = connect.cursor()
    sql = """
        SELECT MAC_ADDRESS, CURRENT_STATE, TIME_OFF, TIME_GREEN, TIME_RED, TIME_YELLOW, ACTUAL_QTY 
        FROM PATLITE_STATE_CONTROL
        WHERE MAC_ADDRESS=?
      """


    params = '58C232FFFE579F0F'
    cursor.execute(sql, params)

    for row in cursor:
        data = [x for x in row]
    time_off, time_green, time_red, time_yellow = data[2], data[3], data[4], data[5]
    time_total = time_off + time_green + time_red + time_yellow
    if data[1] == 0:
        state = 'OFF'
        time = time_off
    elif data[1] == 10:
        state = 'RUNNING'
        time = data[3]
    elif data[1] == 20:
        state = 'STOP'
        time = data[4]
    else:
        state = 'WARNING'
        time = data[5]

    res = {
        'mac_address': data[0],
        'current_state': state,
        'time': time,
        'actual_qty': data[6]
    }
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

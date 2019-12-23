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

# def get_state(param):
#   connect = get_connection()

#   cursor = connect.cursor()
#   sql = """
#           SELECT MAC_ADDRESS, CURRENT_STATE, TIME_OFF, TIME_GREEN, TIME_RED, TIME_YELLOW, ACTUAL_QTY FROM PATLITE_STATE_CONTROL
#           WHERE MAC_ADDRESS=?
#         """
#   params = param
#   cursor.execute(sql, params)
#   return cursor


@app.route('/api/state/<mac_address>')
def get_state(mac_address):
    try:
        connect = get_connection()

        cursor = connect.cursor()
        sql = sql = """
                { CALL Q012_MobileTest (@mac=?) }
              """
        cursor.execute(sql, mac_address)
        rows = cursor.fetchall()

        time_total = rows[0][2] + rows[0][3] + rows[0][4] + rows[0][5]

        if rows[0][1] == 0:
            state = 'OFF'
            time = rows[0][2]
            if time_total != 0:
                time_up = round(time/time_total * 100, 2)
            else:
                time_up = 0
        elif rows[0][1] == 10:
            state = 'RUNNING'
            time = rows[0][3]
            if time_total != 0:
                time_up = round(time/time_total * 100, 2)
            else:
                time_up = 0
        elif rows[0][1] == 20:
            state = 'STOPPED'
            time = rows[0][4]
            if time_total != 0:
                time_up = round(time/time_total * 100, 2)
            else:
                time_up = 0
        else:
            state = 'WARNING'
            time = rows[0][5]
            if time_total != 0:
                time_up = round(time/time_total * 100, 2)
            else:
                time_up = 0
        
        return {
            'name': rows[0][9],
            'status': state,
            'time': time,
            'qty': rows[0][8],
            'up_time': time_up,
            'des': rows[0][10]
        }
            
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connect.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8069)

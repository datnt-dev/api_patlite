from database import get_connection
import pyodbc
import json
import decimal
from flask import jsonify


def get_state():
  connect = get_connection()

  
  cursor = connect.cursor()
  sql = sql = """
                SELECT MAC_ADDRESS, CURRENT_STATE FROM PATLITE_STATE_CONTROL
              """
  cursor.execute(sql)
  # cursor.execute(sql, params)
  # rows = cursor.fetchall()
  # print(rows)
  return cursor


# params = '58C232FFFE579F0F'
cursor = get_state()
columns = [column[0] for column in cursor.description]
print(columns)

results = []

for row in cursor.fetchall():
  results.append(dict(zip(columns, row)))  

print(results)
#   'mac_address': data[0],
#   'state': data[1]
# }

# print(res)


# def get_state():
#     connect = get_connection()

#     cursor = connect.cursor()
#     sql = """
#         SELECT MAC_ADDRESS, CURRENT_STATE, TIME_OFF, TIME_GREEN, TIME_RED, TIME_YELLOW, ACTUAL_QTY 
#         FROM PATLITE_STATE_CONTROL
#         WHERE MAC_ADDRESS=?
#       """

#     params = '58C232FFFE57F7AB'
#     # params = param
#     cursor.execute(sql, params)
#     rows = cursor.fetchall()
#     return rows


# params = '58C232FFFE57F7AB'
# rows = get_state()
# print(rows)

# data = []
# for row in rows:
#     data.append([x for x in row])
#     print(data)

# time_off, time_green, time_red, time_yellow = data[0][2], data[0][3], data[4], data[5]
# time_total = time_off + time_green + time_red + time_yellow
# if data[1] == 0:
#     state = 'OFF'
#     time = time_off
# elif data[1] == 10:
#     state = 'RUNNING'
#     time = data[3]
# elif data[1] == 20:
#     state = 'STOP'
#     time = data[4]
# else:
#     state = 'WARNING'
#     time = data[5]

# res = {
#     'mac_address': data[0],
#     'current_state': state,
#     'time': time,
#     'actual_qty': data[6]
# }
# print(res)

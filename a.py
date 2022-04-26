import pymysql
import os
import time

import datetime
# print('Please provide the username and password:')
# username=input('username:')
# password=input('password:')
i = datetime.datetime.now()
a=str(i).split()[0]
#

print(a>'2021-01-01')
#
# try:
#     conn = pymysql.connect(host='localhost', user='root', password='0000',
#                           db='library', charset='utf8mb4',
#                           cursorclass=pymysql.cursors.DictCursor)
#
# except pymysql.err.OperationalError:
#     print('Error: %d: %s' % (e.args[0], e.args[1]))
#
# cur = conn.cursor()
# user_id=input('User ID:')
# room_id=input('Room ID:')
# date=input('Borrow date(yyyy-mm-dd):')
# select = "select start_time, end_time from user_room_record where date_current='"+ date +"';"
# cur.execute(select)
# result=cur.fetchall()
# ans,flag=[],0
# if len(result):
#     for i in result:
#         tmp=[]
#         tmp.append(i['start_time'])
#         tmp.append(i['end_time'])
#         ans.append(tmp)
#     print("Unavailable time slots:\n",ans)
# start=int(input("Choose start time(hh):"))
# end=int(input("Choose end time(hh):"))
# if len(result):
#     t=[start,end]
#     if start>=end:
#         print("Wrong time slot, retry!")
#         flag=1
#     else:
#         for i,j in ans:
#             if not (i>=t[1] or j<=t[0]):
#                 print("Time conflict, retry!")
#                 flag=1
# if flag==0:
#     cur.callproc("insert_room_record",(user_id,room_id,date,start,end,-1))
#     conn.commit()
#     cur.execute("select @_insert_room_record_5")
#     flag1=cur.fetchall()[0]['@_insert_room_record_5']
#     if flag1==2:
#         print("Room not exists")
#     elif flag==1:
#         print("User not exists")
#     else:
#         print("Success!")
# cur.close()
# input('Press to continue...')
# os.system('cls')
# borrowMenu()

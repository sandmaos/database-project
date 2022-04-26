import pymysql
import os
import time
import datetime
# print('Please provide the username and password:')
# username=input('username:')
# password=input('password:')

try:
    conn = pymysql.connect(host='localhost', user='root', password='0000',
                          db='library', charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)

except pymysql.err.OperationalError:
    print('Error: %d: %s' % (e.args[0], e.args[1]))


######################### Book ########################
def toBook():
    flag=1
    bookMenu()
    while flag!='0':
        flag=input('Choose to continue:')
        if flag=='1':
            getBook()
        elif flag=='2':
            addBook()
        elif flag=='3':
            deleteBook()
    print("Return to main page...")
    time.sleep(2)
    os.system('cls')

def bookMenu():
    print("\t\t\t\t╔══════════════════════════════════╗")
    print("\t\t\t\t║             **Book**             ║")
    print("\t\t\t\t╠══════════════════════════════════╣")
    print("\t\t\t\t║      1 - Book List               ║")
    print("\t\t\t\t║      2 - Add Book                ║")
    print("\t\t\t\t║      3 - Delete Book             ║")
    print("\t\t\t\t║      0 - Return                  ║")
    print("\t\t\t\t╚══════════════════════════════════╝\n")

def getBook():
    try:
        cur = conn.cursor()
        select = "select * from book"
        cur.execute(select)
        print("{:10} {:70} {:30} {:}".format("book_id","book_name","author","availability"))
        for book in cur.fetchall():
            print("{:10} {:70} {:30} {:}".format(book["book_id"],book["book_name"],book["author"],book["availability"]))
        cur.close()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

def addBook():
    try:
        book_id=input('Book ID:')
        book_name=input('Book name:')
        ISBN=input('ISBN:')
        publisher_id=input('Publisher id:')
        author=input('Author:')
        availability='Available'
        cur = conn.cursor()


        cur.close()
        input('Press to continue...')
        os.system('cls')
        bookMenu()

    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

def deleteBook():
    try:
        book_id=input('Book ID:')
        cur = conn.cursor()
        cur.callproc("delete_book",(book_id,-1))
        conn.commit()
        cur.execute("select @_delete_book_1")
        flag=cur.fetchall()[0]['@_delete_book_1']
        if flag==3:
            print("Book removed")
        elif flag==2:
            print("Book not returned")
        elif flag==1:
            print("Book not exists")
        cur.close()
        input('Press to continue...')
        os.system('cls')
        bookMenu()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))



######################### User ########################
def toUser():
    flag=1
    userMenu()
    while flag!='0':
        flag=input('Choose to continue:')
        if flag=='1':
            getUser()
        elif flag=='2':
            addUser()
        elif flag=='3':
            deleteUser()
    print("Return to main page...")
    time.sleep(2)
    os.system('cls')

def userMenu():
    print("\t\t\t\t╔══════════════════════════════════╗")
    print("\t\t\t\t║             **User**             ║")
    print("\t\t\t\t╠══════════════════════════════════╣")
    print("\t\t\t\t║      1 - User List               ║")
    print("\t\t\t\t║      2 - Add User                ║")
    print("\t\t\t\t║      3 - Delete User             ║")
    print("\t\t\t\t║      0 - Return                  ║")
    print("\t\t\t\t╚══════════════════════════════════╝\n")

def getUser():
    try:
        cur = conn.cursor()
        select = "select * from user"
        cur.execute(select)
        print("{:20} {:20} {:20} {:}".format("user_id","user_name"))
        for user in cur.fetchall():
            print("{:20} {:20} {:20} {:}".format(user["user_id"],user["user_name"]))
        cur.close()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

def addUser():
    user_name=input('User name:')
    cur = conn.cursor()
    query="insert into users(user_name) values('"+user_name+"');"
    cur.execute(query)
    conn.commit()

def deleteUser():
    try:
        user_id=input('User ID:')
        cur = conn.cursor()
        cur.callproc("delete_user",(user_id,-1))
        conn.commit()
        cur.execute("select @_delete_user_1")
        flag=cur.fetchall()[0]['@_delete_user_1']
        if flag==3:
            print("User removed")
        elif flag==2:
            print("Have book not returned")
        elif flag==1:
            print("User not exists")
        cur.close()
        input('Press to continue...')
        os.system('cls')
        userMenu()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

######################### Borrow and Return ########################
def toBorrowReturn():
    flag=1
    borrowMenu()
    while flag!='0':
        flag=input('Choose to continue:')
        if flag=='1':
            getUser()
        elif flag=='2':
            getBook()
        elif flag=='3':
            getRoom()
        elif flag=='4':
            returnBook()
        elif flag=='5':
            borrowBook()
        elif flag=='6':
            returnBook()
        elif flag=='7':
            borrowRoom()
        elif flag=='8':
            returnRoom()
    print("Return to main page...")
    time.sleep(2)
    os.system('cls')

def borrowMenu():
    print("\t\t\t\t╔══════════════════════════════════╗")
    print("\t\t\t\t║       **Borrow and Return**      ║")
    print("\t\t\t\t╠══════════════════════════════════╣")
    print("\t\t\t\t║      1 - User List               ║")
    print("\t\t\t\t║      2 - Book List               ║")
    print("\t\t\t\t║      3 - Room List               ║")
    print("\t\t\t\t║      5 - Borrow Book             ║")
    print("\t\t\t\t║      6 - Return Book             ║")
    print("\t\t\t\t║      7 - Borrow Room             ║")
    print("\t\t\t\t║      8 - Return Room             ║")
    print("\t\t\t\t║      0 - Return                  ║")
    print("\t\t\t\t╚══════════════════════════════════╝\n")

def getUser():
    try:
        cur = conn.cursor()
        select = "select * from users"
        cur.execute(select)
        print("{:20} {:20}".format("user_id","user_name"))
        for user in cur.fetchall():
            print("{:20}  {:}".format(user["user_id"],user["user_name"]))
        cur.close()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))


def borrowBook():
    try:
        user_id=input('User ID:')
        book_id=input('Book ID:')
        start_time=input('Borrow date(yyyy-mm-dd):')
        estimated_end_time=input('Estimated return date(yyyy-mm-dd):')
        cur = conn.cursor()
        cur.callproc("Borrow_book",(user_id,book_id,start_time,estimated_end_time,-1))
        conn.commit()
        cur.execute("select @_Borrow_book_4")
        flag=cur.fetchall()[0]['@_Borrow_book_4']
        if flag==5:
            print("Success")
        elif flag==4:
            print("Book not available")
        elif flag==3:
            print("Beyond max book for this user")
        elif flag==2:
            print("Book not exists")
        elif flag==1:
            print("User not exists")
        cur.close()
        input('Press to continue...')
        os.system('cls')
        borrowMenu()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

def returnBook():
    try:
        user_id=input('User ID:')
        book_id=input('Book ID:')
        real_end_time=input('Real return date(yyyy-mm-dd):')
        cur = conn.cursor()
        cur.callproc("Return_book",(user_id,book_id,real_end_time,-1,-1))
        conn.commit()
        cur.execute("select @_Return_book_3")
        flag_success=cur.fetchall()[0]['@_Return_book_3']
        cur.execute("select @_Return_book_4")
        flag_penality=cur.fetchall()[0]['@_Return_book_4']
        if flag_success==4:
            if flag_penality==0:
                print("Success, no penality")
            else:
                print("Success, have overdue penality")
        elif flag_success==3:
            print("Record of this book not exists")
        elif flag_success==2:
            print("Book not exists")
        elif flag_success==1:
            print("User not exists")
        cur.close()
        input('Press to continue...')
        os.system('cls')
        borrowMenu()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))


def borrowRoom():
    try:
        cur = conn.cursor()
        user_id=input('User ID:')
        room_id=input('Room ID:')
        current=datetime.datetime.now()
        now=str(current).split()[0]
        while True:
            date=input('Borrow date(yyyy-mm-dd):')
            if now>date:
                print("Wrong date, retry!")
            else:   break
        select = "select start_time, end_time from user_room_record where date_current='"+ date +"';"
        cur.execute(select)
        result=cur.fetchall()
        ans,flag=[],0
        if len(result):
            for i in result:
                tmp=[]
                tmp.append(i['start_time'])
                tmp.append(i['end_time'])
                ans.append(tmp)
            print("Unavailable time slots:\n",ans)
        start=int(input("Choose start time(hh):"))
        end=int(input("Choose end time(hh):"))
        if start>=end:
            print("Wrong time slot, retry!")
            flag=1
        if len(result):
            t=[start,end]
            for i,j in ans:
                if not (i>=t[1] or j<=t[0]):
                    print("Time conflict, retry!")
                    flag=1
        if flag==0:
            cur.callproc("insert_room_record",(user_id,room_id,date,start,end,-1))
            conn.commit()
            cur.execute("select @_insert_room_record_5")
            flag1=cur.fetchall()[0]['@_insert_room_record_5']
            if flag1==2:
                print("Room not exists")
            elif flag==1:
                print("User not exists")
            else:
                print("Success!")
        cur.close()
        input('Press to continue...')
        os.system('cls')
        borrowMenu()

    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))


######################### Records ########################
def toRecords():
    flag=1
    recordsMenu()
    while flag!='0':
        flag=input('Choose to continue:')
        if flag=='1':
            getBorrowRecords()
        elif flag=='2':
            getRoomRecords()
    print("Return to main page...")
    time.sleep(2)
    os.system('cls')

def recordsMenu():
    print("\t\t\t\t╔══════════════════════════════════╗")
    print("\t\t\t\t║           **Records**            ║")
    print("\t\t\t\t╠══════════════════════════════════╣")
    print("\t\t\t\t║      1 - Borrow Records          ║")
    print("\t\t\t\t║      2 - Room Records            ║")
    print("\t\t\t\t║      0 - Return                  ║")
    print("\t\t\t\t╚══════════════════════════════════╝\n")

def getBorrowRecords():
    try:
        cur = conn.cursor()
        select = "select * from borrow_record"
        cur.execute(select)
        print("{:<{}} {:<{}} {:<{}} {:<{}} {:<{}} {:<{}}".format("book_id",15,"user_id",15,"borrow_time",15,"estimated_end",15,"real_end",15,"penalty",15))
        for record in cur.fetchall():
            print('%-15s%-17s%-17s%-15s%-15s%s'%(record["book_id"],record["user_id"],record["borrow_time_start"], record["borrow_time_Estimated_end"],
            record["borrow_time_real_end"] if record["borrow_time_real_end"] else 'None',record["penalty"] if record["penalty"] else 'None' ))
        cur.close()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))


def getRoomRecords():
    try:
        cur = conn.cursor()
        select = "select * from user_room_record"
        cur.execute(select)
        print("{:20} {:20} {:20} {:20} {:20} {:}".format("user_id","room_id","borrow_time","estimated_end","real_end","penalty"))
        for record in cur.fetchall():
            print("{:20} {:20} {:20} {:20} {:20} {:}".format(record["book_id"],record["user_id"],record["borrow_time_start"],record["borrow_time_Estimated_end"],record["borrow_time_real_end"],record["penalty"]))
        cur.close()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))


######################### Publisher ########################
def toPublisher():
    flag=1
    publisherMenu()
    while flag!='0':
        flag=input('Choose to continue:')
        if flag=='1':
            getPublisher()
        elif flag=='2':
            addPublisher()
        elif flag=='3':
            deletePublisher()
    print("Return to main page...")
    time.sleep(2)
    os.system('cls')

def publisherMenu():
    print("\t\t\t\t╔══════════════════════════════════╗")
    print("\t\t\t\t║           **Publisher**          ║")
    print("\t\t\t\t╠══════════════════════════════════╣")
    print("\t\t\t\t║      1 - Publisher List          ║")
    print("\t\t\t\t║      2 - Add Publisher           ║")
    print("\t\t\t\t║      3 - Delete Publisher        ║")
    print("\t\t\t\t║      0 - Return                  ║")
    print("\t\t\t\t╚══════════════════════════════════╝\n")

def getPublisher():
    try:
        cur = conn.cursor()
        select = "select * from publisher"
        cur.execute(select)
        rows=cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

def addPublisher():
    time.sleep(2)

def deletePublisher():
    time.sleep(2)



######################### Room ########################
def toRoom():
    flag=1
    roomMenu()
    while flag!='0':
        flag=input('Choose to continue:')
        if flag=='1':
            getRoom()
        elif flag=='2':
            addRoom()
        elif flag=='3':
            deleteRoom()
    print("Return to main page...")
    time.sleep(2)
    os.system('cls')

def roomMenu():
    print("\t\t\t\t╔══════════════════════════════════╗")
    print("\t\t\t\t║             **Room**             ║")
    print("\t\t\t\t╠══════════════════════════════════╣")
    print("\t\t\t\t║      1 - Room List               ║")
    print("\t\t\t\t║      2 - Add Room                ║")
    print("\t\t\t\t║      3 - Delete Room             ║")
    print("\t\t\t\t║      0 - Return                  ║")
    print("\t\t\t\t╚══════════════════════════════════╝\n")

def getRoom():
    try:
        cur = conn.cursor()
        select = "select * from study_room"
        cur.execute(select)
        print("{:20}".format("room_id"))
        for room in cur.fetchall():
            print("{:20}".format(room["room_id"]))
        cur.close()
    except pymysql.Error as e:
        print('Error: %d: %s' % (e.args[0], e.args[1]))

def addRoom():
    time.sleep(2)

def deleteRoom():
    time.sleep(2)


######################### Main ########################
flag=1
while flag!='0':
    os.system('cls')
    print("\t\t\t\t╔══════════════════════════════════╗")
    print("\t\t\t\t║  **Welcome To Library System**   ║")
    print("\t\t\t\t╠══════════════════════════════════╣")
    print("\t\t\t\t║      1 - Book                    ║")
    print("\t\t\t\t║      2 - User                    ║")
    print("\t\t\t\t║      3 - Borrow and return       ║")
    print("\t\t\t\t║      4 - Publisher               ║")
    print("\t\t\t\t║      5 - Room                    ║")
    print("\t\t\t\t║      6 - Records                 ║")
    print("\t\t\t\t║      0 - Quit                    ║")
    print("\t\t\t\t╚══════════════════════════════════╝\n")
    flag=input('Choose to continue:')
    if flag=='1':
        os.system('cls')
        toBook()
    elif flag=='2':
        os.system('cls')
        toUser()
    elif flag=='3':
        os.system('cls')
        toBorrowReturn()
    elif flag=='4':
        os.system('cls')
        toPublisher()
    elif flag=='5':
        os.system('cls')
        toRoom()
    elif flag=='6':
        os.system('cls')
        toRecords()

conn.close()

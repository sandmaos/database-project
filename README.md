# library management system
This is the readme file for library management system. 
## Project setup
First build up the library database using the provided .sql file.

To install pymysql library, run
```
pip insatll pymysql 
```
Application initialization
```
python db.py
```
Then provide the username and password to connect MySQL at port 3306.

Main menu:
```
        ╔══════════════════════════════════╗
        ║  **Welcome To Library System**   ║
        ╠══════════════════════════════════╣
        ║      1 - Book                    ║
        ║      2 - User                    ║
        ║      3 - Borrow Service          ║
        ║      4 - Room Register           ║
        ║      5 - Room                    ║
        ║      6 - Publisher               ║
        ║      7 - Files                   ║
        ║      0 - Quit                    ║
        ╚══════════════════════════════════╝
```
<<<<<<< HEAD
=======

>>>>>>> 92c833d2bc3a2a912495c23aabea45a1db23fe68
1. Book menu allows admin to search books by ISBN, keyword and book_id, also allows admin to delete books.
2. User menu allows admin to search user, add user and deletd user.
3. Borrow Service allows admin help user to borrow and return books, also manages the overdue fines.
4. Room Register menu allows admin help user to register for a studing room.
5. Room menu allows admin get room information and track the screen, seat and table in the room.
6. Publisher menu allows admin to add a publisher.
7. Files menu allows user uploade and print the file.

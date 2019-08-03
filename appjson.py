from utils import database_json


print("enter :\n - 'a' to add a new book \n - 'l' to list all books \n - 'r' to mark book as read \n - 'd' to delete a book \n - 'q' to quit \n ")
database_json.create_json ()
while True :
    USER_CHOICE = input('enter the code to perform the desired function: ')
    if USER_CHOICE == 'a' :
        database_json.add()

    elif USER_CHOICE == 'l' :
        lists=database_json.list_all_books()
        print(lists)

    elif USER_CHOICE == 'r' :
        database_json.mark_book()

    elif USER_CHOICE == 'd':
        database_json.delete_book()

    elif USER_CHOICE == 'q' :
            print('exiting from the program')
            break
    else :
        print('invalid input.')
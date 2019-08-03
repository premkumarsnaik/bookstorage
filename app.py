from utils import database


print("enter :\n - 'a' to add a new book \n - 'l' to list all books \n - 'r' to mark book as read \n - 'd' to delete a book \n - 'q' to quit \n ")


while True :
    USER_CHOICE = input('enter the code to perform the desired function: ')
    if USER_CHOICE == 'a' :
        database.add()

    elif USER_CHOICE == 'l' :
        database.list_all_books()

    elif USER_CHOICE == 'r' :
        database.mark_book()

    elif USER_CHOICE == 'd':
        database.book_store = database.delete_book()

    elif USER_CHOICE == 'q' :
            print('exiting from the program')
            break
    else :
        print('invalid input.')

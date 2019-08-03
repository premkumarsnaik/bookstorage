from utils import ddatabase

print("enter :\n - 'a' to add a new book \n - 'l' to list all books \n - 'r' to mark book as read \n - 'd' to delete a book \n - 'q' to quit \n ")
ddatabase.create_book()
while True :
    USER_CHOICE = input('enter the code to perform the desired function: ')
    if USER_CHOICE == 'a' :
        ddatabase.add()

    elif USER_CHOICE == 'l' :
        lists=ddatabase.list_all_books()
        print(lists)

    elif USER_CHOICE == 'r' :
        ddatabase.mark_book()

    elif USER_CHOICE == 'd':
        ddatabase.delete_book()

    elif USER_CHOICE == 'q' :
            print('exiting from the program')
            break
    else :
        print('invalid input.')
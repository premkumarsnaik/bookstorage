from utils import database_csv


print("enter :\n - 'a' to add a new book \n - 'l' to list all books \n - 'r' to mark book as read \n - 'd' to delete a book \n - 'q' to quit \n ")

sample_csv_value = ','.join(['name','author','read'])

with open('utils.csvfile.txt','w') as book_store :
    book_store.write(sample_csv_value)


while True :
    USER_CHOICE = input('enter the code to perform the desired function: ')
    if USER_CHOICE == 'a' :
        database_csv.add()

    elif USER_CHOICE == 'l' :
        database_csv.list_all_books()

    elif USER_CHOICE == 'r' :
        database_csv.mark_book()

    elif USER_CHOICE == 'd':
        database_csv.delete_book()

    elif USER_CHOICE == 'q' :
            print('exiting from the program')
            break
    else :
        print('invalid input.')

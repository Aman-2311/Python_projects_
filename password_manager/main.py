from manager import add_password,view_passwords,search_password,delete_password

def menu():
    while True:
        print("1. Add new password")
        print("2. View passwords")
        print("3. Search passwords")
        print("4. Delete passwords")
        print("5. Exit")

        choice =input("Enter your choice: ")

        if choice =="1":
            add_password()
        elif choice =="2":
            view_passwords()
        elif choice =="3":
            search_password()
        elif choice =="4":
            delete_password()
        elif choice =="5":
            exit()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
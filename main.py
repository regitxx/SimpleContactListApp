def main():
    contacts = {}
    while True:
        print("\nContact List Manager")
        print("1. Add new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Delete a contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contacts[name] = phone
            print(f"Contact '{name}' added successfully!")
        elif choice == '2':
            if contacts:
                print("\nAll Contacts:")
                for name, phone in contacts.items():
                    print(f"Name: {name}, Phone: {phone}")
            else:
                print("No contacts to display.")
        elif choice == '3':
            search_name = input("Enter the name to search: ")
            if search_name in contacts:
                print(f"Found contact: Name: {search_name}, Phone: {contacts[search_name]}")
            else:
                print(f"No contact found with the name: {search_name}")
        elif choice == '4':
            del_name = input("Enter the name of the contact to delete: ")
            if del_name in contacts:
                del contacts[del_name]
                print(f"Contact '{del_name}' deleted successfully!")
            else:
                print(f"No contact found with the name: {del_name}")
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-5).")
if __name__ == "__main__":
    main()

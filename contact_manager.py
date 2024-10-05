import re

contacts = {}

def add_contact(name, mobile):
    try:
        if not re.match(r'^\+\d{1,3}\d{10}$', mobile):
            raise ValueError("Invalid phone number. It must start with '+' and include a country code followed by exactly 10 digits.")
        
        if name in contacts:
            merge_choice = input(f"Contact '{name}' already exists. Do you want to merge this mobile number with the existing contact? (y/n): ").lower()
            
            if merge_choice == 'y':
                if mobile not in contacts[name]:
                    contacts[name].append(mobile)
                    print(f"Contact '{name}' updated with the new number.")
                else:
                    print("This mobile number is already associated with this contact.")
            else:
                print(f"Contact '{name}' not modified.")
        else:
            contacts[name] = [mobile]
            print(f"Contact '{name}' added successfully.")
    
    except ValueError as ve:
        print(f"Error: {ve}")

def search_contact(name):
    if name in contacts:
        for i, mobile in enumerate(contacts[name], start=1):
            print(f"Mobile {i}: {mobile}")
    else:
        print(f"Contact '{name}' not found.")

def main():
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ")
        
        if choice == '1':
            name = input("Enter name: ")
            
            while True:
                mobile = input("Enter mobile number with the country code :  ")
                if re.match(r'^\+\d{1,3}\d{10}$', mobile):
                    add_contact(name, mobile)
                    break
                else:
                    print("Invalid mobile number. Please enter a valid number starting with '+' followed by country code and 10 digits.")
            
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(name)
        
        elif choice == '3':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

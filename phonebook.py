# Phonebook Application

import re
import json

# Initialize an empty dictionary for the phonebook
phonebook = {}

def display_menu():
    """Display the menu options to the user."""
    print("\nPhonebook Menu:")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. List All Contacts")
    print("5. Exit")

def is_valid_number(number):
    """Validate the phone number to be exactly 10 digits."""
    pattern = r"^\d{10}$"  # Example: 10-digit number
    return bool(re.match(pattern, number))

def add_contact():
    """Add a new contact to the phonebook."""
    name = input("Enter the contact name: ").strip()
    if name in phonebook:
        print(f"Contact '{name}' already exists.")
    else:
        number = input("Enter the contact number (10 digits): ").strip()
        if is_valid_number(number):
            phonebook[name] = number
            print(f"Contact '{name}' added successfully.")
        else:
            print("Invalid phone number. Please enter a 10-digit number.")

def search_contact():
    """Search for a contact by name."""
    name = input("Enter the name to search for: ").strip().lower()
    for contact_name, number in phonebook.items():
        if contact_name.lower() == name:
            print(f"Name: {contact_name}, Number: {number}")
            return
    print(f"No contact found with the name '{name}'.")

def delete_contact():
    """Delete a contact from the phonebook."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")

def list_contacts():
    """List all contacts in the phonebook."""
    if phonebook:
        print("\nPhonebook Contacts:")
        for name, number in phonebook.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("The phonebook is empty.")

def save_phonebook():
    """Save phonebook to a file."""
    with open("phonebook.json", "w") as file:
        json.dump(phonebook, file)

def load_phonebook():
    """Load phonebook from a file."""
    global phonebook
    try:
        with open("phonebook.json", "r") as file:
            phonebook = json.load(file)
    except FileNotFoundError:
        phonebook = {}

def main():
    """Main function to run the phonebook application."""
    load_phonebook()  # Load existing phonebook on startup
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            save_phonebook()  # Save phonebook before exiting
            print("Exiting the Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
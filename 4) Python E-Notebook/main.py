from notes_module import add_note, view_notes
from validation import get_valid_name, get_nonempty, get_menu_choice

seprator = '-' * 40

def show_menu():
    print("\n===== Python E-Notebook =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == "1":
            name = get_valid_name("Enter Python E-Note Generator Name: ")
            title = get_nonempty("Enter E-Note Title: ")
            description = get_nonempty("Enter E-Note Description: ")

            add_note(name, title, description)
            print("Note Added Successfully")
            print(seprator)

        elif choice == "2":
            view_notes()
        
        elif choice == "3":
            print("Exiting...")
            break

if __name__ == "__main__": \
    # main only runs when main.py file called
    main()
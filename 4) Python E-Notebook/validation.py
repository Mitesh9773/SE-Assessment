def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if name.replace(" ", "").isalpha() and name != "":
            return name
        print("ERROR: Please enter only letter and spaces.")

def get_nonempty(prompt):
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("ERROR: This feild cannot be empty.")
    
def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return choice
        print("ERROR: Please enter 1, 2, or 3")
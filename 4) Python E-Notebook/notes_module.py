import datetime

seprator = "-" * 40
notes_file = "notes.txt"

def ensure_notes_file():
    """Create notes.txt if it doesn't exist"""
    try:
        open(notes_file, "a", encoding="utf-8").close()
    except:
        pass

def add_note(name: str, title: str, description: str):
    """Add a note to the notes.txt file"""
    ensure_notes_file()
    ts = str(datetime.now())

    block = (
        f"{seprator}\n"
        f"{ts}\n"
        f"E-Note Title : {title}\n"
        f"E-Note Description : {description}\n"
        f"                Note Generator : {name}\n"
    )

    with open(notes_file, "a", encoding="utf-8") as f:
        f.write(block)

def view_notes():
    """View all notes in the notes.txt file"""
    ensure_notes_file()
    with open(notes_file, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        print("No notes found.")
    else:

        print(content)

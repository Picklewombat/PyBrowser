# Terminal Notepad

print("Welcome to Terminal Notepad!")
print("Start typing your notes below. Type 'SAVE' to save and exit.\n")

notes = []

while True:
    line = input("|")
    if line.upper() == "SAVE":
        with open("notes.txt", "w") as file:
            file.write("\n".join(notes))
        print("\nNotes saved to 'notes.txt'. Goodbye!")
        break
    else:
        notes.append(line)

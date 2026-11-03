
# PLP Python Week 7 Assignment
# Program 1: Save, append, and read notes

# Write the first note
with open("notes.txt", "w") as file:
    file.write("My first Python note.\n")

# Add another note without deleting the first one
with open("notes.txt", "a") as file:
    file.write("I am learning Python file handling.\n")

# Read and display all saved notes
try:
    with open("notes.txt", "r") as file:
        print("My Saved Notes:")
        print(file.read())

except FileNotFoundError:
    print("The notes file was not found.")

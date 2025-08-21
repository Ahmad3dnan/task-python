name = input("ُEnter your name: ")
notes = input("Enter your notes: ")

with open("file.txt", "w") as f:
    f.write(f"Hello everyone my name is {name} \nSome of my information {notes}.")

with open("file.txt", "r") as f:
    print(f.read())
    
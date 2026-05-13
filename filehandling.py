# A simple practical file handling project

from pathlib import Path

def readfilelandfolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        if ".git" not in item.parts:
            print(f"{i+1} : {item}")

def createfile():

    try:

        readfilelandfolder()

        name = input("please tell your file name :- ")
        p = Path(name)

        if not p.exists():

            with open(p, "w") as fs:
                data = input("what you want to write in this file :- ")
                fs.write(data)

            print("file created successfully")

        else:
            print("this file already exist")

    except Exception as err:
        print(f"an error occured as {err}")

def readfile():

    try:

        readfilelandfolder()

        name = input("please tell file name to read :- ")
        p = Path(name)

        if p.exists():

            with open(p, "r") as fs:
                data = fs.read()

            print("\nfile content is :- \n")
            print(data)

        else:
            print("file does not exist")

    except Exception as err:
        print(f"an error occured as {err}")

def updatefile():

    try:

        readfilelandfolder()

        name = input("please tell file name to update :- ")
        p = Path(name)

        if p.exists():

            with open(p, "a") as fs:
                data = input("what you want to add :- ")
                fs.write("\n" + data)

            print("file updated successfully")

        else:
            print("file does not exist")

    except Exception as err:
        print(f"an error occured as {err}")

def deletefile():

    try:

        readfilelandfolder()

        name = input("please tell file name to delete :- ")
        p = Path(name)

        if p.exists():

            p.unlink()

            print("file deleted successfully")

        else:
            print("file does not exist")

    except Exception as err:
        print(f"an error occured as {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your response :- "))

if check == 1:
    createfile()

elif check == 2:
    readfile()

elif check == 3:
    updatefile()

elif check == 4:
    deletefile()

else:
    print("invalid choice")
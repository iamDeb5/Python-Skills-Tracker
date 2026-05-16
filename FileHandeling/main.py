from pathlib import Path
import os


def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items} ")



def createFile():
    try:
        
        readFileAndFolder()
        name = input("Please tell your file name :- ")
        p = Path(name)
        
        if not p.exists():
            
            with open(p, "w") as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)
                
            print(F"FILE CREATED SUCCESFULLY")
            
        else:
            print("This file already exist ")
        
    except Exception as err:
        print(f"An error occured as {err} ")
        
        
        
def readFile():
    
    try:
        
        readFileAndFolder()
        name = input("Which file you want to read :- ")
        p = Path(name)
        if p.exists and p.is_file:
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
                
            print("READED SUCCESFULLY")
        else:
            print("The file doesn't exist")
            
    except Exception as err:
        print(f"An error occured as {err}")
        


def updateFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to update :- ")
        p = Path(name)
        
        if p.exists and p.is_file:
            print("Press 1 for change the name of your file :- ")
            print("Press 2 for overwriting the data of your file :- ")
            print("Press 3 for appending some content in your file :- ")
            
            res = int(input("Tell your response :- "))
            
            if res == 1:
                name2 = input("Type your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
                
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("What you want to write this is overwrite the data :- ")
                    fs.write(data)
                    
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("What you want to append this is append the data :- ")
                    fs.write(" "+data)

    except Exception as err:
        print(f"An error occured as {err}")
        
        
        
def deleteFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to delete :- ")
        p = Path(name)
        
        if p.exists and p.is_file:
            os.remove(p)
            print("File remove succesfully")
            
        else:
            print("No such file exist")
            
    except Exception as err:
        print(f"An error occured as {err}")
        
        
        
        

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please enter your response :- "))

if check == 1:
    createFile()
    
if check == 2:
    readFile()
    
if check == 3:
    updateFile()
    
if check == 4:
    deleteFile()
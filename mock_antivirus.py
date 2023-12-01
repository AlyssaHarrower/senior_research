
from tkinter import *
from tkinter.ttk import *

 
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

#set up tkinter window and dimensions
root = Tk()
root.geometry('200x100')

#signature variable retrieved from file
f = open('BinSignature.txt', 'r')
sig = str(f.read())
f.close()
 
# This function will be used to open and read the file chosen
def open_file():
    f = askopenfile(mode ='b+r', filetypes =[('Executable Files', '*.exe')])
    if f is not None:
        filedata = str(f.read())
        f.close()
        filebin = ''.join(format(ord(i), '08b') for i in filedata)
        if sig in filebin: #checks for binary signature in file binary
            print("detected")  
        else:
            print("not detected") 
 
#button on GUI that will allow user to retrieve a specific .exe file
btn = Button(root, text ='Open file', command = lambda:open_file())
btn.pack(side = TOP, pady = 10)

mainloop()

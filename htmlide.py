from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import random
import os
import webbrowser
root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("Notepad PT.2")
openimg=ImageTk.PhotoImage(Image.open("open.png"))

runimg = Image.open("play.png")
runimg=runimg.resize((25,25))
exitimg=ImageTk.PhotoImage(runimg)
saveimg=ImageTk.PhotoImage(Image.open("save.png"))
label1=Label(root,text="File Name")
label1.place(relx=0.5, rely=0.1,anchor=CENTER)
inputbox=Entry(root)
inputbox.place(relx=0.7,rely=0.1,anchor=CENTER)
textbox=Text(root, height=40, width=80)
textbox.place(relx=0.5, rely=0.7,anchor=CENTER)
name=""
def openfile():
    global name
    textbox.delete(1.0, END)
    inputbox.delete(0, END)
    textfile=filedialog.askopenfilename(title="Open Text File",filetypes=(("Text File","*.html"),))
    print(textfile)
    name=os.path.basename(textfile)
    formatedname=name.split('.')[0]
    inputbox.insert(END, formatedname)
    root.title(formatedname)
    textfile=open(name,'r')
    paragraph=textfile.read()
    textbox.insert(END, paragraph)
    textfile.close()

def save():
    input_name= inputbox.get()
    file=open(input_name+".html","w")
    data=  textbox.get("1.0",END)
    print(data)
    file.write(data)
    inputbox.delete(0,END)
    textbox.delete(1.0,END)
    messagebox.showinfo("Update","Success")

def run():
    global name
    webbrowser.open(name)

button1=Button(root,text="Open File",image=openimg, command=openfile)
button1.place(relx=0.1, rely=0.1,anchor=CENTER)
button2=Button(root,text="Run File",image=exitimg, command=run)
button2.place(relx=0.2, rely=0.1,anchor=CENTER)
button3=Button(root,text="Save File",image=saveimg, command=save)
button3.place(relx=0.3, rely=0.1,anchor=CENTER)


root.mainloop()
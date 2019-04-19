from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from cryptography.fernet import Fernet
import datetime
import sys
import os.path
import time



def new_key():
    txt.insert(INSERT,'Generating a new key will overwrite the existing key and thus you wont be able to decrypt your written diary\n') 
    txt.insert(INSERT,'All your information would be lost\n')                                   #to print the given text on the textbox
    txt.insert(INSERT,"Do you wish to continue Y/N\n")
    flagBox = messagebox.askquestion ('Warning','Do you wish to continue Y/N',icon = 'warning') #messagebox yes or no input
    
    if flagBox == 'yes':                                                                        #if flag == 'Y'
        if os.path.exists("key.key"):
            os.remove("key.key")
        key=Fernet.generate_key()
        txt.insert(INSERT,key)
        fkey=open("key.key","wb")                                                               #saving key in a txt file
        fkey.write(key)
        fkey.close()
    else:
        txt.insert(INSERT,'Not generated')
        

def write_save():                                                                               #Just to print the date and time on text box
    now = datetime.datetime.now()
    mtxt.insert(INSERT,now.strftime("%Y-%m-%d %H:%M\n"))                                        #prints date and time
    mtxt.insert(INSERT,"About today.\n")                                                    #reads multiple line input from user
   

def write_fh():
    now = datetime.datetime.now()
    dtxt = mtxt.get("1.0",END)
    #File handling part
    #if os.path.exists("Diary.txt")==False and os.path.exists("Diary.encrypted"):
       # decrypt()
    file=open("Diary.txt","a")
    ##dtxt = ''.join(msg) #converts list to a string
    ##mtxt.insert(INSERT,dtxt)
    ##file.write(now.strftime("\n~ %Y-%m-%d %H:%M \n \n"))
    file.write(dtxt)
    file.write('-'*80)
    file.write('\n')
    mtxt.insert(INSERT,'\n')
    file.close()
    ##mtxt.insert(INSERT,'-'*80) #for horizontal dashes
    

def encrypt():
    #keytp()
    # File Encryption
    file=open("Diary.txt","rb")
    data=file.read()
    file.close()
    fer=Fernet(key)
    encrypted=fer.encrypt(data)
    file=open("Diary.encrypted","wb") #writing encrypted file
    file.write(encrypted)
    file.close()

def delog():
    #Deleting the original diary file
    if os.path.exists("Diary.txt"):
        os.remove("Diary.txt")

def decrypt():
    #keytp()
    #Decrypting the file
    file=open("Diary.encrypted","rb")
    data=file.read()
    file.close()
    fer=Fernet(key)
    decrypted=fer.decrypt(data)
    file=open("Diary.txt","wb") #writing decrypted file
    file.write(decrypted)
    file.close()
    messagebox.showinfo('Decrypted', 'Decrypted The Diary')

def erase():
    delog()
    if os.path.exists("key.key"):
        os.remove("key.key")
    if os.path.exists("Diary.encrypted"):
        os.remove("Diary.encrypted")
    messagebox.showinfo('Erased', 'Erased All The Traces')#Erase done messagebox

def b2():
    write_fh()
    encrypt()
    #delog()
    mtxt.delete(1.0,END) #clear The main Textbox

    
def exitw():
    exitBox = messagebox.askquestion ('Warning','Do you want to exit',icon = 'warning') #exitmessagebox
    if exitBox== 'yes':
        window.destroy()
        delog()
        exit()
    else:
        flagstop=0
    
#root = Tk()

window = Tk()
window.title("Encrypted Diary")
window.geometry('900x450')
window.configure(background="wheat2")
window.iconbitmap(default='Diary.ico')



frame1 = Frame(window)                                                              #F1
frame1.pack()
lbl = Label(frame1, text="OSTL Mini Project") #test label
lbl.grid(row=1, column=1, sticky=W)

frame2 = Frame(window)                                                              #F2
frame2.pack()
txt = scrolledtext.ScrolledText(frame2,width=60,height=7)  #The progess textbox
txt.grid(column=0,row=1)

frame3 = Frame(window)                                                              #F3
frame3.pack()
b1 = Button(frame3, text="Take input in Diary", command = b2, cursor = "sizing")
b1.pack(side=LEFT)


frame4 = Frame(window)                                                              #F4
frame4.pack()
b2 = Button(frame4, text="Write\nin Diary", command=write_save, cursor = "arrow")
b3 = Button(frame4, text="Decrypt\nthe Diary", command=decrypt, cursor = "arrow")
b6 = Button(frame4, text="Generate \na new key", command=new_key, cursor = "exchange")
b2.pack(side=LEFT) 
b3.pack(side=LEFT)
b6.pack(side = LEFT)




frame6 = Frame(window)                                                              #F6
frame6.pack()
mtxt = scrolledtext.ScrolledText(frame6,width=40,height=10)  #The main textbox where we will write in diary
mtxt.grid(column=0,row=5)

frame7 = Frame(window)                                                              #F7
frame7.pack()
b4 = Button(frame7, text="Erase all traces", command=erase)
b4.pack(side = LEFT)

frame8 = Frame(window)                                                              #F8
frame8.pack()
b5 = Button(frame8, text="Exit", command=exitw, cursor = "heart")
b5.pack(side = LEFT)

txt.insert(INSERT,'>> Checking whether a key is generated before or not\n')
#time.sleep(0.3)
window.after(1000,txt.insert(INSERT,''))
#time.sleep(0.3)
#txt.insert(INSERT,'...')
window.after(1000,txt.insert(INSERT,''))
#time.sleep(0.3)
#txt.insert(INSERT,'...')
window.after(1000,txt.insert(INSERT,''))
#time.sleep(0.3)
#txt.insert(INSERT,'...')
window.after(1000,txt.insert(INSERT,'>>'))
#time.sleep(0.3)
if os.path.exists("key.key")== False:  #Checking wether a key is generated before or not
    txt.insert(INSERT,'A key file was not present in the directory\n')
    txt.insert(INSERT,'First time key generation\n\n')
    #key generation
    key=Fernet.generate_key()
    txt.insert(INSERT,key)
    txt.insert(INSERT,'\n\n')
    fkey=open("key.key","wb")  #saving key in a txt file
    fkey.write(key)
    fkey.close()

else:
    f=open("key.key","rb")
    key=f.read()
    f.close()
    txt.insert(INSERT,'A key file is present in the directory\n\n')

if os.path.exists("Diary.txt")==False and os.path.exists("Diary.encrypted"): #The diary text file should be present to writing
    file=open("Diary.encrypted","rb")
    data=file.read()
    file.close()
    fer=Fernet(key)
    decrypted=fer.decrypt(data)
    file=open("Diary.txt","wb") #writing decrypted file
    file.write(decrypted)
    file.close()

window.mainloop()


			

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:37:03 2021

@author: Ali İhsan Sarı
"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tasks import tasks

machine = tasks()

filez = None

def konum_al():
    
    savedir = 'pdf/'
    global filez
    
    try:
        
        filez = filedialog.askopenfilenames(parent=root, title='Dosyaları Seçin')
        root.tk.splitlist(filez)
        name = e1.get()
        
        if len(filez) == 0: 
            messagebox.showerror('Please select files', 'You have to choose the file. Please select a file and try again. If you select a file and get this error, contact me.')
        
        else:
            separate = rb1.get()

            if name:
                name = 'converted'
            else:
                pass
            	
            machine.photo_to_pdf(filez, separate, savedir, name)
            e1.delete(0, END)
            
            messagebox.showinfo('Process completed', 'Thank you for choosing me. You can get the output file from the pdf folder in the folder. Producer: Ali İhsan Sarı, I wish you a good day.')
            
            root.destroy()
    
    except Exception as e:
        print(e)
        messagebox.showerror("Failed Transaction", "If you are encountering this problem more than once, please report it to the producer and please make sure that the type of your file is in photo format.")

root = Tk()
root.title('Jpg2Pdf')
root.geometry('350x220')
root.resizable(False, False)
root.config(bg='#1a1a2e')

try:
    root.iconbitmap('icon/a.ico')
    
except:
    messagebox.showinfo('No Logo Appears', 'If the logo is not visible, there is no problem. Either icon file in the file named icon has been changed. Or the file may have been deleted or damaged. This is just a visual deficiency and certainly does not cause any problems in the conversion.')


rb1 = BooleanVar()


h1 = Label(root, text = 'Welcome to the Jpg2Pdf version 1.2 application')
h2 = Label(root, text = 'File name:')
h3 = Label(root, text = 'Progress')
e1 = Entry(root)
b1 = Button(root, text = 'Get Files', command = konum_al)
r1 = Radiobutton(root, text ='Save all photos separately as pdf', variable = rb1 ,value=True)
r2 = Radiobutton(root, text ='Save all photos to the same pdf file', variable = rb1 ,value=False)

e1.insert(0, 'converted')

h1.config(bg='#1a1a2e', fg ='gray')
h2.config(bg='#1a1a2e', fg = 'gray')
h3.config(bg='#1a1a2e', fg = 'gray')
e1.config(bg='#1a1a2e', fg ='gray')
b1.config(bg='#1a1a2e', fg ='gray')
r1.config(bg='#1a1a2e', fg ='gray')
r2.config(bg='#1a1a2e', fg ='gray')


h1.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 3)
h2.grid(row = 1, column = 0)
e1.grid(row = 1, column = 1, padx = 10, pady = 10)
b1.grid(row = 2, column = 0, padx = 10, pady = 10)
r1.grid(row = 2, column = 1, padx = 10, pady = 10)
r2.grid(row = 3, column = 1, padx = 10, pady = 10)
h3.grid(row = 4, column = 0, padx = 0, pady = 10)

root.mainloop()

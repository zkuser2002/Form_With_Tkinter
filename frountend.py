from tkinter import *
import backend

def clear_list():
    list1.delete(0,END)

def fill_list(books):
    for book in books:
        list1.insert(END,book)

window=Tk()
window.title('Book Store')
#=================Labels=================
lbl1=Label(window,text='Title')
lbl1.grid(row=0,column=0)

lbl2=Label(window,text='Autor')
lbl2.grid(row=0,column=2)

lbl3=Label(window,text='Year')
lbl3.grid(row=1,column=0)

lbl4=Label(window,text='ISBM')
lbl4.grid(row=1,column=2)

#=================Entries=================
title_text=StringVar()
ent1=Entry(window,textvariable=title_text)
ent1.grid(row=0,column=1)

author_text=StringVar()
ent2=Entry(window,textvariable=author_text)
ent2.grid(row=0,column=3)

year_text=StringVar()
ent3=Entry(window,textvariable=year_text)
ent3.grid(row=1,column=1)

ISBM_text=StringVar()
ent4=Entry(window,textvariable=ISBM_text)
ent4.grid(row=1,column=3)

#=================Listbox=================
list1=Listbox(window,width=30,height=5)
list1.grid(row=2,column=0,rowspan=5,columnspan=2)

scrol1=Scrollbar(window)
scrol1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=scrol1.set)
scrol1.configure(command=list1.yview)

def get_selected_row(event):
    global selected_book
    if len(list1.curselection())>0:
        index=list1.curselection()[0]
        selected_book=list1.get(index)
    #title
        ent1.delete(0,END)
        ent1.insert(END,selected_book[1])
    #author
        ent2.delete(0,END)
        ent2.insert(END,selected_book[2])
    #year
        ent3.delete(0,END)
        ent3.insert(END,selected_book[3])
    #isbn
        ent4.delete(0,END)
        ent4.insert(END,selected_book[4])




list1.bind('<<ListboxSelect>>',get_selected_row)
#=================Button=================

def view_command():
    clear_list()
    books=backend.view()
    fill_list(books)


btn1=Button(window,text='View All',width=12,command=lambda:view_command())
btn1.grid(row=2,column=3)

def search_command():
    clear_list()
    books=backend.search(title_text.get(),author_text.get(),year_text.get(),ISBM_text.get())
    fill_list(books)

btn2=Button(window,text='Search Entry',width=12,command=search_command)
btn2.grid(row=3,column=3)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),ISBM_text.get())
    view_command()

btn3=Button(window,text='Add Entry',width=12,command=lambda:add_command())
btn3.grid(row=4,column=3)

def update_command():
    backend.update(selected_book[0],title_text.get(),author_text.get(),year_text.get(),ISBM_text.get())
    view_command()


btn4=Button(window,text='Update Selected',width=12,command=update_command)
btn4.grid(row=5,column=3)

def delete_command():
    backend.delete(selected_book[0])
    view_command()

btn5=Button(window,text='Delete Selected',width=12,command=delete_command)
btn5.grid(row=6,column=3)


btn6=Button(window,text='Close',width=12,command=window.destroy)
btn6.grid(row=7,column=3)

view_command()
window.mainloop()
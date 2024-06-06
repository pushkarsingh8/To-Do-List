from tkinter import*
from tkinter import messagebox
from prettytable import PrettyTable
#Todo-List

app = Tk()
size = "370x500"
app.geometry(size)
app.title("To Do-List")
app.config(bg="light blue")

listt = []

def clearr():
    for widget in app.winfo_children():
        widget.destroy()
        
#adding list step by step:-
def add_list():
    title = box_1.get()
    descp = box_2.get("1.0",END).strip()
    
    
      
    listtt = {
        "title" : title,
        "descp" : descp
    }
    
    listt.append(listtt)
    messagebox.showinfo("Added","List is Successfully Added")
    main()
    
        
#it's add task with using widgets
def add_task():
    clearr()
    app.geometry(size)
    title = Label(app,text="Add Task",font=("Bold",17),bg="light blue")
    title.place(x=150,y=13) 
    
    title_1 = Label(app,text="Title :- ",font="Arial",bg="light blue")
    title_1.place(x=75,y=95)
    
    global box_1
    box_1 = Entry(app,font="serif")
    box_1.place(x=110,y=120) 
    
    title_2 = Label(app,text="Description :- ",font="Arial",bg="light blue")
    title_2.place(x=30,y=180)
    
    global box_2
    box_2 = Text(app,font="serif",width=22,height=6)
    box_2.place(x=110,y=205)  
    
    submit = Button(app,text="Submit",font=18,command=add_list,bg="light green")
    submit.place(x=170,y=350)
    
    #it's to take back home screen of app
    b = Button(app,text="Back",command=main,bg="light green")
    b.place(x=12,y=11)
    
    
    
    
      
    
    
    
    
#it's contain all list in tabular form:--
def view_list():
    if not listt:
        l2 = Label(text="Empty\nNo List Available",font="Bold")
        l2.place(x=130,y=220)
        
        
    else:
        table = PrettyTable()
        table.field_names = ["Index","Title","Description"]
        
        for index , task in enumerate(listt):
            table.add_row([index +1, task["title"],task["descp"]])
            
        return table
            
    
    
    


def view_task():
    clearr()
    table = view_list()
    app.geometry(size)
    title = Label(app,text="View Task",font=("Bold",15),bg="light blue")
    title.place(x=150,y=13) 
    

    
    if table:
        table_label = Label(app,text=table.get_string(),font=("Arial",10),justify=LEFT,wraplength=300)
        table_label.place(x=40,y=50)
    
    b = Button(app,text="Back",command=main,bg="light green")
    b.place(x=12,y=11)
    
    
    
def search_list():
    #button to give a response to search a specific list:--
    data = box_3.get() 
    
    for list_find in listt:
        if list_find['title'].lower() == data.lower():
            result = f"Title: {list_find['title']}\nDescription: {list_find['descp']}"
            l11 = Label(text=result,font=("Arial",10))
            l11.place(x=80,y=200)
            box_3.delete(0,END)
            return
    
    l11 = Label(app,text="Title Not found")
    l11.place(x=140,y=200)
    
    



def search_task():
    clearr()
    title = Label(app,text="Search Task",font=("Bold",15),bg="light blue")
    title.place(x=140,y=13) 
    app.geometry(size)
    title_1 = Label(app,text="Title:-",font="serif",bg="light blue")
    title_1.place(x=32,y=77)
    
    search_Button = Button(app,text="Go",command=search_list,bg="light green")
    search_Button.place(x=290,y=77)
    
    global box_3
    box_3 = Entry(app,font="serif")
    box_3.place(x=100,y=80)
    
    result = Label(app,text="Result Here",font=("Arial",12,"underline"))
    result.place(x=140,y=140)
    
    b = Button(app,text="Back",command=main,bg="light green")
    b.place(x=12,y=11)
    

def check():
    #to update a list for first check a title is have or not:--
    data = box_4.get()
    for list_find in listt:
        if list_find['title'].lower() == data.lower():
            search_Button.config(bg="Green",fg="White")
            return
        
    search_Button.config(bg="Red",fg="White")
    box_4.delete(0,END)
                
    
    
    
    
def update_list():
    data = box_4.get()    
    
    if not data:
        messagebox.showwarning("Input Error","Please enter a title to update")
        return
    
    for list_find in listt:
        if list_find['title'].lower() == data.lower():
            
            new_title = title_nw.get()
            new_descp = descp_nw.get("1.0",END).strip()
            
            if new_title:
                list_find['title'] = new_title
            if new_descp:
                list_find['descp'] = new_descp
            
            messagebox.showinfo("Updated","Task updated succsessfully")
            title_nw.delete(0,END)
            descp_nw.delete("1.0",END)
            return
            
    messagebox.showerror("Not found",f"{data} Not found")

    

def update_task():
    clearr()
    app.geometry(size)
    title = Label(app,text="Update Task",font=("Bold",15),bg="light blue")
    title.place(x=140,y=13) 
    
    title_1 = Label(app,text="Title:-",font="serif",bg="light blue")
    title_1.place(x=32,y=77)
    
    global box_4
    box_4 = Entry(app,font="serif")
    box_4.place(x=100,y=80)
    
    nw_title = Label(app,text="New-Title:- ",bg="light blue")
    nw_title.place(x=32,y=120)
    
    global title_nw
    title_nw = Entry(app)
    title_nw.place(x=100,y=120)
    
    nw_descp = Label(app,text="New-Descrption:- ",bg="light blue")
    nw_descp.place(x=32,y=160)
    
    global descp_nw
    descp_nw = Text(app,width=22, height = 6)
    descp_nw.place(x=100,y=180)
    
    update_btn = Button(app,text="Update",command=update_list,bg="light green")
    update_btn.place(x=170,y=350)
    
    global search_Button
    search_Button = Button(app,text="Go",command=check,bg="light green")
    search_Button.place(x=290,y=77)
    
    
    b = Button(app,text="Back",command=main,bg="light green")
    b.place(x=12,y=11)
    

def delete_list():
    title  = box_5.get().strip()
    
    if not title:
        messagebox.showwarning("Input Error","Please enter a title to delete")
        return
    
    for listtt in listt:
        if listtt['title'].lower() == title.lower():
            listt.remove(listtt)
            messagebox.showinfo("Deleted",f"{title} Permanenet Remove ")
            box_5.delete(0,END)
            return
        
    
    messagebox.showerror("Not found",f"{title} Not found")
        


    
def delete_task():
    clearr()    
    app.geometry(size)
    title = Label(app,text="Delete Task",font=("Bold",15),bg="light blue")
    title.place(x=140,y=13) 
    
    
    title_1 = Label(app,text="Title:-",font="serif",bg="light blue")
    title_1.place(x=32,y=77)
    
    global box_5
    box_5 = Entry(app,font="serif")
    box_5.place(x=100,y=80)
    
    delete_btn = Button(app,text="Delete",command=delete_list,bg="light green")
    delete_btn.place(x=290,y=77)
    
    b = Button(app,text="Back",command=main,bg="light green")
    b.place(x=12,y=11)
    



#main class ----
def main():
    clearr()
    #Labels
    x = 25
    y = 80
    y_sp = 50

    title = Label(app,text="To Do-List",font=("Bold",20),bg="light blue")
    title.place(x=120,y=10)

    for i in range(5):
        label = Label(app,text=f"{i+1}.",font="Bold",bg="light blue")
        label.place(x=x,y=y)
        y+=y_sp
        

    add = Button(app,text="Add task",font=("Helvetica",12),width=22,command=add_task,bg="light green")
    add.place(x=85,y=79)

    view = Button(app,text="View task",font=("Helvetica",12),width=22,command=view_task,bg="light green")
    view.place(x=85,y=129)

    search = Button(app,text="Search task",font=("Helvetica",12),width=22,command=search_task,bg="light green")
    search.place(x=85,y=179)

    update = Button(app,text="Update task",font=("Helvetica",12),width=22,command=update_task,bg="light green")
    update.place(x=85,y=229)

    delete = Button(app,text="Delete task",font=("Helvetica",12),width=22,command=delete_task,bg="light green")
    delete.place(x=85,y=279)
    
    



main()
app.mainloop()
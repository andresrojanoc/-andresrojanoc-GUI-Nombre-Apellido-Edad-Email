#! python3
from tkinter import *
from back import Testing
from back import TestingListKeys
from back import TestingAddKeys
from back import TestingRemoveKeys
from back import TestingModifyKeys

data = Testing("data.json")

class Window(object):

    def __init__(self, window):
        self.window = window
        self.window.wm_title("User Interface")

        l1 = Label(window, text="Nombre")
        l1.grid(row=0,column=0)

        l2 = Label(window, text="Apellido")
        l2.grid(row=0,column=2)

        l3 = Label(window, text="Edad")
        l3.grid(row=1,column=0)

        l4 = Label(window, text="Email")
        l4.grid(row=1,column=2)

        self.e1_value=StringVar()
        self.e1 = Entry(window,textvariable=self.e1_value)
        self.e1.grid(row=0,column=1)

        self.e2_value=StringVar()
        self.e2 = Entry(window,textvariable=self.e2_value)
        self.e2.grid(row=0,column=3)

        self.e3_value=StringVar()
        self.e3 = Entry(window,textvariable=self.e3_value)
        self.e3.grid(row=1,column=1)

        self.e4_value=StringVar()
        self.e4 = Entry(window,textvariable=self.e4_value)
        self.e4.grid(row=1,column=3)

        self.list1=Listbox(window,height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1 = Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1 = Button(window,text="View all",width=12,command=self.view_command)
        b1.grid(row=2,column=3)

        b2 = Button(window,text="Add entry",width=12,command=self.add_command)
        b2.grid(row=3,column=3)

        b3 = Button(window,text="Delete entry",width=12,command=self.delete_command)
        b3.grid(row=4,column=3)

        b4 = Button(window,text="Modify entry",width=12,command=self.update_command)
        b4.grid(row=5,column=3)

    def get_selected_row(self,event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,selected_tuple[0])
            self.e2.delete(0,END)
            self.e2.insert(END,selected_tuple[1])
            self.e3.delete(0,END)
            self.e3.insert(END,selected_tuple[2])
            self.e4.delete(0,END)
            self.e4.insert(END,selected_tuple[3])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in TestingListKeys.list_keys(data):
            entry = [row[0][8:],row[1][10:],row[2][6:],row[3][7:]]
            self.list1.insert(END,entry)

    def add_command(self):
        TestingAddKeys.add_keys(data,self.e1_value.get(),self.e2_value.get(),self.e3_value.get(),self.e4_value.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.e1_value.get(),self.e2_value.get(),self.e3_value.get(),self.e4_value.get()))

    def delete_command(self):
        TestingRemoveKeys.remove_key(data,self.e1_value.get(),self.e2_value.get(),self.e3_value.get(),self.e4_value.get())
        self.view_command()

    def update_command(self):
        TestingModifyKeys.modify_key(data,self.e1_value.get(),self.e2_value.get(),self.e3_value.get(),self.e4_value.get())
        self.view_command()

def main():
    window = Tk()
    Window(window)
    window.mainloop()

if __name__ == "__main__":
    main()

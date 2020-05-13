import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy
import mysql.connector

#connecting mysql
mydb=mysql.connector.connect(host='localhost',user='root',passwd='password',database='project_kisan')
mycursor=mydb.cursor()

def expenses():
    class Table:
    	def __init__(self,root):  
    		for i in range(total_rows): 
    			for j in range(total_columns): 
    				self.e =tk.Entry(root, width=20,font=('Arial',16))
    				self.e.grid(row=i, column=j)
    				self.e.insert(END, lst[i][j])
                    
   
    mycursor.execute('Select * from expenses')    #Executing SQL commands
    lst=[]
    for i in mycursor:
        a=numpy.array(i)
        lst.append(a)
        
    total_rows=len(lst) 
    total_columns=len(lst[0]) 
     
    root=Tk()
    root.title('Expenses')
    root.iconbitmap(r'C:\Users\Prince Ashwin\Desktop\Personal\STUDIES\Computer\Project\expense.ico')
    t=Table(root) 
    root.mainloop()
    
def price():
    class Table:
    	def __init__(self,root):  
    		for i in range(total_rows): 
    			for j in range(total_columns): 
    				self.e =tk.Entry(root, width=20,font=('Arial',16))
    				self.e.grid(row=i, column=j)
    				self.e.insert(END, lst[i][j])
                    
   
    mycursor.execute('Select * from price')    #Executing SQL commands
    lst=[]
    for i in mycursor:
        a=numpy.array(i)
        lst.append(a)
        
    total_rows=len(lst) 
    total_columns=len(lst[0]) 
     
    root=Tk()
    root.title('Price Of Items')
    t=Table(root) 
    root.mainloop()

def transport():
    class Table:
    	def __init__(self,root):  
    		for i in range(total_rows): 
    			for j in range(total_columns): 
    				self.e =tk.Entry(root, width=20,font=('Arial',16))
    				self.e.grid(row=i, column=j)
    				self.e.insert(END, lst[i][j])
                    
   
    mycursor.execute('Select * from transport')    #Executing SQL commands
    lst=[]
    for i in mycursor:
        a=numpy.array(i)
        lst.append(a)
        
    total_rows=len(lst) 
    total_columns=len(lst[0]) 
     
    root=Tk()
    root.title('Transport')
    root.iconbitmap(r'C:\Users\Prince Ashwin\Desktop\Personal\STUDIES\Computer\Project\transport.ico')
    t=Table(root) 
    root.mainloop()
    
def profit_out():
    bud=int(B1.get())
    mycursor.execute('select sum(Amount) from expenses')   #Executing SQL commands
    for i in mycursor:
        a=list(i)
        for x in a:
            pro=bud-x
            out['text']=str(pro)

root=tk.Tk()
root.title('KISAN')
root.iconbitmap(r'C:\Users\Prince Ashwin\Desktop\Personal\STUDIES\Computer\Project\people.ico')

#Adding Entry Widget
B1=tk.Entry(root,font=('arial',20),bd=25,justify='center')
B1.grid(columnspan=6,row=2)

#Adding 'Show Profit' Button
tk.Button(root,text='Show Profit',command=profit_out).grid(row=4,column=1,pady=10)

#Creating Label
ttk.Label(root,font=('times'),text='Profit per crop = Rs.').grid(column=2,row=4)
out=ttk.Label(root,font=('times'),text='')
out.grid(column=3,row=4,pady=10)

#Adding images to button
button_image3=tk.PhotoImage(file=r"C:\Users\Prince Ashwin\Desktop\Personal\STUDIES\Computer\Project\expense.png")
photoimage3=button_image3.subsample(30,30)

#Adding 'Expense' Button
details_button=tk.Button(root,text='Expenses',command=lambda : expenses())
details_button.config(image=photoimage3,compound=LEFT)
details_button.grid(row=5,column=2,padx=10,pady=10)

button_image2=tk.PhotoImage(file=r"C:\Users\Prince Ashwin\Desktop\Personal\STUDIES\Computer\Project\Price.png")
photoimage2=button_image2.subsample(35,35)

#Adding 'Price of items' Button
price_button=tk.Button(root,text='Price Of Items',command=lambda : price())
price_button.config(image=photoimage2,compound=LEFT)
price_button.grid(row=6,column=2,padx=10,pady=10)

button_image1=tk.PhotoImage(file=r"C:\Users\Prince Ashwin\Desktop\Personal\STUDIES\Computer\Project\call button.png")
photoimage=button_image1.subsample(1,1)

#Adding 'call transport' button
call_button=tk.Button(root,text='Call Transport',image=photoimage,command=lambda : transport())
call_button.config(image=photoimage,compound=LEFT)
call_button.grid(row=7,column=2,padx=10,pady=10)

#Adding 'Budget per crop' Label
ttk.Label(root,font=('times'),text='Budget per crop').grid(column=2,row=1)

root.mainloop()
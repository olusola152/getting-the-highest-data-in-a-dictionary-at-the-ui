import tkinter as tk
from tkinter import messagebox
a={}
def students ():
    try:
            student=txtstudent.get() 
            score=int(txtscore.get())            
            a[student]=score
            maximumkey=""
            maximumvalue=-1
            for key in a:
             if a[key]>maximumvalue:
              maximumvalue=a[key]
              maximumkey=key
            datas.delete(0, tk.END)
            datas.insert(tk.END,maximumkey)
            txtstudent.delete(0,tk.END)
            txtscore.delete(0,tk.END)
            messagebox.showinfo("Sucess","Values Recorded Sucessfully")       
    except ValueError:
       messagebox.showwarning("Warning","Invalid Details")     
root=tk.Tk()
root.title("STUDENT MANAGEMENT SYSTEM")
root.geometry("500x500")
root.config(background="black")       
studentlabel=tk.Label(root,text="Student Name",bg="black",fg="white",font=("Arial",10,"bold"))
studentlabel.grid(row=0,column=0,padx=5,pady=5)
txtstudent=tk.Entry(root,font=("Arial",10,"bold"))
txtstudent.grid(row=0,column=1,padx=5,pady=5)
scorelabel=tk.Label(root,text="Score",bg="black",fg="white",font=("Arial",10,"bold"))
scorelabel.grid(row=1,column=0,padx=5,pady=5)
txtscore=tk.Entry(root,font=("Arial",10,"bold"))
txtscore.grid(row=1,column=1,padx=5,pady=5)
answerlabel=tk.Label(root,text="Record",bg="black",fg="white",font=("Arial",10,"bold"))
answerlabel.grid(row=2,column=0,padx=5,pady=5)
datas=tk.Entry(root,font=("Arial",10,"bold"))
datas.grid(row=2,column=1,padx=5,pady=5)
btn=tk.Button(root,text="Save",command=students,bg="black",fg="white",font=("Arial",10,"bold"))
btn.grid(row=3,column=1,padx=5,pady=5)
root.mainloop()
from tkinter import *
import os
import subprocess

#Function
def display_frame(frame) :
	frame.pack_forget()
	frame.pack()

def back() :
	global root
	global add_frame
	global frame,search_frame,delete_frame,modify_frame,add_victim_frame
	global add_case_frame,search_frame,search_victim_frame,delete_frame,delete_victim_frame,modify_frame,modify_victim_frame

	for i in (frame,add_frame,search_frame,delete_frame,modify_frame,add_victim_frame,search_frame,search_victim_frame,delete_frame,delete_victim_frame,modify_frame,modify_victim_frame):

		i.pack_forget()
	display_frame(frame)

def add() :
	global frame,root,add_frame
	frame.pack_forget()
	add_frame = Frame(root,background="black")
	button = ['Add FIR Details','Go to Main Menu']
	function  = [add_victim,back]
	for i in range(len(button)) :
		Button(add_frame,text=button[i],command=function[i],height=1,width=20,background="pink",font=("Century Gothic", 16,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(add_frame)

def search() :
	global frame,root,search_frame
	frame.pack_forget()
	search_frame = Frame(root,background="black")
	button = ['Search FIR Details','Go to Main Menu']
	function  = [search_victim,back]
	for i in range(len(button)) :
		Button(search_frame,text=button[i],command=function[i],height=1,width=20,background="pink",font=("Century Gothic", 16,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(search_frame)

def delete() :
	#global add_frame
	global frame,root,delete_frame
	frame.pack_forget()
	delete_frame = Frame(root,background="black")
	button = ['Delete FIR Details','Go to Main Menu']
	function  = [delete_victim,back]
	for i in range(len(button)) :
		Button(delete_frame,text=button[i],command=function[i],height=1,width=20,background="pink",font=("Century Gothic", 16,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(delete_frame)

def modify() :
	global frame,root,modify_frame
	frame.pack_forget()
	modify_frame = Frame(root,background="black")
	button = ['Modify FIR Details','Go to Main Menu']
	function  = [modify_victim,back]
	for i in range(len(button)) :
		Button(modify_frame,text=button[i],command=function[i],height=1,width=20,background="pink",font=("Century Gothic", 16,"bold"),fg="black").pack(side=TOP, expand=YES ,padx=20, pady=30)
	display_frame(modify_frame)


#Add Menu
def add_victim() :
	global add_frame,root,add_victim_frame
	global v1,v2,v3,v4,v5,v6,v7
	add_frame.pack_forget()
	add_victim_frame = Frame(root,background="black")
	
	
	label1=Label(add_victim_frame,text="Enter the FIR NO.",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label1.pack()
	#label1.place(x=50,y=100)
	v1=Entry(add_victim_frame,font=("Courier New", 16))
	v1.pack()
	#v1.place(x=100,y=150)

	label2=Label(add_victim_frame,text="Enter the VICTIM name",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label2.pack()
	v2=Entry(add_victim_frame,font=("Courier New", 16))
	#label2.place(x=100,y=200)
	v2.pack()
	#v2.place(x=100,y=250)

	label3=Label(add_victim_frame,text="Enter ACCUSED name",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label3.pack()
	#label3.place(x=100,y=300)
	v3=Entry(add_victim_frame,font=("Courier New", 16))
	v3.pack()
	#v3.place(x=100,y=350)

	label4=Label(add_victim_frame,text="Enter the CASE DATE",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label4.pack()
	#label4.place(x=100,y=400)
	v4=Entry(add_victim_frame,font=("Courier New", 16))
	v4.pack()
	#v4.place(x=100,y=450)

	label5=Label(add_victim_frame,text="Enter the CASE TIME",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label5.pack()
	#label5.place(x=100,y=500)
	v5=Entry(add_victim_frame,font=("Courier New", 16))
	v5.pack()
	#v5.place(x=100,y=550)

	label6=Label(add_victim_frame,text="Enter the CASE DESCRIPTION",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label6.pack()
	#label6.place(x=100,y=600)
	v7=Entry(add_victim_frame,font=("Courier New", 16))
	v7.pack()
	#v7.place(x=100,y=650)

	label7=Label(add_victim_frame,text="Enter the CASE STATUS",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label7.pack()
	#label7.place(x=100,y=350)
	v6=Entry(add_victim_frame,font=("Courier New", 16))
	v6.pack()
	#v6.place(x=100,y=230)

	b1=Button(add_victim_frame,text="Enter",command=gett,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b1.pack(side = LEFT)

	b2=Button(add_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=RIGHT, expand=YES ,padx=20, pady=15)
	#b2.pack(side = RIGHT)
	display_frame(add_victim_frame)


def gett():

	command='python Insert.py '+v1.get()+" "+v2.get()+" "+v3.get()+" "+v4.get()+" "+v5.get()+" "+v6.get()+" "+v7.get()
	os.system(command)
	print(command)
	



#Search
def search_victim() :
	global search_frame,root,search_victim_frame
	global vs1,vs2,vs3,vs4
	global lbl
	search_frame.pack_forget()
	search_victim_frame = Frame(root,background="black")
	global vs1,vs2,vs3

	lbl = Label(search_victim_frame, text='',background="black",font=("Courier New", 16,"bold"),fg="#C91F37")
	lbl.pack(side=TOP, expand=YES ,padx=20, pady=15)


	key=Label(search_victim_frame,text="Enter FIR NO.",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#key.pack()
	vs3=Entry(search_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	vs3.pack(side=TOP, expand=YES ,padx=20, pady=15)

	b1=Button(search_victim_frame,text="Enter",command=get1,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b1.pack(side=LEFT)

	b2=Button(search_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=RIGHT, expand=YES ,padx=20, pady=15)
	#b2.pack(side = RIGHT)
	display_frame(search_victim_frame)


def get1():

	command='python Search.py '+" "+vs3.get()



	output = subprocess.check_output(command, shell=True)

	lbl['text'] = output.strip()


	os.system(command)
	print(command)




#Delete
def delete_victim() :
	#global add_frame
	global delete_frame,root,delete_victim_frame
	global vd1,vd2,vd3
	global lbl1
	delete_frame.pack_forget()
	delete_victim_frame = Frame(root,background="black")
#	global vs1,vs2,vs3
	global lbl
	lbl1 = Label(delete_victim_frame, text='',background="black",font=("Courier New", 16,"bold"),fg="#C91F37")
	lbl1.pack(side=TOP, expand=YES ,padx=20, pady=15)



	key=Label(delete_victim_frame,text="Enter FIR NO.",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#key.pack()
	vd3=Entry(delete_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	vd3.pack(side=TOP, expand=YES ,padx=20, pady=15)

	b1=Button(delete_victim_frame,text="Enter",command=delete1,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b1.pack(side=LEFT)

	b2=Button(delete_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#2.pack(side = RIGHT)
	display_frame(delete_victim_frame)

def delete1():
	command='python Delete.py '+" "+vd3.get()



	output = subprocess.check_output(command, shell=True)

	lbl1['text'] = output.strip()

	os.system(command)
	print(command)

	display_frame(delete_victim_frame)


def get_modify():
	command='python Modify.py '+" "+v3.get()+" "+vs4.get()


	print("modified")
	output = subprocess.check_output(command, shell=True)

	lbl1['text'] = output.strip()

	os.system(command)
	print(command)

	display_frame(modify_victim_frame)

#Modify
def modify_victim():
	global modify_frame,root,modify_victim_frame
	global v1,v2,v3,v4,v5,vs4
	global lbl1


	modify_frame.pack_forget()
	modify_victim_frame = Frame(root,background="black")

	lbl1 = Label(modify_victim_frame, text='',background="black",font=("Courier New", 16,"bold"),fg="#C91F37")
	lbl1.pack(side=TOP, expand=YES ,padx=20, pady=15)




	label3=Label(modify_victim_frame,text="Enter FIR NO.",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#label3.pack()
	v3=Entry(modify_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	v3.pack(side=TOP, expand=YES ,padx=20, pady=15)

	key1=Label(modify_victim_frame,text="Enter new Status.",background="black",font=("Courier New", 16,"bold"),fg="#C91F37").pack(side=TOP, expand=YES ,padx=20, pady=15)
	#key1.pack()
	vs4=Entry(modify_victim_frame,font=("Courier New", 16,"bold"),fg="black")
	vs4.pack(side=TOP, expand=YES ,padx=20, pady=15)

	b1=Button(modify_victim_frame,text="Enter",command=get_modify,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b1.pack(side = LEFT)

	b2=Button(modify_victim_frame,text="Back",command=back,font=("Century Gothic", 16,"bold"),bg='#89C4F4').pack(side=LEFT, expand=YES ,padx=20, pady=15)
	#b2.pack(side = RIGHT)
	display_frame(modify_victim_frame)




#Main Program
root = Tk(className = "GUI")
frame=add_frame=search_frame=delete_frame=modify_frame = Frame(root,background="black")
root.minsize(200,200)
root.geometry("500x900")
root.title("Crime Files")
root.configure(background='black')

add_victim_frame = add_case_frame = Frame(root)
search_victim_frame  = Frame(root)
delete_victim_frame  = Frame(root)
modify_victim_frame = Frame(root)

label_head = Label(frame, text="FIR Portal",width=15,font=("Tahoma", 40,"bold"),fg ="#9D2933", background='black',justify="center").pack(side=TOP, expand=YES ,padx=20, pady=30)


#Creating Main_Menu Frame
button = ['Register FIR','Search FIR','Delete FIR','Modify FIR']
function = [add,search,delete,modify]
for i in range(len(button)) :
	Button(frame,text=button[i],command=function[i],height=2,width=20,background="pink",font=("Century Gothic", 16,"bold")).pack(side=TOP, expand=YES ,padx=20, pady=30)
#Display
display_frame(frame)
root.mainloop()

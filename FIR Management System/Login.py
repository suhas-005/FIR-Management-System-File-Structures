import sys
import os
from tkinter import *
import textwrap
from PIL import Image,ImageTk
def sin():
	os.system("python Signup.py")

def printtext():
	global entry_1,entry_2
	uname = entry_1.get()
	password = entry_2.get()
	entry_1.delete(first=0,last=100)
	entry_2.delete(first=0,last=100)
	string = uname+"|"+password
	print(string)

	string= (''.join(format(ord(x), 'b') for x in string))
	hashrec(string)

def dest():
	ahead.close()
	root.destroy()

def wordret(wa,wb,wc):
	a=int(wa,2)^int(wb,2)^int(wc,2)
	return '{0:032b}'.format(a)

def F1(S2,S3,S4):
	return (S2&S3)|(~S2&S4)
def F2(S2,S3,S4):
	return S2^S3^S4
def F3(S2,S3,S4):
	return (S2&S3)|(S2&S4)|(S3&S4)
def F4(S2,S3,S4):
	return S2^S3^S4

def process(chunk):
	words=[]
	# print(chunk)
	words=textwrap.wrap(chunk, 32)
	# print(words)
	# for i in range(0,3):
	words.append(wordret(words[0],words[1],words[2]))
	return words

def compress(words):
	k1=0x5A827999 # Constant Ci
	k2=0x6ED9EBA1
	k3=0x8F1BBCDC
	k4=0xCA62C1D6
	s1 = 0x67452301 #5 Register variables
	s2 = 0xEFCDAB89
	s3 = 0x98BADCFE
	s4 = 0x10325476
	s5 = 0xC3D2E1F0
	h1=s1
	h2=s2
	h3=s3
	h4=s4
	h5=s5
	for i in range(0,3):
		temp=s5+(s1<<5)+F1(s2,s3,s4)+k1+int(words[i],2)
		s5=s4
		s4=s3
		s3=s2
		s2=s1
		s1=temp
	h1 = h1 + s1 & 0xffffffff

	return h1


def hashrec(string):
	length=len(string)
	print(string)
	low=0
	high=20

	while(length>20):
		chunk=string[low:high]
		binlength='{0:064b}'.format(20)
		chunk+=binlength
		obj1=process(chunk)
		length=length-20
		low=low+20
		high=high+20
		obj2=compress(obj1)
		# print("inside while")

	if(length==20):
		# print("testing inside 20")
		string+='1'
		#append length
		length='{0:064b}'.format(length)
		string+=length
		obj1=process(string)
		obj2=compress(obj1)
	elif(length<20):
		#string='{0:b}'.format(ord(x) for x in message
		string+='1'
		length=len(string)
		for i in range(length,20):
			string+='0'
		#append length
		length='{0:064b}'.format(length)
		# print("lenght 2 :",length)
		# print("str",string)
		string+=length
		#print(string)
		#print(len(string))
		obj1=process(string)
		obj2=compress(obj1)
	hashis= '%08x' % (obj2)
	print("Hash Generated :",hashis)
	flag = 0
	for lines in ahead:
		words = lines.split("|")
		if words[0] == hashis:
			flag = 1
			root.withdraw()
			command = 'python HomePage.py'
			caller(command)
			root.update()
			root.deiconify()
	if flag == 0:
		print("not found")
	# printtext()

def caller(command):
	os.system(command)

# ahead = open("hashcontnet.txt","r")
ahead = open("hashcontent.txt","r")
root = Tk()
root.configure(background='#264348')
root.geometry('500x900')
root.title("Login GUI")

label_head = Label(root, text="FIR Portal",width=15,font=("Tahoma", 40,"bold"),fg ="#E68364", background='black',justify="center")
label_head.place(x=0,y=5)

label_0 = Label(root, text="LOGIN",width=23,font=("Tahoma", 20,"bold"), background='#264348',fg ="white")
label_0.place(x=50,y=270)

label_1 = Label(root, text="Username",width=13,font=("Courier New", 16,"bold"), background='#264348')
label_1.place(x=50,y=350)

entry_1 = Entry(root, width=14,font=("Courier New",17))
entry_1.pack()
entry_1.focus_set()
entry_1.place(x=242,y=350)

label_2 = Label(root, text="Password",width=13,font=("Courier New", 16,"bold"), background='#264348')
label_2.place(x=50,y=400)

entry_2 = Entry(root, width=14,font=("Courier New",17),show="*")
entry_2.pack()
entry_2.focus_set()
entry_2.place(x=240,y=400)

image = Image.open("signuplogo.png")
resize_image = image.resize((150, 150))
img = ImageTk.PhotoImage(resize_image)
label_img = Label(image=img,background="white")
label_img.image = img
label_img.pack()
label_img.place(x=175, y=100)


b = Button(root, text='Login',width=13,height=1,bg='#afa394',fg='black',background="#89C4F4",font=("Century Gothic", 16,"bold"), command=printtext).place(x=156,y=580)
Button(root, text='Quit',width=13,height=1,bg='#afa394',fg='black',background="#FF0000",font=("Century Gothic", 16,"bold"),command=dest).place(x=156,y=630)
Button(root, text='Sign-up',width=13,height=1,bg='#afa394',background="#89C4F4",font=("Century Gothic", 16,"bold"),fg='black',command=sin).place(x=156,y=680)
root.mainloop()

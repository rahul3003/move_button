from tkinter import *

root = Tk()
root.title("Box game")
root.geometry("500x500")

clicked =True
countdown=0
countright=0

frame = Frame(root,padx=5,pady=5)
frame.grid(row=0,column=1,ipadx=10,ipady=5)

my_label=Label(frame)

def moveLabel(countdown,countright):
	global my_label

	my_label.destroy()
	my_label=Label(frame, text="M")
	my_label.grid(row=countdown,column=countright)
	

def click_down():
	global clicked,countdown

	if clicked== True and countdown<num-1:
		countdown+=1
		return moveLabel(countdown,countright)

def click_up():
	global clicked,countdown

	if clicked== True and countdown > 0:
		countdown-=1
		return moveLabel(countdown,countright)

def click_right():
	global clicked,countright

	if clicked == True and countright<num-1:
		countright+=1
		return moveLabel(countdown,countright)

def click_left():
	global clicked,countright
	if clicked == True and countright>0:
		countright-=1
		return moveLabel(countdown,countright)

def gridisplay(n):
	for i in range(n):
		for j in range(n):
			if i==0 and j==0:
				b=Button(frame, text="",height=3,width=6)
				b.grid(row=i,column=j)
			else:
				b=Button(frame, text="",height=3,width=6)
				b.grid(row=i,column=j)


#def displayDevil():
	#Label(frame, text = "D").grid(row=3,column=3)
	#return 3

frame2=Frame(root)
frame2.grid(row=0,column=0,ipadx=5,ipady=5)

#bulid buttons
down = Button(frame2, text="down ",height=3, width=6, command=click_down)
down.grid(row=0,column=0)

right = Button(frame2, text="right",height=3, width=6, command=click_right)
right.grid(row=1,column=0)

left = Button(frame2, text="left",height=3, width=6, command=click_left)
left.grid(row=2,column=0)

up = Button(frame2, text="up",height=3, width=6, command=click_up)
up.grid(row=3,column=0)

num=6
moveLabel(countdown, countright)
gridisplay(num)
#displayDevil()
root.mainloop()





import tkinter														#imports tkinter Module

root = tkinter.Tk()													#sets "root" variable (base window) to tkinter.Tk class

x = tkinter.PhotoImage(file="x.png")								#image import, must be inside root
o = tkinter.PhotoImage(file="o.png")	
blank = tkinter.PhotoImage(file="blank.png")	

button1_status = "blank"
button2_status = "blank"
button3_status = "blank"
button3_status = "blank"
button4_status = "blank"
button5_status = "blank"
button6_status = "blank"
button7_status = "blank"
button8_status = "blank"
button9_status = "blank"

turn = 0
gameover = False

def click(status, num):

	global button1
	global turn
	global gameover

	global button1_status
	global button2_status
	global button3_status
	global button3_status
	global button4_status
	global button5_status
	global button6_status
	global button7_status
	global button8_status
	global button9_status

	if gameover == False:

		if num == 1:
			if button1_status == "blank" and turn % 2 == 0:
				button1.config(image=x)
				button1_status = "x"
				turn = turn + 1
				win_check()
			elif button1_status == "blank" and turn % 2 != 0:
				button1.config(image=o)
				button1_status = "o"
				turn = turn + 1
				win_check()
		elif num == 2:
			if button2_status == "blank" and turn % 2 == 0:
				button2.config(image=x)
				button2_status = "x"
				turn = turn + 1
				win_check()
			elif button2_status == "blank" and turn % 2 != 0:
				button2.config(image=o)
				button2_status = "o"
				turn = turn + 1
				win_check()
		elif num == 3:
			if button3_status == "blank" and turn % 2 == 0:
				button3.config(image=x)
				button3_status = "x"
				turn = turn + 1
				win_check()
			elif button3_status == "blank" and turn % 2 != 0:
				button3.config(image=o)
				button3_status = "o"
				turn = turn + 1
				win_check()
		elif num == 4:
			if button4_status == "blank" and turn % 2 == 0:
				button4.config(image=x)
				button4_status = "x"
				turn = turn + 1
				win_check()
			elif button4_status == "blank" and turn % 2 != 0:
				button4.config(image=o)
				button4_status = "o"
				turn = turn + 1
				win_check()
		elif num == 5:
			if button5_status == "blank" and turn % 2 == 0:
				button5.config(image=x)
				button5_status = "x"
				turn = turn + 1
				win_check()
			elif button5_status == "blank" and turn % 2 != 0:
				button5.config(image=o)
				button5_status = "o"
				turn = turn + 1
				win_check()
		elif num == 6:
			if button6_status == "blank" and turn % 2 == 0:
				button6.config(image=x)
				button6_status = "x"
				turn = turn + 1
				win_check()
			elif button6_status == "blank" and turn % 2 != 0:
				button6.config(image=o)
				button6_status = "o"
				turn = turn + 1
				win_check()
		elif num == 7:
			if button7_status == "blank" and turn % 2 == 0:
				button7.config(image=x)
				button7_status = "x"
				turn = turn + 1
				win_check()
			elif button7_status == "blank" and turn % 2 != 0:
				button7.config(image=o)
				button7_status = "o"
				turn = turn + 1
				win_check()
		elif num == 8:
			if button8_status == "blank" and turn % 2 == 0:
				button8.config(image=x)
				button8_status = "x"
				turn = turn + 1
				win_check()
			elif button8_status == "blank" and turn % 2 != 0:
				button8.config(image=o)
				button8_status = "o"
				turn = turn + 1
				win_check()
		elif num == 9:
			if button9_status == "blank" and turn % 2 == 0:
				button9.config(image=x)
				button9_status = "x"
				turn = turn + 1
				win_check()
			elif button9_status == "blank" and turn % 2 != 0:
				button9.config(image=o)
				button9_status = "o"
				turn = turn + 1
				win_check()
			
def win_check():

	global button1_status
	global button2_status
	global button3_status
	global button3_status
	global button4_status
	global button5_status
	global button6_status
	global button7_status
	global button8_status
	global button9_status
	
	global gameover

	if button1_status == "x" and button2_status == "x" and button3_status == "x":
		print("X wins")
		gameover = True
	elif button4_status == "x" and button5_status == "x" and button6_status == "x":
		print("X wins")
		gameover = True
	elif button7_status == "x" and button8_status == "x" and button9_status == "x":
		print("X wins")
		gameover = True
	elif button1_status == "x" and button4_status == "x" and button7_status == "x":
		print("X wins")
		gameover = True
	elif button2_status == "x" and button5_status == "x" and button8_status == "x":
		print("X wins")
		gameover = True
	elif button3_status == "x" and button6_status == "x" and button9_status == "x":
		print("X wins")
		gameover = True
	elif button1_status == "x" and button5_status == "x" and button9_status == "x":
		print("X wins")
		gameover = True
	elif button3_status == "x" and button5_status == "x" and button7_status == "x":
		print("X wins")
		gameover = True
	
	elif button1_status == "o" and button2_status == "o" and button3_status == "o":
		print("O wins")
		gameover = True
	elif button4_status == "o" and button5_status == "o" and button6_status == "o":
		print("O wins")
		gameover = True
	elif button7_status == "o" and button8_status == "o" and button9_status == "o":
		print("O wins")
		gameover = True
	elif button1_status == "o" and button4_status == "o" and button7_status == "o":
		print("O wins")
		gameover = True
	elif button2_status == "o" and button5_status == "o" and button8_status == "o":
		print("O wins")
		gameover = True
	elif button3_status == "o" and button6_status == "o" and button9_status == "o":
		print("O wins")
		gameover = True
	elif button1_status == "o" and button5_status == "o" and button9_status == "o":
		print("O wins")
		gameover = True
	elif button3_status == "o" and button5_status == "o" and button7_status == "o":
		print("O wins")
		gameover = True	
		
canvas = tkinter.Canvas(root, width=318, height=358)										#defines "canvas" variable, including location(inside root)
canvas.pack()														#activates canvas variable using "pack" placement method

frame1 = tkinter.Frame(canvas, bg="red",)
frame1.place(width=318, height=40)

frame2 = tkinter.Frame(canvas, bg="blue",)
frame2.place(y=40, width=318, height=318)

label = tkinter.Label(frame1, text="test", bg="yellow")
label.pack(side="left")



#dropdown_default = StringVar(root)
#variable.set("test1") # default value

dropdown = tkinter.OptionMenu(frame1, "a", "test", "one", "two", "three")
dropdown.place(relx=.5, rely=.5, width=100, height=30)











button1 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button1_status, 1))
button1.grid(row=0, column=0)
button2 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button2_status, 2))
button2.grid(row=0, column=1)
button3 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button3_status, 3))
button3.grid(row=0, column=2)
button4 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button4_status, 4))
button4.grid(row=1, column=0)
button5 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button5_status, 5))
button5.grid(row=1, column=1)
button6 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button6_status, 6))
button6.grid(row=1, column=2)
button7 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button7_status, 7))
button7.grid(row=2, column=0)
button8 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button8_status, 8))
button8.grid(row=2, column=1)
button9 = tkinter.Button(frame2, image=blank, width=100, height=100, command=lambda: click(button9_status, 9))
button9.grid(row=2, column=2)

root.mainloop()															#tells root variable (base window) to remain on screen
#Imports tkinter module (Used for drawing GUI).
import tkinter

#Sets Root variable (base window) to tkinter.Tk class.
root = tkinter.Tk()

#Sets title of window			
root.title("Tic-Tac-Toe")

#Variables for image imports - must be inside Root.
x = tkinter.PhotoImage(file="x.png")								
o = tkinter.PhotoImage(file="o.png")	
blank = tkinter.PhotoImage(file="blank.png")	

#Defining other variables used for game status.
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

def click(status, num): #This function is called when one of the buttons is clicked.

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
	global turn
	global gameover

	if gameover == False:
		#This should probably be turned into a Loop at some point.
		if num == 1: 
			if button1_status == "blank" and turn % 2 == 0:
				button1.config(image=x)
				button1_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button1_status == "blank" and turn % 2 != 0:
				button1.config(image=o)
				button1_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 2:
			if button2_status == "blank" and turn % 2 == 0:
				button2.config(image=x)
				button2_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button2_status == "blank" and turn % 2 != 0:
				button2.config(image=o)
				button2_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 3:
			if button3_status == "blank" and turn % 2 == 0:
				button3.config(image=x)
				button3_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button3_status == "blank" and turn % 2 != 0:
				button3.config(image=o)
				button3_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 4:
			if button4_status == "blank" and turn % 2 == 0:
				button4.config(image=x)
				button4_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button4_status == "blank" and turn % 2 != 0:
				button4.config(image=o)
				button4_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 5:
			if button5_status == "blank" and turn % 2 == 0:
				button5.config(image=x)
				button5_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button5_status == "blank" and turn % 2 != 0:
				button5.config(image=o)
				button5_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 6:
			if button6_status == "blank" and turn % 2 == 0:
				button6.config(image=x)
				button6_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button6_status == "blank" and turn % 2 != 0:
				button6.config(image=o)
				button6_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 7:
			if button7_status == "blank" and turn % 2 == 0:
				button7.config(image=x)
				button7_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button7_status == "blank" and turn % 2 != 0:
				button7.config(image=o)
				button7_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 8:
			if button8_status == "blank" and turn % 2 == 0:
				button8.config(image=x)
				button8_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button8_status == "blank" and turn % 2 != 0:
				button8.config(image=o)
				button8_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
		elif num == 9:
			if button9_status == "blank" and turn % 2 == 0:
				button9.config(image=x)
				button9_status = "x"
				turn = turn + 1
				label.config(text="O's turn.")
				win_check()
			elif button9_status == "blank" and turn % 2 != 0:
				button9.config(image=o)
				button9_status = "o"
				turn = turn + 1
				label.config(text="X's turn.")
				win_check()
			
def win_check(): #This function is called at the end of each button click.

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
	
	#This should probably be turned into a Loop at some point.
	if button1_status == "x" and button2_status == "x" and button3_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button4_status == "x" and button5_status == "x" and button6_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button7_status == "x" and button8_status == "x" and button9_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button1_status == "x" and button4_status == "x" and button7_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button2_status == "x" and button5_status == "x" and button8_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button3_status == "x" and button6_status == "x" and button9_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button1_status == "x" and button5_status == "x" and button9_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button3_status == "x" and button5_status == "x" and button7_status == "x":
		label.config(text="X wins!")
		gameover = True
	elif button1_status == "o" and button2_status == "o" and button3_status == "o":
		label.config(text="O wins!")
		gameover = True
	elif button4_status == "o" and button5_status == "o" and button6_status == "o":
		label.config(text="O wins!")
		gameover = True
	elif button7_status == "o" and button8_status == "o" and button9_status == "o":
		label.config(text="O wins!")
		gameover = True
	elif button1_status == "o" and button4_status == "o" and button7_status == "o":
		label.config(text="O wins!")
		gameover = True
	elif button2_status == "o" and button5_status == "o" and button8_status == "o":
		label.config(text="O wins!")
		gameover = True
	elif button3_status == "o" and button6_status == "o" and button9_status == "o":
		label.config(text="O wins!")
		gameover = True
	elif button1_status == "o" and button5_status == "o" and button9_status == "o":
		label.config(text="O wins!")
		gameover = True
	elif button3_status == "o" and button5_status == "o" and button7_status == "o":
		label.config(text="O wins!")
		gameover = True	

canvas = tkinter.Canvas(root, width=318, height=358) #Defines Canvas variable (area in window where GUI elements can be arranged), with location inside Root window					
canvas.pack() #activates canvas variable using "pack" placement method		

frame1 = tkinter.Frame(canvas) #frame1 is the space for the label that displays the game status.
frame1.place(width=318, height=40)

frame2 = tkinter.Frame(canvas) #frame2 is the space for the 9 buttons.
frame2.place(y=40, width=318, height=318)

label = tkinter.Label(frame1, text="X's turn.", bg="white", font=("", 16)) #label displays the game status.
label.place(rely=.1, width=318, height=30)

#Below, each variable for the 9 button is defined and then placed inside frame2.
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

root.mainloop() #This line causes the Root window to remain on the screen.
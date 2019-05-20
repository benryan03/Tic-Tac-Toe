import tkinter														#imports tkinter Module

root = tkinter.Tk()													#sets "root" variable (base window) to tkinter.Tk class

x = tkinter.PhotoImage(file="x.png")								#image import, must be inside root
o = tkinter.PhotoImage(file="o.png")	
blank = tkinter.PhotoImage(file="blank.png")	

button1_clicked_status = False
button2_clicked_status = False
button3_clicked_status = False
button3_clicked_status = False
button4_clicked_status = False
button5_clicked_status = False
button6_clicked_status = False
button7_clicked_status = False
button8_clicked_status = False
button9_clicked_status = False


def click(status, num):

	global button1

	global button1_clicked_status
	global button2_clicked_status
	global button3_clicked_status
	global button3_clicked_status
	global button4_clicked_status
	global button5_clicked_status
	global button6_clicked_status
	global button7_clicked_status
	global button8_clicked_status
	global button9_clicked_status

	if num == 1:
		if button1_clicked_status == False:
			button1.config(image=x)
			button1_clicked_status = True
	elif num == 2:
		if button2_clicked_status == False:
			button2.config(image=x)
			button2_clicked_status = True
	elif num == 3:
		if button3_clicked_status == False:
			button3.config(image=x)
			button3_clicked_status = True
	elif num == 4:
		if button4_clicked_status == False:
			button4.config(image=x)
			button4_clicked_status = True
	elif num == 5:
		if button5_clicked_status == False:
			button5.config(image=x)
			button5_clicked_status = True
	elif num == 6:
		if button6_clicked_status == False:
			button6.config(image=x)
			button6_clicked_status = True
	elif num == 7:
		if button7_clicked_status == False:
			button7.config(image=x)
			button7_clicked_status = True
	elif num == 8:
		if button8_clicked_status == False:
			button8.config(image=x)
			button8_clicked_status = True
	elif num == 9:
		if button9_clicked_status == False:
			button9.config(image=x)
			button9_clicked_status = True
		

canvas = tkinter.Canvas(root)										#defines "canvas" variable, including location(inside root)
canvas.pack()														#activates canvas variale using "pack" placement method

button1 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button1_clicked_status, 1))
button1.grid(row=0, column=0)
button2 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button2_clicked_status, 2))
button2.grid(row=0, column=1)
button3 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button3_clicked_status, 3))
button3.grid(row=0, column=2)
button4 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button4_clicked_status, 4))
button4.grid(row=1, column=0)
button5 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button5_clicked_status, 5))
button5.grid(row=1, column=1)
button6 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button6_clicked_status, 6))
button6.grid(row=1, column=2)
button7 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button7_clicked_status, 7))
button7.grid(row=2, column=0)
button8 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button8_clicked_status, 8))
button8.grid(row=2, column=1)
button9 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button9_clicked_status, 9))
button9.grid(row=2, column=2)











root.mainloop()															#tells root variable (base window) to remain on screen
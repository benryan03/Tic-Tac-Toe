import tkinter														#imports tkinter Module

root = tkinter.Tk()													#sets "root" variable (base window) to tkinter.Tk class

x = tkinter.PhotoImage(file="x.png")								#image import, must be inside root
o = tkinter.PhotoImage(file="o.png")	
blank = tkinter.PhotoImage(file="blank.png")	

button1_clicked_status = False
button2_clicked_status = False
button3_clicked_status = False
button4_clicked_status = False
button5_clicked_status = False
button6_clicked_status = False
button7_clicked_status = False
button8_clicked_status = False
button9_clicked_status = False

def click(buttonx):
	print(buttonx)
	buttonx=str(buttonx)
	#buttonx = int(buttonx[16])
	#var = "button" + str(buttonx) + "_clicked_status"
	print(buttonx)
	#for x in range (1, 9):
	#	if x == buttonx:
	#		print(var)
		
		
		
		

canvas = tkinter.Canvas(root)										#defines "canvas" variable, including location(inside root)
canvas.pack()														#activates canvas variale using "pack" placement method

button1 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button1))
button1.grid(row=0, column=0)
button2 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button2))
button2.grid(row=0, column=1)
button3 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button3))
button3.grid(row=0, column=2)
button4 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button4))
button4.grid(row=1, column=0)
button5 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button5))
button5.grid(row=1, column=1)
button6 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button6))
button6.grid(row=1, column=2)
button7 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button7))
button7.grid(row=2, column=0)
button8 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button8))
button8.grid(row=2, column=1)
button9 = tkinter.Button(canvas, image=blank, width=100, height=100, command=lambda: click(button9))
button9.grid(row=2, column=2)











root.mainloop()															#tells root variable (base window) to remain on screen
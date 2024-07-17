# Length Convertor Program
from tkinter import *

root = Tk()
root.title = ("Length Convertor ")
root.geometry("800x600+50+50")
f = ("Times New Roman", 30, "bold")


def convert():
	
	try:
			
		Inch = float(ent_inch.get())
		result = Inch * 25.4
		msg = "" + str(round(result, 2))
		lab_msg.configure(text=msg)
	except Exception as e:
		msg = "issue " + str(e)
		lab_msg.configure(text=msg)

	


lab_title = Label(root, text="Length Convert", font=f)
lab_title.pack()

lab_inch = Label(root, text="enter the inch ", font=f)
ent_inch = Entry(root, font=f)
btn_convert = Button(root, text="Convert Milimetre", font=f, command=convert)
lab_msg = Label(root, font=f)

lab_inch.pack(pady=5)
ent_inch.pack(pady=5)
btn_convert.pack(pady=5)
lab_msg.pack(pady=5)

root.mainloop()


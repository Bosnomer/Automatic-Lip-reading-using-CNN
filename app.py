import tkinter as tk
from tkinter import filedialog, Text, Canvas
import os
import tkinter.ttk as ttk
from tkinter.ttk import Frame
from PIL import Image, ImageTk
import cv2
from main import prediction

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


root = tk.Tk()
maxWidth = 800
maxHeight = 800
root.geometry('%dx%d+%d+%d' % (maxWidth,maxHeight,0,0))

#var = tk.StringVar()

def close_window():
	root.destroy()
	exit()

def click():
	
	output.delete(0.0, tk.END)
	input_var = prediction(var)
	output.insert(tk.END, input_var)


def playVideo(path):
	
	#Capture video frames
	mainFrame = Frame(root)
	mainFrame.place(x=20, y=430)
	lmain = tk.Label(mainFrame)
	lmain.grid(row=0, column=0)

	cap = cv2.VideoCapture(path)

	def show_frame():
		try:
			ret, frame = cap.read()
			dim = (350, 250)
			frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

			cv2image   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

			img   = Image.fromarray(cv2image)
			imgtk = ImageTk.PhotoImage(image = img)
			lmain.imgtk = imgtk
			lmain.configure(image=imgtk)
			lmain.after(10, show_frame)
		except:
			pass

	show_frame()



def addVideo():
	global var
	root.filename = filedialog.askopenfilename(initialdir="/home/nikhere/", title="Select File", filetypes=(("MP4","*.mp4"),("All Files","*.*")))
	my_label = tk.Label(root, text=root.filename, font="none 10")
	my_label.place(x=120, y=375)
	var = root.filename
		
	play = tk.Button(root, text="Play Video", padx=10, pady=5, fg="white", bg="#263D42", command=lambda: playVideo(var))
	play.place(x=80, y=400)


	
#canvas = tk.Canvas(root, height=600, width=700, bg="#263D42")
#canvas.pack()




root.title("Lip Reading Classification")

canvas_width = 800
canvas_height = 10
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")

head_label = tk.Label(root, text="Welcome to Lip Reading", font="none 40 bold")
head_label.pack()


canvas_width = 800
canvas_height = 10
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.pack()

y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y, fill="#476042")


#w.create_line(0, 0, 0, 20, fill="#476042", width=3)
w = Canvas(root, width=200, height=230)
w.place(x=230, y=75)

w.create_line(0, 0, 0, 230, fill="#476042", width=3)

#left side
lline1_label = tk.Label(root, text="This is a Classification", font="none 10")
lline1_label.place(x=10, y=90)

lline2_label = tk.Label(root, text="project. It classifies 10", font="none 10")
lline2_label.place(x=10, y=110)

lline3_label = tk.Label(root, text="words and 10 phrases.", font="none 10")
lline3_label.place(x=10, y=130)

lline4_label = tk.Label(root, text="Dataset used is ", font="none 10")
lline4_label.place(x=10, y=150)

lline4_label = tk.Label(root, text="MIRACL-VC1 dataset.", font="none 10")
lline4_label.place(x=10, y=170)

lline5_label = tk.Label(root, text="We have used a CNN model", font="none 10")
lline5_label.place(x=10, y=190)

lline6_label = tk.Label(root, text="for classification. ", font="none 10")
lline6_label.place(x=10, y=210)

lline7_label = tk.Label(root, text="you like the project.", font="none 10")
lline7_label.place(x=10, y=150)




#right side

#rline1_label = tk.Label(root, text="This project is ", font="none 10")
#rline1_label.place(x=710, y=90)







load = Image.open("/home/nikhere/Desktop/PROJECTFINAL/ActiveCodes/imgUsed.jpeg")
render = ImageTk.PhotoImage(load)
img = tk.Label(root, image=render)
img.image = render
#img = img.resize((250, 250), Image.ANTIALIAS)
img.place(x=250, y=100)
#img.pack()

w = Canvas(root, width=10, height=230)
w.place(x=570, y=75)

w.create_line(0, 0, 0, 230, fill="#476042", width=3)


rline1_label = tk.Label(root, text="This Project is created by:", font="none 10")
rline1_label.place(x=580, y=90)

rline2_label = tk.Label(root, text="Nikhil Kesarkar(A843)", font="none 10")
rline2_label.place(x=580, y=110)

rline3_label = tk.Label(root, text="Poornachandra Kongara(A849)", font="none 10")
rline3_label.place(x=580, y=130)

rline4_label = tk.Label(root, text="Manthan Kothari(A851)", font="none 10")
rline4_label.place(x=580, y=150)

rline5_label = tk.Label(root, text="under the guidance of", font="none 10")
rline5_label.place(x=580, y=180)

rline6_label = tk.Label(root, text="Mr. Suresh Mestry", font="none 10 underline")
rline6_label.place(x=580, y=200)


w = Canvas(root, width=800, height=20)
w.place(x=0, y=300)

w.create_line(0, 0, 800, 0, fill="#476042", width=3)


head1_label = tk.Label(root, text="Choose a video file", font="none 15 bold")
head1_label.place(x=20, y=310)


openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addVideo)
openFile.place(x=80, y=340)

head2_label = tk.Label(root, text="File Choosed : ", font="none 10")
head2_label.place(x=10, y=375)

head3_label = tk.Label(root, text="Video to Text", font="none 15 bold")
head3_label.place(x=550, y=310)


convert = tk.Button(root, text="CONVERT", padx=30, pady=15, fg="white", bg="#263D42", command=click)
convert.place(x=380, y=450)

output = Text(root, width=40, height=10)
output.place(x=500, y=420)

exit_label = tk.Label(root, text="THANK YOU !", font="none 15 bold")
exit_label.place(x=550, y=600)

exit1_label = tk.Label(root, text="Click Here to Exit", font="none 15")
exit1_label.place(x=530, y=630)

exitbut = tk.Button(root, text="EXIT", padx=25, pady=10, fg="white", bg="#263D42", command=close_window)
exitbut.place(x=570, y=660)



root.mainloop()

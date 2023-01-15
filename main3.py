from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import cv2
import numpy as np

# creating root widget
class Birds():
    def __init__(self):
        self.root = Tk()
        name_var1=StringVar()
        name_var2=StringVar()
        name_var3=StringVar()
        # give it a title
        self.root.title("CHIDIYA UDD")
        # re-sizing the output window
        # size-factors
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.6
        # output window geometry
        self.root.geometry(f"{int(1440*sf)}x{int(1024*sf3)}")
        bgimg = np.array(Image.open(r"desk1.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        self.img_label = Label(self.root,image = bgimg)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)


        bgimg2 = np.array(Image.open(r"group1.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))


        self.name_1 = Entry(self.root,textvariable = name_var1, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
        self.name_1.place(x=int(sf*327),y=int(sf*450))
        self.name_2 = Entry(self.root,textvariable = name_var2, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
        self.name_2.place(x=int(sf*327),y=int(sf*550))
        self.name_3 = Entry(self.root,textvariable = name_var3, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
        self.name_3.place(x=int(sf*327),y=int(sf*650))

        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="black")
        self.button.place(x=int(115*sf), y=int(815*sf))
        self.root.mainloop()
    def rulepage(self):
        bgimg = np.array(Image.open(r"desk22.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        img_label = Label(self.root,image = bgimg)
        img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        self.root.mainloop()
        

    def startcall(self):
        self.img_label.destroy()
        self.button.destroy()
        self.name_1.destroy()
        self.name_3.destroy()
        self.name_2.destroy()
        self.rulepage()
b = Birds()

    


    

# # set background image
# bgimg = np.array(Image.open(r"desk1.png"))
# bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
# bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
# img_label = Label(root,image = bgimg)
# img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)


# bgimg2 = np.array(Image.open(r"group1.png"))
# bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
# bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))


# name_1 = Entry(root,textvariable = name_var1, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
# name_1.place(x=int(sf*327),y=int(sf*450))
# name_2 = Entry(root,textvariable = name_var2, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
# name_2.place(x=int(sf*327),y=int(sf*550))
# name_3 = Entry(root,textvariable = name_var3, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
# name_3.place(x=int(sf*327),y=int(sf*650))

# button = Button(root, image=bgimg2,command=lambda: [startcall(),rulepage()], relief="flat", bg="black")
# button.place(x=int(115*sf), y=int(815*sf))







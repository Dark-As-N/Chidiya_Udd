import time
import os
import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
import cv2
import numpy as np
from hdpitkinter import *


# creating a class
class Birds():
    # a constructor
    def __init__(self):
        # creating the application widget
        self.root = Tk()
        # input names of the players
        name_var1=StringVar()
        name_var2=StringVar()
        name_var3=StringVar()
        # give the applicationa a title
        self.root.title("CHIDIYA UDD")
        # re-sizing the output window
        # size-factors
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.6
        # output window geometry
        self.root.geometry(f"{int(1440*sf)}x{int(1024*sf3)}")
        # set background on the front page
        bgimg = np.array(Image.open(r"desk1.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        self.img_label = Label(self.root,image = bgimg)
        # place the background image
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        # import image for button styling
        bgimg2 = np.array(Image.open(r"group1.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # player name entry text-box
        self.name_1 = Entry(self.root,textvariable = name_var1, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
        self.name_1.place(x=int(sf*327),y=int(sf*450))
        self.name_2 = Entry(self.root,textvariable = name_var2, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
        self.name_2.place(x=int(sf*327),y=int(sf*550))
        self.name_3 = Entry(self.root,textvariable = name_var3, font=('calibre',20,'normal'), bg="#FFFFFF", relief="flat")
        self.name_3.place(x=int(sf*327),y=int(sf*650))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="black")
        # place the button
        self.button.place(x=int(115*sf), y=int(815*sf))
        self.root.mainloop()
    # code for the rules page
    def rulepage(self):
        # set the background image
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.6
        bgimg = np.array(Image.open(r"desk2222.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        img_label = Label(self.root,image = bgimg)
        img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        # import image for the begin button styling
        bgimg2 = np.array(Image.open(r"duplicate.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        self.button = Button(self.root, image=bgimg2,command=self.startcall2, relief="flat", bg="white")
        # place the image
        self.button.place(x=int(938*sf), y=int(810*sf))
        self.root.mainloop()
    # a function to destroy the intro page
    def startcall(self):
        self.img_label.destroy()
        self.button.destroy()
        self.name_1.destroy()
        self.name_3.destroy()
        self.name_2.destroy()
        # automatically call the next page (rules page)
        self.rulepage()
    # a function to destroy the rules page
    def startcall2(self):
        self.img_label.destroy()
        self.button.destroy()
        self.name_1.destroy()
        self.name_3.destroy()
        self.name_2.destroy()   
        # automatically calls the countdown     
        self.pagebuffer()
    # countdown after the begin button is clicked
    def pagebuffer(self):
        # setup the background image 
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.6
        bgimg2 = np.array(Image.open(r"desk3.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        img_label = Label(self.root,image = bgimg2)
        img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        # import an image over the loaded background image
        bgimg = np.array(Image.open(r"page3.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        self.img_label = Label(self.root,image = bgimg)   
        # place, wait for a second and destroy
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        self.root.update_idletasks()
        self.root.after(1000, self.img_label.destroy())
        # import an image over the loaded background image
        bgimg = np.array(Image.open(r"page2.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        self.img_label = Label(self.root,image = bgimg)  
        # place, wait for a second and destroy
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        self.root.update_idletasks()
        self.root.after(1000, self.img_label.destroy())
        # import an image over the loaded background image
        bgimg = np.array(Image.open(r"page1.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        self.img_label = Label(self.root,image = bgimg)   
        # place, wait for a second and destroy
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        self.root.update_idletasks()
        self.root.after(1000, self.img_label.destroy())
        # import an image over the loaded background image
        bgimg = np.array(Image.open(r"page0.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        self.img_label = Label(self.root,image = bgimg)   
        # place, wait for a second and destroy
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        self.root.update_idletasks()
        self.root.after(1000, self.img_label.destroy())
        self.page()
        self.root.mainloop()   
    
    # start shooting images
    def page(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.6
        bgimg = np.array(Image.open(r"desk3.png"))
        bgimg = cv2.resize(bgimg, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg = ImageTk.PhotoImage(Image.fromarray(bgimg))
        img_label = Label(self.root,image = bgimg)
        img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)

        # opencv        
        cap=cv2.VideoCapture(1)
        # cap = cv2.VideoCapture(1)
        cap.read()
        # new = time.time() + 3        
        buffer = []
        prev_frame_time = 0
        new_frame_time = 0
        text = ''
        sf = 1.5
        # capture motion
        def capture_motion(list2):
            buffer = []
            prev_frame_time = 0
            new_frame_time = 0
            text = ''
            sf = 1.5
            for i in range(1):
                ret1,frame1= cap.read()
                frame1 = cv2.resize(frame1, (int(frame1.shape[1] * sf), int(frame1.shape[0] * sf)))
                gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
                gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)
                buffer.append(gray1)

            a = time.time() + 1
            while(time.time() < a):
                global camera_closed
                ret2,frame2=cap.read()
                frame2 = cv2.resize(frame2, (int(frame2.shape[1] * sf), int(frame2.shape[0] * sf)))
                gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
                gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)
                deltaframe = cv2.absdiff(buffer[0], gray2)
                buffer.append(gray2)
                buffer[:] = buffer[1:]
                threshold = cv2.threshold(deltaframe, 50, 255, cv2.THRESH_BINARY)[1]   
                      
                countour,heirarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for i in countour:
                    if cv2.contourArea(i) < 20:
                        continue
                    (x, y, w, h) = cv2.boundingRect(i)
                    mid = (int) (x + h/2)
                
                    if (mid < 320):
                        cv2.rectangle(frame2, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        frame2 = cv2.putText(frame2, "1", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        list2[0] = 1

                
                
                    elif (mid < 640):
                        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        frame2 = cv2.putText(frame2, "2", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        list2[1] = 1

                
                    elif (mid>640):
                        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 2)
                        frame2 = cv2.putText(frame2, "3", (60, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        list2[2] = 1
                frame2 = cv2.putText(frame2, text, (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                # cv2.imshow('window',frame2)
                if cv2.waitKey(1) == ord('q'):
                    camera_closed = True
                    cv2.destroyAllWindows()
                    cap.release()
                    break
                new_frame_time = time.time()
                fps = 1/(new_frame_time-prev_frame_time)
                prev_frame_time = new_frame_time 
                text = 'FPS ' + str(round(fps, 1))
            return list2
        i = 1
        list3 = [0,0,0]
        camera_closed = False
        while camera_closed == False :
        # while i<=10:
            x=time.time()
            print('Be Ready')
            # create a list of photo directory
            path = r"C:\Users\91865\syntax_error\Images"
            dir_list = os.listdir(path)
            s = random.choice(dir_list)

            self.bgimg2 = np.array(Image.open(path+'\\'+s))
            self.bgimg2 = cv2.resize(self.bgimg2, None, fx = 0.6, fy = 0.6, interpolation=cv2.INTER_LINEAR)
            self.bgimg2 = ImageTk.PhotoImage(Image.fromarray(self.bgimg2))
            self.img_label = Label(self.root, image=self.bgimg2, bg="black")
            self.img_label.place(x=int(320*self.sf2), y=int(212*self.sf2))
            self.root.update_idletasks()                                   
            time.sleep(0.4)
            liststar = [0,0,0]
            liststar = capture_motion(liststar)
            print (liststar)
            
            tempTuple = os.path.splitext(s)
            filename = tempTuple[0]
            res = [int(i) for i in filename.split() if i.isdigit()]
            x=res[0]
            print(x)
            if (x>16):
                if (liststar[0]==1 or liststar[1]==1 or liststar[2]==1):
                    if(liststar[0]==1 and liststar[1]==1 and liststar[2]==1):
                        print("Execute all")
                        self.mainpage7()   
                    elif(liststar[0]==1 and liststar[1]==1 and liststar[2]==0):
                        print("Execute player 1 and 2")
                        self.mainpage4()   
                    elif(liststar[0]==1 and liststar[1]==0 and liststar[2]==1):
                        print("Execute player 1 and 3")
                        self.mainpage5()   
                    elif(liststar[0]==0 and liststar[1]==1 and liststar[2]==1):
                        print("Execute player 2 and 3")
                        self.mainpage6()   
                    elif(liststar[0]==1 and liststar[1]==0 and liststar[2]==0):
                        print("Execute player 1")
                        self.mainpage1()   
                    elif(liststar[0]==0 and liststar[1]==1 and liststar[2]==0):
                        print("Execute player 2")
                        self.mainpage2()   
                    elif(liststar[0]==0 and liststar[1]==0 and liststar[2]==1):
                        print("Execute player 3")
                        self.mainpage3()   
                else:
                    print("Dont execute")
            else:
                if (liststar[0]==0 or liststar[1]==0 or liststar[2]==0):
                    if(liststar[0]==0 and liststar[1]==0 and liststar[2]==0):
                        print("Execute all")
                        self.mainpage7()   
                    elif(liststar[0]==0 and liststar[1]==0 and liststar[2]==1):
                        print("Execute player 1 and 2")
                        self.mainpage4()   
                    elif(liststar[0]==0 and liststar[1]==1 and liststar[2]==0):
                        print("Execute player 1 and 3")
                        self.mainpage5()   
                    elif(liststar[0]==1 and liststar[1]==0 and liststar[2]==0):
                        print("Execute player 2 and 3")
                        self.mainpage6()   
                    elif(liststar[0]==0 and liststar[1]==1 and liststar[2]==1):
                        print("Execute player 1")
                        self.mainpage1()   
                    elif(liststar[0]==1 and liststar[1]==0 and liststar[2]==1):
                        print("Execute player 2")
                        self.mainpage2()   
                    elif(liststar[0]==1 and liststar[1]==1 and liststar[2]==0):
                        print("Execute player 3")
                        self.mainpage3()   
                else:
                    print("Dont execute")
            y=time.time()
            print(y-x)       
            
            list3 = [0,0,0]
            i+=1
        time.sleep(1)
        cv2.destroyAllWindows()
        self.mainpage()        
        self.root.mainloop()

    def mainpage(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"desktop444.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()

    def mainpage1(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"PLAYER1.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()

    def mainpage2(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"PLAYER2.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()

    def mainpage3(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"PLAYER3.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()

    def mainpage4(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"PLAYER12.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()

    def mainpage5(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"PLAYER13.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()

    def mainpage6(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"PLAYER23.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()

    def mainpage7(self):
        sf = 0.6
        self.sf2 = 0.6
        sf3 = 0.5
        bgimg5 = np.array(Image.open(r"ALL.png"))
        bgimg5 = cv2.resize(bgimg5, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg5 = ImageTk.PhotoImage(Image.fromarray(bgimg5))
        self.img_label = Label(self.root,image = bgimg5)
        self.img_label.place(x = 0, y = 0, relheight = 1, relwidth = 1)
        
        # print(4)
        bgimg2 = np.array(Image.open(r"retry.png"))
        bgimg2 = cv2.resize(bgimg2, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg2 = ImageTk.PhotoImage(Image.fromarray(bgimg2))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg2,command=lambda: [self.startcall()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(97*self.sf2), y=int(842*self.sf2))

        bgimg3 = np.array(Image.open(r"quit.png"))
        bgimg3 = cv2.resize(bgimg3, None, fx = self.sf2, fy = self.sf2, interpolation=cv2.INTER_AREA)
        bgimg3 = ImageTk.PhotoImage(Image.fromarray(bgimg3))
        # button creation and hyperlinking it to the next page
        self.button = Button(self.root, image=bgimg3,command=lambda: [self.root.destroy()], relief="flat", bg="#081920")
        # place the button
        self.button.place(x=int(564*self.sf2), y=int(842*self.sf2))
        self.root.mainloop()


	














































































































































    
    

   

b = Birds()

    


    


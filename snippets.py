# # # # from tkinter import *
#
# # # # root = Tk()
#
# # # # def move_window(event):
# # # #     root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
#
#
# # # # root.overrideredirect(True) # turns off title bar, geometry
# # # # root.geometry('400x100+0+0') # set new geometry
#
# # # # # make a frame for the title bar
# # # # title_bar = Frame(root, bg='white', relief='raised', bd=2)
#
# # # # # put a close button on the title bar
# # # # close_button = Button(title_bar, text='X', command=root.destroy)
#
# # # # # a canvas for the main area of the window
# # # # window = Canvas(root, bg='black')
#
# # # # # pack the widgets
# # # # title_bar.pack(expand=1, fill=X)
# # # # close_button.pack(side=RIGHT)
# # # # window.pack(expand=1, fill=BOTH)
#
# # # # # bind title bar motion to the move window function
# # # # root.bind('<B1-Motion>', move_window)
#
# # # # root.mainloop()
#
# # # import cv2
#
# # # cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
# # # ret,frame = cap.read() # return a single frame in variable `frame`
#
# # # while(True):
# # #     cv2.imshow('img1',frame) #display the captured image
# # #     if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y'
# # #         cv2.imwrite('images/c1.png',frame)
# # #         cv2.destroyAllWindows()
# # #         break
#
# # # cap.release()
#
# from tkinter import *
# from PIL import Image, ImageTk
#
# root = Tk()
#
# frame1 = Frame(root)
# frame1.pack()
#
# scr = Scrollbar(frame1)
# scr.pack()
#
# # scr.config(yscrollcommand=frame1.yview)
#
# imgs = ['3823-200.png', '1779916.jpg', '2ea7e6b03f3c85f2dcbdb8ff734e4a63.jpg', '240_F_211876011_nLPovSx53fDyL25d3MkBsTMUzf1hvDBZ.jpg']
# t = ['one', 'two', 'three']
#
# canvas = Canvas(root)
# canvas.pack()
#
# for i in range(0, 3):
#     image=Image.open(imgs[i])
#     img = ImageTk.PhotoImage(image)
#     h = image.size
#     print(h)
#     canvas.create_image(0, 0, image=img)
#
# root.mainloop()
#
# # import sqlite3
#
# # image = 'D:\\python\\axum university\\db.db'
#
# # with open(image, 'rb') as f:
# #     file = f.read()
# #     print(file)
#
# # con = sqlite3.connect('db.db')
# # cur = con.cursor()
#
# # cur.execute('''CREATE TABLE IF NOT EXISTS sss(
# #     fil TEXT
# # )''')
#
# # con.commit()
#
# # cur.execute('''INSERT INTO sss VALUES (?)''', (file,))
# # con.commit()
import tkinter as tk


class PopUpConfirmQuit(tk.Toplevel):
    """A TopLevel popup that asks for confirmation that the user wants to quit.
                                                                              .
    Upon confirmation, the App is destroyed.
    If not, the popup closes and no further action is taken
    """
    def __init__(self, master=None):
        super().__init__(master)
        tk.Label(self, text="Are you sure you want to quit").pack()
        tk.Button(self, text='confirm', command=master.destroy, fg='red').pack(side=tk.RIGHT, fill=tk.BOTH, padx=5, pady=5)
        tk.Button(self, text='Nooooo!', command=self.destroy).pack(side=tk.RIGHT, fill=tk.BOTH, padx=5, pady=5)


class App(tk.Tk):
    """a minimal example App containing only a QUIT button, that launches
    a confirmation popup window
    """
    def __init__(self):
        super().__init__()
        self.quitbutton = tk.Button(self, text='QUIT', command=lambda: PopUpConfirmQuit(self))
        self.quitbutton.pack()
        self.mainloop()


App()

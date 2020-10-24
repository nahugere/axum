'''
    code authored by Abyssinya codes
'''

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pathlib
from BackEngine import BackEnd

engine = BackEnd()

file_dir = str(pathlib.Path(__file__).parent.absolute())

class App:

    def __init__(self):
        self.master = Tk()
        self.master.geometry('1200x900')
        self.master.config(bg="#F8FBFC")
        self.master.title("ኣክሱም ዩኒቨርሲቲ |   Aksum University")
        self.signin()
        self.master.mainloop()

    def signin(self):
        # sigin_container
        self.sigin_container = Frame(self.master, width=450, height=593, bg="#F8FBFC")
        self.sigin_container.place(relx=0.5, rely=0.45, anchor=CENTER)

        # sign in components
        self.logo_image = ImageTk.PhotoImage(Image.open(file_dir+'\\files\\assets\\images\\aksum_university_logo.png'))
        self.logo = Label(self.sigin_container, image=self.logo_image, bg="#F8FBFC")
        self.logo.place(relx=0.5, rely=0.15, anchor=CENTER)

        self.welcome_message = Label(self.sigin_container, text="እንኳዕ ብደሓን መጹ", bg="#F8FBFC", fg="#5A5959", font=("consolas", 30))
        self.welcome_message.place(relx=0.5, rely=0.35, anchor=CENTER)

        self.username_text = Label(self.sigin_container, text="ናይ ተጠቃሚ ስም", bg="#F8FBFC", fg="#5D5D5D", font=("consolas", 17))
        self.username_text.place(relx=0.25, rely=0.5, anchor=CENTER)

        self.input_image = ImageTk.PhotoImage(Image.open(file_dir+'\\files\\assets\\images\\input_background_big.png'))
        self.username_background = Label(self.sigin_container, image=self.input_image, bg="#F8FBFC")
        self.username_background.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.username_input = Entry(self.username_background, font=("arial", 20, "bold"), bg="#DBDBDB", width=25, border=0, fg="#5A5959")
        self.username_input.place(x=10, y=15)


        self.password_text = Label(self.sigin_container, text="ናይ ተጠቃሚ ምስጢር ቁልፊ", bg="#F8FBFC", fg="#5D5D5D", font=("consolas", 17))
        self.password_text.place(relx=0.35, rely=0.68, anchor=CENTER)

        self.password_backgoround = Label(self.sigin_container, image=self.input_image, bg="#F8FBFC")
        self.password_backgoround.place(relx=0.5, rely=0.76, anchor=CENTER)
        self.password_input = Entry(self.password_backgoround, font=("arial", 25, "bold"), bg="#DBDBDB", width=20, border=0, fg="#5A5959", show="\u2022")
        self.password_input.place(x=10, y=15)


        self.sign_in_image = ImageTk.PhotoImage(Image.open(file_dir+'\\files\\assets\\images\\signin_button.png'))
        self.sign_in_button = Button(self.sigin_container, image=self.sign_in_image, border=0, bg="#F8FBFC", command=lambda place=self.sigin_container: self.home(place))
        self.sign_in_button.place(relx=0.5, rely=0.9, anchor=CENTER)


    def get(self):
        print(self.fname.get())
        print(self.lname.get())
        print(self.phone.get())
        print(self.cname.get())
        print(self.serial.get())

    '''register'''
    def register(self):

        self.register_body_container = Frame(self.master, bg='white')
        self.register_body_container.pack(side=RIGHT, fill=BOTH, expand=1)


        self.background_frame_1.config(bg='#0278AE')
        self.background_frame_2.config(bg='#FBFBFB')
        self.background_frame_3.config(bg='#FBFBFB')

        self.register_image_label.config(bg="#0278AE", image=self.register_image_sel)
        self.register_text.config(bg="#0278AE", fg="white")

        # register elements
        self.entry_background_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\small_entry.png"))

        self.entry_background_1 = Label(self.register_body_container, image=self.entry_background_image, bg="#FFFFFF")
        self.entry_background_1.place(relx=0.05, rely=0.09)

        self.fname = Entry(self.entry_background_1, font=("arial", 15, "bold"), width=32, bg="#ECECEC", border=0, fg="#5A5959")
        self.fname.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.fname_text = Label(self.register_body_container, text="ሽም", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.fname_text.place(relx=0.05, rely=0.05)

        # last name entry
        self.entry_background_2 = Label(self.register_body_container, image=self.entry_background_image, bg="#FFFFFF")
        self.entry_background_2.place(relx=0.05, rely=0.2)

        self.lname = Entry(self.entry_background_2, font=("arial", 15, "bold"), width=32, bg="#ECECEC", border=0, fg="#5A5959")
        self.lname.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.lname_text = Label(self.register_body_container, text="ሽም ኣቦ", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.lname_text.place(relx=0.05, rely=0.16)

        # number name entry
        self.entry_background_3 = Label(self.register_body_container, image=self.entry_background_image, bg="#FFFFFF")
        self.entry_background_3.place(relx=0.05, rely=0.31)

        self.phone = Entry(self.entry_background_3, font=("arial", 15, "bold"), width=32, bg="#ECECEC", border=0, fg="#5A5959")
        self.phone.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.phone_text = Label(self.register_body_container, text="ናይ ወናኒ ስልኪ ቁጽሪ", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.phone_text.place(relx=0.05, rely=0.27)

        # computer name entry
        self.entry_background_3 = Label(self.register_body_container, image=self.entry_background_image, bg="#FFFFFF")
        self.entry_background_3.place(relx=0.05, rely=0.42)

        self.cname = Entry(self.entry_background_3, font=("arial", 15, "bold"), width=32, bg="#ECECEC", border=0, fg="#5A5959")
        self.cname.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.cname_text = Label(self.register_body_container, text="ናይ ኮምፒተር ሽም", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.cname_text.place(relx=0.05, rely=0.38)

        # computer serial name entry
        self.entry_background_3 = Label(self.register_body_container, image=self.entry_background_image, bg="#FFFFFF")
        self.entry_background_3.place(relx=0.05, rely=0.53)

        self.serial = Entry(self.entry_background_3, font=("arial", 15, "bold"), width=32, bg="#ECECEC", border=0, fg="#5A5959")
        self.serial.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.serial_text = Label(self.register_body_container, text="ናይ ኮምፒተር መለለዪ", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.serial_text.place(relx=0.05, rely=0.49)

        self.container_1 = Frame(self.register_body_container, bg="white")
        self.container_1.place(relx=0.05, rely=0.6)

        # person picture
        self.ppic_text = Label(self.container_1, text="ናይ ወናኒ ፎቶ", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.ppic_text.grid(row=0, column=0)

        self.upload_button = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\images\\upload button.png"))

        self.ppic_button = Button(self.container_1, image=self.upload_button, bg="#FFFFFF", fg="#5A5959", border=0)
        self.ppic_button.grid(row=1, column=0)

        # computer picture
        self.cpic_text = Label(self.container_1, text="ናይ ኮምፒተር ፎቶ", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.cpic_text.grid(padx=(80, 0), row=0, column=1)

        self.cpic_button = Button(self.container_1, image=self.upload_button, bg="#FFFFFF", fg="#5A5959", border=0)
        self.cpic_button.grid(padx=(80, 0), row=1, column=1)

        # save button
        self.register_button = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\images\\save_button.png"))

        self.register_save = Button(self.register_body_container, image=self.register_button, bg="#FFFFFF", border=0, command=self.show)
        self.register_save.place(relx=0.05, rely=0.73)

    def show(self):
        try:
            self.register_body_container.pack_forget()
        except:
            pass

        datas = engine.fetchData()

        self.list_body_container = Frame(self.master, bg='white')
        self.list_body_container.pack(side=RIGHT, fill=BOTH, expand=1)

        x = 0
        for y in range(0, len(datas['name'])):
            self.list_container = Frame(self.list_body_container, bg='white', width=450, height=230)
            self.list_container.pack(side=LEFT, anchor=N, pady=(10, 0), padx=(10, 0))

            self.image_frame = Frame(self.list_container, bg="#9F9F9F", width=450, height=230)
            self.image_frame.pack(side=TOP)
            
            self.name = Label(self.list_container, text="ምሉእ ስም፦ "+datas['name'][x], bg="#FFFFFF", fg="#5A5959", font=('arial', 15)).pack(side=TOP, anchor=W)
            self.name = Label(self.list_container, text="ናይ ወናኒ ስልኪ፦ "+datas['number'][x], bg="#FFFFFF", fg="#5A5959", font=('arial', 15)).pack(side=TOP, anchor=W)
            self.name = Label(self.list_container, text="ናይ ኮምፒተር ስም፦ "+datas['pc'][x], bg="#FFFFFF", fg="#5A5959", font=('arial', 15)).pack(side=TOP, anchor=W)
            self.name = Label(self.list_container, text="ናይ ኮምፒተር መለለዪ፦ "+datas['serial'][x], bg="#FFFFFF", fg="#5A5959", font=('arial', 15)).pack(side=TOP, anchor=W)

            x=+1

    def home(self, place):
        # checking where the "request" is coming from
        if place:
            place.place_forget()
        
        # changing background
        self.master.config(bg="white")

        # nav elements
        self.nav_container = Frame(self.master, width=250, height=self.master.winfo_screenheight(), bg="#FBFBFB")
        self.nav_container.pack(side=LEFT, fill=Y)
        
        self.nav_logo_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\images\\aksum_university_logo_small.png"))
        self.nav_logo = Label(self.nav_container, image=self.nav_logo_image, bg="#FBFBFB").place(relx=0.5, rely=0.15, anchor=CENTER)

        self.university_name = Label(self.nav_container, text="ኣክሱም ዩኒቨርሲቲ", bg="#FBFBFB", fg="#5A5959", font=("arial", 17, "bold"))
        self.university_name.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.background_frame_1 = Frame(self.nav_container, width=250, height=55, bg="#FBFBFB")
        self.background_frame_2 = Frame(self.nav_container, width=250, height=55, bg="#FBFBFB")
        self.background_frame_3 = Frame(self.nav_container, width=250, height=55, bg="#FBFBFB")

        self.background_frame_1.place(x=0, rely=0.35)
        self.background_frame_2.place(x=0, rely=0.45)
        self.background_frame_3.place(x=0, rely=0.55)

        
        self.register_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\edit.png"))
        self.list_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\list.png"))
        self.search_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\search.png"))

        self.register_image_sel = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\edit_sel.png"))
        self.list_image_sel = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\list_sel.png"))
        self.search_image_sel = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\search_sel.png"))



        # register
        self.register_image_label = Label(self.background_frame_1, image=self.register_image, bg="#FBFBFB")
        self.register_image_label.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.register_text = Label(self.background_frame_1, text="መዝገብ", bg="#FBFBFB", font=("arial", 15))
        self.register_text.place(relx=0.5, rely=0.5, anchor=CENTER)

        # list
        self.list_image_label = Label(self.background_frame_2, image=self.list_image, bg="#FBFBFB")
        self.list_image_label.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.list_text = Label(self.background_frame_2, text="ዝርዝር", bg="#FBFBFB", font=("arial", 15))
        self.list_text.place(relx=0.5, rely=0.5, anchor=CENTER)

        # search
        self.search_image_label = Label(self.background_frame_3, image=self.search_image, bg="#FBFBFB")
        self.search_image_label.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.search_text = Label(self.background_frame_3, text="ኣልሽ", bg="#FBFBFB", font=("arial", 15))
        self.search_text.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.register()

app = App()
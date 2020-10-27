'''
    code authored by Abyssinya codes
'''

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import pathlib
from io import BytesIO
from BackEngine import BackEnd

engine = BackEnd()

file_dir = str(pathlib.Path(__file__).parent.absolute())

class App:

    def __init__(self):
        self.master = Tk()
        self.master.geometry('1200x900')
        self.master.config(bg="#FFFFFF")
        self.master.title("ኣክሱም ዩኒቨርሲቲ |   Aksum University")
        self.signin()
        self.master.mainloop()

    def messages(self, message, message_type):
        self.message_container = Frame(self.master, highlightthickness=1)
        self.message_container.place(relx=0.23, y=10)
        self.message = Label(self.message_container, text=message, font=('arial', 13))
        self.message.place(x=8, rely=0.5, anchor=W)
        self.error_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\images\\error.png"))
        self.success_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\images\\success.png"))
        self.close_button = Button(self.message_container, border=0, command=self.message_container.place_forget)
        self.close_button.place(relx=0.95, rely=0.5, anchor=CENTER)

        if message_type == 'error':
            self.message_container.config(highlightbackground="#F5C6CB", highlightcolor="#F5C6CB", width=700, height=50, highlightthickness=2, bd=0, bg='#F8D7DA')
            self.message.config(fg='#721C24', bg='#F8D7DA')
            self.close_button.config(image=self.error_image, bg="#F8D7DA")

        elif message_type == 'success':
            self.message_container.config(highlightbackground="#C3E6CB", highlightcolor="#C3E6CB", width=500, height=50, highlightthickness=2, bd=0, bg='#D4EDDA')
            self.message.config(fg='#155724', bg='#D4EDDA')
            self.close_button.config(image=self.success_image, bg="#D4EDDA")


    def signin(self):

        # self.message_container = Frame(self.master, highlightbackground="#F5C6CB", highlightcolor="#F5C6CB", width=500, height=200, highlightthickness=1, bd=0, bg='#F8D7DA')
        # self.message_container.place(x=50, y=10)
        # sigin_container
        self.sigin_container = Frame(self.master, width=450, height=593, bg="#FFFFFF")
        self.sigin_container.place(relx=0.5, rely=0.45, anchor=CENTER)

        # sign in components
        self.logo_image = ImageTk.PhotoImage(Image.open(file_dir+'\\files\\assets\\images\\aksum_university_logo.png'))
        self.logo = Label(self.sigin_container, image=self.logo_image, bg="#FFFFFF")
        self.logo.place(relx=0.5, rely=0.15, anchor=CENTER)

        self.welcome_message = Label(self.sigin_container, text="እንኳዕ ብደሓን መጹ", bg="#FFFFFF", fg="#5A5959", font=("consolas", 30))
        self.welcome_message.place(relx=0.5, rely=0.35, anchor=CENTER)

        self.username_text = Label(self.sigin_container, text="ናይ ተጠቃሚ ስም", bg="#FFFFFF", fg="#5D5D5D", font=("consolas", 17))
        self.username_text.place(relx=0.25, rely=0.5, anchor=CENTER)

        self.input_image = ImageTk.PhotoImage(Image.open(file_dir+'\\files\\assets\\images\\input_background_big.png'))
        self.username_background = Label(self.sigin_container, image=self.input_image, bg="#FFFFFF")
        self.username_background.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.username_input = Entry(self.username_background, font=("arial", 20, "bold"), bg="#DBDBDB", width=25, border=0, fg="#5A5959")
        self.username_input.place(x=10, y=15)


        self.password_text = Label(self.sigin_container, text="ናይ ተጠቃሚ ምስጢር ቁልፊ", bg="#FFFFFF", fg="#5D5D5D", font=("consolas", 17))
        self.password_text.place(relx=0.35, rely=0.68, anchor=CENTER)

        self.password_backgoround = Label(self.sigin_container, image=self.input_image, bg="#FFFFFF")
        self.password_backgoround.place(relx=0.5, rely=0.76, anchor=CENTER)
        self.password_input = Entry(self.password_backgoround, font=("arial", 25, "bold"), bg="#DBDBDB", width=20, border=0, fg="#5A5959", show="\u2022")
        self.password_input.place(x=10, y=15)


        self.sign_in_image = ImageTk.PhotoImage(Image.open(file_dir+'\\files\\assets\\images\\signin_button.png'))
        self.sign_in_button = Button(self.sigin_container, image=self.sign_in_image, border=0, bg="#FFFFFF", command=lambda place=self.sigin_container: self.home(place))
        self.sign_in_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    def saveData(self):
        fname = str(self.fname.get())
        lname = str(self.lname.get())
        phone = str(self.phone.get())
        cname = str(self.cname.get())
        serial = str(self.serial.get())
        try:
            ppic = self.ppic_data
            cpic = self.cpic_data
        except:
            ppic = ''
            cpic = ''

        res = engine.addDataEngine(fname, lname, phone, cname, serial, ppic, cpic)
        if res==True:
            self.fname.delete(0, END)
            self.lname.delete(0, END)
            self.phone.delete(0, END)
            self.cname.delete(0, END)
            self.serial.delete(0, END)
            txt = self.ppic_text['text']
            self.ppic_text['text'] = txt[0:-1]
            self.cpic_text['text'] = self.cpic_text['text'][0:-1]
            self.messages(fname+' ብትክክል ተመዝጊቡ ኣሎ','success')
        else:
            self.messages(res,'error')

    '''register'''
    def register(self, event):

        self.des_prev()

        self.register_body_container = Frame(self.master, bg='white')
        self.register_body_container.pack(side=RIGHT, fill=BOTH, expand=1)


        self.register_text.config(fg='#000000')
        self.list_text.config(fg='#000000')
        self.search_text.config(fg='#000000')

        self.register_image_label.config(image=self.register_image)
        self.list_image_label.config(image=self.list_image)
        self.search_image_label.config(image=self.search_image)

        self.register_image_label.config(bg="#0278AE", image=self.register_image_sel)
        self.register_text.config(bg="#0278AE", fg="white")

        # register elements
        self.entry_background_image = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\svg\\small_entry.png"))

        # first name entry
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

        # filedialog
        def getFile(type_pic):
            file = filedialog.askopenfilename(filetypes=[("Image files", ".png .jpg .jpeg .gif")])
            if file == '':
                dir_ = ''
                return None

            file_dir = file.split('/')
            dir_ = ''
            for f in range(0, len(file_dir)-1):
                dir_ = dir_ + file_dir[f] + '\\'
            dir_ += file_dir[-1]
            if type_pic == 'ppic':
                self.ppic_data = dir_
                txt = self.ppic_text['text']
                self.ppic_text['text'] = txt+'*'


            elif type_pic == 'cpic':
                self.cpic_data = dir_
                txt = self.cpic_text['text']
                self.cpic_text['text'] = txt+'*'

        # person picture
        self.ppic_text = Label(self.container_1, text="ናይ ወናኒ ፎቶ", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.ppic_text.grid(row=0, column=0)

        self.upload_button = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\images\\upload button.png"))

        self.ppic_button = Button(self.container_1, image=self.upload_button, bg="#FFFFFF", fg="#5A5959", border=0, command=lambda: getFile('ppic'))
        self.ppic_button.grid(row=1, column=0)

        # computer picture
        self.cpic_text = Label(self.container_1, text="ናይ ኮምፒተር ፎቶ", font=("arial", 15), bg="#FFFFFF", fg="#5A5959")
        self.cpic_text.grid(padx=(80, 0), row=0, column=1)

        self.cpic_button = Button(self.container_1, image=self.upload_button, bg="#FFFFFF", fg="#5A5959", border=0, command=lambda: getFile('cpic'))
        self.cpic_button.grid(padx=(80, 0), row=1, column=1)

        # save button
        self.register_button = ImageTk.PhotoImage(Image.open(file_dir+"\\files\\assets\\images\\save_button.png"))

        self.register_save = Button(self.register_body_container, image=self.register_button, bg="#FFFFFF", border=0, command=self.saveData)
        self.register_save.place(relx=0.05, rely=0.73)

    def des_prev(self):
        try:
            self.register_body_container.destroy()
        except:
            pass
        try:
            self.specific_frame_container.destroy()
        except:
            pass
        try:
            self.search_body_container.destroy()
        except:
            pass
        try:
            self.show_body_container.destroy()
        except:
            pass

    def show(self, event):
        self.des_prev()

        self.show_body_container = Frame(self.master, bg='white')
        self.show_body_container.pack(side=RIGHT, fill=BOTH, expand=1)

        self.del_img = Image.open(file_dir+'\\files\\assets\\images\\delete.png')
        self.view_img = Image.open(file_dir+'\\files\\assets\\images\\view.png')

        self.delete_image = ImageTk.PhotoImage(self.del_img.resize((self.del_img.size[0]-15, self.del_img.size[1]-8), Image.ANTIALIAS))
        self.view_image = ImageTk.PhotoImage(self.view_img.resize((self.del_img.size[0]-15, self.del_img.size[1]-8), Image.ANTIALIAS))

        datas = engine.fetchAllData()
        if datas == []:
            self.lbl = Label(self.show_body_container, text="ምንም ዓይነት እኩብ ሓበሬታ ኣየእተዉን! በይዞኦም ተመሊሶም ሓበሬታ የእትዉ", font=('arial', 20), bg="white", fg='#5e5e5e')
            self.lbl.place(rely=0.5, relx=0.5, anchor=CENTER)

        c = 0
        self.ids = []
        row = 0
        column = [0, 1]
        for data in datas:
            id = data[0]
            self.ids.append(id)

        for data in datas:
            self.frame_container = Frame(self.show_body_container, width=500, height=400, bg="#FBFBFB")
            self.frame_container.pack(side=TOP, fill=X, padx=(20, 20), pady=(20,0), anchor=N)

            self.frame_container_1 = Frame(self.frame_container, bg="#FBFBFB")
            self.frame_container_1.pack(side=LEFT, fill=X, padx=(20, 20), pady=(20,0))

            self.frame_container_2 = Frame(self.frame_container, bg="#FBFBFB")
            self.frame_container_2.pack(side=RIGHT, fill=X, padx=(20, 20), pady=(20,0))

            self.full_name_text = Label(self.frame_container_1, text='ምሉእ ስም፦ '+data[1]+' '+data[2], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(20,0), padx=(24,0))
            self.phone_number = Label(self.frame_container_1, text='ናይ ወናኒ ስልኪ፦ '+data[3], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(5,0), padx=(24,0))
            self.computer_name = Label(self.frame_container_1, text='ናይ ኮምፒተር ስም፦ '+data[4], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(5,0), padx=(24,0))
            if data[5]!=None:
                self.computer_serial = Label(self.frame_container_1, text='ናይ ኮምፒተር መለለዪ፦ '+data[5], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(5, 20), padx=(24,0))
            self.delete_btn = Button(self.frame_container_2, bg="#FBFBFB", text=self.ids[c], image=self.delete_image, border=0)
            self.view_btn = Button(self.frame_container_2, bg="#FBFBFB", image=self.view_image, border=0)

            cur_id = self.delete_btn['text']

            self.delete_btn.bind("<Button-1>", lambda event, pk=cur_id: self.delete_item(event, pk))
            self.view_btn.bind("<Button-1>", lambda event, pk=cur_id: self.show_item(event, pk))

            self.delete_btn.pack(side=TOP, pady=(0, 15), padx=(0, 10), anchor=CENTER)
            self.view_btn.pack(side=TOP, pady=(15,0), padx=(0, 10), anchor=CENTER)

            c+=1

    def delete_item(self, event, pk):
        if messagebox.askquestion(title="ጥንቃቀ!", message='እዚ እኩብ ሓበሬታ ክትድምስሱ ኢኹም ትሙክሩ ዘለኹም! ርግጸኛ ዲኹም?')==True:
            engine.delData(pk)
            self.show('nothing')

    def show_item(self, event, pk):
        datas = engine.fetchSpecifiedData('id', pk)

        self.des_prev()

        self.specific_frame_container = Frame(self.master, bg='white')
        self.specific_frame_container.pack(side=RIGHT, fill=BOTH, expand=1)

        for data in datas:

            self.person_image_data = Image.open(BytesIO(data[6]))
            WP, HP = self.person_image_data.size
            if WP>=HP:
                wp = 400
                hp = int((wp*HP)/WP)

            if WP<HP:
                hp = 400
                wp = int((hp*WP)/HP)


            self.computer_image_data = Image.open(BytesIO(data[7]))
            WC, HC = self.computer_image_data.size

            if WC>=HC:
                wc = 400
                hc = int((wc*HC)/WC)

            if WC<HC:
                hc = 400
                wc = int((hc*WC)/HC)


            self.pic_container = Frame(self.specific_frame_container, bg="white")
            self.pic_container.pack(side=TOP, anchor=W)

            self.text_container = Frame(self.specific_frame_container, bg="white")
            self.text_container.pack(side=TOP, anchor=W)

            self.person_image = ImageTk.PhotoImage(self.person_image_data.resize((wp, hp), Image.ANTIALIAS))
            self.ppic_label = Label(self.pic_container, bg="white", image=self.person_image).pack(side=LEFT, anchor=N, padx=(20, 0), pady=(20, 20))

            self.computer_image = ImageTk.PhotoImage(self.computer_image_data.resize((wc, hc), Image.ANTIALIAS))
            self.cpic_label = Label(self.pic_container, bg="white", image=self.computer_image).pack(side=LEFT, anchor=N, padx=(20, 0), pady=(20, 20))

            self.specify_fname = Label(self.text_container, fg="#797979", text="ምሉእ ስም፦ "+data[1]+' '+data[2], bg="white", font=('consolas', 20)).pack(side=TOP, anchor=W, padx=(20, 0))
            self.specify_pnum = Label(self.text_container, fg="#797979", text="ናይ ወናኒ ስልኪ፦ "+data[3], bg="white", font=('consolas', 20)).pack(side=TOP, anchor=W, padx=(20, 0))
            self.specify_cname = Label(self.text_container, fg="#797979", text="ናይ ኮምፒተር ስም፦ "+data[4], bg="white", font=('consolas', 20)).pack(side=TOP, anchor=W, padx=(20, 0))
            self.specify_cserial = Label(self.text_container, fg="#797979", text="ናይ ኮምፒተር መለለዪ፦ "+data[5], bg="white", font=('consolas', 20)).pack(side=TOP, anchor=W, padx=(20, 0))

            self.specific_delete_btn = Button(self.text_container, bg="#FBFBFB", text=data[0], image=self.delete_image, border=0)
            self.specific_delete_btn.pack(side=TOP, anchor=W, padx=(20, 0), pady=(30,0))

            self.specific_delete_btn.bind("<Button-1>", lambda event, pk=data[0]: self.delete_item(event, pk))

    def search(self, event):

        self.des_prev()

        self.search_body_container = Frame(self.master, bg='white')
        self.search_body_container.pack(side=RIGHT, fill=BOTH, expand=1)

        self.top_search_container = Frame(self.search_body_container, bg="white", width=300, height=100)
        self.top_search_container.pack(side=TOP, fill=X)

        self.result_search_container = Frame(self.search_body_container, bg="white", width=300, height=100)
        self.result_search_container.pack(side=TOP, fill=BOTH, expand=1)

        self.search_input_image_data = Image.open(file_dir+'\\files\\assets\\images\\small_entry.png')
        self.search_input_image = ImageTk.PhotoImage(self.search_input_image_data.resize((335, self.search_input_image_data.size[1]-18), Image.ANTIALIAS))

        self.search_button_image_data = Image.open(file_dir+'\\files\\assets\\images\\search_btn.png')
        self.search_button_image = ImageTk.PhotoImage(self.search_button_image_data.resize((self.search_button_image_data.size[0]-22, self.search_button_image_data.size[1]-23), Image.ANTIALIAS))

        self.info_lbl = Label(self.top_search_container, text='ክደልይዎ ዝደለዩ ቓል ኣብዚ የእትዉ', bg="white", font=('arial', 15), fg="#747474").pack(side=TOP, anchor=W, padx=(20, 0), pady=(30, 0))
        self.lbl_2 = Label(self.top_search_container, text='ብምንታይ እዩ ድሌትኩም', bg="white", font=('arial', 15), fg="#747474").place(x=380, y=33)

        self.search_lbl = Label(self.top_search_container, image=self.search_input_image, bg="white")
        self.search_lbl.pack(side=LEFT, padx=(20, 0), pady=(10, 0))

        self.search_entry = Entry(self.search_lbl, bg="#ECECEC", border=0, font=('arial',17), width=21)
        self.search_entry.place(x=10, rely=0.5, anchor=W)

        self.val_dict = {"fname":"ብናይ መጀመርያ ሽም", "lname":"ብናይ ኣቦ ሽም", "cname":"ብናይ ኮምፒተር ሽም", "pnum":"ብስልኪ ቑጽሪ", "cserial":"ብናይ ኮምፒተር መለለዪ"}

        self.search_by_var = StringVar()
        self.search_by_values = ["ብናይ መጀመርያ ሽም", "ብናይ ኣቦ ሽም", "ብናይ ኮምፒተር ሽም", "ብስልኪ ቑጽሪ", "ብናይ ኮምፒተር መለለዪ"]
        self.search_by = ttk.Combobox(self.top_search_container, textvariable=self.search_by_var, values=self.search_by_values, font=("arial", 15), width=17)
        self.search_by.set('ብናይ መጀመርያ ሽም')
        self.search_by.pack(side=LEFT, padx=(20, 0), pady=(10, 0))

        def show_search_results(datas):
            try:
                self.frame_container.destroy()
            except:
                pass
            self.del_img = Image.open(file_dir+'\\files\\assets\\images\\delete.png')
            self.view_img = Image.open(file_dir+'\\files\\assets\\images\\view.png')

            self.delete_image = ImageTk.PhotoImage(self.del_img.resize((self.del_img.size[0]-15, self.del_img.size[1]-8), Image.ANTIALIAS))
            self.view_image = ImageTk.PhotoImage(self.view_img.resize((self.del_img.size[0]-15, self.del_img.size[1]-8), Image.ANTIALIAS))

            if datas == []:
                self.lbl = Label(self.result_search_container, text="እቲ ዘእተውዎ ቃል ክርከብ ኣይከኣለን", font=('arial', 20), bg="white", fg='#5e5e5e')
                self.lbl.place(rely=0.5, relx=0.5, anchor=CENTER)

            c = 0
            self.ids = []
            row = 0
            column = [0, 1]
            for data in datas:
                id = data[0]
                self.ids.append(id)

            for data in datas:
                self.frame_container = Frame(self.result_search_container, width=500, height=400, bg="#FBFBFB")
                self.frame_container.pack(side=TOP, fill=X, padx=(20, 20), pady=(20,0), anchor=N)

                self.frame_container_1 = Frame(self.frame_container, bg="#FBFBFB")
                self.frame_container_1.pack(side=LEFT, fill=X, padx=(20, 20), pady=(20,0))

                self.frame_container_2 = Frame(self.frame_container, bg="#FBFBFB")
                self.frame_container_2.pack(side=RIGHT, fill=X, padx=(20, 20), pady=(20,0))

                self.full_name_text = Label(self.frame_container_1, text='ምሉእ ስም፦ '+data[1]+' '+data[2], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(20,0), padx=(24,0))
                self.phone_number = Label(self.frame_container_1, text='ናይ ወናኒ ስልኪ፦ '+data[3], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(5,0), padx=(24,0))
                self.computer_name = Label(self.frame_container_1, text='ናይ ኮምፒተር ስም፦ '+data[4], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(5,0), padx=(24,0))
                if data[5]!=None:
                    self.computer_serial = Label(self.frame_container_1, text='ናይ ኮምፒተር መለለዪ፦ '+data[5], bg='#FBFBFB', font=('arial', 15)).pack(anchor=W, pady=(5, 20), padx=(24,0))
                self.delete_btn = Button(self.frame_container_2, bg="#FBFBFB", text=self.ids[c], image=self.delete_image, border=0)
                self.view_btn = Button(self.frame_container_2, bg="#FBFBFB", image=self.view_image, border=0)

                cur_id = self.delete_btn['text']

                self.delete_btn.bind("<Button-1>", lambda event, pk=cur_id: self.delete_item(event, pk))
                self.view_btn.bind("<Button-1>", lambda event, pk=cur_id: self.show_item(event, pk))

                self.delete_btn.pack(side=TOP, pady=(0, 15), padx=(0, 10), anchor=CENTER)
                self.view_btn.pack(side=TOP, pady=(15,0), padx=(0, 10), anchor=CENTER)

                c+=1


        def get_search():
            word = str(self.search_entry.get())
            if word == '':
                self.messages('ምንም ዓይነት ዋጋ ኣየእተዉን' ,'error')
                return
            term = str(self.search_by_var.get())
            search_by_val = ''
            for val in self.val_dict:
                if term == self.val_dict[val]:
                    search_by_val = val

                    break

            datas = engine.fetchSpecifiedData(search_by_val, word)
            show_search_results(datas)


        self.search_button = Button(self.top_search_container, image=self.search_button_image, bg="white", border=0, command=get_search)
        self.search_button.pack(side=LEFT, padx=(20, 0), pady=(10, 0))

        # top_serach_container

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
        self.register_text = Label(self.background_frame_1, text="መዝግብ", bg="#FBFBFB", font=("arial", 15))
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

        self.register_text.bind('<Button-1>', self.register)
        self.list_text.bind('<Button-1>', self.show)
        self.search_text.bind('<Button-1>', self.search)

        self.register_image_label.bind('<Button-1>', self.register)
        self.list_image_label.bind('<Button-1>', self.show)
        self.search_image_label.bind('<Button-1>', self.search)

        self.register('nothing')

        def __del__(self):
            print("hey")

app = App()

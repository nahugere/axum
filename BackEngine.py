from db import DataBase
from configparser import ConfigParser
import pathlib
import random

config = ConfigParser()
config.read("config.ini")
file = config["database"]['file_name']

file_dir = str(pathlib.Path(__file__).parent.absolute())
dataBase = DataBase(file_dir+"\\files\\data\\"+file)

img_folder = config['database']['image_dir']
img_path = file_dir+"\\files\\data\\"+img_folder

class BackEnd:

    def __init__(self):
        self.chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&?'
        self.chars_list = []

        for char in self.chars:
            self.chars_list.append(char)
        print(self.chars_list)

    def fetchData(self):
        datas = dataBase.fetchAll()
        return datas

    def addData(self, fname, lname, pnum, cname, cserial, ppic, cpic):

        ext = '.png'

        x = 1
        char_list = ''
        while x<=6:
            rand = random.choice(self.chars)
            char_list += rand
            x+=1

        with open(ppic, 'rb') as f:
            p_file = f.read()

        with open(img_path+char_list+ext, 'w') as f:
            u_file = f.write(p_file)
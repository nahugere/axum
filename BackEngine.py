from db import DataBase
from configparser import ConfigParser
from os import walk
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

    def fetchAllData(self):
        datas = dataBase.fetchAll()
        return datas

    def addDataEngine(self, fname, lname, pnum, cname, cserial, ppic, cpic):

        p_file = ''
        c_file = ''

        if ppic != '':
            with open(ppic, 'rb') as f:
                p_file = f.read()

        if cpic != '':
            with open(cpic, 'rb') as f:
                c_file = f.read()

        if ppic == '':
            with open(file_dir+'\\files\\assets\\images\\no_image.png', 'rb') as f:
                p_file = f.read()

        if cpic == '':
            with open(file_dir+'\\files\\assets\\images\\no_image.png', 'rb') as f:
                c_file = f.read()

        if fname=='' or lname=='' or cname=='':
            return "ግቡእ ዝኮነ ዋጋ ኣይሃቡን! በይዞኦም ተመሊሶም ብስሩዕ ይምልኡ"

        if cserial == '' and cpic == '' :
            return "ብዛዕባ እታ ኮምፒተር ግቡእ ዝኮነ መለለዪ ስለ ዘይሃቡ አንደገና ተመሊሶም ብስሩዕ ይምልኡ"

        if pnum == '' and ppic == '' :
            return "ብዛዕባ እቲ ሰብ ግቡእ ዝኮነ መለለዪ ስለ ዘይሃቡ አንደገና ተመሊሶም ብስሩዕ ይምልኡ"

        if cserial == '' and cpic != '':
            cserial = ''

        elif cserial != '' and cpic == '':
            cpic = ''

        if pnum == '' and ppic != '':
            pnum = ''

        elif pnum != '' and ppic == '':
            ppic = ''


        result = dataBase.addData(fname, lname, pnum, cname, cserial, p_file, c_file)
        return result

    def delData(self, id):
        dataBase.deleteData(id)

    def fetchSpecifiedData(self, term, val):
        datas = dataBase.searchData(term, val)
        return datas

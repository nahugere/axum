# import os
# from twilio.rest import Client
#
# account_sid = 'ACbe06c06b1e12052aeb1b30aa1f5f201f'
# auth_token = '14992ab19c64f74e9702ed7405577dc7'
#
# client = Client(account_sid, auth_token)
#
# client.messages.create(
#     to = '+251927105719',
#     from_ = '+14158959573',
#     body = "Yes that's right I just sent you an sms"
# )
# #
import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication




app = QApplication(sys.argv)

web = QWebEngineView()

web.load(QUrl("https://www.codeloop.org"))

web.show()


sys.exit(app.exec_())

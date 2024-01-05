import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
print('-------connect-------')
print('enter into calculator')

form_class = uic.loadUiType("calculator.ui")[0]


class Cal(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_1.clicked.connect(self.button_1)
        self.btn_2.clicked.connect(self.button_2)
        self.btn_3.clicked.connect(self.button_3)
        self.btn_4.clicked.connect(self.button_4)
        self.btn_5.clicked.connect(self.button_5)
        self.btn_6.clicked.connect(self.button_6)
        self.btn_7.clicked.connect(self.button_7)
        self.btn_8.clicked.connect(self.button_8)
        self.btn_9.clicked.connect(self.button_9)
        self.btn_0.clicked.connect(self.button_0)
        self.btn_sum.clicked.connect(self.button_sum)
        self.btn_sub.clicked.connect(self.button_sub)
        self.btn_mul.clicked.connect(self.button_mul)
        self.btn_div.clicked.connect(self.button_div)
        self.btn_eql.clicked.connect(self.button_eql)
        self.btn_del.clicked.connect(self.button_del)
        self.btn_reset.clicked.connect(self.button_reset)

    def button_1(self):
        self.enter("1")

    def button_2(self):
        self.enter("2")

    def button_3(self):
        self.enter("3")

    def button_4(self):
        self.enter("4")

    def button_5(self):
        self.enter("5")

    def button_6(self):
        self.enter("6")

    def button_7(self):
        self.enter("7")

    def button_8(self):
        self.enter("8")

    def button_9(self):
        self.enter("9")

    def button_0(self):
        self.enter("0")

    def button_sum(self):
        self.enter("+")

    def button_sub(self):
        self.enter("-")

    def button_mul(self):
        self.enter("*")

    def button_div(self):
        self.enter("/")

    def button_del(self):
        message = self.window.text()
        self.window.setText(message[:-1])

    def button_reset(self):
        self.window.clear()

    def button_eql(self):
        data = self.window.text()
        clientSocket.sendto(data.encode(), ('127.0.0.1', 12345))
        message, addr = clientSocket.recvfrom(2048)
        self.window.setText(message.decode())

    def enter(self, new):
        message = self.window.text()
        self.window.setText(message + new)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Cal = Cal()
    Cal.show()
    app.exec_()

clientSocket.close()

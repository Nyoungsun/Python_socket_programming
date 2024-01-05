from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 12345))
serverSocket.listen(1)
print('-------waiting-------')

connSocket, addr = serverSocket.accept()
print('-------connect-------')

answer = 0
number = []
message = ''

data = connSocket.recv(1024).decode()

for i in range(0, len(data)):
    if data[i] == '+' or data[i] == '-' or data[i] == '*' or data[i] == '/':
        op = data[i]
        number.append(int(data[0:i]))
        number.append(int(data[i + 1:]))
        break
if op == '+':
    message = '%d%s%d=%d' % (number[0], op, number[1], number[0] + number[1])
    answer = answer + number[0] + number[1]
elif op == '-':
    message = '%d%s%d=%d' % (number[0], op, number[1], number[0] - number[1])
    answer = answer + number[0] - number[1]
elif op == '*':
    message = '%d%s%d=%d' % (number[0], op, number[1], number[0] * number[1])
    answer = answer + number[0] * number[1]
elif op == '/':
    message = '%d%s%d=%d' % (number[0], op, number[1], number[0] / number[1])
    answer = answer + number[0] / number[1]

connSocket.send(message.encode())
print('--------send---------')
serverSocket.close()

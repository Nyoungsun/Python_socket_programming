from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', 12345))
print('-------waiting-------')

data, addr = serverSocket.recvfrom(2048)
data = data.decode()

answer = 0
number = []
message = ''

for i in range(0, len(data)):
    if data[i] == '+' or data[i] == '-' or data[i] == '*' or data[i] == '/':
        op = data[i]
        number.append(int(data[0:i]))
        number.append(int(data[i + 1:]))
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

serverSocket.sendto(message.encode(), addr)
print('--------send---------')


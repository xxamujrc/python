
# importing the required module
import matplotlib.pyplot as plt
from numpy import printoptions
import serial
import time

port = serial.Serial('COM2', 9600)
port.timeout = 1


def gp():
    # while 1:
    # i = input("enter your command: ").strip()
    # if 'done' in i:
    #     print('program finished')
    #     break
    # port.write(i.encode())
    time.sleep(0.5)
    print(port.readline().decode('ascii'))
    port.close()


a = gp()
print(list[a])
# x axis values
# x = [b]
# corresponding y axis values
# y = [2, 4, 1, 5]

# plotting the points
# plt.plot(x, y)
plt.plot(x)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()

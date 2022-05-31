from tkinter import font
import serial
from tkinter import *
from matplotlib import markers, projections, pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# geeksforgeeks, stackoverflow,  python, github
app = Tk()
app.state('zoomed')
app.config(background='#123456')

a = []
b = []
c = []
d = []

plt.ion()
plt.style.use('ggplot')
fig = plt.figure(figsize=(15, 7), dpi=100)
ay = fig.add_subplot(321) # ph
by = fig.add_subplot(322) # temp
cy = fig.add_subplot(323) # humi
dy = fig.add_subplot(325) # tds
ser = serial.Serial('COM2', 9600)


def gph(i):
    while True:
        ser.reset_input_buffer()
        data = ser.readline().decode('ascii')
        dataArray = data.split(',')
        print(data)
# pan dagdag sa graph
        value1 = float(dataArray[0])
        a.append(value1)
        plt.ylim(20, 40)
        ay.plot(a, color='b')
        ay.set_title('ph')

        value2 = float(dataArray[1])
        b.append(value2)
        plt.ylim(0, 14)
        by.plot(b, color='r')
        by.set_title('temp')

        plt.draw()
        plt.pause(0.00001)


fig.suptitle('data plotting')
plot_canvas = FigureCanvasTkAgg(fig, app, gph)
plot_canvas.get_tk_widget().pack()
ani = animation.FuncAnimation(fig, gph, interval=1000, blit=True)
plot_canvas.draw()

app.mainloop()

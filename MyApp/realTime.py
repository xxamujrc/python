from tkinter import font
from turtle import left, right, title
import serial
from tkinter import *
import numpy as np
from matplotlib import markers, projections, pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.interpolate import make_interp_spline

root = Tk()
root.geometry('1600x800')
root.title('Real Time Monitoring')
root.state('zoomed')
root.config(background='#2D3235')

i = 0
yar1 = []
yar2 = []
yar3 = []
yar4 = []

plt.ion()
plt.style.use('dark_background')  # dark_background, ggplot, bmh
color = "#2D3235"
fig = plt.figure(figsize=(15, 7), dpi=100, facecolor=color)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ser = serial.Serial('COM2', 9600)


def animate(i):
    while 1:
        # for i in range(1000):
        ser.reset_input_buffer()
        data = ser.readline().decode('ascii')
        data_array = data.split(',')
        print(data)
    # ------------------------------------------+
        yvalue1 = float(data_array[0])
        yar1.append(yvalue1)
        plt.ylim(16, 50)
        ax1.plot(yar1, color='blue')
        ax1.set_xlim(left=max(0, i-24), right=i+24)
        ax1.set_title('Temperature')
    # ------------------------------------------+
        yvalue2 = float(data_array[1])
        yar2.append(yvalue2)
        plt.ylim(0, 100)
        ax2.plot(yar2, color='green')
        ax2.set_xlim(left=max(0, i-24), right=i+24)
        ax2.set_title('Humidity')
    # ------------------------------------------+
        yvalue3 = float(data_array[2])
        yar3.append(yvalue3)
        plt.ylim(0, 15)
        ax3.plot(yar3, color='red')
        ax3.set_xlim(left=max(0, i-24), right=i+24)
        ax3.set_title('ph Level')
    # ------------------------------------------+
        yvalue4 = float(data_array[3])
        yar4.append(yvalue4)
        plt.ylim(0, 3000)
        ax4.plot(yar4, color='orange')
        ax4.set_xlim(left=max(0, i-24), right=i+24)
        ax4.set_title('TDS')
    # ------------------------------------------+
        plt.draw()
        plt.pause(0.00001)
        i += 1


fig.suptitle('Real-time Monitoring System', fontweight='bold')
plot_canvas = FigureCanvasTkAgg(fig, root, animate)
plot_canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
ani = animation.FuncAnimation(fig, animate, interval=1000, blit=True)
plot_canvas.draw()

root.mainloop()

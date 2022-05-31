from tkinter import font
import serial
from tkinter import *
import numpy as np
from matplotlib import markers, projections, pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyttsx3
import speech_recognition as sr

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
color = "#001219"
fig = plt.figure(figsize=(15.2, 8), dpi=100, facecolor=color)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)
ser = serial.Serial('COM2', 9600)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def mainGraph():
    def animate(i):
        while 1:
            # for i in range(1000):
            ser.reset_input_buffer()
            data = ser.readline().decode('ascii')
            data_array = data.split(',')
            # print(data)
        # ------------------------------------------+
            yvalue1 = float(data_array[0])
            yar1.append(yvalue1)
            plt.ylim(19, 40)
            ax1.plot(yar1, color='#005f73', linestyle='dotted', marker='o',
                     markerfacecolor='#0a9396', markersize=6, linewidth=1)
            ax1.set_xlim(left=max(0, i-5), right=i+5)
            ax1.set_title('Temperature')
        # ------------------------------------------+
            yvalue2 = float(data_array[1])
            yar2.append(yvalue2)
            plt.ylim(0, 100)
            ax2.plot(yar2, color='#94d2bd', linestyle='dotted',
                     marker='o', markersize=6, markerfacecolor='#e9d8a6', linewidth=1)
            ax2.set_xlim(left=max(0, i-5), right=i+5)
            ax2.set_title('Humidity')
        # ------------------------------------------+
            yvalue3 = float(data_array[2])
            yar3.append(yvalue3)
            plt.ylim(0, 15)
            ax3.plot(yar3, color='#9b2226', linestyle='dotted',
                     marker='o', markersize=6, markerfacecolor='#ae2012', linewidth=1)
            ax3.set_xlim(left=max(0, i-5), right=i+5)
            ax3.set_title('Acidity')
        # ------------------------------------------+
            yvalue4 = float(data_array[3])
            yar4.append(yvalue4)
            plt.ylim(0, 3000)
            ax4.plot(yar4, color='#ca6702', linestyle='dotted',
                     marker='o', markersize=6, markerfacecolor='#ee9b00', linewidth=1)
            ax4.set_xlim(left=max(0, i-5), right=i+5)
            ax4.set_title('Salinity')
        # ------------------------------------------+
            plt.draw()
            plt.pause(0.00001)
            i += 1

    fig.suptitle('Real-time Monitoring System', fontweight='bold')
    plot_canvas = FigureCanvasTkAgg(fig, root, animate)
    plot_canvas.get_tk_widget().pack()
    ani = animation.FuncAnimation(fig, animate, interval=1000, blit=True)
    plot_canvas.draw()

    root.mainloop()


speak("""hi, welcome to real time monitoring application made by mr. ryan.
if you wan to continue... say YES...
otherwise... say NO""")
r = sr.Recognizer()
with sr.Microphone() as source:
    # speak("Say Anything, i'm listening")
    print(" listening...")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio, language='en-Ph')
    print("you said: {}".format(text))
    if "yes" in text:
        speak("projecting data monitoring...")
        mainGraph()
    elif "no" in text:
        exit()
except:
    speak('say it again')

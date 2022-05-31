from random import random
import tkinter
import customtkinter
import serial
# from tkinter import *
import numpy as np
from matplotlib import markers, projections, pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyttsx3
import time
import speech_recognition as sr

customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x180")
app.title("Milo")

# greet = ['calibrating', 'analyzing', 'generating', 'projecting']

# creating tts
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function for buttons


def takeCommand():
    speak("okay sir")
    mainProgram()


y_padding = 13

frame_1 = customtkinter.CTkFrame(master=app, corner_radius=15)
frame_1.pack(pady=10, padx=10, fill="both", expand=True)

button_1 = customtkinter.CTkButton(
    master=frame_1, text="TAKE COMMAND", corner_radius=8,
    command=takeCommand,
    hover_color="#38444A")
button_1.pack(pady=y_padding, padx=10)
# button_1.place(relx = 0.5, rely=0.5, anchor=tkinter.CENTER)

# ------ graphs - main program ---------


def mainProgram():
    print("full program ----------- ok")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say Anything, i'm listening")
        print(" listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='en-Ph')
        print("you said: {}".format(text))
        if "real time status" in text:
            speak("calibrating real time monitoring system...")
            fullGraph()
        elif "room temperature" in text:
            # speak(a)
            speak("projecting room temperature...")
            temp()
        elif "humidity status" in text:
            speak("processing humidity status...")
            hum()
        elif "acidity level" in text:
            speak("measuring acidity level...")
            ph()
        elif "salinity level" in text:
            speak("analyzing salinity level...")
            tds()
        elif "close" in text:
            speak("program, shutting down")
        else:
            speak("pardon me sir")
            mainProgram()
    except:
        speak('say it again')
        mainProgram()


def fullGraph():
    print("full graph ----------- ok")
    i = 0
    yar1 = []
    yar2 = []
    yar3 = []
    yar4 = []

    plt.ion()
    plt.style.use('Solarize_Light2')  # dark_background, ggplot, bmh
    color = "#2D3235"
    fig = plt.figure(figsize=(16, 8), dpi=100, facecolor=color)
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ser = serial.Serial('COM2', 9600)

    def animate(i):
        while 1:
            ser.reset_input_buffer()
            data = ser.readline().decode('ascii')
            data_array = data.split(',')
            print(data)

            yValue_1 = float(data_array[0])
            yar1.append(yValue_1)
            plt.ylim(20, 40)
            ax1.plot(yar1, color='blue')
            ax1.set_xlim(left=max(0, i-24), right=i+24)
            ax1.set_title('Temperature')

            yValue_2 = float(data_array[1])
            yar2.append(yValue_2)
            plt.ylim(0, 100)
            ax2.plot(yar2, color='green')
            ax2.set_title('Humidity')

            yValue_3 = float(data_array[2])
            yar3.append(yValue_3)
            plt.ylim(0, 14)
            ax3.plot(yar3, color='red')
            ax3.set_title('ph Level')

            yValue_4 = float(data_array[3])
            yar4.append(yValue_4)
            plt.ylim(0, 3000)
            ax4.plot(yar4, color='blue')
            ax4.set_title('TDS')

            plt.pause(0.0001)
            i += 1

    fig.suptitle('Real-time Monitoring System', fontweight='bold')
    plot_canvas = FigureCanvasTkAgg(fig, app, animate)
    # plot_canvas.get_tk_widget().grid(column=1, row=1)
    ani = animation.FuncAnimation(fig, animate, interval=1000, blit=True)
    plot_canvas.draw()
    mainProgram()


def temp():
    print("temp ----------- ok")
    i = 0
    yar1 = []
    plt.ion()
    plt.style.use('Solarize_Light2')  # dark_background, ggplot, bmh
    color = "#2D3235"
    # fig = plt.figure(figsize=(16, 8), dpi=100, facecolor=color)
    fig, ax1 = plt.subplots()
    ser = serial.Serial('COM2', 9600)

    def animate(i):
        while 1:
            ser.reset_input_buffer()
            data = ser.readline().decode('ascii')
            data_array = data.split(',')
            print(data)

            yvalue1 = float(data_array[0])
            yar1.append(yvalue1)
            plt.ylim(20, 40)
            ax1.plot(yar1, color='blue')
            ax1.set_xlim(left=max(0, i-24), right=i+24)
            ax1.set_title('Temperature')

            plt.pause(0.0001)
            i += 1
    fig.suptitle('Real-time Monitoring System', fontweight='bold')
    plot_canvas = FigureCanvasTkAgg(fig, app, animate)
    # plot_canvas.get_tk_widget().grid(column=1, row=1)
    ani = animation.FuncAnimation(fig, animate, interval=1000, blit=True)
    plot_canvas.draw()
    mainProgram()


def hum():
    print("hum ----------- ok")
    i = 0
    yar2 = []
    plt.ion()
    plt.style.use('Solarize_Light2')  # dark_background, ggplot, bmh
    color = "#2D3235"
    fig = plt.figure(figsize=(16, 8), dpi=100, facecolor=color)
    mainProgram()


def ph():
    print("acidity level ----------- ok")
    i = 0
    yar3 = []
    plt.ion()
    plt.style.use('Solarize_Light2')  # dark_background, ggplot, bmh
    color = "#2D3235"
    fig = plt.figure(figsize=(16, 8), dpi=100, facecolor=color)
    mainProgram()


def tds():
    print("tds ----------- ok")
    i = 0
    yar4 = []
    plt.ion()
    plt.style.use('Solarize_Light2')  # dark_background, ggplot, bmh
    color = "#2D3235"
    fig = plt.figure(figsize=(16, 8), dpi=100, facecolor=color)
    mainProgram()


app.mainloop()

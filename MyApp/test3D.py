# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt


# # function for z axea
# def f(x, y):
#     return np.sin(np.sqrt(x ** 2 + y ** 2))


# # x and y axis
# x = np.linspace(-1, 5, 10)
# y = np.linspace(-1, 5, 10)

# X, Y = np.meshgrid(x, y)
# Z = f(X, Y)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.plot_wireframe(X, Y, Z, color='green')
# ax.set_title('wireframe geeks for geeks')
# plt.show()
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go

# fig = make_subplots(rows=3, cols=1)

# fig.append_trace(go.Scatter(
#     x=[3, 4, 5],
#     y=[1000, 1100, 1200],
# ), row=1, col=1)

# fig.append_trace(go.Scatter(
#     x=[2, 3, 4],
#     y=[100, 110, 120],
# ), row=2, col=1)

# fig.append_trace(go.Scatter(
#     x=[0, 1, 2],
#     y=[10, 11, 12]
# ), row=3, col=1)


# fig.update_layout(height=600, width=600, title_text="Stacked Subplots")
# fig.show()
# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt


# # Creating dataset
# x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
# y = x.copy().T  # transpose
# z = (np.sin(x ** 2) + np.cos(y ** 2))

# # Creating figure
# fig = plt.figure(figsize=(14, 9))
# ax = plt.axes(projection='3d')

# # Creating plot
# ax.plot_surface(x, y, z)

# # show plot
# plt.show()

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *


class testme:
    def __init__(self, frame1):
        self.frame1 = frame1
        self.button = Button(self.frame1, text="DRAWME", command=self.plot)
        self.button1 = Button(self.frame1, text="CLEARME",
                              command=self.clearme)
        self.button.pack()
        self.button1.pack()

    def plot(self):
        f = Figure(figsize=(5, 1))
        aplt = f.add_subplot(111)
        aplt.plot([1, 2, 3, 6])
        self.wierdobject = FigureCanvasTkAgg(f, master=self.frame1)
        self.wierdobject.get_tk_widget().pack()
        self.wierdobject.draw()

    def clearme(self):
        self.wierdobject.get_tk_widget().pack_forget()


root = Tk()
aframe = Frame(root)
testme(aframe)
aframe.pack()  # packs a frame which given testme packs frame 1 in testme
root.mainloop()

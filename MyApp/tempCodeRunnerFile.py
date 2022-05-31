# import ttk
import tkinter as tk
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")


a = Figure(figsize=(4, 4))
plot_a = a.add_subplot(111)

b = Figure(figsize=(4, 4))
plot_b = b.add_subplot(111)

x = [1, 2, 3, 4, 5]
y_a = [1, 4, 9, 16, 25]
y_b = [25, 16, 9, 4, 1]


def updateGraphs(i):

    plot_a.clear()
    plot_a.plot(x, y_a)

    plot_b.clear()
    plot_b.plot(x, y_b)


class TransientAnalysis(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Transient Analysis GUI: v1.0")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (GraphPageA, GraphPageB):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GraphPageA)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class GraphPageA(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="Show Graph B",
                             command=lambda: controller.show_frame(GraphPageB))
        button1.grid(row=1, column=0, pady=20, padx=10, sticky='w')

        canvasA = FigureCanvasTkAgg(a, self)
        canvasA.draw()
        canvasA.get_tk_widget().grid(row=1, column=1, pady=20, padx=10, sticky='nsew')


class GraphPageB(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        button1 = tk.Button(self, text="Show Graph A",
                             command=lambda: controller.show_frame(GraphPageA))
        button1.grid(row=1, column=0, pady=20, padx=10, sticky='w')

        canvasB = FigureCanvasTkAgg(b, self)
        canvasB.draw()
        canvasB.get_tk_widget().grid(row=1, column=1, pady=20, padx=10, sticky='nsew')


app = TransientAnalysis()
app.geometry("800x600")
aniA = animation.FuncAnimation(a, updateGraphs, interval=1000)
aniB = animation.FuncAnimation(b, updateGraphs, interval=1000)
app.mainloop()

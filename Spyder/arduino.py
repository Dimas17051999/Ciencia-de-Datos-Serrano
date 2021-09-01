#pip install tk
import tkinter
#pip install tk-tools
import tk_tools
#pip install pyserial
import serial
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import datetime

datos=np.array([])
condicion=False

arduino=serial.Serial('com3',9600)

def plot_datos():
    pass

def plot_iniciar():
    pass

def plot_detener():
    pass

def cerrar_ventana():
    arduino.close()
    igu.destroy()

igu=tkinter.Tk()
#igu=tkinter.Toplevel()
igu.title("Osciloscopio")
igu.configure(background='white')
igu.geometry("900x720")

fig=Figure(figsize=(8,4),dpi=100)
ax=fig.add_subplot(111)
ax.set_title("Voltaje del sensor")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Voltaje")
ax.grid(True,linestyle='-.')
ax.set_xlim(0,100)
ax.set_ylim(0,5)
linea=ax.plot([],[],color='green',marker='o',markersize=6)[0]

canvas=FigureCanvasTkAgg(fig,master=igu)
canvas.get_tk_widget().grid(row=0,column=0,rowspan=2,
                            columnspan=2,padx=30,pady=30)
canvas.draw()

boton_iniciar=tkinter.Button(igu,text='Iniciar Gráfica',
                            font=('Verdana',14),padx=10,
                            pady=10,bg='green',fg='white',
                            command=lambda:plot_iniciar())

boton_detener=tkinter.Button(igu,text='Pausar Gráfica',
                            font=('Verdana',14),padx=10,
                            pady=10,bg='red',fg='white',
                            command=lambda:plot_detener())

boton_cerrar=tkinter.Button(igu,text='Cerrar Ventana',
                            font=('Verdana',14),padx=10,
                            pady=10,command=cerrar_ventana)

etiqueta=tkinter.Label(igu,text='Voltaje leído del sensor: ',
                       font=('Verdana',18),bg='white')

display=tk_tools.SevenSegmentDigits(igu,digits=4,
                                    background='white',
                                    digit_color='black',
                                    height=60)

etiqueta.grid(row=2,column=0)
display.grid(row=2,column=1,pady=10)
boton_iniciar.grid(row=3,column=0,pady=20)
boton_detener.grid(row=3,column=1,pady=20)
boton_cerrar.grid(row=4,column=0,columnspan=2)

arduino.reset_input_buffer()
igu.after(1,plot_datos)

igu.mainloop()



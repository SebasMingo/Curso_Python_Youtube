#--->Interfaz grafica en python de Usuario en Python #67
#vamos a utilizar el modulo Tkinter que viene integrado con python
#Diferencias entre Widgets y ventanas, 
# los widgets son elementos de la intefaz grafica como botones, cuadros de texto, etiqeutas, imagenes, etc
# las ventanas sirven como contenedores para alojar estos widgets
#####from tkinter import * 
#Importamos tkinter
#Empezamos crando una ventana simple, le damos el nombre "windows", para instanciar esa ventana lo igualamos a Tk()
#####windows = Tk()
#Cambiamos el tamanho de la ventana, esto tiene que ir antes de mainloop
#####windows.geometry('600x600')
#Para cambiar el titulo de ventana
#####windows.title('Fabiu')
#Vamos a cambiar el icono(favicon), cambiamos al formato Photoimage que es el formato que tkinter soporta, creamos primeramente una variable que se llama icono
#####icono = PhotoImage(file='C:/Users/chiar/Downloads/python.png')
#Necesitamos configurar el icono de nuestra ventana, hay una funcion que se encarga de eso que es iconphoto
#####windows.iconphoto(True, icono)
#Para mostar nuestra ventana
#####windows.mainloop()


#--->Etiquetas con Tkinter en Python #68
#####from tkinter import *

#####window = Tk()

#####label = Label(window, 
              #####text='Hola, quieres aprender a programar?', 
              #####font=('Arial', 40, 'bold'), 
              #####fg= '#00FFFF', 
              #####bg='black',
              #####relief='raised',
              #####bd=20,
              #####padx=50,
              #####pady=50)
#####label.pack(padx=150, pady=150)
#####label.place(x=100, y=100)

#####window.mainloop()


#--->Como Crear un Boton en Python con Tkinter #69

#####from tkinter import *

#####def click():
    #####print('Hiciste click en el boton!')
#####window = Tk()

#####imagen = PhotoImage(file='C:/Users/chiar/#####Downloads/click1.png')

#####boton = Button(window, 
               #####text='Haz click', command=click, 
               #####font=('Arial', 20, 'bold'), fg='red', 
               #####bg='#fff',
               #####activeforeground='red',
               #####activebackground='#fff',
               #####state='active',
               #####relief='raised',
               #####bd=10,
               #####padx=15,
               #####pady=15,
               #####image=imagen,
               #####compound='top'
               #####)
#####boton.pack()

#####window.mainloop()

#--->Widget de Entrada en Python con Tkinter #70

#####from tkinter import *

#####def enviar():
    #####nombre_usuario = entrada.get()
    #####print('Hola ' + nombre_usuario)
    #####entrada.config(state=DISABLED)
    # este comando despues de que le demos enviar desabilita y ya no podremos ingresar mas datos

#####def reset():
    #####entrada.delete(0, END)

#####def eliminar():
    #####entrada.delete( len(entrada.get())-1, END)

#####window = Tk()

#####entrada = Entry(window, font=('Arial',50), fg='red', bg='#000')

#####entrada.insert(0,'Hola')
#Imprime por defecto "Hola"

#####entrada.pack(side=LEFT)

#####boton_enviar = Button(window, text='Enviar', command=enviar)
#####boton_enviar.pack(side=RIGHT)

#####boton_resetear = Button(window, text='Reset', command=reset)
#####boton_resetear.pack(side=RIGHT)

#####boton_eliminar = Button(window, text='Eliminar', command=eliminar)
#####boton_eliminar.pack(side=RIGHT)

#####window.mainloop()
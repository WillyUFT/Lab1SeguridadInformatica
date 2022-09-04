# Vamos a hacer una interfaz para que se vea lindo, importemos tkinter
import tkinter as TK
from turtle import color, title  # Biblioteca para realizar interfaces gráficas
import cifrados

#Acá están las acciones que cada botón debe ejecutar
def AccionesBotones(boton):
    if boton == "rot 8":
        # Se toma el mensaje escrito en la casilla de mensaje
        msjCifrado = cifrados.rotN(mensaje.get(1.0, "end-1c"), 8)
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0","end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Rot 8: " + msjCifrado)
    elif boton == "vignere":
        # Se toma el mensaje escrito en la casilla de mensaje
        msjCifrado = cifrados.vigenere(mensaje.get(1.0, "end-1c"), "heropassword")
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0","end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Vignere: " + msjCifrado)
    elif boton == "rot 12":
        # Se toma el mensaje escrito en la casilla de mensaje
        msjCifrado = cifrados.rotN(mensaje.get(1.0, "end-1c"), 12)
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0","end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Rot 12: " + msjCifrado)
    elif boton == "rot -8":
        # Se toma el mensaje escrito en la casilla de mensaje encriptado
        msjDescifrado = cifrados.rotN(mensajeEncriptado.get(1.0, "end-1c"), -8)
        # Se borra lo que pueda estar escrito en la casilla de mensaje
        mensaje.delete("1.0","end")
        # Se escribe en la casilla de mensaje el resultado
        mensaje.insert("end", "Rot -8: " + msjDescifrado)
    elif boton == "-vignere":
        # Se toma el mensaje escrito en la casilla de mensaje encriptado
        msjDescifrado = cifrados.des_vigenere(mensajeEncriptado.get(1.0, "end-1c"), "heropassword")
        # Se borra lo que pueda estar escrito en la casilla de mensaje
        mensaje.delete("1.0","end")
        # Se escribe en la casilla de mensaje el resultado
        mensaje.insert("end", "Vignere: " + msjDescifrado)
    elif boton == "rot -12":
        # Se toma el mensaje escrito en la casilla de mensaje encriptado
        msjDescifrado = cifrados.rotN(mensajeEncriptado.get(1.0, "end-1c"), -12)
        # Se borra lo que pueda estar escrito en la casilla de mensaje
        mensaje.delete("1.0","end")
        # Se escribe en la casilla de mensaje el resultado
        mensaje.insert("end", "Rot -12: " + msjDescifrado)
    elif boton == "desafio 1":
        # Se toma el mensaje escrito en la casilla de mensaje
        msjCifrado = cifrados.desafio1(mensaje.get(1.0, "end-1c"))
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0","end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Desfío 1: " + msjCifrado)
    elif boton == "desafio 2":
        # En este caso no se manda nada, solo se llama a la función
        msjCifrado = cifrados.desafio2(False, "")
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0","end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Desfío 2: " + msjCifrado)
    elif boton == "desafio 2 custom":
        # Se toma el mensaje escrito en la casilla de mensaje
        msjCifrado = cifrados.desafio2(True, mensaje.get(1.0, "end-1c"))
        # Se borra lo que pueda estar escrito en la casilla de mensaje encriptado
        mensajeEncriptado.delete("1.0","end")
        # Se escribe en la casilla de mensaje encriptado el resultado
        mensajeEncriptado.insert("end", "Desfío 2: " + msjCifrado)
        
# Creamos la ventana
ventana = TK.Tk()
ventana.geometry("1000x500")
ventana.resizable(height=False, width=False)
ventana.title("Seguridad informática")
ventana.iconbitmap("miko.ico")

# Fondito
pantalla = TK.PhotoImage(file="akukin.png")
fotopantalla = TK.Label(ventana, image=pantalla)
fotopantalla.place(x=0, y=0)


## Lado izquierdo de Aqua
# Este es el cosito que dice mensaje
mensajeLabel = TK.Label(ventana, text="Mensaje")
mensajeLabel.place(x=100, y=170, width=190)

# Acá se pondrá el mensaje que quiere encriptar el cliente.
mensaje = TK.Text(ventana)
mensaje.place(x=100, y=190, width=190, height=100)

# Este es el cosito que dice encriptar y eso
botonesEncriptadoLabel = TK.Label(ventana, text="Encriptar mediante: ")
botonesEncriptadoLabel.place(x=100, y=300, width=190)

# Este es el boton para el rot 8
TK.Button(ventana, text="Rot 8", command=lambda: AccionesBotones("rot 8")).place(
    x=100, y=330, width=60
)

# Este es el boton para el Vignere
TK.Button(ventana, text="Vignere", command=lambda: AccionesBotones("vignere")).place(
    x=165, y=330, width=60
)

# Este es el boton para el rot 12
TK.Button(ventana, text="Rot 12", command=lambda: AccionesBotones("rot 12")).place(
    x=230, y=330, width=60
)

# Boton para el desafío 1
TK.Button(ventana, text="Desafío 1", command=lambda: AccionesBotones("desafio 1")).place(
    x=100, y=365, width=190
)

##Lado derecho de Aqua
# Este es el cosito que dice mensaje encriptado
mensajeEncriptadoLabel = TK.Label(ventana, text="Mensaje encriptado")
mensajeEncriptadoLabel.place(x=710, y=170, width=190)

# Acá se pondrá el mensaje que quiere encriptar el cliente.
mensajeEncriptado = TK.Text(ventana)
# mensajeEncriptado.config(state=TK.DISABLED)
mensajeEncriptado.place(x=710, y=190, width=190, height=100)

# Este es el cosito que dice encriptar y eso
botonesDesEncriptadoLabel = TK.Label(ventana, text="Desencriptar mediante: ")
botonesDesEncriptadoLabel.place(x=710, y=300, width=190)

# Este es el boton para el rot -8
TK.Button(ventana, text="Rot -8", command=lambda: AccionesBotones("rot -8")).place(
    x=710, y=330, width=60
)

# Este es el boton para el Vignere
TK.Button(
    ventana, text="Vignere", command=lambda: AccionesBotones("-vignere")
).place(x=775, y=330, width=60)

# Este es el boton para el rot -12
TK.Button(ventana, text="Rot -12", command=lambda: AccionesBotones("rot -12")).place(
    x=840, y=330, width=60
)

# Boton para el desafío 2
TK.Button(ventana, text="Desafío 2", command=lambda: AccionesBotones("desafio 2")).place(
    x=710, y=365, width=190
)

# Boton para el desafío 2 custom
TK.Button(ventana, text="Desafío 2 Personalizado", command=lambda: AccionesBotones("desafio 2 custom")).place(
    x=710, y=395, width=190
)

# Coso para que no se cierre
ventana.mainloop()
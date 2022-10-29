from tkinter import *
import socket

try:
	janela = Tk()
	janela.title("Host checker")
	janela.geometry("500x500")
	janela["bg"] = "black"

	def conecta():
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(3)
			r = s.connect_ex((ip1.get(), int(porta1.get())))
			if(r == 0):
				resultado1.config(text = "Host {} está no ar!".format(ip1.get()))
			else:
				resultado1.config(text = "Host {} está fora do ar!".format(ip1.get()))
		except socket.error:
			resultado1.config(text = "Host invalida!")
	ip1 = Entry(janela)
	ip1.place(x=160, y=100)
	ip1.insert(0, "HOST")

	botao1 = Button(janela, text="Conectar", command=conecta)
	botao1.place(x=200,y=200)

	resultado1 = Label(janela)
	resultado1.place(x=150, y=300)
	resultado1["fg"] = "white"
	resultado1["bg"] = "black"
	porta1 = Entry(janela)
	porta1.place(x=160, y=75)
	porta1.insert(0, "PORTA")

	janela.mainloop()
except:
	print("Ocorreu um erro no programa!")
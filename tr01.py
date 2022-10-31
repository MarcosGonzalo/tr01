from tkinter import *
import re
import pyodbc

server = "localhost"
bd = "bd_user"
usuario = "trabajo"
password = "senati"

try:
	conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};SERVER='+server+';DATABASE='+bd+';UID='+usuario+';PWD=' + password)
	print("conection exitosa")
except Exception as e:
	print("Nada papi")


def createFrame():
	frame = frame1 = Frame( width=400,height=320)
	frame.config(bg = "gray")
	frame.config(relief = "raised")
	frame.config(bd = "5")
	return frame

class Registro_tienda():
	def __init__(self):
		root = Tk()
		root.title('Ferretería El tornillo feliz')
		 
		miFrame = Frame(root)
		miFrame.pack()
		#------- Label y entry DNI --------------------------------
		self.obtenerDni=StringVar()
		lDni = Label(miFrame, text='DNI:')
		lDni.grid(row=0, column=0, sticky='e', pady=5, padx=5)
		tDni = Entry(miFrame,textvariable=self.obtenerDni)
		tDni.grid(row=0, column=1, pady=5, padx=5)

		#------- Label y entry Apallido --------------------------------
		self.obtenerApellido=StringVar()
		lApellido = Label(miFrame, text='Apellido:')
		lApellido.grid(row=1, column=0, sticky='e', pady=5, padx=5)
		tApellido = Entry(miFrame,textvariable=self.obtenerApellido)
		tApellido.grid(row=1, column=1, pady=5, padx=5)
		#------- Label y entry Nombre --------------------------------
		self.obtenerNombre=StringVar()
		lNombre = Label(miFrame, text='Nombre:')
		lNombre.grid(row=1, column=2, sticky='e', pady=5, padx=5)
		tNombre = Entry(miFrame,textvariable=self.obtenerNombre)
		tNombre.grid(row=1, column=3, pady=5, padx=5)
		#------- Label y entry Diección --------------------------------
		self.obtenerDir=StringVar()
		lDireccion = Label(miFrame, text='Dirección:')
		lDireccion.grid(row=2, column=0, sticky='e', pady=5, padx=5)
		tDireccion = Entry(miFrame,textvariable=self.obtenerDir)
		tDireccion.grid(row=2, column=1, columnspan=3, sticky='we',pady=5, padx=5)
		#------- Label y entry Teléfono --------------------------------
		self.obtenerTel=StringVar()
		lTel = Label(miFrame, text='Teléfono:')
		lTel.grid(row=3, column=0, sticky='e', pady=5, padx=5)
		tTel = Entry(miFrame,textvariable=self.obtenerTel)
		tTel.grid(row=3, column=1,columnspan=3, sticky='we', pady=5, padx=5)
		#---------------------------------------------------------------
		miFrame1 = Frame(root)
		miFrame1.pack()
		#------- Label y entry,s Código producto -----------------------
		self.tCodigo1 = StringVar()
		self.tCodigo2 = StringVar()
		self.tCodigo3 = StringVar()
		lCodigo = Label(miFrame1, text='Cod_Prod')
		lCodigo.grid(row=4, column=0,sticky='e', pady=5, padx=5)
		Codigo1 = Entry(miFrame1, textvariable = self.tCodigo1, width=7)
		Codigo1.grid(row=5, column=0, pady=5, padx=5)
		Codigo2 = Entry(miFrame1, textvariable = self.tCodigo2, width=7)
		Codigo2.grid(row=6, column=0, pady=5, padx=5)
		Codigo3 = Entry(miFrame1, textvariable = self.tCodigo3, width=7)
		Codigo3.grid(row=7, column=0, pady=5, padx=5)
		#------- Label y entry,s Descripción ---------------------------
		lDes = Label(miFrame1, text='Descripción')
		lDes.grid(row=4, column=1,sticky='ew', pady=5, padx=5)
		tDes1 = Entry(miFrame1, width=7, state="readonly")
		tDes1.grid(row=5, column=1, pady=5, padx=5)
		tDes2 = Entry(miFrame1, width=7, state="readonly")
		tDes2.grid(row=6, column=1, pady=5, padx=5)
		tDes3 = Entry(miFrame1, width=7, state="readonly")
		tDes3.grid(row=7, column=1, pady=5, padx=5)
		#------- Label y entry,s Unidad --------------------------------
		lUni = Label(miFrame1, text='Unidad')
		lUni.grid(row=4, column=2,sticky='ew', pady=5, padx=5)
		tUni1 = Entry(miFrame1, width=7, state="readonly")
		tUni1.grid(row=5, column=2, pady=5, padx=5)
		tUni2 = Entry(miFrame1, width=7, state="readonly")#width número de caracteres
		tUni2.grid(row=6, column=2, pady=5, padx=5)
		tUni3 = Entry(miFrame1, width=7, state="readonly")
		tUni3.grid(row=7, column=2, pady=5, padx=5)
		#------- Label y entry,s Cantidad ------------------------------
		self.tCantidad1 = StringVar()
		self.tCantidad2 = StringVar()
		self.tCantidad3 = StringVar()

		lCantidad = Label(miFrame1, text='Cantidad')
		lCantidad.grid(row=4, column=3,sticky='ew', pady=5, padx=5)
		Cantidad1 = Entry(miFrame1, textvariable = self.tCantidad1, width=7)
		Cantidad1.grid(row=5, column=3, pady=5, padx=5)
		Cantidad2 = Entry(miFrame1, textvariable = self.tCantidad2, width=7)#width número de caracteres
		Cantidad2.grid(row=6, column=3, pady=5, padx=5)
		Cantidad3 = Entry(miFrame1, textvariable = self.tCantidad1, width=7)
		Cantidad3.grid(row=7, column=3, pady=5, padx=5)
		#------- Label y entry,s Precio --------------------------------
		lPrecio = Label(miFrame1, text='Precio')
		lPrecio.grid(row=4, column=4,sticky='ew', pady=5, padx=5)
		tPrecio1 = Entry(miFrame1, width=7, state="readonly")
		tPrecio1.grid(row=5, column=4, pady=5, padx=5)
		tPrecio2 = Entry(miFrame1, width=7, state="readonly")#width número de caracteres
		tPrecio2.grid(row=6, column=4, pady=5, padx=5)
		tPrecio3 = Entry(miFrame1, width=7, state="readonly")
		tPrecio3.grid(row=7, column=4, pady=5, padx=5)
		#------- Label y entry,s Subtotal ------------------------------
		lSubtotal = Label(miFrame1, text='Subtotal')
		lSubtotal.grid(row=4, column=5,sticky='ew', pady=5, padx=5)
		tSubtotal1 = Entry(miFrame1, width=7, state="readonly")
		tSubtotal1.grid(row=5, column=5, pady=5, padx=5)
		tSubtotal2 = Entry(miFrame1, width=7, state="readonly")#width número de caracteres
		tSubtotal2.grid(row=6, column=5, pady=5, padx=5)
		tSubtotal3 = Entry(miFrame1, width=7, state="readonly")
		tSubtotal3.grid(row=7, column=5, pady=5, padx=5)
		#------- Label y entry,s Total --------------------------------
		lTotal = Label(miFrame1, text='Total')
		lTotal.grid(row=7, column=6,sticky='ew', pady=5, padx=5)
		tTotal = Entry(miFrame1, width=7, state="readonly")
		tTotal.grid(row=7, column=7, pady=5, padx=5)
		#------ Botón guardar -----------------------------------------
		guardar=Button(miFrame1, text='Guradar', command = self.comprobar)
		guardar.grid(row=8, column=3, pady=5, padx=5)
		 
		root.mainloop()

	def comprobar(self):
		print(type(self.obtenerDni.get()))

		if "" in [self.obtenerDni.get(), self.obtenerTel.get(),self.obtenerApellido.get(), self.obtenerNombre.get()]:
			print("no puedes enviar valores vacions")
			return
		if not(len(self.obtenerDni.get()) == 8 and not(bool(re.search("[a-zA-Z]+",self.obtenerDni.get())))):
			print("dni debe ser igual 8 digitos y no debe contener letras")
			self.obtenerDni.set("")
			return

		if not(len(self.obtenerTel.get()) == 9 and not(bool(re.search("[a-zA-Z]+",self.obtenerTel.get())))):
			print("error en telefono")
			self.obtenerTel.set("")
			return


		if bool(re.search("[0-9]+", self.obtenerApellido.get())) or bool(re.search("[0-9]+", self.obtenerNombre.get())):
			print("Apellido")
			self.obtenerApellido.set("")
			return


		cursor = conexion.cursor()
		consulta = """Insert into usuario(nombre, apellido, dni, telefono, direccion)values(?,?,?,?,?);"""
		cursor.execute(consulta,self.obtenerNombre.get(),self.obtenerApellido.get(),self.obtenerDni.get(),self.obtenerTel.get(),self.obtenerDir.get())
		cursor.commit()
		cursor.close()
		

		cursord = conexion.cursor()
		cursord.execute("select * from usuario;")
		personas = cursord.fetchall()
		for persona in personas:
			print(persona)
		cursord.close()
		conexion.close()
	






		frame1 = createFrame()
		frame2 = createFrame()

		frame1.pack()
		frame2.pack()

		title1 = Label(frame1, text = "Datos del Comprador", bg = "gray")

		displayDni = Label(frame1, text = "Dni:",bg = "gray")
		userDni = Label(frame1, text = self.obtenerDni.get(),bg = "gray")
		# capaturamos los datos del user
		displayName = Label(frame1, text = "Name:",bg = "gray")
		userName = Label(frame1, text = self.obtenerNombre.get(),bg = "gray")

		displayLastname = Label(frame1, text = "Lastname:",bg = "gray")
		userLastname = Label(frame1, text = self.obtenerApellido.get(),bg = "gray")

		displayDireccion = Label(frame1, text = "Direccion:",bg = "gray")
		userDireccion = Label(frame1, text = self.obtenerDir.get(),bg = "gray")

		displayTelefono = Label(frame1, text = "Telefono:",bg = "gray")
		userTelefono = Label(frame1, text = self.obtenerTel.get(),bg = "gray")

		#posicionamos las etiquetas
		title1.grid(column = 0, row = 0, padx = 200)

		displayDni.grid(column = 0,row = 1)
		userDni.grid(column = 1,row = 1)

		displayName.grid(column = 0,row = 2)
		userName.grid(column = 1,row = 2)

		displayLastname.grid(column = 0,row = 3)
		userLastname.grid(column = 1,row = 3)

		displayDireccion.grid(column = 0,row = 4)
		userDireccion.grid(column = 1,row = 4)

		displayTelefono.grid(column = 0,row = 5)
		userTelefono.grid(column = 1,row = 5)
		
		#colocamos los datos del producto
		title2 = Label(frame2, text = "Producto")

		displayCodigo1 = Label(frame2, text ="Codigo: ", bg = "gray")
		displayCodigo2 = Label(frame2, text ="Codigo: ", bg = "gray")
		displayCodigo3 = Label(frame2, text ="Codigo: ", bg = "gray")

		productoCodigo1 = Label(frame2, text = self.tCodigo1.get(), bg = "gray")
		productoCodigo2 = Label(frame2, text = self.tCodigo2.get(), bg = "gray")
		productoCodigo3 = Label(frame2, text = self.tCodigo3.get(), bg = "gray")

		displayCantidad1 = Label(frame2, text ="cantidad: ", bg = "gray")
		displayCantidad2 = Label(frame2, text ="cantidad: ", bg = "gray")
		displayCantidad3 = Label(frame2, text ="cantidad: ", bg = "gray")

		productoCantidad1 = Label(frame2, text = self.tCantidad1.get(), bg = "gray")
		productoCantidad2 = Label(frame2, text = self.tCantidad2.get(), bg = "gray")
		productoCantidad3 = Label(frame2, text = self.tCantidad3.get(), bg = "gray")

		#le ponemos posiciones a las etiquetas
		title2.grid(column = 0, row = 0, padx = 215)

		displayCodigo1.grid(column = 0, row = 1)
		displayCodigo2.grid(column = 0, row = 3)
		displayCodigo3.grid(column = 0, row = 5)

		productoCodigo1.grid(column = 1, row = 1)
		productoCodigo2.grid(column = 1, row = 3)
		productoCodigo3.grid(column = 1, row = 5)

		displayCantidad1.grid(column = 0, row = 2)
		displayCantidad2.grid(column = 0, row = 4)
		displayCantidad3.grid(column = 0, row = 6)

		productoCantidad1.grid(column = 1, row = 2)
		productoCantidad2.grid(column = 1, row = 4)
		productoCantidad3.grid(column = 1, row = 6)

		#root.mainloop()

 
app = Registro_tienda()
app.comprobar()


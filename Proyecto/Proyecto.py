from tkinter import *
from tkinter import ttk
import pymysql.cursors
import os
import tkinter.messagebox as MessageBox

def ventana_inicial():    
    ventana_inicio= Tk()
    ventana_inicio.geometry("550x380+350+170")
    ventana_inicio.title("Asigandor de Horarios")
    ventana_inicio.resizable(False,False)
    ventana_inicio.config(background = "#213141")

    titulo_inicial = Label(ventana_inicio,text = "BIENVENIDOS, SOMOS EL GRUPO 1", font = ("arial black", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_inicial.pack()

    label_inicial = Label(ventana_inicio,text = "Programa de asignacion de horarios para una institución", font = ("Cambria", 12),bg = "#FFEEDD")
    label_inicial.place(x = 85, y = 70)

    boton_login = Button(ventana_inicio,text = "Acceder", command=ventana_login,  width = "30", height = "2", bg = "#00CD63")
    boton_login.place(x = 170, y = 150)

    boton_registro = Button(ventana_inicio,text = "Registrarse", command=ventana_registro, width = "30", height = "2", bg = "#00CD63")
    boton_registro.place(x = 170, y = 220)
    
    ventana_inicio.mainloop()
    
def ventana_login():        
    ventana_login= Tk()
    ventana_login.geometry("510x380+370+170")
    ventana_login.title("Iniciar sesion")
    ventana_login.resizable(False,False)
    ventana_login.config(background = "#213141")
    titulo_login = Label(ventana_login,text = "Inicie sesion | GRUPO 1", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_login.pack()

    label_usuario = Label(ventana_login, text = "Nombre de usuario", bg = "#FFEEDD")
    label_usuario.place(x = 210, y = 70)
    label_contraseña = Label(ventana_login, text = "Contraseña", bg = "#FFEEDD")
    label_contraseña.place(x = 233, y = 130)

    txt_usuario = Entry(ventana_login, width = "40")
    txt_contraseña = Entry(ventana_login, width = "40",  show = "*")

    txt_usuario.place(x = 140, y = 100)
    txt_contraseña.place(x =140, y = 160)

    btn_acceder = Button(ventana_login,text = "Acceder", command=ventana_principal, width = "30", height = "2", bg = "#00CD63")
    btn_acceder.place(x = 155, y = 200)
    
    label_sugerencia = Label(ventana_login, text = "¿No tienes una cuenta? Registrate", bg = "#FFEEDD")
    label_sugerencia.place(x = 175, y = 260)
    
    btn_registrarse = Button(ventana_login,text = "Registrarse", command=ventana_registro, width = "30", height = "2", bg = "#00CD63")
    btn_registrarse.place(x = 155, y = 300)

def ventana_registro():
    ventana_resgitro = Tk()
    ventana_resgitro.geometry("600x620+350+10")
    ventana_resgitro.title("Registrate")
    ventana_resgitro.resizable(False,False)
    ventana_resgitro.config(background = "#213141")
    titulo_registro = Label(ventana_resgitro,text = "Registrate para acceder", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_registro.pack()

    label_Nombre_Usuario = Label(ventana_resgitro,text = "Nombre de Usuario", bg = "#FFEEDD")
    label_Nombre_Usuario.place(x = 22, y = 70)
    label_Contraseña = Label(ventana_resgitro,text = "Contraseña", bg = "#FFEEDD")
    label_Contraseña.place(x = 22, y = 130)
    label_perfil = Label(ventana_resgitro,text = "Perfil", bg = "#FFEEDD")
    label_perfil.place(x = 22, y = 190)
    label_Cedula = Label(ventana_resgitro,text = "Digite Cedula", bg = "#FFEEDD")
    label_Cedula.place(x = 22, y = 250)
    label_Telefono= Label(ventana_resgitro,text = "Telefono", bg = "#FFEEDD")
    label_Telefono.place(x = 22, y = 310)
    label_Correo = Label(ventana_resgitro,text = "Correo", bg = "#FFEEDD")
    label_Correo.place(x = 22, y = 370)
    label_Tipo_Via = Label(ventana_resgitro,text = "Tipo de via", bg = "#FFEEDD")
    label_Tipo_Via.place(x = 22, y = 430)
    label_Numero_letra_Via = Label(ventana_resgitro,text = "Numero letra via", bg = "#FFEEDD")
    label_Numero_letra_Via.place(x = 22, y = 490)
    label_Via_urbana= Label(ventana_resgitro,text = "Via Urbana", bg = "#FFEEDD")
    label_Via_urbana.place(x = 22, y = 550)
    label_Tipo_Via_Generadora = Label(ventana_resgitro,text = "Tipo via Generadora", bg = "#FFEEDD")
    label_Tipo_Via_Generadora.place(x = 280, y = 70)
    label_Sufijo = Label(ventana_resgitro,text = "Sufijo", bg = "#FFEEDD")
    label_Sufijo.place(x = 280, y = 130)
    label_Numero_Placa = Label(ventana_resgitro,text = "Numero de placa", bg = "#FFEEDD")
    label_Numero_Placa.place(x = 280, y = 190)
    label_Adicional = Label(ventana_resgitro,text = "Adicional", bg = "#FFEEDD")
    label_Adicional.place(x = 280, y = 250)

    txt_nombre_usuario = Entry(ventana_resgitro, width = "30")
    txt_nombre_usuario.place(x = 22, y = 100)
    txt_contraseña = Entry(ventana_resgitro, width = "40",  show = "*")
    txt_contraseña.place(x = 22, y = 160)
    txt_perfil = Entry(ventana_resgitro, width = "30")
    txt_perfil.place(x = 22, y = 220)
    txt_cedula = Entry(ventana_resgitro, width = "30")
    txt_cedula.place(x = 22, y = 280)
    txt_telefono = Entry(ventana_resgitro, width = "30")
    txt_telefono.place(x = 22, y = 340)
    txt_correo = Entry(ventana_resgitro, width = "30")
    txt_correo.place(x = 22, y = 400)
    txt_tipo_via = Entry(ventana_resgitro, width = "30")
    txt_tipo_via.place(x = 22, y = 460)
    txt_numero_via_letra = Entry(ventana_resgitro, width = "30")
    txt_numero_via_letra.place(x = 22, y = 520)
    txt_via_urbana = Entry(ventana_resgitro, width = "30")
    txt_via_urbana.place(x = 22, y = 580)
    txt_tipo_via_generadora = Entry( ventana_resgitro,width = "30")
    txt_tipo_via_generadora.place(x = 280, y = 100)
    txt_sufijo = Entry(ventana_resgitro, width = "30")
    txt_sufijo.place(x = 280, y = 160)
    txt_numero_placa = Entry(ventana_resgitro, width = "30")
    txt_numero_placa.place(x = 280, y = 220)
    txt_adicional= Entry(ventana_resgitro, width = "30")
    txt_adicional.place(x = 280, y = 280)

    btn_registro= Button(ventana_resgitro,text = "Registrarse", width = "30", height = "2", bg = "#00CD63")
    btn_registro.place(x = 280, y = 350)

def ventana_principal():
    ventana_principal= Tk()
    ventana_principal.geometry("550x550+350+50")
    ventana_principal.title("Pagina Pricipal")
    ventana_principal.resizable(False,False)
    ventana_principal.config(background = "#213141")
    titulo_principal = Label(ventana_principal,text = "Bienvenidos a nuestro programa", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_principal.pack()

    label_descripcion = Label(ventana_principal,text = "Desde aquí podras insertar, eliminar y actualizar datos de nuestra base de datos,\n dependiendo de su rango", bg = "#FFEEDD")
    label_descripcion.place(x = 70, y = 70)

    btn_1 = Button(ventana_principal,text = "Docentes",command=docentes, width = "20", height = "2", bg = "#00CD63")
    btn_1.place(x = 60, y = 150)

    btn_2 = Button(ventana_principal,text = "Asignatura", command=asignatura, width = "20", height = "2", bg = "#00CD63")
    btn_2.place(x = 60, y = 250)

    btn_3 = Button(ventana_principal,text = "Programa", command=programa, width = "20", height = "2", bg = "#00CD63")
    btn_3.place(x = 60, y = 350)

    btn_4 = Button(ventana_principal,text = "Reporte", command=reporte, width = "20", height = "2", bg = "#00CD63")
    btn_4.place(x = 350, y = 150)

    btn_5 = Button(ventana_principal,text = "Historial",command=historial, width = "20", height = "2", bg = "#00CD63")
    btn_5.place(x = 350, y = 250)

    btn_6 = Button(ventana_principal,text = "Registrar Usuarios", command=ventana_consulta_registro, width = "20", height = "2", bg = "#00CD63")
    btn_6.place(x = 350, y = 350)
    
    btn_6 = Button(ventana_principal,text = "Registrar Tipos de Usuarios", command=tipo_usuario, width = "20", height = "2", bg = "#00CD63")
    btn_6.place(x = 200, y = 450)
    
def docentes():
    ventana_docente = Tk()
    ventana_docente.geometry("1270x680+0+0")
    ventana_docente.title("Formulario De Registro Docente")
    ventana_docente.resizable(False,False)
    ventana_docente.config(background = "#213141")
    titulo_docente = Label(ventana_docente, text = "Formulario De Registro Docente", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_docente.pack()
    
    label_Primer_Nombre= Label(ventana_docente,text = "Primer Nombre", bg = "#FFEEDD")
    label_Primer_Nombre.place(x = 22, y = 70)
    label_segundo_Nombre = Label(ventana_docente,text = "Segundo Nombre", bg = "#FFEEDD")
    label_segundo_Nombre.place(x = 22, y = 130)
    label_Primer_apellido = Label(ventana_docente,text = "Primer Apellido", bg = "#FFEEDD")
    label_Primer_apellido.place(x = 22, y = 190)
    label_segundo_apellido = Label(ventana_docente,text = "Segundo Nombre", bg = "#FFEEDD")
    label_segundo_apellido.place(x = 22, y = 250)
    label_cedula= Label(ventana_docente,text = "Digite Cedula", bg = "#FFEEDD")
    label_cedula.place(x = 22, y = 310)
    label_telefono = Label(ventana_docente,text = "Telefono", bg = "#FFEEDD")
    label_telefono.place(x = 22, y = 370)
    label_correo = Label(ventana_docente,text = "Correo", bg = "#FFEEDD")
    label_correo.place(x = 22, y = 430)
    
    label_tipo_via = Label(ventana_docente,text = "Tipo de via", bg = "#FFEEDD")
    label_tipo_via.place(x = 280, y = 70)
    label_numero_via = Label(ventana_docente,text = "Numero letra via", bg = "#FFEEDD")
    label_numero_via.place(x = 280, y = 130)
    label_via_urbana = Label(ventana_docente,text = "Via Urbana", bg = "#FFEEDD")
    label_via_urbana.place(x = 280, y = 190)
    label_tipo_via_generadora = Label(ventana_docente,text = "Tipo via Generadora", bg = "#FFEEDD")
    label_tipo_via_generadora.place(x = 280, y = 250)
    label_sufijo = Label(ventana_docente,text = "Sufijo", bg = "#FFEEDD")
    label_sufijo.place(x = 280, y = 310)
    label_numero_placa = Label(ventana_docente,text = "Numero de placa", bg = "#FFEEDD")
    label_numero_placa.place(x = 280, y = 370)
    label_adicional= Label(ventana_docente,text = "Adicional", bg = "#FFEEDD")
    label_adicional.place(x = 280, y = 430)
    
    label_postgrado = Label(ventana_docente,text = "Posgrado", bg = "#FFEEDD")
    label_postgrado.place(x = 520, y = 70)
    label_experiencia = Label(ventana_docente,text = "Años de Experiencia", bg = "#FFEEDD")
    label_experiencia.place(x = 520, y = 130)
    label_asignatura = Label(ventana_docente,text = "Id de la Asignatura", bg = "#FFEEDD")
    label_asignatura.place(x = 520, y = 190)
    label_programa= Label(ventana_docente,text = "Id del Programa", bg = "#FFEEDD")
    label_programa.place(x = 520, y = 250)
    label_eps = Label(ventana_docente,text = "Eps", bg = "#FFEEDD")
    label_eps.place(x = 520, y = 310)
    label_edad = Label(ventana_docente,text = "Edad", bg = "#FFEEDD")
    label_edad.place(x = 520, y = 370)
    label_sexo= Label(ventana_docente,text = "Seleccione su sexo", bg = "#FFEEDD")
    label_sexo.place(x = 520, y = 430)
    
    txt_primer_nombre = Entry(ventana_docente, width = "30")
    txt_primer_nombre.place(x = 22, y = 100)
    txt_segundo_nombre = Entry(ventana_docente, width = "30")
    txt_segundo_nombre.place(x = 22, y = 160)
    txt_primer_apellido = Entry(ventana_docente, width = "30")
    txt_primer_apellido.place(x = 22, y = 220)
    txt_segundo_apellido = Entry(ventana_docente, width = "30")
    txt_segundo_apellido.place(x = 22, y = 280)
    txt_cedula = Entry(ventana_docente, width = "30")
    txt_cedula.place(x = 22, y = 340)
    txt_telefono = Entry(ventana_docente, width = "30")
    txt_telefono.place(x = 22, y = 400)
    txt_correo = Entry(ventana_docente, width = "30")
    txt_correo.place(x = 22, y = 460)
    
    txt_tipo_via = Entry(ventana_docente, width = "30")
    txt_tipo_via.place(x = 280, y = 100)
    txt_numero_letra_via = Entry(ventana_docente, width = "30")
    txt_numero_letra_via.place(x = 280, y = 160)
    txt_via_urbana = Entry(ventana_docente, width = "30")
    txt_via_urbana.place(x = 280, y = 220)
    txt_tipo_via_generadora = Entry(ventana_docente, width = "30")
    txt_tipo_via_generadora.place(x = 280, y = 280)
    txt_sufijo = Entry(ventana_docente, width = "30")
    txt_sufijo.place(x = 280, y = 340)
    txt_numero_placa = Entry(ventana_docente, width = "30")
    txt_numero_placa.place(x = 280, y = 400)
    txt_adicional = Entry(ventana_docente, width = "30")
    txt_adicional.place(x = 280, y = 460)
    
    txt_postgrado = Entry(ventana_docente, width = "30")
    txt_postgrado.place(x = 520, y = 100)
    txt_experiencia = Entry(ventana_docente, width = "30")
    txt_experiencia.place(x = 520, y = 160)
    txt_asignatura = Entry(ventana_docente, width = "30")
    txt_asignatura.place(x = 520, y = 220)
    txt_programa = Entry(ventana_docente, width = "30")
    txt_programa.place(x = 520, y = 280)
    txt_eps = Entry(ventana_docente, width = "30")
    txt_eps.place(x = 520, y = 340)
    txt_edad = Entry(ventana_docente, width = "30")
    txt_edad.place(x = 520, y = 400)
    combo=ttk.Combobox(ventana_docente, width = "30")
    combo['values']=('Mascuino', 'Femenino', 'Otro')
    combo.place(x=520, y=460)
    
    label_años_experiencia= Label(ventana_docente,text = "Años de experiencia", bg = "#FFEEDD")
    label_años_experiencia.place(x = 750, y = 70)
    label_lugar_trabajo = Label(ventana_docente,text = "Ultimo lugar de trabaja", bg = "#FFEEDD")
    label_lugar_trabajo.place(x = 750, y = 130)
    label_telefono = Label(ventana_docente,text = "Telefono del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_telefono.place(x = 750, y = 190)
    label_correo = Label(ventana_docente,text = "Correo del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_correo.place(x = 750, y = 250)
    label_cargo = Label(ventana_docente,text = "Cargo", bg = "#FFEEDD")
    label_cargo.place(x = 750, y = 310)
    label_tipo_via = Label(ventana_docente,text = "Tipo de via del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_tipo_via.place(x = 750, y = 370)
    
    label_numero_via = Label(ventana_docente,text = "Numero letra via del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_numero_via.place(x = 1000, y = 70)
    label_via_urbana = Label(ventana_docente,text = "Via Urbana del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_via_urbana.place(x = 1000, y = 130)
    label_tipo_via_generadora = Label(ventana_docente,text = "Tipo via Generadora del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_tipo_via_generadora.place(x = 1000, y = 190)
    label_sufijo = Label(ventana_docente,text = "Sufijo del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_sufijo.place(x = 1000, y = 250)
    label_numero_placa = Label(ventana_docente,text = "Numero de placa del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_numero_placa.place(x = 1000, y = 310)
    label_adicional= Label(ventana_docente,text = "Adicional del ultimo lugar de trabajo", bg = "#FFEEDD")
    label_adicional.place(x = 1000, y = 370)
    
    txt_años_experiencia = Entry(ventana_docente, width = "30")
    txt_años_experiencia.place(x = 750, y = 100)
    txt_lugar_trabajo = Entry(ventana_docente, width = "30")
    txt_lugar_trabajo.place(x = 750, y = 160)
    txt_telefono = Entry(ventana_docente, width = "30")
    txt_telefono.place(x = 750, y = 220)
    txt_correo = Entry(ventana_docente, width = "30")
    txt_correo.place(x = 750, y = 280)
    txt_cargo = Entry(ventana_docente, width = "30")
    txt_cargo.place(x = 750, y = 340)
    txt_tipo_via = Entry(ventana_docente, width = "30")
    txt_tipo_via.place(x = 750, y = 400)
    
    txt_numero_letra_via = Entry(ventana_docente, width = "30")
    txt_numero_letra_via.place(x = 1000, y = 100)
    txt_via_urbana = Entry(ventana_docente, width = "30")
    txt_via_urbana.place(x = 1000, y = 160)
    txt_tipo_via_generadora = Entry(ventana_docente, width = "30")
    txt_tipo_via_generadora.place(x = 1000, y = 220)
    txt_sufijo = Entry(ventana_docente, width = "30")
    txt_sufijo.place(x = 1000, y = 280)
    txt_numero_placa = Entry(ventana_docente, width = "30")
    txt_numero_placa.place(x = 1000, y = 340)
    txt_adicional = Entry(ventana_docente, width = "30")
    txt_adicional.place(x = 1000, y = 400)
    
    btn_registrar= Button(ventana_docente,text = "Registrar", width = "30", height = "2", bg = "#00CD63")
    btn_registrar.place(x = 180, y = 550)
    
    label_consulta=Label(ventana_docente, text="Para consultar solo dijite el nombre de usuario", bg = "#FFEEDD")
    label_consulta.place(x=520, y=510)
    
    btn_consulta= Button(ventana_docente,text = "Consultar", width = "30", height = "2", bg = "#00CD63")
    btn_consulta.place(x = 520, y = 550)
    
    label_eliminar=Label(ventana_docente, text="Para Eliminar solo dijite el nombre de usuario", bg = "#FFEEDD")
    label_eliminar.place(x=900, y=510)
    
    btn_eliminar= Button(ventana_docente,text = "Eliminar", width = "30", height = "2", bg = "#00CD63")
    btn_eliminar.place(x = 900, y = 550)

def asignatura():
    ventana_asignatura= Tk()
    ventana_asignatura.geometry("550x550+350+30")
    ventana_asignatura.title("Asigandor de Horarios")
    ventana_asignatura.resizable(False,False)
    ventana_asignatura.config(background = "#213141")
    titulo_asignatura = Label(ventana_asignatura,text = "BIENVENIDOS, SOMOS EL GRUPO 1", font = ("arial black", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_asignatura.pack()
    
    label_codigo = Label(ventana_asignatura,text = "Codigo", bg = "#FFEEDD")
    label_codigo.place(x = 250, y = 70)
    label_nombre= Label(ventana_asignatura,text = "Nombre", bg = "#FFEEDD")
    label_nombre.place(x = 250, y = 130)
    label_creditos = Label(ventana_asignatura,text = "Creditos", bg = "#FFEEDD")
    label_creditos.place(x = 250, y = 190)
    label_intensidad_horaria = Label(ventana_asignatura,text = "Intensidad Horaria", bg = "#FFEEDD")
    label_intensidad_horaria.place(x = 230, y = 250)
    label_fecha= Label(ventana_asignatura,text = "Fecha", bg = "#FFEEDD")
    label_fecha.place(x = 260, y = 310)
    label_requisitos = Label(ventana_asignatura,text = "Requisitos", bg = "#FFEEDD")
    label_requisitos.place(x = 250, y = 370)
    
    txt_codigo = Entry(ventana_asignatura, width = "30")
    txt_codigo.place(x = 190, y = 100)
    txt_nombre = Entry(ventana_asignatura, width = "30")
    txt_nombre.place(x = 190, y = 160)
    txt_creditos = Entry(ventana_asignatura, width = "30")
    txt_creditos.place(x = 190, y = 220)
    txt_intensidad_horaria = Entry(ventana_asignatura,  width = "30")
    txt_intensidad_horaria.place(x = 190, y = 280)
    txt_fecha = Entry(ventana_asignatura,  width = "30")
    txt_fecha.place(x = 190, y = 340)
    txt_requisitos = Entry(ventana_asignatura, width = "70")
    txt_requisitos.place(x = 70, y = 400)
    
    def send_data():
    
      bd=pymysql.connect(
          host="localhost",
          user="root",
          password="",
          db="grupo_1_proyecto"
      )
      fcursor=bd.cursor()
      sql="INSERT INTO tasignatura (nCodigo, cNombre, cRequisitos, nCreditos, nIntensidadHoraria, dCreacion) VALUES('{0}','{1}','{2}','{3}','{4}','{5}')".format(txt_codigo.get(), txt_nombre.get(), txt_requisitos.get(), txt_creditos.get(), txt_intensidad_horaria.get(), txt_fecha.get())
    
      try:
          fcursor.execute(sql)
          bd.commit()
          MessageBox.showinfo(message="Registro Exitoso",title="Aviso")
      except: 
          bd.rollback
          MessageBox.showinfo(message="Registro Anulado",title="Aviso")
      bd.close()

    
    btn_registrar= Button(ventana_asignatura,text = "Registrar", command=send_data, width = "15", height = "2", bg = "#00CD63")
    btn_registrar.place(x = 40, y = 490)
    
    label_consulta=Label(ventana_asignatura, text="Para consultar solo dijite \n el codigo de la asignatura", bg = "#FFEEDD")
    label_consulta.place(x=210, y=430)

    btn_consulta= Button(ventana_asignatura,text = "Consultar", width = "15", height = "2", bg = "#00CD63")
    btn_consulta.place(x = 220, y = 490)
    
    label_eliminar=Label(ventana_asignatura, text="Para Eliminar solo dijite \n el codigo de la asignatura", bg = "#FFEEDD")
    label_eliminar.place(x=390, y=430)

    btn_eliminar= Button(ventana_asignatura,text = "Eliminar", width = "15", height = "2", bg = "#00CD63")
    btn_eliminar.place(x = 400, y = 490)

def programa():
    ventana_programa= Tk()
    ventana_programa.geometry("550x550+350+30")
    ventana_programa.title("Asigandor de Horarios")
    ventana_programa.resizable(False,False)
    ventana_programa.config(background = "#213141")
    titulo_programa = Label(ventana_programa,text = "Formulario de Programas", font = ("arial black", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_programa.pack()
    
    label_codigo = Label(ventana_programa,text = "Codigo", bg = "#FFEEDD")
    label_codigo.place(x = 250, y = 70)
    label_nombre= Label(ventana_programa,text = "Nombre", bg = "#FFEEDD")
    label_nombre.place(x = 250, y = 130)
    label_asignatura = Label(ventana_programa,text = "Asignatura", bg = "#FFEEDD")
    label_asignatura.place(x = 250, y = 190)
    label_semestres = Label(ventana_programa,text = "Semestre", bg = "#FFEEDD")
    label_semestres.place(x = 230, y = 250)
    
    codigo =StringVar()
    nombre=StringVar()
    asignatura=StringVar()
    semestre=StringVar()
    
    txt_codigo = Entry(ventana_programa, textvariable = codigo, width = "30")
    txt_codigo.place(x = 190, y = 100)
    txt_nombre = Entry(ventana_programa,textvariable = nombre, width = "30")
    txt_nombre.place(x = 190, y = 160)
    txt_asignatura= Entry(ventana_programa,textvariable = asignatura, width = "30")
    txt_asignatura.place(x = 190, y = 220)
    txt_semestres = Entry(ventana_programa,textvariable = semestre, width = "30")
    txt_semestres.place(x = 190, y = 280)
    
    def send_data():
    
      bd=pymysql.connect(
          host="localhost",
          user="root",
          password="",
          db="grupo_1_proyecto"
      )
      fcursor=bd.cursor()
      sql="INSERT INTO tprograma(nCodigoPrograma, cNombrePrograma, nIdAsignatura, nSemestre) VALUES('{0}','{1}','{2}','{3}')".format(codigo.get(), nombre.get(), asignatura.get(), semestre.get())
    
      try:
          fcursor.execute(sql)
          bd.commit()
          MessageBox.showinfo(message="Registro Exitoso",title="Aviso")
      except: 
          bd.rollback
          MessageBox.showinfo(message="Registro Anulado",title="Aviso")
      bd.close()
    
    btn_registrar= Button(ventana_programa,text = "Registrar", command=send_data, width = "15", height = "2", bg = "#00CD63")
    btn_registrar.place(x = 40, y = 450)
    
    label_consulta=Label(ventana_programa, text="Para consultar solo dijite \n el codigo de la asignatura", bg = "#FFEEDD")
    label_consulta.place(x=210, y=400)

    btn_consulta= Button(ventana_programa,text = "Consultar", width = "15", height = "2", bg = "#00CD63")
    btn_consulta.place(x = 220, y = 450)
    
    label_eliminar=Label(ventana_programa, text="Para Eliminar solo dijite \n el codigo de la asignatura", bg = "#FFEEDD")
    label_eliminar.place(x=390, y=400)

    btn_eliminar= Button(ventana_programa,text = "Eliminar", width = "15", height = "2", bg = "#00CD63")
    btn_eliminar.place(x = 400, y = 450)

def reporte():
    ventana_reporte= Tk()
    ventana_reporte.geometry("450x500+420+60")
    ventana_reporte.title("Asigandor de Horarios")
    ventana_reporte.resizable(False,False)
    ventana_reporte.config(background = "#213141")
    titulo_reporte = Label(ventana_reporte,text = "Reportes", font = ("arial black", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_reporte.pack()
    
    label_codigo = Label(ventana_reporte,text = "Codigo", bg = "#FFEEDD")
    label_codigo.place(x = 200, y = 70)
    label_fecha= Label(ventana_reporte,text = "Fecha", bg = "#FFEEDD")
    label_fecha.place(x = 200, y = 130)
    label_asignatura = Label(ventana_reporte,text = " Id de la Aignatura", bg = "#FFEEDD")
    label_asignatura.place(x = 170, y = 190)
    label_docentes = Label(ventana_reporte,text = "Id del Docente", bg = "#FFEEDD")
    label_docentes.place(x = 180, y = 250)
    label_programa = Label(ventana_reporte,text = "Id del Programa", bg = "#FFEEDD")
    label_programa.place(x = 180, y = 310)
    
    txt_codigo = Entry(ventana_reporte, width = "30")
    txt_codigo.place(x = 130, y = 100)
    txt_fecha = Entry(ventana_reporte, width = "30")
    txt_fecha.place(x = 130, y = 160)
    txt_asignatura= Entry(ventana_reporte, width = "30")
    txt_asignatura.place(x = 130, y = 220)
    txt_docentes = Entry(ventana_reporte, width = "30")
    txt_docentes.place(x = 130, y = 280)
    txt_programa = Entry(ventana_reporte, width = "30")
    txt_programa.place(x = 130, y = 340)
    
    label_consulta=Label(ventana_reporte, text="Para consultar solo dijite \n el codigo de la asignatura", bg = "#FFEEDD")
    label_consulta.place(x=150, y=390)

    btn_consulta= Button(ventana_reporte,text = "Consultar", width = "15", height = "2", bg = "#00CD63")
    btn_consulta.place(x = 160, y = 450)

def historial():
    ventana_historial= Tk()
    ventana_historial.geometry("440x450+420+60")
    ventana_historial.title("Asigandor de Horarios")
    ventana_historial.resizable(False,False)
    ventana_historial.config(background = "#213141")
    titulo_historial = Label(ventana_historial,text = "Historial", font = ("arial black", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_historial.pack()
    
    label_codigo = Label(ventana_historial,text = "Codigo", bg = "#FFEEDD")
    label_codigo.place(x = 200, y = 70)
    label_fecha= Label(ventana_historial,text = "Fecha", bg = "#FFEEDD")
    label_fecha.place(x = 205, y = 130)
    label_reporte = Label(ventana_historial,text = " Id del Reporte", bg = "#FFEEDD")
    label_reporte.place(x = 190, y = 190)
    
    txt_codigo = Entry(ventana_historial, width = "30")
    txt_codigo.place(x = 130, y = 100)
    txt_fecha = Entry(ventana_historial, width = "30")
    txt_fecha.place(x = 130, y = 160)
    txt_reporte= Entry(ventana_historial, width = "30")
    txt_reporte.place(x = 130, y = 220)
    
    label_consulta=Label(ventana_historial, text="Para consultar solo dijite \n el codigo de la asignatura", bg = "#FFEEDD")
    label_consulta.place(x=150, y=270)

    btn_consulta= Button(ventana_historial,text = "Consultar", width = "18", height = "2", bg = "#00CD63")
    btn_consulta.place(x = 160, y = 320)
    
def ventana_consulta_registro():
    ventana_resgitro_crud = Tk()
    ventana_resgitro_crud.geometry("600x620+350+10")
    ventana_resgitro_crud.title("Registrate")
    ventana_resgitro_crud.resizable(False,False)
    ventana_resgitro_crud.config(background = "#213141")
    titulo_registro = Label(ventana_resgitro_crud,text = "Registrate para acceder", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_registro.pack()

    label_Nombre_Usuario = Label(ventana_resgitro_crud,text = "Nombre de Usuario", bg = "#FFEEDD")
    label_Nombre_Usuario.place(x = 22, y = 70)
    label_Contraseña = Label(ventana_resgitro_crud,text = "Contraseña", bg = "#FFEEDD")
    label_Contraseña.place(x = 22, y = 130)
    label_perfil = Label(ventana_resgitro_crud,text = "Perfil", bg = "#FFEEDD")
    label_perfil.place(x = 22, y = 190)
    label_Cedula = Label(ventana_resgitro_crud,text = "Cedula", bg = "#FFEEDD")
    label_Cedula.place(x = 22, y = 250)
    label_Telefono= Label(ventana_resgitro_crud,text = "Telefono", bg = "#FFEEDD")
    label_Telefono.place(x = 22, y = 310)
    label_Correo = Label(ventana_resgitro_crud,text = "Correo", bg = "#FFEEDD")
    label_Correo.place(x = 22, y = 370)
    label_Tipo_Via = Label(ventana_resgitro_crud,text = "Tipo de via", bg = "#FFEEDD")
    label_Tipo_Via.place(x = 22, y = 430)
    label_Numero_letra_Via = Label(ventana_resgitro_crud,text = "Numero letra via", bg = "#FFEEDD")
    label_Numero_letra_Via.place(x = 22, y = 490)
    label_Via_urbana= Label(ventana_resgitro_crud,text = "Via Urbana", bg = "#FFEEDD")
    label_Via_urbana.place(x = 22, y = 550)
    label_Tipo_Via_Generadora = Label(ventana_resgitro_crud,text = "Tipo via Generadora", bg = "#FFEEDD")
    label_Tipo_Via_Generadora.place(x = 280, y = 70)
    label_Sufijo = Label(ventana_resgitro_crud,text = "Sufijo", bg = "#FFEEDD")
    label_Sufijo.place(x = 280, y = 130)
    label_Numero_Placa = Label(ventana_resgitro_crud,text = "Numero de placa", bg = "#FFEEDD")
    label_Numero_Placa.place(x = 280, y = 190)
    label_Adicional = Label(ventana_resgitro_crud,text = "Adicional", bg = "#FFEEDD")
    label_Adicional.place(x = 280, y = 250)

    txt_nombre_usuario = Entry(ventana_resgitro_crud, width = "30")
    txt_nombre_usuario.place(x = 22, y = 100)
    txt_contraseña = Entry(ventana_resgitro_crud, width = "40",  show = "*")
    txt_contraseña.place(x = 22, y = 160)
    txt_perfil = Entry(ventana_resgitro_crud, width = "30")
    txt_perfil.place(x = 22, y = 220)
    txt_cedula = Entry(ventana_resgitro_crud, width = "30")
    txt_cedula.place(x = 22, y = 280)
    txt_telefono = Entry(ventana_resgitro_crud, width = "30")
    txt_telefono.place(x = 22, y = 340)
    txt_correo = Entry(ventana_resgitro_crud, width = "30")
    txt_correo.place(x = 22, y = 400)
    txt_tipo_via = Entry(ventana_resgitro_crud, width = "30")
    txt_tipo_via.place(x = 22, y = 460)
    txt_numero_via_letra = Entry(ventana_resgitro_crud, width = "30")
    txt_numero_via_letra.place(x = 22, y = 520)
    txt_via_urbana = Entry(ventana_resgitro_crud, width = "30")
    txt_via_urbana.place(x = 22, y = 580)
    txt_tipo_via_generadora = Entry( ventana_resgitro_crud,width = "30")
    txt_tipo_via_generadora.place(x = 280, y = 100)
    txt_sufijo = Entry(ventana_resgitro_crud, width = "30")
    txt_sufijo.place(x = 280, y = 160)
    txt_numero_placa = Entry(ventana_resgitro_crud, width = "30")
    txt_numero_placa.place(x = 280, y = 220)
    txt_adicional= Entry(ventana_resgitro_crud, width = "30")
    txt_adicional.place(x = 280, y = 280)
    
    btn_registrar= Button(ventana_resgitro_crud,text = "Registrar", width = "30", height = "2", bg = "#00CD63")
    btn_registrar.place(x = 280, y = 330)
    
    label_consulta=Label(ventana_resgitro_crud, text="Para consultar solo dijite el nombre de usuario", bg = "#FFEEDD")
    label_consulta.place(x=280, y=390)

    btn_consulta= Button(ventana_resgitro_crud,text = "Consultar", width = "30", height = "2", bg = "#00CD63")
    btn_consulta.place(x = 280, y = 440)
    
    label_eliminar=Label(ventana_resgitro_crud, text="Para Eliminar solo dijite el nombre de usuario", bg = "#FFEEDD")
    label_eliminar.place(x=280, y=500)

    btn_eliminar= Button(ventana_resgitro_crud,text = "Eliminar", width = "30", height = "2", bg = "#00CD63")
    btn_eliminar.place(x = 280, y = 550)
    
def tipo_usuario():
    ventana_tipo_usuario= Tk()
    ventana_tipo_usuario.geometry("550x550+350+30")
    ventana_tipo_usuario.title("Asigandor de Horarios")
    ventana_tipo_usuario.resizable(False,False)
    ventana_tipo_usuario.config(background = "#213141")
    titulo_tipo_usuario = Label(ventana_tipo_usuario,text = "Formulario de Programas", font = ("arial black", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
    titulo_tipo_usuario.pack()
    
    label_tipo_usuario = Label(ventana_tipo_usuario,text = "Nombre del tipo de usuario", bg = "#FFEEDD")
    label_tipo_usuario.place(x = 210, y = 70)
    label_descripcion = Label(ventana_tipo_usuario,text = "Descripcion", bg = "#FFEEDD")
    label_descripcion.place(x = 240, y = 130)
    
    tipo_usuario=StringVar()
    descripcion=StringVar()
    
    txt_tipo_usuario = Entry(ventana_tipo_usuario,  width = "30")
    txt_tipo_usuario.place(x = 190, y = 100)
    txt_descripcion = Entry(ventana_tipo_usuario, width = "70")
    txt_descripcion.place(x = 70, y = 160)
    
    def send_data():

      bd=pymysql.connect(
          host="localhost",
          user="root",
          password="",
          db="grupo_1_proyecto"
      )
      fcursor=bd.cursor()
      sql="INSERT INTO t_tipousuario (cTipoUsuario,	cDescripcion) VALUES('{0}','{1}')".format(txt_tipo_usuario.get(), txt_descripcion.get())
    
      try:
          fcursor.execute(sql)
          bd.commit()
          MessageBox.showinfo(message="Registro Exitoso",title="Aviso")
      except: 
          bd.rollback
          MessageBox.showinfo(message="Registro Anulado",title="Aviso")
      bd.close()
    
    btn_registrar = Button(ventana_tipo_usuario,text = "Registrarse", command=send_data, width = "25", height = "2",  bg = "#00CD63")
    btn_registrar.place(x = 190, y = 210)
    
    label_consulta=Label(ventana_tipo_usuario, text="Para consultar solo dijite el nombre de usuario", bg = "#FFEEDD")
    label_consulta.place(x=170, y=260)

    btn_consulta= Button(ventana_tipo_usuario,text = "Consultar", width = "25", height = "2", bg = "#00CD63")
    btn_consulta.place(x = 190, y = 310)
    
    label_eliminar=Label(ventana_tipo_usuario, text="Para Eliminar solo dijite el nombre de usuario", bg = "#FFEEDD")
    label_eliminar.place(x=170, y=380)

    btn_eliminar= Button(ventana_tipo_usuario,text = "Eliminar", width = "25", height = "2", bg = "#00CD63")
    btn_eliminar.place(x = 190, y = 430)

ventana_inicial()
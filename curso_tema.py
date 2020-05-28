class Curso_Tema():
    def __init__(self,idcurso_tema,idcurso,idtema):
        self.__idcurso_tema = idcurso_tema
        self.__idcurso = idcurso
        self.__idtema = idtema
    @property
    def idcurso_tema(self):
        return self.__idcurso_tema
    @property 
    def idcurso(self):
        return self.__idcurso
    @property 
    def idtema(self):
        return self.__idtema
    @idcurso_tema.setter
    def idcurso_tema(self):
        self.__idcurso_tema = valor
    @idcurso.setter
    def idcurso(self):
        self.__idcurso = valor
    @idtema.setter
    def idtema(self):
        self.__idtema = valor

    def Agregar(self):
        archivo = open("./archivos/curso_tema.txt","a",encoding='utf8')
        archivo.write( str(self.__idcurso_tema) + '|' + str(self.__idcurso) + '|' + str(self.__idtema))
        archivo.write("\n")    
        archivo.close() 
    def Eliminar(self):
        archivo = open("./archivos/curso_tema.txt","r",encoding ='utf8')

        lista = []
        for x in archivo:
            datos = x.split("\n")
            if datos[0] != (self.__idcurso_tema + "|" + self.__idcurso + "|" + self.__idtema):
                lista.append(datos[0])
                archivo2 = open("./archivos/curso_tema.txt","w",encoding = "utf8")
                for i in lista:
                    archivo2.write(i + "\n")
                    archivo2.close()
        archivo.close()
    def Modificar(self):
         f = open("./archivos/curso_tema.txt")
         
         cam = []
         for line in f:
             linea = line.split("|")
             self.__idcurso_tema = linea[0]
             self.__idcurso = linea[1]
             self.__idtema = linea[2]
             if self.__idcurso_tema != self.__idcurso_tema:
                 cam += line
         f.close()
         for renglon in cam:
            datos = renglon.split("|")
            if datos[0] == (self.__idcurso_tema,):
                self.__idcurso_tema = int(input("ingrese el idcurso_tema modificado"))
                self.__idcurso = input("ingrese el idcurso  modificado")
                self.__idtema = int(input("ingrese el idtema modificado"))
                datosNuevos = datos[1].replace(datos[1], self.__descripcion + "|" + self.__idempleado + "\n")
                datosCambiados = (datos[0] + "|" + datosNuevos)
                cam.append(datosCambiados)
         f =open("./archivos/curso_tema.txt","w")  
         f.write(cam)
         cam.remove()  
         f.close()
class Curso():
    def __init__(self,idcurso,descripcion,idempleado):
        self.__idcurso = idcurso
        self.__descripcion = descripcion
        self.__idempleado = idempleado
    @property 
    def idcurso(self):
        return self.__idcurso
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def idempleado(self):
        return self.__idempleado  
    @idcurso.setter
    def idcurso(self):
        self.__idcurso = valor
    @descripcion.setter 
    def descripcion(self):
        self.__descripcion = valor
    @idempleado.setter   
    def idempleado(self):
        self.__idempleado = valor

    def Agregar(self):
        archivo = open("./archivos/curso.txt","a",encoding='utf8')
        archivo.write( str(self.__idcurso) + '|' + self.__descripcion + '|' + str(self.__idempleado))
        archivo.write("\n")    
        archivo.close()
    def Eliminar(self):
        archivo = open("./archivos/curso.txt","r",encoding ='utf8')

        lista = []
        for x in archivo:
            datos = x.split("\n")
            if datos[0] != (self.__idcurso + "|" + self.__descripcion + "|" + self.__idempleado):
                lista.append(datos[0])
                archivo2 = open("./archivos/curso.txt","w",encoding = "utf8")
                for i in lista:
                    archivo2.write(i + "\n")
                    archivo2.close()
        archivo.close()

      
    def Modificar(self):
         f = open("./archivos/curso.txt")
         
         cam = []
         for line in f:
             linea = line.split("|")
             self.__idcurso = linea[0]
             self.__descripcion = linea[1]
             self.__idempleado = linea[2]
             if self.__idcurso != self.__idcurso:
                 cam += line
         f.close()
         for renglon in cam:
            datos = renglon.split("|")
            if datos[0] == (self.__idcurso,):
                self.__idcurso = int(input("ingrese el idcurso modificado"))
                self.__descripcion = input("ingrese la descripcion  modicado")
                self.__idempleado = int(input("ingrese el idempleado modificado"))
                datosNuevos = datos[1].replace(datos[1], self.__descripcion + "|" + self.__idempleado + "\n")
                datosCambiados = (datos[0] + "|" + datosNuevos)
                cam.append(datosCambiados)
         f =open("./archivos/curso.txt","w")  
         f.write(cam)  
         f.close()
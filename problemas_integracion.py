#Problema 6

class persona:
    def __init__(self,nombre="",edad=0,dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        
    @property
    def nombre(self):
        return self.__nombre
    
    def nombre(self,nombre):
        if isinstance(nombre,str):       
            self.__nombre = nombre
        else:
            raise ValueError("El nombre debe ser un string")
        
    @property
    def edad(self):
        return self.__edad
    
    def edad(self,edad):
        if isinstance(edad,int) and edad > 0:
            self.__edad = edad
        else:
            raise ValueError("la edad debe ser un entero positivo")
        
    @property
    def dni(self):
        return self.__dni
    
    def dni(self,dni):
        if isinstance(dni,str) and len(dni) == 9:
            self.__dni = dni
        else:
            raise ValueError("El DNI debe ser un string de 9 caracteres")
        
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")
        
    def es_mayor_de_edad(self):
        return self.edad >= 18  

#Problema 7

class cuenta:
    def __init__(self,titular,cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
        
    @property
    def titular(self):
        return self.__titular

    def titular(self,titular):
        self.__titular = titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        
    def retirar(self,cantidad):
        if cantidad >0:
            self.__cantidad -= cantidad
        
    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")     
    
cuenta1 = cuenta("Marcelo Gon", 20000)
cuenta1.mostrar()


cuenta1.ingresar(5000)
cuenta1.mostrar()

cuenta1.retirar(50000)
cuenta1.mostrar()

cuenta1.titular("Pepe")
cuenta1.mostrar()

cuenta2 = cuenta("Pepita")
cuenta2.mostrar()

#Problema 8

class cuenta_joven(cuenta):
    def __init__(self, titular, cantidad=0,bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        
        
    def bonificacion(self):
        return self.bonificacion
    
    def bonificacion(self,bonificacion):
        self.bonificacion = bonificacion   
        
    def es_titular_valido(self):
        edad = self.titular.edad()
        return edad >= 18 and edad <25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
            
    def mostrar(self):
        print("Cuenta Joven")
        print(f"Bonificación: {self.bonificacion}")
        
persona1 = persona("pepa",20,3672)
cuenta3 = cuenta_joven(persona1,1000,5)
persona1.mostrar()
cuenta3.mostrar()
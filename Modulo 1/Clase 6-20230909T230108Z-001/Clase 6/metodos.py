class Metodos:
    def __init__(self) -> None:
        pass
    
    def primo( self, prim):
        inicio = 1
        total=0 
        while (inicio < prim +1):
            if((prim % inicio) == 0):
                total = total +1
            inicio = inicio+1
        if(total == 2):
            return True 
        else:
    
            return False 
    
    def conversor_de_grados(self, valor, medida_origen, medida_destino):
        if(medida_origen == medida_destino):
            return valor
        elif(medida_origen == "celsius"  and  medida_destino == "farenheit" ):
            return (valor * 9/5) + 32
        elif (medida_origen == "celsius" and medida_destino == "kelvin"):
            return valor + 273.15
        elif (medida_destino == "farenheit" and medida_destino == "celsius"):
            result = (valor - 32) * 5/9
            return round(result, 2)
        elif (medida_origen == "farenheit" and medida_destino == "kelvin"):
            result = ((valor - 32) * 5/9 )+ 273.15
            return round(result, 2)
        elif(medida_origen == "kelvin" and medida_destino == "celsius"):
            result = valor - 273.15
            return round(result, 2)
        elif (medida_origen == "kelvin" and medida_destino == "farenheit"):
            result = (valor - 273.15) * 9/5 +32
            return round(result, 2)   
     
    
    def factorial(self, numero):
        if(type(numero) ==  float or numero < 0):
            print("El numero tiene que ser entero y mayor a 0")
        elif (numero <= 1):
            return 1
        else:
            result = numero * self.factorial(numero - 1)
        return result
    
    def valor_modal(self, lista):
        lista_unicos = []
        lista_repeticiones = []
        if len(lista) == 0:
            return None
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
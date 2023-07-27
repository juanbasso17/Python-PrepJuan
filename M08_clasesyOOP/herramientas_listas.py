class Herramientas_listas:
    def __init__(self, lista_numeros):          #ahora en el metodo constructor ya hay incluida una lista como argumento.
        self.lista= lista_numeros

    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print(f'El número {i} es primo')
            else:
                print(f'El número {i} no es primo')

    def __verifica_primo(self,nro):
        if nro <= 1:
            return False
        for i in range(2,nro):
            if nro % i == 0:
                return False
        return True

    def valor_modal(self,menor):    #hay que hacer varios cambios para adaptar Herramientas para que funcione con listas como argumento.
        unicos= []
        repetidos= []
        if len(self.lista) == 0:
            return None
        if menor:
            self.lista.sort()           # 'self.lista' ahora reemplaza todos los lugares en la funcion donde estaba 'lista'
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in unicos:
                i= unicos.index(elemento)
                repetidos[i] += 1
            else:
                unicos.append(elemento)
                repetidos.append(1)
        moda= unicos[0]
        maximo= repetidos[0]
        for i, elemento in enumerate(unicos):
            if repetidos[i]>maximo:
                moda= unicos[i]
                maximo= repetidos[i]
        return moda, maximo
    
    def conversor_temperatura(self,origen,destino):
        for i in self.lista:
            print(f'{i} grados {origen} equivalen a {self.__conversor_temperatura(i,origen,destino)} grados {destino}')

    def __conversor_temperatura(self,valor,origen,destino):
        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor
            elif destino == 'farenheit':
                valor_destino = (valor * (9/5) + 32)
            elif destino == 'kelvin':
                valor_destino = valor + 273.15
            else:
                print('Parámetro incorrecto')
        elif origen == 'farenheit':
            if destino == 'farenheit':
                valor_destino = valor
            elif destino == 'celsius':
                valor_destino = ((valor - 32) * 5) / 9
            elif destino == 'kelvin':
                valor_destino = (((valor - 32) * 5) / 9) + 273.15
            else:
                print('Parámetro incorrecto')
        elif origen == 'kelvin':
            if destino == 'kelvin':
                valor_destino= valor
            elif destino == 'celsius':
                valor_destino= valor - 273.15
            elif destino == 'farenheit':
                valor_destino= (valor - 273.15) * 9/5 + 32
            else:
                print('Parámetro incorrecto')
        else:
            print('Parámetro de origen incorrecto')
        return valor_destino

    def factorial(self):
        for i in self.lista:
            print(f'El factorial de {i} es {self.__factorial(i)}')

    def __factorial(self,numero):
        if type(numero) != int:
            return 'Debe ser un número entero'
        if numero < 0:
            return 'Debe ser un número positivo'
        if numero <= 1:
            return 1
        numero= numero * self.__factorial(numero - 1)
        return numero
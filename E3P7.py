class Jugador:
    def __init__(self, cedula, nombre, edad, experiencia, posicion): # constructor de la clase Jugador
        self.__cedula = cedula
        self.__nombre = nombre
        self.__edad = edad
        self.__experiencia = experiencia
        self.__posicion = posicion

    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter 
    def cedula(self, value):
        self.__cedula = value

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property
    def experiencia(self):
        return self.__experiencia
    @experiencia.setter
    def experiencia(self, value):
        self.__experiencia = value
    
    @property
    def posicion(self):
        return self.__posicion
    @posicion.setter
    def posicion(self, value):
        self.__posicion = value

    def data(self):
        return [self.__cedula, self.__nombre, self.__edad, self.__experiencia, self.__posicion]

    def __str__(self):
        return f'cedula {self.__cedula} | nombre {self.__nombre} | edad {self.__edad} | experiencia {self.__experiencia} | posicion {self.__posicion}'

class Equipo:
    def __init__(self, nombre): # constructor de a clase Equipo
        self.__nombre = nombre
        self.__titulares = list()
        self.__suplentes = list()

    @property
    def nombre(self):
        return self.__nombre
    @property
    def titulares(self):
        return self.__titulares
    @property
    def suplentes(self):
        return self.__suplentes

    def agregar_titular(self, jugador): # agrega titular a la lista y controla el maximo de 5 player
        if len(self.__titulares) < 5:
            self.__titulares.append(jugador)
        else:
            print('Equipo titulares completo')

    def agregar_suplentes(self, jugador): # agrega suplentes a la lista y controla el maximo de 45
        if len(self.__suplentes) < 45:
            self.__suplentes.append(jugador)
        else:
            print('Lista de sumplentes completa')  

    def cambiar_suplente_como_titular(self, cedula):
        jugador = []
        indice_suplente = 0
        retorno = False
        for sup in self.__suplentes:
            if sup[0] == cedula:
                indice_suplente = self.__suplentes.index(sup)
                jugador = sup.copy()
        if len(jugador) != 0:
            controlCantTitulares = 0
            for titul in self.__titulares:
                indice = self.__titulares.index(titul)
                if titul[4] == jugador[4]:
                    self.__suplentes.pop(indice_suplente)
                    self.agregar_suplentes(titul)
                    self.__titulares[indice] = jugador
                    retorno = True
                    break
                controlCantTitulares += 1
            if controlCantTitulares == 4 and len(self.__titulares) < 5:
                self.__titulares.append(jugador)
                retorno = True
        else:
            print(f'El jugador con cedula {cedula} no esta en lista de suplentes')       
        return retorno

    def __str__(self) -> str:
        titulares_str = ''
        suplentes_str = ''
        for eq in self.__titulares:
            titulares_str += eq.__str__() + '\n' + '                '
        for sup in self.__suplentes:
            suplentes_str += sup.__str__() + '\n' + '                '
        return f'Equipo = {self.__nombre} \n --> Titulares: {titulares_str} \n --> Suplentes: {suplentes_str}' 

if __name__ == "__main__":
    jugador1 = Jugador(12345678, 'Pedro', 30, 5, 'Pivot')
    jugador2 = Jugador(22344568, 'ONil', 45, 10, 'Base')
    jugador3 = Jugador(32345678, 'Michel', 23, 3, 'Alero')
    jugador4 = Jugador(4234568, 'Pitingo', 15, 1, 'Ala-Pivot')
    jugador5 = Jugador(52345678, 'Bryan', 45, 20, 'Escolta')
    jugador6 = Jugador(62345678, 'Mahtias', 31, 5, 'Pivot')
    jugador7 = Jugador(72345678, 'Seba', 35, 8, 'Base')
    jugador8 = Jugador(82345678, 'Juan', 28, 11, 'Alero')
    jugador9 = Jugador(92345678, 'Fernando', 30, 15, 'Ala-Pivot')
    jugador10 = Jugador(12345671, 'Curry', 26, 7, 'Escolta')
    jugador11 = Jugador(12345672, 'Fransisco', 28, 5, 'Alero')
    jugador12 = Jugador(12345673, 'Pisiquelo', 35, 5, 'Ala-Pivot')
    jugador13 = Jugador(12345674, 'CurryJr', 14, 1, 'Escolta')
    titulares1 = [jugador1.data(),jugador2.data(),jugador3.data(),jugador4.data(),jugador5.data()]
    suplentes1 = [jugador6.data(),jugador7.data(),jugador8.data(),jugador9.data(),jugador10.data(),jugador11.data(),jugador12.data(),jugador13.data()]
    eq1 = Equipo('UM')
    for j in titulares1:
        eq1.agregar_titular(j)
    for j in suplentes1:
        eq1.agregar_suplentes(j)
    print(eq1)
    print('-'*30)
    print("   //   CAMBIO   //   entra 12345674")
    resultado = eq1.cambiar_suplente_como_titular(12345674)
    print(f'    Cambio fue autorizado?   {resultado}')
    print('-'*30)
    print(eq1)
# Model of the Xazam app
import requests

class Model:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        # self.lista_notas = ["C",
        #     "C♯/D♭",
        #     "D",
        #     "D♯/E♭",
        #     "E",
        #     "F",
        #     "F♯/G♭",
        #     "G",
        #     "G♯/A♭",
        #     "A",
        #     "A♯/B♭",
        #     "B"]
        self.lista_notas = ["do",
            "do♯/re♭",
            "re",
            "re♯/mi♭",
            "mi",
            "fa",
            "fa♯/sol♭",
            "sol",
            "sol♯/la♭",
            "la",
            "la♯/si♭",
            "si"]
        self.distancias = dict(zip(
            ["Segunda menor (2m)",
            "Segunda mayor (2M)",
            "Tercera menor (3m)",
            "Tercera mayor (3M)",
            "Cuarta justa (4j)",
            "Cuarta aumentada (4aum)",
            "Quinta justa (5j)",
            "Sexta menor (6m)",
            "Sexta mayor (6M)",
            "Séptima menor (7m)",
            "Séptima mayor (7M)",
            "Octava (8a)"],
            list(range(1,13))))
    
    def get_example(interval_size):
        # interval_size es un entero positivo para intervalos ascendentes
        # y un entero negativo para intervalos descententes
        from random import randint
        i = randint(0,11)
        nota_1 = self.lista_notas[i]
        nota_2 = self.lista_notas[(i+interval_size)%12]
        return f"{nota_1} - {nota_2}"
    
    # Este método recibe el nombre de un intervalo (notación corta), y un string "asc" o "des"
    # indicando si es ascendente o descendente
    def get_songs(interval, asc_des):
        URL = f"http://{self.server_address}:{server_port}/songs/{interval}/{asc_des}"
        try:
            req = requests.get(URL)
            if req.status_code != 200:
                raise RuntimeError()
            responsedata = req.json().get('data')
            if responsedata is None:
                raise ValueError()
            songs_list = list()
            # Converts the list of lists to a list of tuples because that's what the view was designed for
            # Plus, tuples are inmutable and we shouldn't want to change a song's information
            for songdata in responsedata:
                songs_list.append(tuple(songdata))
            return songs_list
        except Exception:
            raise RuntimeError("I/O ERROR: Unexpected response or no response from backend server")

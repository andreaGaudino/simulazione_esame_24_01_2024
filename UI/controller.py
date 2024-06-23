import warnings

import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.metodo = None
        self.anno = None
        self.S = None


    def fillDD(self):
        #fill ddAnno
        anni = DAO.getAnni()
        anniDD = list(map(lambda x: ft.dropdown.Option(x), anni))
        self._view.ddAnno.options = anniDD

        #fill ddMetodo
        metodi = DAO.getMetodi()
        metodiDD = list(map(lambda x: ft.dropdown.Option(text=x[1], key=x[0]), metodi))
        self._view.ddMetodo.options = metodiDD
        self._view.update_page()

    def handle_creaGrafo(self, e):
        self.anno = self._view.ddAnno.value
        if self.anno is None:
            self._view.create_alert("Anno non inserito")
            self._view.txtResult.clean()
            self._view.update_page()
            return
        self.metodo = self._view.ddMetodo.value
        if self.metodo is None:
            self._view.create_alert("Metodo non inserito")
            self._view.txtResult.clean()
            self._view.update_page()
            return
        self.S = self._view.valoreS.value
        if self.S == "":
            self._view.create_alert("Valore numerico non inserito")
            self._view.txtResult.clean()
            self._view.update_page()
            return
        try:
            self.sFloat = float(self.S)
        except ValueError:
            self._view.create_alert("Valore inserito non numerico")
            self._view.txtResult.clean()
            self._view.update_page()
            return

        self._model.buildGraph(self.anno, self.metodo, self.sFloat)
        n, e = self._model.graphDetails()
        self._view.txtResult.clean()
        self._view.txtResult.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self._view.btnCalcolaRedditizzi.disabled = False
        self._view.btnCalcolaPercorso.disabled = False
        self._view.update_page()
    def handleCalcolaRedditizzi(self, e):
        result = self._model.calcolaRedditizzi()
        self._view.txtResult.controls.append(ft.Text(f"\n\n\nI prodotti più redditizzi sono:"))
        for i in result:
            self._view.txtResult.controls.append(ft.Text(f"Prodotto {i.prodotto} ricavo={i.somma}"))
        self._view.update_page()

    def handlePercorso(self, e):
        soluzione = self._model.calcolaPercorso()
        self._view.txtResult.controls.append(ft.Text(f"\n\nPercorso più lungo di lunghezza {len(soluzione)-1}"))
        for i in soluzione:
            self._view.txtResult.controls.append(ft.Text(f"{i.prodotto} --> profitto {i.somma}"))

        self._view.update_page()







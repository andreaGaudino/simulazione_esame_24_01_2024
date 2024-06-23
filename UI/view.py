import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None



    def load_interface(self):
        # title
        self._title = ft.Text("simulazione esame 24/01/2024", color="blue", size=24)
        self._page.controls.append(self._title)

        #row1
        self.ddMetodo = ft.Dropdown(label="Metodo vendita")
        self.ddAnno = ft.Dropdown(label="Anno")
        self.valoreS = ft.TextField(label="Scegli valore numerico")

        row1 = ft.Row([ft.Container(self.ddAnno, width=200),
                       ft.Container(self.ddMetodo, width=200),
                       ft.Container(self.valoreS, width=200)], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self._controller.fillDD()

        #row2
        self.btnGraph = ft.ElevatedButton(text="Crea grafo", on_click=self._controller.handle_creaGrafo)
        self.btnCalcolaRedditizzi = ft.ElevatedButton(text="Calcola redditizzi", on_click=self._controller.handleCalcolaRedditizzi, disabled=True)
        self.btnCalcolaPercorso = ft.ElevatedButton(text="Calcola percorso", on_click=self._controller.handlePercorso, disabled=True)
        row2 = ft.Row([ft.Container(self.btnGraph, width=200),
                       ft.Container(self.btnCalcolaRedditizzi, width=200),
                       ft.Container(self.btnCalcolaPercorso, width=200)], alignment=ft.MainAxisAlignment.CENTER
                      )
        self._page.controls.append(row2)


        self.txtResult = ft.ListView()
        row3 = ft.Row([self.txtResult])
        self._page.controls.append(row3)


        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

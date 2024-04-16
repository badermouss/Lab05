import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._ddCorsi = None
        self._btnCerca = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)

        # row 1
        self._ddCorsi = ft.Dropdown(label="corso",
                                    hint_text="Selezionare un corso",
                                    width=500,
                                    options=[])
        listaCorsi = self._controller.popolaDD()
        for element in listaCorsi:
            self._ddCorsi.options.append(ft.dropdown.Option(key=element.codCorso, text=element.__str__()))
        self.update_page()

        self._btnCerca = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handleRicerca)

        row1 = ft.Row([self._ddCorsi, self._btnCerca],
                      alignment=ft.MainAxisAlignment.CENTER)

        # row 2
        self._txtMatr = ft.TextField(hint_text="matricola")
        self._txtNome = ft.TextField(read_only=True, hint_text="nome")
        self._txtCognome = ft.TextField(read_only=True, hint_text="cognome")

        row2 = ft.Row([self._txtMatr, self._txtNome, self._txtCognome], alignment=ft.MainAxisAlignment.CENTER)

        # row 3
        self._btnCercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                   on_click=self._controller.handleRicercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handleRicercaCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleIscrivi)

        row3 = ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20)

        self._page.add(self._title, row1, row2, row3, self.txt_result)
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
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

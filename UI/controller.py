import flet as ft
from model.model import Model
from database.corso_DAO import CorsiDao


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.corsi = []
        self.studenti = []

    def handleRicerca(self, e):
        corsoScelto = self._view._ddCorsi.value
        if corsoScelto is None:
            self._view.create_alert("Selezionare un corso!")
        else:
            self._view.txt_result.controls.clear()
            listaStudenti = self._model.get_studenti_del_corsoM(corsoScelto)
            self._view.txt_result.controls.append(ft.Text(
                f"Numero di studenti iscritti al corso: {len(listaStudenti)}")
            )
            for studente in listaStudenti:
                self._view.txt_result.controls.append(ft.Text(studente.__str__()))

            self._view.update_page()

    def handleRicercaStudente(self, e):
        self.aggiungiStudenti()
        for studente in self.studenti:
            if studente.matricola == int(self._view._txtMatr.value):
                self._view._txtNome.value = studente.nome
                self._view._txtCognome.value = studente.cognome
                self._view.update_page()
                return
            elif self._view._txtMatr is None:
                self._view.create_alert("Scrivere una matricola!")
                return
        self._view.create_alert("Nessuno studente trovato con questa matricola")

    def handleRicercaCorsi(self, e):
        self.aggiungiStudenti()
        self._view.txt_result.controls.clear()
        studenteScelto = int(self._view._txtMatr.value)
        esiste = False
        for studente in self.studenti:
            if studente.matricola == studenteScelto:
                esiste = True
                break
            elif self._view._txtMatr is None:
                self._view.create_alert("Scrivere una matricola!")
                return
        if not esiste:
            self._view.create_alert("Nessuno studente trovato con questa matricola")
            return

        listaCorsi = self._model.get_corsi_studenteM(studenteScelto)
        self._view.txt_result.controls.append(ft.Text(
            f"Risultano {len(listaCorsi)} corsi")
        )
        for corso in listaCorsi:
            self._view.txt_result.controls.append(ft.Text(corso.__str__()))

        self._view.update_page()

    def handleIscrivi(self, e):
        self.aggiungiStudenti()
        self._view.txt_result.controls.clear()
        studenteScelto = int(self._view._txtMatr.value)
        esisteStudente = False
        for studente in self.studenti:
            if studente.matricola == studenteScelto:
                esisteStudente = True
                break
            elif self._view._txtMatr is None:
                self._view.create_alert("Scrivere una matricola!")
                return
        if not esisteStudente:
            self._view.create_alert("Nessuno studente trovato con questa matricola")
            return

        corsoScelto = self._view._ddCorsi.value
        if corsoScelto is None:
            self._view.create_alert("Selezionare un corso!")

        listaCorsi = self._model.get_corsi_studenteM(studenteScelto)
        for corso in listaCorsi:
            if corso.codCorso == corsoScelto:
                self._view.create_alert("Lo studente è già iscritto a questo corso!")
                return

        CorsiDao.iscrivi_studente(studenteScelto, corsoScelto)
        self._view.txt_result.controls.append(ft.Text("Studente iscritto correttamente", color="green"))
        self._view.update_page()



    def popolaDD(self):
        for corso in self._model.get_corsiM():
            self.corsi.append(corso)

        return self.corsi

    def aggiungiStudenti(self):
        for studente in self._model.get_studentiM():
            self.studenti.append(studente)

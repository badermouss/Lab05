from database.corso_DAO import CorsiDao
from database.studente_DAO import StudentiDao


class Model:
    def __init__(self):
        self.corsi = []
        self.studenti = []

    def get_corsiM(self):
        c = CorsiDao()
        for corso in c.get_corsi():
            self.corsi.append(corso)
        return self.corsi

    def get_studentiM(self):
        s = StudentiDao()
        for studente in s.get_studenti():
            self.studenti.append(studente)
        return self.studenti

    def get_studenti_del_corsoM(self, codCorso):
        s = StudentiDao()
        result = []
        for studente in s.get_studenti_del_corso(codCorso):
            result.append(studente)
        return result

    def get_corsi_studenteM(self, matricola):
        c = CorsiDao()
        result = []
        for corso in c.get_corsi_studente(matricola):
            result.append(corso)
        return result



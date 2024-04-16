# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model import studente


class StudentiDao:
    def __init__(self):
        self.result = []

    def get_studenti(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                    FROM studente"""

        cursor.execute(query)
        for row in cursor.fetchall():
            sTemp = studente.Studente(row["matricola"],
                                      row["cognome"],
                                      row["nome"],
                                      row["CDS"])
            self.result.append(sTemp)
        cursor.close()
        cnx.close()
        return self.result

    @staticmethod
    def get_studenti_del_corso(codCorso):
        cnx = get_connection()
        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """select s.*
                from iscrizione i, studente s
                where i.codins = %s and s.matricola = i.matricola """
        cursor.execute(query, (codCorso,))
        for row in cursor:
            sTemp = studente.Studente(row["matricola"],
                                      row["cognome"],
                                      row["nome"],
                                      row["CDS"])
            result.append(sTemp)
        cursor.close()
        cnx.close()
        return result




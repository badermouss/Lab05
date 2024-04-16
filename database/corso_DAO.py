# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model import corso


class CorsiDao:
    def __init__(self):
        self.result = []

    def get_corsi(self):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                    FROM corso"""

        cursor.execute(query)
        for row in cursor.fetchall():
            self.result.append(corso.Corso(row["codins"],
                                           row["crediti"],
                                           row["nome"],
                                           row["pd"])
                               )

        cursor.close()
        cnx.close()
        return self.result

    def get_corsi_studente(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """
                SELECT c.*
                FROM iscrizione i, corso c
                WHERE i.matricola = %s and i.codins = c.codins"""
        cursor.execute(query, (matricola, ))
        result = []
        for row in cursor:
            cTemp = corso.Corso(row["codins"],
                                row["crediti"],
                                row["nome"],
                                row["pd"])
            result.append(cTemp)
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def iscrivi_studente(matricola, codCorso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """
                INSERT INTO iscrizione
                (matricola, codins)
                VALUES (%s, %s)"""

        cursor.execute(query, (matricola, codCorso))
        cnx.commit()
        cursor.close()
        cnx.close()
        return









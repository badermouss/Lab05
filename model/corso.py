from dataclasses import dataclass



@dataclass
class Corso:
    codCorso: str
    crediti: int
    nomeCorso: str
    periodoDidattico: int


    def __str__(self):
        return f"{self.nomeCorso} ({self.codCorso})"



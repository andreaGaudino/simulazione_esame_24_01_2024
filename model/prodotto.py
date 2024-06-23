from dataclasses import dataclass

@dataclass
class Prodotto:
    prodotto: int
    somma: float


    def __hash__(self):
        return hash(self.prodotto)
    def __str__(self):
        return f"{self.prodotto} -- {self.somma}"
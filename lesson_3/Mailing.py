from Adress import Adress

class Mailing:

    def __init__(self, to_address: Adress, from_address: Adress, cost: float, track: str):
        self.to_adress = to_address
        self.from_adress = from_address
        self.cost = cost
        self.track = track 

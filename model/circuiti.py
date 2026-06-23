from dataclasses import dataclass


@dataclass
class Circuit:
    circuitId: int
    circuitRef: str
    name: str
    location: str
    country: str
    lat:float
    lng: float
    alt:int
    url: str


    def __post_init__(self):
        self.piloti = {}
    def __hash__(self):
        return self.circuitId

    def __repr__(self):
        return f"Circuit(id={self.circuitId}, name='{self.name}', country='{self.country}', piloti={self.piloti})"
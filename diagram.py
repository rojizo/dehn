from curve import Curve
from points import DiagramPoint, SignedDiagramPoint

class Diagram:
    def __init__(self):
        self._curves = []

    def new_curve(self, name: str) -> (Curve, Curve):
        a = Curve()
        a._name = name

        ta = Curve()

        a.set_sister(ta)

        self._curves.append([a, ta])

        return a, ta

    def __str__(self) -> str:
        rep = "\n".join(f"({str(a)}) == ({str(b)})" for a, b in self._curves)
        return f"[{rep}]"

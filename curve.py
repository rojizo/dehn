from points import SignedDiagramPoint


class Curve(list[SignedDiagramPoint]):
    def __init__(self):
        self._sister = None
        super().__init__()
        self._name = None

    def __str__(self) -> str:
        rep = ",".join([str(x) for x in super()])
        rep = f"[{rep}]"
        if not(self._name is None):
            rep = f"{self._name} = {rep}"
        return rep

    def set_sister(self, sisterCurve) -> None:
        if self._sister is None:
            if sisterCurve._sister is None:
                self._sister = sisterCurve
                sisterCurve._sister = self
            else:
                raise ValueError("The given sisterCurve is already set")
        else:
            raise ValueError("You cannot assign the sisterCurve twice")

    def __getitem__(self, item: int) -> SignedDiagramPoint:
        return super()[item % len(super())]

    def append(self, point: SignedDiagramPoint) -> None:
        if type(point) != SignedDiagramPoint:
            raise TypeError(f"__object should be a SignedDiagramPoint but it is {type(SignedDiagramPoint)}")

        point._position_in_diagram = len(self)
        point._curve = self
        super().append(point)

class Point:
    def __init__(self, ID):
        self._ID = ID
        self._triplet = {str(i): DiagramPoint(self, i) for i in [1, 2, 3]}

    def __repr__(self):
        return str(self._ID)

    def get_triplet(self):
        return self._triplet

    def diagram_point(self, i: int):
        return self._triplet[str(i)]

    def __getitem__(self, item):
        return self.diagram_point(item)


class DiagramPoint:
    def __init__(self, P3D: Point, num_in_triplet: int):
        if type(P3D) != Point:
            raise TypeError(f"Type of P3D must Point but it is {type(P3D)}")
        if type(num_in_triplet) != int:
            raise TypeError(
                f"`num_in_triplet' should be integer but it is `{num_in_triplet}' of type {type(num_in_triplet)}")
        if not (1 <= num_in_triplet <= 3):
            raise ValueError(f"`num_in_triplet' must be 1, 2 or 3, but it is {num_in_triplet}")

        self._manifold_point = P3D
        self._num_in_triplet = num_in_triplet

        self._negative = SignedDiagramPoint(self, -1)
        self._positive = SignedDiagramPoint(self, +1)

    def __repr__(self):
        return f"{repr(self._manifold_point)}_{self._num_in_triplet}"

    def __pos__(self):
        return self.positive()

    def positive(self):
        return self._positive

    def __neg__(self):
        return self.negative()

    def negative(self):
        return self._negative


class SignedDiagramPoint:
    def __init__(self, P2D: DiagramPoint, sign: int):
        if type(P2D) != DiagramPoint:
            raise TypeError(f"Type of P2D must be DiagramPoint but it is {type(P2D)}")
        if type(sign) != int:
            raise TypeError(f"`sign' must be integer but it is {type(sign)}")
        if -1 != sign != 1:
            raise ValueError(f"`sign' should be -1 or 1")
        self._diagram_point = P2D
        self._sign = sign

        # Info in the diagram
        self._curve = None
        self._position_in_diagram = None

    def __repr__(self):
        return ("+" if self._sign == 1 else "-") + repr(self._diagram_point)

    def add_to_curve(self, curve):
        curve.append(self)

    def __next__(self):
        return self._curve[self._position_in_diagram + 1]

    def is_positive(self) -> bool:
        return self._sign == 1

    def is_negative(self) -> bool:
        return self._sign == -1

    @property
    def curve(self):
        return self._curve

    @property
    def diagram_point(self):
        return self._diagram_point

    def __neg__(self):
        return self._diagram_point.negative() if self._sign == 1 else self._diagram_point.positive()

class Point:
    def __init__(self, ID):
        self._ID = ID

    def __repr__(self):
        return str(self._ID)


class DiagramPoint:
    def __init__(self, P3D: Point, num_in_triplet: int):
        if type(P3D) != Point:
            raise ValueError(f"Type of P3D must Point but it is {type(P3D)}")
        if type(num_in_triplet) != int:
            raise ValueError(
                f"`num_in_triplet' should be integer but it is `{num_in_triplet}' of type {type(num_in_triplet)}")
        if not (1 <= num_in_triplet <= 3):
            raise ValueError(f"`num_in_triplet' must be 1, 2 or 3, but it is {num_in_triplet}")

        self._manifold_point = P3D
        self._num_in_triplet = num_in_triplet

        self._negative = None
        self._positive = None

    def __repr__(self):
        return f"{repr(self._manifold_point)}_{self._num_in_triplet}"

    def __pos__(self):
        return self.positive()

    def positive(self):
        if not (self._positive in None):
            self._positive = SignedDiagramPoint(self, +1)
        return self._positive

    def __neg__(self):
        return self.negative()

    def negative(self):
        if not (self._negative is None):
            self._negative = SignedDiagramPoint(self, -1)
        return self._negative


class SignedDiagramPoint:
    def __init__(self, P2D: DiagramPoint, sign: int):
        if type(P2D) != P2D:
            raise ValueError(f"Type of P2D must be DiagramPoint but it is {type(P2D)}")
        if type(sign) != int:
            raise ValueError(f"`sign' must be integer but it is {type(sign)}")
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
        self._position_in_diagram = len(curve)
        self._curve = curve
        self._curve.append(self)

    def __next__(self):
        return self._curve[(self._position_in_diagram + 1) % len(self._curve)]


class Curve:
    def __init__(self):
        self._list = []
        self._sister = None

    def set_sister(self, sisterCurve):
        if self._sister is None:
            if sisterCurve._sister is None:
                self._sister = sisterCurve
                sisterCurve._sister = self
            else:
                raise ValueError("The given sisterCurve is already set")
        else:
            raise ValueError("You cannot assign the sisterCurve twice")

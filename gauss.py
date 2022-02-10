import copy as _copy

class Point:
    class Point2D:
        def __init__(self, P, i: int):
            self.P = P
            self.ID = i
            self.sign = +1

        def __repr__(self):
            return f"{self.P}_{self.ID}"

        def __neg__(self):
            ret = Point.Point2D(self.P, self.ID)
            ret.sign = -self.sign
            return ret

        @property
        def point(self):
            return self.P

        @property
        def i(self):
            return self.ID

    def __init__(self, ID: int):
        self.ID = ID
        self.printable_representation = None

    def __repr__(self):
        if self.printable_representation is None:
            self.printable_representation = ""
            val = self.ID
            while True:
                self.printable_representation += chr(val % 26 + 65)
                val //= 26
                if val == 0:
                    break

        return self.printable_representation

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, item: int):
        if not (1 <= item <= 3):
            raise ValueError("Item should be 1, 2 or 3")
        return self.Point2D(self, item)


class GaussDiagram:
    points = []
    curves = []

    @staticmethod
    def from_string_representation(rep: list[list[str]]):
        ret = GaussDiagram()

        points = {}
        for c, tc in rep:
            c.split(",")
            tc.split(",")



        return ret

    def __init__(self):
        pass

    def add_point(self):
        self.points.append(Point(len(self.points)))
        return self.points[-1]

    def add_curve(self, curve, sister_curve):
        if len(curve) != len(sister_curve):
            raise ValueError("The sister curves have no the same length")

        for i, P1, P2 in enumerate(zip(curve, sister_curve)):
            if P1.point != P2.point:
                raise ValueError(f"The curves are not properly aligned: {i}-th plane points are {P1} and {P2}")

            if not (P1.point in self.points):
                raise ValueError(f"The point {P1.point} does not belongs to the diagram")

            # Ok... add the curve
            self.curves.append([_copy.deepcopy(curve), _copy.deepcopy(sister_curve)])

    def check_consistency(self):
        return True

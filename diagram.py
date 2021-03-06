from curve import Curve
from points import *


class Diagram:

    @staticmethod
    def from_string_representation(rep: list[list[str]]):
        D = Diagram()

        point_names = set()
        for c, tc in rep:
            for x in c.split(","):
                point_names.add(x.strip()[:-1].replace("+", "").replace("-", ""))
            for x in tc.split(","):
                point_names.add(x.strip()[:-1].replace("+", "").replace("-", ""))

        points = {P: Point(P) for P in point_names}

        def parse_curve(c, a) -> None:
            for x in c.split(","):
                triplet = int(x.strip()[-1])
                name = x.strip()[:-1].replace("+", "").replace("-", "")
                a.append(+points[name][triplet] if x[0] != "-" else -points[name][triplet])

        for i, (c, tc) in enumerate(rep):
            a, ta = D.new_curve(f"c{i}")
            parse_curve(c, a)
            parse_curve(tc, ta)

        return D

    def __init__(self):
        self._curves = []

    def new_curve(self, name: str) -> (Curve, Curve):
        a = Curve()
        a._name = name

        ta = Curve()

        a.set_sister(ta)

        a._position = len(self._curves)
        a._sisterness = 0
        ta._position = len(self._curves)
        ta._sisterness = 1

        self._curves.append([a, ta])

        return a, ta

    def __str__(self) -> str:
        rep = "\n".join(f"({str(a)}) == ({str(b)})" for a, b in self._curves)
        return f"[{rep}]"

    def is_realizable(self) -> bool:
        # Which class we belong to
        relations = {(sign, i, s): k for k, (sign, i, s) in enumerate((sign, i, s) for i in range(len(self._curves))
                                                                      for s in [0, 1]
                                                                      for sign in [-1, 1])}
        # Equivalence classes
        classes = [{(sign, i, s)} for i in range(len(self._curves)) for s in [0, 1] for sign in [-1, 1]]

        def identify(a, b):
            classes[relations[a]].update(classes[relations[b]])
            for j in classes[relations[b]]:
                relations[j] = relations[a]
            # TODO: make some cleanup... not really needed but could be fine

        # We start with the second kind relations
        for i in range(len(self._curves)):
            identify((-1, i, 0), (1, i, 1))  # alpha- = talpha+
            identify((1, i, 0), (-1, i, 1))  # alpha+ = talpha-

        # Now we should complete the relation with the first kind relations
        for alpha, talpha in self._curves:
            for P, tP in zip(alpha, talpha):
                # --*-P--> is related with --*-tP-->
                # Then the neighbouring curves producing those points are related

                # Which curve is producing --*-P-->? Depends on the sign of the point
                #       ???                  ???
                #       ???  -               ??? +
                #    ?????????????????????           ????????????????????????
                #       *                  *
                #       ???                  ???
                #     alpha              alpha
                #
                # Then for negative point the neighbouring curve defining * is the positive (right one)
                # For the positive point the curve is the negative one

                crossing_curve_number = (-P).curve._position
                crossing_curve_sign = 1 if P.is_negative() else -1
                tcrossing_curve_number = (-tP).curve._position
                tcrossing_curve_sign = 1 if tP.is_negative() else -1

                identify((tcrossing_curve_sign, tcrossing_curve_number, (-tP).curve._sisterness),
                         (crossing_curve_sign, crossing_curve_number, (-P).curve._sisterness))

                # Something similar happens for ---P-*-> is related with ---tP-*->
                crossing_curve_number = (-P).curve._position
                crossing_curve_sign = -1 if P.is_negative() else 1
                tcrossing_curve_number = (-tP).curve._position
                tcrossing_curve_sign = -1 if tP.is_negative() else 1

                identify((tcrossing_curve_sign, tcrossing_curve_number, (-tP).curve._sisterness),
                         (crossing_curve_sign, crossing_curve_number, (-P).curve._sisterness))


        print(relations)
        print(classes)

        # Connectivity of the graph
        # TODO: implement the algorithm ourselves
        import networkx as nx
        import matplotlib.pyplot as plt
        G = nx.Graph()
        for alpha in (x for c in self._curves for x in c):
            for i in range(len(alpha)):
                G.add_edge(str(alpha[i].diagram_point), str(alpha[(i+1)%len(alpha)].diagram_point))
        if not nx.is_connected(G):
            return False

        # Check if it is realizable
        for i in range(len(self._curves)):
            for s in [0, 1]:
                if relations[(1, i, s)] == relations[(-1, i, s)]:
                    return False

        return True

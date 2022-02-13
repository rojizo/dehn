from diagram import Diagram


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    from diagram import Diagram
    import points

    # %%
    D = Diagram()
    a, ta = D.new_curve("alfa")
    P = points.Point("P")
    Q = points.Point("Q")
    # %%
    a.extend([+P[1], -Q[1], +Q[1], +Q[2], -P[2], -P[1]])
    ta.extend([+P[2], -Q[2], -Q[3], +Q[3], -P[3], +P[3]])
    # %%
    print(D.is_realizable())

    print(D)


    D=Diagram.from_string_representation([["P1,-Q1,Q1,Q2,-P2,-P1", "P2,-Q2,-Q3,Q3,-P3,P3"]])
    print(D)
    # %%

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

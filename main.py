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
    # %%

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

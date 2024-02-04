import pulp


def main():
    model = pulp.LpProblem("Company", pulp.LpMaximize)

    x1 = pulp.LpVariable("x1", 0, None, pulp.LpContinuous)  # Lemonade
    x2 = pulp.LpVariable("x2", 0, None, pulp.LpContinuous)  # Fruit juice

    model += x1 + x2, "profit"

    model += 2 * x1 + x2 <= 100, "water"
    model += x1 <= 50, "sugar"
    model += x1 <= 30, "lemon juice"
    model += 2 * x2 <= 40, "fruit puree"

    model.solve()

    print(f"Status: {pulp.LpStatus[model.status]}")
    print(f"Optimal units of Lemonade: {x1.varValue}")
    print(f"Optimal units of Fruit Juice: {x2.varValue}")
    print(f"Profit: {model.objective.value()}")


if __name__ == "__main__":
    main()



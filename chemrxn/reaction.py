class Reaction:
    """Represents a single chemical reaction."""

    def __init__(self, stoich, k, orders=None):
        self.stoich = stoich
        self.k = float(k)
        self.orders = orders or {}

    @property
    def reactants(self):
        return {k: -v for k, v in self.stoich.items() if v < 0}

    @property
    def products(self):
        return {k: v for k, v in self.stoich.items() if v > 0}

    def __repr__(self):
        reactant_str = ' + '.join(
            [f"{coef}{name}" if coef != 1 else name
             for name, coef in self.reactants.items()]
        )

        product_str = ' + '.join(
            [f"{coef}{name}" if coef != 1 else name
             for name, coef in self.products.items()]
        )

        return f"{reactant_str} -> {product_str} (k={self.k})"
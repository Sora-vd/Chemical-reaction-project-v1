class Reaction:
    """Represents a single chemical reaction."""

    def __init__(self, reactants, products, rate_constant):
        self.reactants = reactants  # list of Species objects
        self.products = products    # list of Species objects
        self.rate_constant = rate_constant  # float

    def __repr__(self):
        reactant_str = ' + '.join([r.name for r in self.reactants])
        product_str = ' + '.join([p.name for p in self.products])
        return f"{reactant_str} -> {product_str} (k={self.rate_constant})"

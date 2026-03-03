class Reaction:
    """Represents a single chemical reaction."""

    def __init__(self, stoich, k, orders=None, name=None):
        """parameters: 
        stoich (dict of reactant/product names to stoichiometric coefficients, positive for products, negative for reactants), 
        k (float rate constant), 
        orders (dict of reactant names to reaction orders)"""
        self.stoich = stoich
        self.k = float(k) #store as float to ensure consistent type for rate calculations
        self.orders = orders or {}
        self.name = name

    @property
    def reactants(self):
        """Returns a dictionary of reactants with their stoichiometric coefficients (negative values)"""
        return {k: -v for k, v in self.stoich.items() if v < 0}

    @property
    def products(self):
        """Returns a dictionary of products with their stoichiometric coefficients (positive values)"""
        return {k: v for k, v in self.stoich.items() if v > 0}

    def rate(self, species_dict):
        """mass-action rate law: rate = k * product of [C_i^order_i] for reactants"""
        rate = self.k
        for name, order in self.orders.items():
            rate *= species_dict[name].ct ** order
        return rate

    def dc_dt(self, species_dict):
        """Return contribution of this reaction to dC/dt for each species as a dictionary"""
        r = self.rate(species_dict)
        dc_dt = {}
        for name, coef in self.stoich.items():
            dc_dt[name] = coef * r
        return dc_dt

    def __repr__(self):
        """Returns a readable reaction string representation, e.g. '2A + B -> C (k=0.1)'"""
        #format reactants 
        reactant_str = ' + '.join(
            [f"{coef}{name}" if coef != 1 else name
             for name, coef in self.reactants.items()]
        )

        #format products
        product_str = ' + '.join(
            [f"{coef}{name}" if coef != 1 else name
             for name, coef in self.products.items()]
        )

        return f"{reactant_str} -> {product_str} (k={self.k})"
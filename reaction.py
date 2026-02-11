def rate(self):
    rate = self.rate_constant
    for species, coeff in self.reactants.items():
        order = abs(coeff)
        rate *= species.ct ** order
    return rate

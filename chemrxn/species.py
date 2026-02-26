import pandas as pd
import os
molecules = pd.read_csv(os.getcwd() + "/input.csv", index_col="formula")

class Species: 
    """A class to represent a chemical species in a reaction."""

    def __init__(self, formula):
        self.name = molecules.loc[formula, "compound"]
        self._c0 = molecules.loc[formula, "c0"] #use property setter to validate c0
        self.formula = formula 
        self.state = molecules.loc[formula, "state"]
        
    #initial concentration 
    @property 
    def c0(self): 
        return self._c0 
    
    @c0.setter
    def c0(self, value):
        if value < 0:
            raise ValueError("Initial concentration cannot be negative")
        self._c0 = float(value)
        self.ct = float(value) # set current concentration to initial concentration when c0 is updated
    
    #reset concentration to initial value
    def reset(self):
        self.ct = self._c0

    def update_concentration(self, new_ct):
        if new_ct < 0:
            raise ValueError("Concentration cannot be negative")
        self.ct = new_ct
    
    def __repr__(self):
        return f"Species(name={self.name}, formula={self.formula}, state={self.state}, c0={self._c0})"
    


# test class
water = Species("H2O") 
print(f"water: {water}")
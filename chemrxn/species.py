import pandas as pd
import os
molecules = pd.read_csv(os.getcwd() + "/input.csv", index_col="formula")

class Species: 
    """A class to represent a chemical species in a reaction."""

    def __init__(self, formula):
        """Initializes a species with its properties.

        Parameters:
        formula (str): molecular formula of the species
        c0 (float): initial concentration of the species in mol/l
        name (string): name of the molecule
        state (string): state of the species
        
        """
        self.name = molecules.loc[formula, "compound"]
        self._c0 = molecules.loc[formula, "c0"] #use property setter to validate c0
        self.formula = formula 
        self.state = molecules.loc[formula, "state"]
        
    @property 
    def c0(self): 
        """getter method of initial concentration
    
        Parameters:
        c0 (float): initial concentration in mol/l
    
        Returns:
        float: initial concentration
        
        """
        return self._c0 
    
    @c0.setter
    def c0(self, value):
        """setter method of initial concentration

        Validates that the set initial concentration is larger than 0 or 0. Also resets the concentration at time t to the new initial concentration.
    
        Parameters:
        c0 (float): initial concentration in mol/l
        
        """
        if value < 0:
            raise ValueError("Initial concentration cannot be negative")
        self._c0 = float(value)
        self.ct = float(value) # set current concentration to initial concentration when c0 is updated
    
    #reset concentration to initial value
    def reset(self):
        """resets the concentration at time t to the initial concentration to restart the reaction simulation"""
        self.ct = self._c0

    def update_concentration(self, new_ct):
        """validates that the new concentration at time t is larger than 0 or 0 and updates the concentration at time t to the new concentration
    
        Parameters:
        new_ct (float):  concentration at time t
        
        """
        if new_ct < 0:
            raise ValueError("Concentration cannot be negative")
        self.ct = new_ct
    
    def __repr__(self):
        """returns spring representation of the species parameters
    
        Returns:
        str: Species(name= , formula= , state= , c0= )
        
        """
        return f"Species(name={self.name}, formula={self.formula}, state={self.state}, c0={self._c0})"
    


# test class
water = Species("H2O") 
print(f"water: {water}")
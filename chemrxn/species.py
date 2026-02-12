class Species: 
    import pandas as pd
    molecules = pd.read_csv("", index_col=0)
    
    def __init__(self, name, c0, formula=None, state=None):
        self.name = name
        self._c0 = c0
        self.ct = c0
        self.formula = formula
        self.state = state

    @property 
    def c0(self): 
        return self._c0 
    
    @c0.setter
    def c0(self, value):
        if value < 0:
            raise ValueError("Initial concentration cannot be negative")
        self._c0 = value
        self.ct = value
    
    def reset(self):
        self.ct = self._c0

    def __repr__(self):
        return f"Species(name={self.name}, formula={self.formula}, state={self.state}, c0={self._c0}, ct={self.ct})"
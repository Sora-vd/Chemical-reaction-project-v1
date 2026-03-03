import matplotlib
matplotlib.use("TkAgg")

import numpy as np 
import matplotlib.pyplot as plt


class ReactionNetwork: 
    """Represents a network of chemical reactions."""
    def __init__(self, species, reactions, t_start, t_end, dt):
        self.species = species #dict of species name to Species object
        self.reactions = reactions #list of Reaction objects
        self.t_start = float(t_start)
        self.t_end = float(t_end)
        self.dt = float(dt) #simulation time interval

        #fixed species order 
        self._names = list(self.species.keys())

        #time grid 
        self.time_points = np.arange(t_start, t_end + dt, dt)

        #storage of concentration history for each species over time, initialized as empty lists
        self.concentration_history = {name: [] for name in self._names}

        self.rate_history = [[] for _ in self.reactions]

    def get_species(self, name):
        return self.species[name]
    

    def dC_dt(self, t, concentrations):
        """
        Computes rate of change of concentrations over time (dC/dt).
        Parameters:
        t (float): current time 
        concentrations: numpy array
        returns: numpy array of dC/dt vector in consistent species order
        """

        # Update Species objects with current concentrations 
        for i, name in enumerate(self._names):
            self.species[name].ct = concentrations[i]

        # Initialize total derivates 
        dCdt = {name: 0.0 for name in self._names}

        # Sum contributions from each reaction
        for reaction in self.reactions:
            reaction_contribution = reaction.dc_dt(self.species)
            for name, value in reaction_contribution.items():
                dCdt[name] += value

        # store for optional inspection
        self.increments = dCdt

        # Return ordered vector
        return np.array([
            dCdt[name] for name in self._names
        ])
    
    def simulate(self):
        """simulate euler integration of the reaction network over time"""

        #initial concentration vector
        concentrations = np.array([self.species[name].c0 for name in self._names])

        for t in self.time_points:
            #store current concentrations
            for i, name in enumerate(self._names):
                self.species[name].ct = concentrations[i]

            for i, name in enumerate(self._names):
                self.concentration_history[name].append(concentrations[i])
           
            #compute and store current reaction rates
            for i, reaction in enumerate(self.reactions):
                current_rate = reaction.rate(self.species)
                self.rate_history[i].append(current_rate)

            #compute derivatives
            dCdt = self.dC_dt(t, concentrations)

            #update concentrations using Euler's method
            concentrations += dCdt * self.dt 
            #+= modifies array in place - loop correctly stores value before updating & ensures all updates happen simultaneously

    def plot_all(self):
        plt.close("all")

        fig, axs = plt.subplots(2, 1, figsize=(10, 8))

        # Concentration plot
        for name in self._names:
            axs[0].plot(self.time_points,
                    self.concentration_history[name],
                    label=name)
        axs[0].set_title("Concentration vs Time")
        axs[0].set_xlabel("Time")
        axs[0].set_ylabel("Concentration")
        axs[0].legend(loc="upper right")
        axs[0].grid()

        # Rate plot
        for i, rate_list in enumerate(self.rate_history):
            reaction = self.reactions[i]
            
            axs[1].plot(self.time_points,
                    rate_list,
                    label=str(str(reaction.name)))
        axs[1].set_title("Rate vs Time")
        axs[1].set_xlabel("Time")
        axs[1].set_ylabel("Rate")
        axs[1].legend()
        axs[1].grid()
        
        plt.tight_layout()
        plt.show()
      

        
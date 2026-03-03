import pandas as pd
import os

from species import Species
from reaction import Reaction
from network import ReactionNetwork


def load_species(filepath):
    df = pd.read_csv(filepath, index_col="formula") #load the iput

    species_dict = {
        formula: Species(formula)
        for formula in df.index
    }

    return species_dict, df


def build_reaction_from_csv(df):
    """
    Builds H2O2 decomposition reaction:
    2 H2O2 -> 2 H2O + O2
    """

    # Extract rate constant from H2O2 row
    k = float(df.loc["H2O2", "k"])

    # Extract reaction order
    order = float(df.loc["H2O2", "order"])

    stoich = {
        "H2O2": -2,
        "H2O": 2,
        "O2": 1
    }

    orders = {
        "H2O2": order
    }

    return Reaction(stoich=stoich, k=k, orders=orders)


def main():

    filepath = os.path.join(os.getcwd(), "input.csv")

    species, df = load_species(filepath)

    reaction = build_reaction_from_csv(df)

    network = ReactionNetwork(
        species=species,
        reactions=[reaction],
        t_start=0,
        t_end=5000,
        dt=1
    )

    network.simulate()
    network.plot_all()
    

if __name__ == "__main__":
    main()
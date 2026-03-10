# Chemical Reaction Simulator

**A Python project for simulating chemical reactions and tracking concentration over time**

## Description 
The program models first and second-order chemical reactions when the initial concentration of the reactant is known. This program can help students and teachers gain a better understanding of reaction rates and kinetics. 

Once the user registers:
- The reactant
- The initial concentration
- The rate constant

The program computes and visualizees concentration as a function of time. 

The simulator has three core components:
- Species --> stores chemical data
- Reaction --> computes reaction rates
- ReactionNetwork --> integrates over time and generates plots

### Kinetic Models Implemented

#### First-order reaction
 Integrated rate law:
 ln(A)t = -k t + ln(A)0
#### Second-order reaction
 Integrated rate law:
1 / (A)t = k t + 1 / (A)0

#### Variables:

(A)t = Concentration at time t

(A)0 = Initial Concentration

k = Rate constant

t = time

## Features
- Object-oriented design

- Private initial concentration handling

- First-order reaction simulation

- Second-order reaction simulation

- Concentration vs time plots

- Reaction rate vs time plots

## Installation
### Prerequisites

- Python 3.8+

- NumPy

- SciPy

- Matplotlib

- Pandas

### Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/chemical-reaction-simulator.git
cd chemical-reaction-simulator
```

2. Install dependencies

```bash
pip install -r requirements.txt
```
If you do not have a requirements file: 
```bash
pip install numpy scipy matplotlib pandas
```
## Usage Example 

### First Order Reaction Example:
```bash
from species import Species
from reaction import Reaction
from network import ReactionNetwork

#Create species
A = Species("H2O2")
B = Species("H2O")
C = Species("O2")

#Define first-order reaction
reaction = Reaction(
    stoich={"H2O2": -2, "H2O": 2, "O2": 1},
    k=0.2,
    orders={"H2O2": 1}
)

#Create network
network = ReactionNetwork(
    species={A.formula: A, B.formula: B, C.formula: C},
    reactions=[reaction],
    t_start=0,
    t_end=50,
    dt=0.1
)

#Run simulation
network.simulate()

#Plot results
network.plot_all()
```
## Project Structure

```bash
chemical-reaction-simulator/
│
├── species.py      # Species class (data only)
├── reaction.py     # Reaction definition and rate calculations
├── network.py      # Time integration and system management
├── plotting.py     # Plotting functions
├── examples/       # Example scripts
├── requirements.txt
├── README.md
└── LICENSE
```
## Architecture Overview

### Species (species.py)

Stores and validates one chemical species.

#### Attributes:

- name

- formula

- state

- _c0 (private initial concentration)

- ct (current concentration)

#### Methods:

- c0 property + setter

- reset()

- __repr__() (optional)


### Reaction (reaction.py)

Defines one reaction and computes its rate.

#### Attributes:

- stoich (signed stoichiometric dictionary)

- k (rate constant)

- orders (power-law orders)

#### Rate rule:

If orders is empty:

r = k

Otherwise:

r = k × Π (C_i ^ order_i)

Concentration change:

dC_i/dt = ν_i × r

This class does not integrate over time or generate plots.

### ReactionNetwork (network.py)

Responsible for:

- Managing time grid

- Integrating differential equations

- Generating plots

### Attributes:

- t_start, t_end, dt

- species

- reactions

#### Methods:

- rhs(t, y)

- simulate()

- plot_concentrations()

- plot_rates()

## Possible Reactions Included

- First-order hydrogen peroxide decomposition

- Second-order nitrogen dioxide decomposition

## Contributing

1. Fork the repository

2. Create a new branch

3. Commit your changes

4. Submit a pull request

### Guidelines:

Keep Species as a data-only class

Do not mix plotting inside Reaction

Keep integration logic inside ReactionNetwork

## License

MIT License

Copyright (c) [2026] [Gunes Beleli, Karolina Kuipec, Emma Bornemann, Sora van de Wiel]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors

- Gunes Beleli
- Karolina Kuipec
- Emma Bornemann 
- Sora van de Wiel 

## Future Improvements

- Reversible reactions

- Temperature-dependent rate constants

- Database integration for rate constants

- Reaction network graph visualization

- GUI interface


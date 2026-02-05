# Chemical-reaction-project-v1
A Python project for representing chemical species, reactions, and reaction networks.

## MVP Goals (Week 2)
- Define `Species`
- Define `Reaction` with stoichiometry
- Define `State` (amounts of species)
- Define `ReactionNetwork` (apply reaction extent, basic validation)
- Load a network from JSON (`data/sample_network.json`)
- Basic unit tests with pytest

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

pip install -U pip pytest
pytest
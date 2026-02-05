import json
from pathlib import Path

from chemrxn.species import Species
from chemrxn.reaction import Reaction


def load_network_from_json(path: str | Path):
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))

    # ---- basic validation (shows data handling skills) ----
    for key in ("network", "species", "reactions"):
        if key not in data:
            raise ValueError(f"Missing top-level key '{key}' in {path}")

    net = data["network"]
    for k in ("t_start", "t_end", "dt"):
        if k not in net:
            raise ValueError(f"Missing network setting '{k}' in {path}")
    if net["dt"] <= 0:
        raise ValueError("dt must be > 0")
    if net["t_end"] <= net["t_start"]:
        raise ValueError("t_end must be > t_start")

    # ---- build species objects ----
    species_by_id: dict[str, Species] = {}
    species_list: list[Species] = []

    for s in data["species"]:
        for k in ("id", "name", "c0"):
            if k not in s:
                raise ValueError(f"Species missing '{k}': {s}")
        if s["id"] in species_by_id:
            raise ValueError(f"Duplicate species id: {s['id']}")
        if s["c0"] < 0:
            raise ValueError(f"Initial concentration cannot be negative: {s}")

        sp = Species(
            name=s["name"],
            c0=s["c0"],
            formula=s.get("formula"),
            state=s.get("state"),
        )
        species_by_id[s["id"]] = sp
        species_list.append(sp)

    # ---- build reactions ----
    reactions: list[Reaction] = []
    for r in data["reactions"]:
        for k in ("id", "type", "rate_constant", "stoichiometry"):
            if k not in r:
                raise ValueError(f"Reaction missing '{k}': {r}")

        if r["rate_constant"] < 0:
            raise ValueError(f"rate_constant must be >= 0: {r}")

        # verify species ids in stoichiometry exist
        for sid in r["stoichiometry"].keys():
            if sid not in species_by_id:
                raise ValueError(f"Reaction '{r['id']}' references unknown species id '{sid}'")

        # convert stoichiometry dict into reactants/products dicts keyed by Species objects
        reactants = {}
        products = {}
        for sid, coeff in r["stoichiometry"].items():
            sp = species_by_id[sid]
            if coeff < 0:
                reactants[sp] = coeff
            elif coeff > 0:
                products[sp] = coeff

        rxn = Reaction(
            reactants=reactants,
            products=products,
            rate_constant=r["rate_constant"]
        )
        reactions.append(rxn)

    return species_list, reactions, net

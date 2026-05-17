"""
Benchmark entry point — Percorso Evolutivo Pathfinder
=====================================================
Dimostra l'utilizzo del Pathfinder su una griglia di esempio.

Struttura del progetto:
    cell.py         — Classe Cell (singola cella della griglia)
    grid.py         — Classe Grid (griglia di gioco)
    pathfinder.py   — Classe Pathfinder (BFS con stati)
    main.py         — Questo file

Esecuzione:
    python main.py
"""

from grid import Grid
from pathfinder import Pathfinder


def main():
    # --- Costruisce una griglia 8x8 riproducibile ---
    grid = Grid.build_example(rows=8, cols=8, seed=42)

    print("=== GRIGLIA ===")
    print("Legenda: P=Spawn  O=Obiettivo  X=Muro  T=Trappola  R=Risorsa  .=Vuota\n")
    grid.print_grid()

    start  = grid.spawn_position
    target = grid.target_position
    print(f"Spawn:     {start}")
    print(f"Obiettivo: {target}\n")

    # --- Esegue il Pathfinder con parametri diversi ---
    pathfinder = Pathfinder(grid)

    scenarios = [
        {"player_score": 20, "max_breakable_walls": 0, "max_convertible_traps": 0},
        {"player_score": 20, "max_breakable_walls": 2, "max_convertible_traps": 0},
        {"player_score": 20, "max_breakable_walls": 2, "max_convertible_traps": 2},
    ]

    for i, params in enumerate(scenarios, 1):
        reachable, path = pathfinder.is_reachable(
            start=start,
            target=target,
            **params
        )
        print(f"Scenario {i}: score={params['player_score']}  "
              f"walls={params['max_breakable_walls']}  "
              f"traps={params['max_convertible_traps']}")
        if reachable:
            print(f"  Raggiungibile — percorso ({len(path)} passi): {path}")
        else:
            print(f"  Non raggiungibile")
        print()


if __name__ == "__main__":
    main()

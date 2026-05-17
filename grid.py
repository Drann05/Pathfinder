import random
from cell import Cell


class Grid:
    """
    Griglia di gioco semplificata per il benchmark del Pathfinder.
    Espone solo l'interfaccia necessaria al Pathfinder:
    - Costanti dei tipi di cella
    - height, width
    - get_cell(position)
    - set_cell(position, cell_type)
    - print_grid()
    """

    MURO           = 'X'
    RISORSA        = 'R'
    TRAPPOLA       = 'T'
    OBIETTIVO      = 'O'
    PUNTO_DI_PARTENZA = 'P'
    CELLA_VUOTA    = '.'

    def __init__(self, rows: int, cols: int):
        self._rows = rows
        self._cols = cols
        # Inizializza tutta la griglia come muri
        self.grid = [
            [Cell(r, c, self.MURO) for c in range(cols)]
            for r in range(rows)
        ]
        self._spawn_position = None
        self._target_position = None

    # ------------------------------------------------------------------
    #   Interfaccia pubblica usata dal Pathfinder
    # ------------------------------------------------------------------

    @property
    def height(self) -> int:
        return self._rows

    @property
    def width(self) -> int:
        return self._cols

    @property
    def spawn_position(self) -> tuple[int, int]:
        return self._spawn_position

    @property
    def target_position(self) -> tuple[int, int]:
        return self._target_position

    def get_cell(self, position: tuple[int, int]) -> Cell:
        """Restituisce il riferimento alla cella in posizione (row, col)."""
        row, col = position
        return self.grid[row][col]

    def set_cell(self, position: tuple[int, int], cell_type: str):
        """Imposta il tipo della cella in posizione (row, col)."""
        row, col = position
        self.grid[row][col].set_type(cell_type)
        if cell_type == self.PUNTO_DI_PARTENZA:
            self._spawn_position = position
        elif cell_type == self.OBIETTIVO:
            self._target_position = position

    # ------------------------------------------------------------------
    #   Factory: costruisce una griglia di esempio per i test
    # ------------------------------------------------------------------

    @classmethod
    def build_example(cls, rows: int = 8, cols: int = 8, seed: int = 42) -> "Grid":
        """
        Costruisce una griglia di esempio riproducibile tramite seed.
        Layout:
        - Percorso libero garantito da (0,0) a (rows-1, cols-1)
        - Muri, trappole e risorse piazzati casualmente nelle celle rimanenti
        - Spawn in (0,0), Obiettivo in (rows-1, cols-1)
        """
        random.seed(seed)
        g = cls(rows, cols)

        # 1. Scava un percorso garantito in linea retta (N→S poi O→E)
        for r in range(rows):
            g.set_cell((r, 0), cls.CELLA_VUOTA)
        for c in range(cols):
            g.set_cell((rows - 1, c), cls.CELLA_VUOTA)

        # 2. Popola il resto con celle casuali
        cell_pool = [cls.CELLA_VUOTA] * 6 + [cls.RISORSA] * 2 + [cls.TRAPPOLA] * 2
        for r in range(rows):
            for c in range(cols):
                if g.get_cell((r, c)).type == cls.MURO:
                    g.set_cell((r, c), random.choice(cell_pool))

        # 3. Piazza spawn e obiettivo
        g.set_cell((0, 0), cls.PUNTO_DI_PARTENZA)
        g.set_cell((rows - 1, cols - 1), cls.OBIETTIVO)

        return g

    # ------------------------------------------------------------------
    #   Utility
    # ------------------------------------------------------------------

    def print_grid(self):
        """Stampa la griglia su stdout."""
        for row in self.grid:
            print(' '.join(cell.type for cell in row))
        print()

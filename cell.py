class Cell:
    """
    Rappresenta una singola cella della griglia di gioco.
    Ogni cella è caratterizzata da una posizione (row, col) e un tipo.
    """

    CELL_TYPES = {
        'O': 'green',   # Obiettivo
        'P': 'blue',    # Punto di partenza
        'X': 'black',   # Muro (non attraversabile)
        'T': 'red',     # Trappola (-5 punti)
        'R': 'yellow',  # Risorsa (+10 punti)
        '.': 'white'    # Cella vuota
    }

    def __init__(self, row: int, col: int, cell_type: str):
        self._row = row
        self._col = col
        self._type = None
        self.set_type(cell_type)

    def set_type(self, cell_type: str):
        if cell_type not in self.CELL_TYPES:
            raise ValueError(f"Tipo non valido: '{cell_type}'. Valori accettati: {list(self.CELL_TYPES.keys())}")
        self._type = cell_type

    def is_walkable(self) -> bool:
        """Restituisce False solo per i muri ('X'), True per tutto il resto."""
        return self._type != 'X'

    def get_score_modifier(self) -> int:
        """Restituisce il modificatore di punteggio associato al tipo di cella."""
        if self._type == 'T': return -5
        if self._type == 'R': return 10
        if self._type == 'O': return 20
        return 0

    @property
    def type(self) -> str:
        return self._type

    @property
    def position(self) -> tuple[int, int]:
        return self._row, self._col

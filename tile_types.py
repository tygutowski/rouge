from typing import Tuple

import numpy as np

class Color:
    ROUGE = (204,  66,  94)
    HEART = (135,  53,  85)
    DARK =  ( 31,  16,  42)
    FLOOR = ( 74,  48,  82)
    WALL =  (166, 133, 159)

graphic_dt = np.dtype(
    [
        ('ch', np.int32), # Unicode codepoint
        ('fg',     '3B'), # 3 unsigned bytes (RGB)
        ('bg',     '3B'),
    ]
)

tile_dt = np.dtype(
    [
        ('walkable',    np.bool_),  # true if this tile can be walked over.
        ('transparent', np.bool_),  # true if this tile doesn't block FOV.
        ('dark',        graphic_dt),  # graphics for when this tile is not in FOV.
        ('light',       graphic_dt),
    ]
)

def new_tile(
    *, # force keywords
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

SHROUD = np.array((ord(' '), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(' '), Color.FLOOR, tuple(subpixel/4 for subpixel in Color.FLOOR)),
    light=(ord(' '), Color.FLOOR, tuple(subpixel/2 for subpixel in Color.FLOOR)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(' '), Color.WALL, tuple(subpixel/4 for subpixel in Color.WALL)),
    light=(ord(' '), Color.WALL, tuple(subpixel/2 for subpixel in Color.WALL)),
)
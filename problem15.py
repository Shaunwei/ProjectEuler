#!/usr/bin/python
#! -*- coding: utf-8 -*-
__author__ = 'shaunwei'
"""
Lattice paths
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

solution thinking:
to finish all moves, if is a 2x2 grid.
The program needs to do `2 rights and 2 down` in any order.
It's not a permutation. but we could do permutation then remove the same(very slow)

solution2:
r r d d
r d r d
r d d r
d r r d
d r d r
d d r r
"""
GRID_SIZE = [20, 20]


def get_lattice_paths(grid_size):
    def rec_path(grid_siz):
        if grid_siz == [0, 0]:
            return 1

        paths = 0
        if grid_siz[0] > 0:
            paths += rec_path([grid_siz[0]-1, grid_siz[1]])
        if grid_siz[1] > 0:
            paths += rec_path([grid_siz[0], grid_siz[1]-1])
        return paths
    return rec_path(grid_size)



if __name__ == '__main__':
    assert 6 == get_lattice_paths([2, 2]), '2x2 grid has 6 paths'
    print(get_lattice_paths(GRID_SIZE)) # this will take fowever

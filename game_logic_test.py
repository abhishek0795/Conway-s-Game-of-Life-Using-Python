""" Implementing the test cases of the game. """

import grid # importing the required classes to run this test cases functions.

def test_create_grid():
    """ Creating the grid by passing the matrix values """
    matrix = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]
    A = grid.Grid(matrix)
    assert A.life_grid == matrix


def test_is_alive():
    """ Testing the alive conditions of the neighbours. """
    matrix = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]
    A = grid.Grid(matrix)
    assert A.is_alive(1, 1)
    assert not A.is_alive(0, 0)
    assert not A.is_alive(2, 1)


def test_get_neighbours():
    """ Testing the get neighbours details in the grid. """
    matrix = [[0, 0, 0], [1, 1, 1], [1, 0, 0]]
    A = grid.Grid(matrix)
    """ for the cell in the middle """
    assert A.get_neighbours(1, 1) == 3
    """ for the left edge """
    assert A.get_neighbours(1, 0) == 2
    """ for the right edge """
    assert A.get_neighbours(1, 2) == 1
    """ for the top edge """
    assert A.get_neighbours(0, 1) == 3
    """ for the bottom edge """
    assert A.get_neighbours(2, 1) == 4
    """ for the top left corner """
    assert A.get_neighbours(0, 0) == 2
    """ for the top right corner """
    assert A.get_neighbours(0, 2) == 2
    """ for the bottom left corner """
    assert A.get_neighbours(2, 0) == 2
    """ for the bottom right corner """
    assert A.get_neighbours(2, 2) == 2 


def test_kill_cell():
    """ Testing the dead cells details in the grid. """
    matrix = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]
    A = grid.Grid(matrix)
    A.kill_cell(1, 1)
    assert not A.is_alive(1, 1)
    A.kill_cell(2, 0)
    assert not A.is_alive(2, 0)


def test_birth_cell():
    """ Testing the birth cells details in the grid. """
    matrix = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]
    A = grid.Grid(matrix)
    A.birth_cell(0, 0)
    assert A.is_alive(0, 0)
    A.birth_cell(0, 2)
    assert A.is_alive(0, 2)


def test_size():
    """ Testing the size of the matrix value in the grid. """
    matrix = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]
    A=grid.Grid(matrix)
    assert A.size() == 3


def test_grid_as_array():
    """ Testing the whether the size of the grid is similar to the length matrix passed in the grid class. """
    matrix = [[0, 0, 0], [0, 1, 1], [1, 0, 0]]
    A=grid.Grid(matrix)
    assert len(A.grid_as_array()) == len(matrix)


def test_apply_rules():
    """ Testing all applied game rules is working in terms of live and dead cells. """
    matrix = [[0, 0, 0], [1, 1, 1], [1, 0, 0]]
    A=grid.Grid(matrix)
    assert A.is_alive(1, 2)
    assert not A.is_alive(0, 1)
   

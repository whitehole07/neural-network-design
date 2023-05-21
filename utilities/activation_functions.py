__all__ = ["hardlim", "hardlims"]

import numpy as np


def hardlim(x):
    """
    The hardlim activation function returns 1 if the input is greater than or equal to 0,
    and 0 otherwise.

    Parameters:
    x (np.ndarray): The input to the function

    Returns:
    (np.ndarray): The output of the function, either 1 or 0
    """
    return np.where(x >= 0, 1, 0)


def hardlims(x):
    """
    The symmetrical hardlim activation function returns 1 if the input is greater than or equal to 0,
    and -1 otherwise.

    Parameters:
    x (np.ndarray): The input to the function

    Returns:
    (np.ndarray): The output of the function, either 1 or -1
    """
    return np.where(x >= 0, 1, -1)

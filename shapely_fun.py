#!/usr/bin/env python

"""Find the shapely value for members of a colation, either exactly or with a monte-carlo approximation."""
# The shapely value for each player is the marginal value added by the player for joining the coalition,
# averaged over all possible permutaions of players joining. Since the number of permutations is the
# factorial of the number of players, unless the number of players is small we will have to settle for an approximate
# solution based on a random subset

from itertools import permutations
from collections import defaultdict
from random import shuffle
from fractions import Fraction


def exact(players, fun):
    """Find the exact shapely values. Players is an iterable, fun is a function that takes a tuple
       of players as its parameter and returns a dict of values for that permutation."""
    values = {}
    count = 0
    for perm in permutations(players):
        val = fun(perm)
        count += 1
        for player in val:
            if player in values:
                values[player] += val[player]
            else:
                values[player] = val[player]
    for player in players:
        values[player] /= count
    return values

def exact_fraction(players, fun):
    """Same as exact, except it retruns values as fractions rather than floats.
       The value function should always return integer values for this to be even remotely useful.
    """
    values = defaultdict(int)
    count = 0
    for perm in permutations(players):
        val = fun(perm)
        count += 1
        for player in val:
            values[player] += val[player]
    for player in players:
        values[player] = Fraction(values[player], count)
    return dict(values)


def monte_carlo(players, fun, num):
    """Find the monte carlo approximation using n tries. """
    values = {}
    count = 0
    perm = list(players)
    for ii in range(num):
        shuffle(perm)
        val = fun(perm)
        count += 1
        for player in val:
            if player in values:
                values[player] += val[player]
            else:
                values[player] = val[player]
    for player in players:
        values[player] /= count
    return values

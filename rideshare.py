#!/usr/bin/env python
""" Example shapely problem from 
https://www.reddit.com/r/GAMETHEORY/comments/zyezjl/i_have_the_formula_i_just_need_some_help_with_the/
The players are sharing a giant taxi. Each player is identified by an integer, which is also the distance along the
road he lives from the bar. The taxi value (cost) is the total miles driven, so the marginal value (cost) for each 
player joining is zero if a higher valued player has joined already, or the players value minus the current value.
"""

from shapely_fun import exact, exact_fraction, monte_carlo

def rideshare_vals(perm):
    sofar = 0
    vals = {}
    for player in perm:
        if player > sofar:
            vals[player] = player - sofar
            sofar = player
        else:
            vals[player] = 0
    return vals



if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--players', type=int, help="number of players")
    parser.add_argument('--exact', help="Find exact solution", action="store_true")
    parser.add_argument('--fraction', help="Find fraction solution", action="store_true")
    parser.add_argument('--monte-carlo', help="Iterations for Monte Carlo approximation", type=int, default=None, dest="monte_carlo")
    args = parser.parse_args()
    if args.exact:
        players = [player for player in range(1, args.players + 1)]
        print(exact(players, rideshare_vals))
    if args.fraction:
        players = [player for player in range(1, args.players + 1)]
        print(exact_fraction(players, rideshare_vals))
    if args.monte_carlo:
        players = [player for player in range(1, args.players + 1)]
        print(monte_carlo(players, rideshare_vals, args.monte_carlo))

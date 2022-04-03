from itertools import combinations
from scipy.special import binom

def solution(num_buns, num_required):
    """ Solution to the Google Foobar Challenge "Free the Bunny Workers".
    An enumeration for the different num_required is performed.
    """
    # Two trivial cases: num_required = 1 and num_required == num_buns
    if num_required == 1:
        return [[0] for _ in range(num_buns)]
    elif num_required == num_buns:
        return [[i] for i in range(num_buns)]
    elif num_required == 2:
        # For this case, the number of keys per bunny is
        # equals to num_buns and from the total list of keys

        # The bunny distribution
        bunny_dist = list()

        # We move backward for the lexicographical ordering
        for i in range(num_buns - 1, -1, -1):
            # for each bunny one different key is removed
            bunny_keys = [j for j in range(num_buns) if j != i]
            bunny_dist.append(bunny_keys)

        return bunny_dist

def test_solution(bunny_dist, num_buns, num_required, verbose=False):
    """ We verify that the bunny keys distribution is OK by performing all the
    unions of the num_required - 1 bunnies and union of num_required bunnies
    """
    # Convert list to set
    bunny_dist = [set(bunny) for bunny in bunny_dist]

    # Print the solution
    if verbose: print(f'Testing solution({num_buns:d}, {num_required:d}) = ', bunny_dist)

    # Retrieve number of keys - +1 for the 0 beginning index of python
    num_keys = max([max(tmp_list) for tmp_list in bunny_dist]) + 1
    total_keys = set(range(num_keys))

    # All combinations of nr among nb
    all_combinations_nr = combinations(list(range(num_buns)), num_required)
    # All combinations of nr - 1 among nb
    all_combinations_nrm1 = combinations(list(range(num_buns)), num_required - 1)

    # Check that all the nr unions make indeed the total number of keys
    for comb in all_combinations_nr:
        nr_total_keys = set()
        for bunny_id in comb:
            nr_total_keys = nr_total_keys | bunny_dist[bunny_id]
        if nr_total_keys != total_keys:
            if verbose: print("The union of nr combination ", comb, " of keys ", nr_total_keys, " does not yield the total number of keys")
            return False
    if verbose: print('---> All nr-size combinations are equal to the total number of keys')

    # Check that all the nr - 1 unions make indeed the total number of keys
    for comb in all_combinations_nrm1:
        nr_total_keys = set()
        for bunny_id in comb:
            nr_total_keys = nr_total_keys | bunny_dist[bunny_id]
        if nr_total_keys == total_keys:
            if verbose: print("The union of (nr - 1) combination ", comb, " of keys yield the total number of keys")
            return False
    if verbose: print('---> All (nr-1)-size combinations are not equal to the total number of keys\n')
    return True

def opposite_dist(bunny_dist):
    """ Opposite distribution of keys \bar{D} = {K / d_i for d_i in D} """
    # Retrieve number of keys - +1 for the 0 beginning index of python
    num_keys = max([max(tmp_list) for tmp_list in bunny_dist]) + 1
    total_keys = set(range(num_keys))
    opp_dist = [total_keys.difference(set(tmp_dist)) for tmp_dist in bunny_dist]
    return opp_dist

def test_opp_solution(bunny_dist, num_buns, num_required, verbose=False):
    """ We verify that the opposite bunny keys distribution is OK by performing all the
    intersections of the num_required - 1 bunnies and union of num_required bunnies
    """
    # Print the solution
    if verbose: print(f'Testing opposite solution({num_buns:d}, {num_required:d}) = ', bunny_dist)

    # All combinations of nr among nb
    all_combinations_nr = combinations(list(range(num_buns)), num_required)
    # All combinations of nr - 1 among nb
    all_combinations_nrm1 = combinations(list(range(num_buns)), num_required - 1)

    # Retrieve number of keys - +1 for the 0 beginning index of python
    num_keys = max([max(tmp_list) for tmp_list in bunny_dist]) + 1
    total_keys = set(range(num_keys))

    # Check that all the nr intersections make indeed the total number of keys
    for comb in all_combinations_nr:
        nr_total_keys = total_keys
        for bunny_id in comb:
            nr_total_keys = nr_total_keys & bunny_dist[bunny_id]
        if nr_total_keys != set():
            if verbose: print("The intersection of nr combination ", comb, " of keys ", nr_total_keys, " does not yield the empty set")
            return
    if verbose: print('---> All nr-size combinations are equal to the empty set')

    # Check that all the nr - 1 intersections make indeed the empty set
    for comb in all_combinations_nrm1:
        nr_total_keys = total_keys
        for bunny_id in comb:
            nr_total_keys = nr_total_keys & bunny_dist[bunny_id]
        if nr_total_keys == set():
            if verbose: print("The intersection of (nr - 1) combination ", comb, " of keys yield the empty set")
            return
    if verbose: print('---> All (nr-1)-size combinations are not equal to the empty set\n')
    return True

def wrapper(num_buns, num_required):
    """ Wrapper for getting solution and testing it. """
    bunny_dist = solution(num_buns, num_required)
    test_solution(bunny_dist, num_buns, num_required)

def test_combinations(num_buns, num_required, num_keys, num_keys_bunny):
    """ Test all opposite combinations of num_keys_bunny among num_keys
    for the num_buns, num_required input."""
    num_keys_bunny_opp = num_keys - num_keys_bunny

     # All combinations of nr among nb
    all_keys_combinations = list(combinations(list(range(num_keys)), num_keys_bunny))
    n_keys_combs = len(all_keys_combinations)

    # Print information
    print(f'Searching for solution({num_buns:d}, {num_required:d}) '
        f'using {num_keys:d} keys and {num_keys_bunny} keys per bunny, {num_keys_bunny_opp} keys per opp bunny')
    print(f'There are {n_keys_combs} combinations of keys')

    # Bunny combinations
    all_bunnies_combs = combinations(list(range(n_keys_combs)), num_buns)
    print(f'There are {int(binom(n_keys_combs, num_buns)):d} bunny combinations of {num_buns:d} bunnies')
    for bunny_comb in all_bunnies_combs:
        tmp_dist = [all_keys_combinations[i] for i in bunny_comb]
        tmp_opp_dist = opposite_dist(tmp_dist)
        if test_opp_solution(tmp_opp_dist, num_buns, num_required):
            test_opp_solution(tmp_opp_dist, num_buns, num_required, verbose=True)


if __name__ == '__main__':
    # Some testing
    wrapper(3, 1)
    wrapper(2, 2)
    wrapper(3, 2)
    wrapper(4, 2)

    # The (5, 3) solution given in the problem presentation
    solution_5_3 = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 6, 7, 8], [0, 3, 4, 6, 7, 9], [1, 3, 5, 6, 8, 9], [2, 4, 5, 7, 8, 9]]
    test_solution(solution_5_3, 5, 3)
    test_opp_solution(opposite_dist(solution_5_3), 5, 3)

    # Manual testing for (4, 3)
    test_combinations(4, 3, 4, 2)
    test_combinations(4, 3, 6, 3)

    # Manual testing for (5, 3)
    test_combinations(4, 3, 5, 3)
    test_combinations(4, 3, 10, 6)
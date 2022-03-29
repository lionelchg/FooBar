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

def test_solution(bunny_dist, num_buns, num_required):
    """ We verify that the bunny keys distribution is OK by performing all the
    unions of the num_required - 1 bunnies and union of num_required bunnies
    """
    # Print the solution
    print(f'Testing solution({num_buns:d}, {num_required:d}) = ', bunny_dist)

    # Retrieve number of keys - +1 for the 0 beginning index of python
    num_keys = max([max(tmp_list) for tmp_list in bunny_dist]) + 1
    total_keys = set(range(num_keys))

    from itertools import combinations
    # All combinations of nr among nb
    all_combinations_nr = combinations(list(range(num_buns)), num_required)
    # All combinations of nr - 1 among nb
    all_combinations_nrm1 = combinations(list(range(num_buns)), num_required - 1)

    # Check that all the nr unions make indeed the total number of keys
    for comb in all_combinations_nr:
        nr_total_keys = list()
        for bunny_id in comb:
            nr_total_keys += bunny_dist[bunny_id]
        # Sort and Convert list to set to remove duplicates
        nr_total_keys.sort()
        nr_total_keys = set(nr_total_keys)
        if nr_total_keys != total_keys:
            raise ValueError("The union of nr combination ", comb, " of keys ", nr_total_keys, " does not yield the total number of keys")
    print('All nr-size combinations are equal to the total number of keys')

    # Check that all the nr - 1 unions make indeed the total number of keys
    for comb in all_combinations_nrm1:
        nr_total_keys = list()
        for bunny_id in comb:
            nr_total_keys += bunny_dist[bunny_id]
        # Sort and Convert list to set to remove duplicates
        nr_total_keys.sort()
        nr_total_keys = set(nr_total_keys)
        if nr_total_keys == total_keys:
            raise ValueError("The union of (nr - 1) combination ", comb, " of keys yield the total number of keys")
    print('All (nr-1)-size combinations are not equal to the total number of keys\n')

def wrapper(num_buns, num_required):
    """ Wrapper for getting solution and testing it. """
    bunny_dist = solution(num_buns, num_required)
    test_solution(bunny_dist, num_buns, num_required)

if __name__ == '__main__':
    # Some testing
    wrapper(3, 1)
    wrapper(2, 2)
    wrapper(3, 2)
    wrapper(4, 2)

    # Manual testing
    test_solution([[0, 1, 2, 3], [2, 3, 4, 5], [4, 5, 6, 7], [0, 1, 6, 7]], 4, 3)
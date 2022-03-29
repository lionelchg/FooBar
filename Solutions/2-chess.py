
def solution(src, dest):
    #Your code here

    def convert(n):
        """ Convert from single identifier
        to tuple in chess grid """
        return (n // 8, n % 8)

    def construct_neighbors(center):
        """ Construct the list of neighbors from
        the center at a 1-knight distance (given as a tuple) """
        # Retrieve the starting point
        i_center = center[0]
        j_center = center[1]
        # Create the list of possible 8 neighbors
        list_i = [1, 1, -1, -1, 2, 2, -2, -2]
        list_j = [2, -2, 2, -2, 1, -1, 1, -1]
        # Filter the list for valid coordinates
        list_1neighbors = [(i_center + i, j_center + j) for i, j in zip(list_i, list_j)
            if i_center + i >= 0 and j_center + j >= 0]
        return list_1neighbors

    src_tuple = convert(src)
    dest_tuple = convert(dest)
    nsrc_dest = 0
    list_neighbors = [src_tuple]
    while not dest_tuple in list_neighbors:
        nsrc_dest += 1
        next_list_neighbors = []
        for square in list_neighbors:
            next_list_neighbors += construct_neighbors(square)
        list_neighbors = list(set(next_list_neighbors))

    return nsrc_dest

print(solution(0, 1))
print(solution(19, 36))
print(solution(0, 18))
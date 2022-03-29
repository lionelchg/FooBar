def solution(l):
    """ Solution to the Google Foobar Challenge "Find the access codes".
    This solution is of complexity O(n^2). The lucky triples are find only
    using two loops by counting the nnumber of divisors of each item
    of the list.
    """
    # c counts the number of divisors of each
    # item of the list
    c = [0] * len(l)
    count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count

def better_solution(l):
    n = len(l)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            # We loop on k only if l[j] is a divisor of l[i]
            if l[j] % l[i] == 0:
                for k in range(j + 1, n):
                    if l[k] % l[j] == 0:
                        count += 1
    return count

def brut_force_solution(l):
    # Your code here
    n = len(l)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if l[j] % l[i] == 0 and l[k] % l[j] == 0:
                    count += 1
    return count

if __name__ == '__main__':
    print(solution([1, 1, 1]))
    print(solution([1, 2, 3, 4, 5, 6]))
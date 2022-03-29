def XOR(n):
    """ Special property of the XOR sum as the same pattern repeats."""
    val = n % 4
    if val == 0:
        return n
    if val == 1:
        return 1
    if val == 2:
        return n + 1
    return 0

def solution(start, length):
    if length == 1:
        return start
    val = XOR(start + 2*(length-1))
    if start > 1:
        val = val ^ XOR(start - 1)
    for i in range(2, length):
        elems = length - i
        init = start + length*i - 1
        val = val ^ XOR(init + elems) ^ XOR(init)

    return val

print(solution(0, 3))
print(solution(17, 4))
print(solution(2000000000, 1))
print(solution(2000000000, 2))

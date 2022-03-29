def solution(s):
    # Your code here
    def findDivisors(n) :
        i = 1
        divisors = []
        while i <= n :
            if (n % i==0) :
                divisors.append(i)
            i = i + 1
        return divisors

    n = len(s)
    factors = findDivisors(n)
    nparts_min = n
    for factor in factors[::-1]:
        ref_seq = s[:factor]
        nparts = int(n / factor)
        find_diff = False
        for i in range(1, nparts):
            if ref_seq != s[i * factor: (i+1) * factor]:
                find_diff = True
        if not find_diff: nparts_min = factor
    return int(n / nparts_min)

test1 = "abcabcabcabc"
test2 = "abccbaabccba"
test3 = "abcabcabcabcaba"


print(solution(test1))
print(solution(test2))
print(solution(test3))


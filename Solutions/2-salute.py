def solution(s):
    nsalutes = 0
    for ichar, char in enumerate(s):
        if char == '>':
            tmp_str = s[ichar:]
            nsalutes += tmp_str.count('<')
    return nsalutes * 2

test1 = "--->-><-><-->-"
test2 = ">----<"
test3 = "<<>><"

print(solution(test1))
print(solution(test2))
print(solution(test3))
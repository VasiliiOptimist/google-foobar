def solution(l):
    left_dividers = [0] * len(l)
    if l[1] % l[0] == 0:
        left_dividers[1] += 1
    magic_triples = 0
    for i in range(2, len(l)):
        for j in range(i - 1, -1, -1):
            if l[i] % l[j] == 0:
                magic_triples += left_dividers[j]
                left_dividers[i] += 1
    return magic_triples

from collections import defaultdict


def use_sieve_of_eratosthenes(num):
    flags = [1] * (num + 1)
    for i in range(2, int(num**0.5) + 1):
        if flags[i]:
            for j in range(i**2, num + 1, i):
                flags[j] = 0
    return [i for i in range(2, len(flags)) if flags[i]]


def factorize(num):
    res = defaultdict(int)
    prime_nums = use_sieve_of_eratosthenes(int(num) + 1)
    i = 0
    div = prime_nums[i]
    while num > 1:
        while num % div == 0:
            res[div] += 1
            num //= div
        i += 1
        if i == len(prime_nums):
            break
        div = prime_nums[i]
    return res


def find_pairs_same(list_num):
    if list_num is None or len(list_num) == 1:
        return 0

    return len(list_num) * (len(list_num) - 1) // 2


def find_pairs_different(list_num1, list_num2):
    if list_num1 is None or list_num2 is None:
        return 0
    # [0, 1, 4] [2, 5]
    res = 0
    for ind1 in list_num1:
        step = 0
        for ind2 in list_num2:
            if ind2 > ind1:
                res += len(list_num2) - step
                break
            step += 1
    return res


def solution(l):
    ls = defaultdict(list)
    ls[l[0]] += [0]
    ls[l[1]] += [1]
    magic_triples = 0
    for i in range(2, len(l)):
        factorization = factorize(l[i])
        # keys = list(factorization.keys())
        # if ls.get(1) and len(ls.get(1)) > 1:
        #     magic_triples += find_pairs_same(ls.get(1))
        # for j in range(len(keys)):
        #     if factorization[keys[j]] > 1:
        #         magic_triples += find_pairs_same(ls.get(keys[j]))

        #     if ls.get(1):
        #         magic_triples += find_pairs_different(
        #             ls.get(1), ls.get(keys[j]))

        #     for k in range(j + 1, len(keys)):
        #         if keys[k] % keys[j] == 0:
        #             magic_triples += find_pairs_different(
        #                 ls.get(keys[j]), ls.get(keys[k]))

        ls[l[i]].extend([i])

    return magic_triples


print(solution([1000000]*200))

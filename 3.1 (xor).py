import math

def calculate_xor_sum(num):
    if num == 0:
        return 0

    len_binary = math.ceil(math.log(num, 2))

    # if num == 2**len_binary:
    #     binary_xor_sum =  [0] * len_binary + [1]
    # else:
    if num // 2 % 2 == 0:
        binary_xor_sum = [(0 if num % 2 == 0 else 1)]
    else:
        binary_xor_sum = [(1 if num % 2 == 0 else 0)]

    for i in range(1, len_binary):
        digit_position = num % (2**(i + 1))
        if digit_position < 2**i:
            binary_xor_sum.append(0)
        else:
            binary_xor_sum.append((0 if digit_position % 2 == 1 else 1))

    if num == 2**len_binary:
        binary_xor_sum.append(1)
        
    return sum([binary_xor_sum[i] * 2**i for i in range(len(binary_xor_sum))])


def solution(start, length):
    mas = []
    xor_sum = 0
    for row in range(length):
        # print(start + row * length, start + row * length + length - row - 1)
        first = start + row * length
        rest = calculate_xor_sum(start + row * length + length - row - 1) ^ calculate_xor_sum(start + row * length)
        xor_sum ^= first ^ rest
        # print(xor_sum)

    return xor_sum

print(solution(17, 4))
# 0 1 2 /
# 3 4 / 5
# 6 / 7 8
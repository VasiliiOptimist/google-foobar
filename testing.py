def sum_dig(num):
    q = 0
    while num>0:
        q+=num%10
        num //= 10
    return q
        
cnt = 0
for num in range(1987654321 // 8):
    n = num
    n_2 = bin(n)[2:]
    for i in range(3):
        if sum_dig(int(n_2, 2))%2==0:
            n_2 = n_2 + "0"
        else:
            n_2 = n_2 + "1"
    if 123456789 <= int(n_2,2) <= 1987654321:
        cnt += 1
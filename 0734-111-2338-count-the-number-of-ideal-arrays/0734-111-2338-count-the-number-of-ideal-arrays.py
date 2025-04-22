MOD = 10**9 + 7
MAX_N = 10**4 + 10
MAX_P = 15

sieve = [0] * MAX_N
for i in range(2, MAX_N):
    if sieve[i] == 0:
        for j in range(i, MAX_N, i):
            sieve[j] = i

prime_exponents = [[] for _ in range(MAX_N)]
for i in range(2, MAX_N):
    x = i
    while x > 1:
        p = sieve[x]
        count = 0
        while x % p == 0:
            x //= p
            count += 1
        prime_exponents[i].append(count)

combinations = [[0] * (MAX_P + 1) for _ in range(MAX_N + MAX_P)]
combinations[0][0] = 1
for i in range(1, MAX_N + MAX_P):
    combinations[i][0] = 1
    for j in range(1, min(i, MAX_P) + 1):
        combinations[i][j] = (combinations[i - 1][j] + combinations[i - 1][j - 1]) % MOD

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        total = 0
        for x in range(1, maxValue + 1):
            ways = 1
            for exponent in prime_exponents[x]:
                ways = ways * combinations[n + exponent - 1][exponent] % MOD
            total = (total + ways) % MOD
        return total

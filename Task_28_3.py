def solve_hanoi_tower(discs):
    if discs == 0: return 0
    hm = 1
    for i in range(2, discs + 1):
        hm = 2 * hm + 1
    return hm
discs = int(input())
print(solve_hanoi_tower(discs))
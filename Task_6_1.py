numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def to_dec(rom):
    dec = 0
    for i, r in numbers:
        while rom.startswith(r):
            dec += i
            rom = rom[len(r):]
    return dec
print(str(to_dec("MMXXIII")))
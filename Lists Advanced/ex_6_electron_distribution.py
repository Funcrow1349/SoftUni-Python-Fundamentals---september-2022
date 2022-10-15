number_of_electrons = int(input())
electrons_left = number_of_electrons
shells = []
for shell in range(1, number_of_electrons + 1):
    if electrons_left <= 0:
        break
    shells.append(2 * (shell ** 2))
    electrons_left -= (2 * (shell ** 2))
shells[-1] -= abs(electrons_left)

print(shells)
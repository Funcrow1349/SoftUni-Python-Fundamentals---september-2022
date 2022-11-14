tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    first_half = ticket[:10]
    second_half = ticket[10:]
    winning = False
    for repetitions in range(10, 5, -1):
        if winning:
            break
        for symbol in first_half:
            if (symbol * repetitions) in first_half and (symbol * repetitions) in second_half and symbol in ['@','#','$','^']:
                if repetitions == 10:
                    print(f'ticket "{ticket}" - {repetitions}{symbol} Jackpot!')
                    winning = True
                    break
                else:
                    print(f'ticket "{ticket}" - {repetitions}{symbol}')
                    winning = True
                    break
    if not winning:
        print(f'ticket "{ticket}" - no match')
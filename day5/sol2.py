def get_seat_number(seat):
    row = int(''.join(['0' if c == 'F' else '1' for c in seat[0:7]]), base=2)
    col = int(''.join(['0' if c == 'L' else '1' for c in seat[7:]]), base=2)
    return row * 8 + col


with open('input.txt', 'r') as f:
    seats = [get_seat_number(seat.strip()) for seat in f.readlines()]
    seats = sorted(seats)
    i = 0
    while i < len(seats) - 1:
        if (seats[i + 1]) != seats[i] + 1:
            print(i, seats[i] + 1)
            break
        i += 1
        

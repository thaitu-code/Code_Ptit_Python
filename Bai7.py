import sys


class Customer:
    def __init__(self, c_id, name, old_idx, new_idx):
        self.id_str = f"KH{c_id:02d}"
        self.name = name.strip()
        self.usage = new_idx - old_idx

        base_cost = 0
        surcharge_rate = 0.0

        if self.usage <= 50:
            base_cost = self.usage * 100
            surcharge_rate = 0.02
        elif self.usage <= 100:
            base_cost = 50 * 100 + (self.usage - 50) * 150
            surcharge_rate = 0.03
        else:
            base_cost = 50 * 100 + 50 * 150 + (self.usage - 100) * 200
            surcharge_rate = 0.05
        total = base_cost * (1 + surcharge_rate)
        self.final_total = int(total + 0.5)


def solve():
    input_data = sys.stdin.read().splitlines()

    lines = [line for line in input_data if line.strip()]
    if not lines:
        return

    n = int(lines[0].strip())
    customers = []

    line_idx = 1
    for i in range(1, n + 1):
        if line_idx >= len(lines):
            break

        name = lines[line_idx]
        old_idx = int(lines[line_idx + 1])
        new_idx = int(lines[line_idx + 2])

        customers.append(Customer(i, name, old_idx, new_idx))
        line_idx += 3
    customers.sort(key=lambda x: (-x.final_total, x.id_str))

    for c in customers:
        print(f"{c.id_str} {c.name} {c.final_total}")


if __name__ == '__main__':
    solve()
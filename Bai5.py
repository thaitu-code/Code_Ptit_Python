import sys


def solve():
    input_data = sys.stdin.read().splitlines()

    lines = [line.strip() for line in input_data if line.strip()]
    if not lines:
        return

    n = int(lines[0])

    stations = {}

    line_idx = 1
    for _ in range(n):
        if line_idx >= len(lines):
            break

        name = lines[line_idx]
        start_time = lines[line_idx + 1]
        end_time = lines[line_idx + 2]
        rainfall = float(lines[line_idx + 3])
        line_idx += 4

        start_h, start_m = map(int, start_time.split(':'))
        end_h, end_m = map(int, end_time.split(':'))

        duration = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        if duration < 0:
            duration += 24 * 60
        if name not in stations:
            stations[name] = {'total_time': 0, 'total_amount': 0.0}

        stations[name]['total_time'] += duration
        stations[name]['total_amount'] += rainfall

    idx = 1
    for name, data in stations.items():
        if data['total_time'] > 0:
            avg_rainfall = (data['total_amount'] / data['total_time']) * 60
        else:
            avg_rainfall = 0.0

        station_id = f"T{idx:02d}"
        print(f"{station_id} {name} {avg_rainfall:.2f}")
        idx += 1


if __name__ == '__main__':
    solve()
import sys


class Student:
    def __init__(self, st_id, name, scores):
        self.original_id = st_id
        self.id_str = f"HS{st_id:02d}"
        self.name = name.strip()

        total_score = scores[0] * 2 + scores[1] * 2 + sum(scores[2:])

        self.avg = round((total_score / 12) + 0.0001, 1)

        # Xếp loại
        if self.avg >= 9.0:
            self.rank = "XUAT SAC"
        elif self.avg >= 8.0:
            self.rank = "GIOI"
        elif self.avg >= 7.0:
            self.rank = "KHA"
        elif self.avg >= 5.0:
            self.rank = "TB"
        else:
            self.rank = "YEU"


def solve():
    input_data = sys.stdin.read().splitlines()

    lines = [line for line in input_data if line.strip()]
    if not lines:
        return

    n = int(lines[0].strip())
    students = []

    line_idx = 1
    for i in range(1, n + 1):
        if line_idx >= len(lines):
            break

        name = lines[line_idx]
        scores = list(map(float, lines[line_idx + 1].split()))

        students.append(Student(i, name, scores))
        line_idx += 2

    students.sort(key=lambda x: (-x.avg, x.original_id))

    for s in students:
        print(f"{s.id_str} {s.name} {s.avg:.1f} {s.rank}")


if __name__ == '__main__':
    solve()
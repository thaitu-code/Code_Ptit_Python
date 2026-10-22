import sys

input_data = sys.stdin.read().split()
if(input_data):
    se = set()
    for i in range(len(input_data)):
        se.add(int(input_data[i]) % 42)
    print(len(se))

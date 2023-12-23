# factors.py

import sys

def factorize(n):
    # Function to factorize a number into two smaller numbers
    for i in range(2, n):
        if n % i == 0:
            return i, n // i

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r") as file:
        for line in file:
            n = int(line.strip())
            p, q = factorize(n)
            print(f"{n}={p}*{q}")

# rsa.py

import sys

def is_prime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize_prime(n):
    # Function to factorize a number into two prime numbers
    for i in range(2, n):
        if n % i == 0 and is_prime(i) and is_prime(n // i):
            return i, n // i

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa.py <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r") as file:
        for line in file:
            n = int(line.strip())
            p, q = factorize_prime(n)
            print(f"{n}={p}*{q}")

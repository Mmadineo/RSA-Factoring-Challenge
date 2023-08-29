#!/usr/bin/python3

import sys

def factorize(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return i, n // i
        return None, None

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r') as file:
            for line in file:
                n = int(line.strip())
                p, q = factorize(n)
                if p is not None:
                    print(f"{n}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == "__main__":
    main()

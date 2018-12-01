def main():
    frequency = 0
    with open("input.txt") as input:
        for change in input:
            frequency += int(change)
    print(f"Answer to challenge #1: {frequency}")

if __name__ == "__main__":
    main()
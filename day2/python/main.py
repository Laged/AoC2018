def check_id(id):
    chars = set(id)
    counts = list(map(lambda char: id.count(char), chars))
    double = 2 in counts
    triple = 3 in counts
    return double, triple

def main():
    doubles = 0
    triples = 0
    with open("input.txt") as input:
        for id in input:
            double, triple = check_id(id.strip())
            if (double):
                doubles += 1
            if (triple):
                triples += 1
    checksum = doubles * triples
    print(f"Answer to challenge #1: {checksum}")

if __name__ == "__main__":
    main()
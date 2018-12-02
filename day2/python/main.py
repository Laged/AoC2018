import difflib

def check_id(id):
    chars = set(id)
    counts = list(map(lambda char: id.count(char), chars))
    double = 2 in counts
    triple = 3 in counts
    return double, triple

def match_result(id1, id2):
    if len(id1) != len(id2):
        return False
    different_chars = 0
    shared_chars = []
    for (index, char) in enumerate(list(id1)):
        if char != id2[index]:
            different_chars += 1
            if different_chars > 1:
                return None
        else:
            shared_chars += char
    if different_chars == 1:
        return "".join(shared_chars)
    return None

def main():
    doubles = 0
    triples = 0
    match_found = False
    with open("input.txt") as input:
        ids = [line.strip() for line in input]
        for id in ids:
            double, triple = check_id(id.strip())
            if (double):
                doubles += 1
            if (triple):
                triples += 1
            # Challenge 2
            if not match_found:
                matches = difflib.get_close_matches(id, ids, 2, 0.2)
                if matches:
                    result = match_result(id, matches[1])
                    if (result):
                        print(f"Answer to challenge #2: {result}")
                        match_found = True

    checksum = doubles * triples
    print(f"Answer to challenge #1: {checksum}")

if __name__ == "__main__":
    main()
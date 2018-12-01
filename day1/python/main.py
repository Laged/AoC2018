def main():
    frequency = 0
    calibrations = []
    calibration_missing = True
    calibration_count = 0
    calibration_limit = 300
    while calibration_missing:
        with open("input.txt") as input:
            for change in input:
                frequency += int(change)
                # Second answer is found after iterating for a while...
                if calibration_missing and frequency in calibrations:
                    print(f"Answer to challenge #2: {frequency}")
                    calibration_missing = False
                calibrations.append(frequency)
        # First answer is found after first iteration
        if calibration_count == 0:
            print(f"Answer to challenge #1: {frequency}")
            print(f"Running calibrations until {calibration_limit} to get answer #2, go get some coffee...")
        calibration_count += 1
        # Stop iteration if limit is hit
        if calibration_count == calibration_limit:
            calibration_missing = False
            print ("Ended calibration loop without finding duplicates")

if __name__ == "__main__":
    main()
import sys
import getopt

def run(path):
    code = []
    numpad = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))
    cur_loc = {"x": 1, "y": 1}

    with open(path, "r") as f:
        for line in f.read().split("\n"):
            for char in line:
                if char == "L":
                    if cur_loc["x"] != 0:
                        cur_loc["x"] -= 1
                elif char == "R":
                    if cur_loc["x"] != 2:
                        cur_loc["x"] += 1
                elif char == "U":
                    if cur_loc["y"] != 0:
                        cur_loc["y"] -= 1
                elif char == "D":
                    if cur_loc["y"] != 2:
                        cur_loc["y"] += 1
                else:
                    print(f'ERROR! {char} is not a valid input character')

            code.append(numpad[cur_loc["y"]][cur_loc["x"]])

    return "".join(code)


if __name__ == "__main__":
    path = "./input.txt"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "v", ["input="])
    except getopt.GetOptError:
        print('answer.py -v --input <inputfile>')
        sys.exit(2)
    
    verbose = False
    
    for opt, arg in opts:
        if opt == "-v":
            verbose = True
        elif opt == "--input":
            path = arg
    
    result = run(path)
    if verbose:
        print(f"Claire's secrect code is {result}! Get inside to run those tests quickly!")
    else:
        print(result)

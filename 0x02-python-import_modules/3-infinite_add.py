#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    whole = 0
    for g in range(len(sys.argv) - 1):
        whole += int(sys.argv[g + 1])
    print("{}".format(whole))

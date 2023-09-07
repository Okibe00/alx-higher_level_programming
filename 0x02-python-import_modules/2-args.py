#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len0 = len(sys.argv)
    if len0 - 1 == 0:
        print(f"{0} arguments.")
    elif len0 - 1 == 1:
        print(f"{1} argument:")
        print(f"{1}: {sys.argv[1]}")
    else:
        print(f"{len0 - 1} arguments:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")

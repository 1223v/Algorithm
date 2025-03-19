import sys

def main():
    sys.stdout.write("50 49\n")

    for i in range(49,0,-1):
        sys.stdout.write(f"{i} {i+1} -1\n")

if __name__  == "__main__":
    main()
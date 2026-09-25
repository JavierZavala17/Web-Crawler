import sys

def main():
    if len(sys.argv) < 2:
        print(f"no website provided")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print(f"too many arguments provided")
        sys.exit(1)
    else:
        base_url = sys.argv[1]
        print(f"starting crawl of: {base_url}")


if __name__ == "__main__":
    main()

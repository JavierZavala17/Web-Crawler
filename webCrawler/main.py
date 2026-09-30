import sys

from crawl import crawl_page


def main() -> None:
    args = sys.argv
    if len(args) < 2:
        print("no website provided")
        sys.exit(1)
    if len(args) > 2:
        print("too many arguments provided")
        sys.exit(1)

    base_url = args[1]

    print(f"starting crawl of: {base_url}...")

    data = crawl_page(base_url)
    print(f"Number of pages found: {len(data)}")
    for value in data.values():
        print(f"{value['url']}: {value['heading']}")

    sys.exit(0)


if __name__ == "__main__":
    main()

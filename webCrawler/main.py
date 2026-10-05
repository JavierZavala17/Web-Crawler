import asyncio
import sys

from crawl import crawl_site_async


async def main() -> None:
    args = sys.argv
    if len(args) != 4:
        print("Wrong number of arguments")
        sys.exit(1)

    base_url = args[1]
    max_concurrency = int(args[2])
    max_pages = int(args[3])

    print(f"starting crawl of: {base_url}...")

    page_data = await crawl_site_async(base_url, max_concurrency, max_pages)

    print(f"Found {len(page_data)} pages:")
    for page in page_data.values():
        print(f"Found {len(page['outgoing_links'])} outgoing links on {page['url']}")

    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())

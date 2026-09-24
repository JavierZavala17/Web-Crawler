from urllib.parse import urlsplit

def normalize_url(input_url: str) -> str:
    parsed_url = urlsplit(input_url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()


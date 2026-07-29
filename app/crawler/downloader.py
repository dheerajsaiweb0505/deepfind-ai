import requests


class Downloader:
    """
    Downloads HTML pages.
    """

    def __init__(self):
        self.headers = {
            "User-Agent": (
                "DeepFindAI/1.0 "
                "(https://github.com/dheerajsaiweb0505/deepfind-ai)"
            )
        }

    def download(self, url: str) -> str | None:
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=10,
            )

            if response.status_code != 200:
                print(f"Failed ({response.status_code}) : {url}")
                return None

            content_type = response.headers.get("Content-Type", "")

            if "text/html" not in content_type:
                print("Not an HTML page")
                return None

            return response.text

        except requests.RequestException as e:
            print(e)
            return None
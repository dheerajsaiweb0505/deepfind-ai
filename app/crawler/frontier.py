from collections import deque


class URLFrontier:
    """
    In-memory URL frontier using FIFO queue.
    This will later be replaced by Redis.
    """

    def __init__(self):
        self.queue = deque()
        self.visited = set()

    def add_url(self, url: str) -> bool:
        """
        Add a URL if it hasn't been seen before.

        Returns True if added, False if duplicate.
        """
        if url in self.visited:
            return False

        self.queue.append(url)
        self.visited.add(url)
        return True

    def get_next_url(self) -> str | None:
        """
        Return the next URL to crawl.
        """
        if not self.queue:
            return None

        return self.queue.popleft()

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def size(self) -> int:
        return len(self.queue)
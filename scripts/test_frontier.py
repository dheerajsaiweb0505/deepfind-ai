from app.crawler.frontier import URLFrontier

frontier = URLFrontier()

frontier.add_url("https://google.com")
frontier.add_url("https://github.com")
frontier.add_url("https://fastapi.tiangolo.com")

print(frontier.get_next_url())
print(frontier.get_next_url())

print(frontier.size())
import requests
def handler(event, context):
    r = requests.get(url='https://news.ycombinator.com/news')
    return {"content": r.text}

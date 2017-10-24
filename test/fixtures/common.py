from scrapy.http import Request, TextResponse


def file_as_response(filename, meta={}):
    from os import path
    current_dir = path.dirname(path.abspath(__file__))
    fullpath = path.join(current_dir, filename)
    with open(fullpath, 'r') as f:
        content = f.read()

    url = 'http://www.example.com'
    req = Request(url, meta=meta)
    return TextResponse(url, request=req, body=content)

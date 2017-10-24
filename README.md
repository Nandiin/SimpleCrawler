# SimpleCrawler

A simple web crawler developed upon [scrapy][scrapy] with some degree of extensibility.

## Brief Introduction

The crawler is able to handle this simplest use case:

- target webpages are linearly constructed, which means there is no need to crawl a subpage.
- given a webpage, it can be determined that whether the crawling process should continue.
- given a webpage, url to next page, if any, can be determined.

A sample parser which crawls basic project information from https://pro.lagou.com/project/kaifa is included in the source
(at `SimpleCrawler/cores/dakun.py`). Theoretically any module that conforms to following prototype would work.

- lays in the folder `cores`
- has a class `Page` in it
- the class `Page` can be constructed with a `scrapy.Response`
- the class `Page` should have a static variable `start_url` holds the url of starting page.
- An instance of class `Page` should have:
    - a `has_next` field indicates whether the crawling process should continue
    - a `next` field holds an url of next page, if any.
    - an `output` field holds a piece of record as `dict`
    

## Usage

```
scrapy crawl simple -a core=<website_parser_module> -o <output_file_name>.<json|cvs|jl|xml> [-L INFO]
```

`-L INFO` is to eliminate the verbose DEBUG logging, if the logging level is set to DEBUG(default value) all exports would be
logged.

`jl` stands for json line. The difference between `file.jl` and `file.json` can be briefly stated that `jl` file contains a bunch of json objects as seperate lines
while `json` joins them as an array of objects. `jl` file may be found convinent for incremental recording while 'json' is easy to read by existing json decoders.
[more information in scrapy docs][doc]


for example:
```
scrapy crawl simple -a core=dakun -o o.json -L INFO
```
`dakun` can be changed to any compatible parser.

[scrapy]: https://scrapy.org/
[doc]: https://docs.scrapy.org/en/latest/topics/feed-exports.html


# coding: utf-8


class Project():
    def __init__(self, response):
        self.name = response.xpath('h3/text()').extract_first()\
            .encode('utf-8')
        self.offer = response.xpath('div[@class="price"]/span/text()')\
            .extract_first().encode('utf-8')
        self.time = response.xpath('div[@class="time"]/div/text()')\
            .extract_first().encode('utf-8')
        self.url = response.xpath('@href')\
            .extract_first().encode('utf-8')
        self.status = response.xpath('div[@class="status"]/span/text()')\
            .extract_first().encode('utf-8')
        self.output = {
            'name': self.name, 'offer': self.offer, 'status': self.status,
            'time': self.time, 'url': self.url
        }


class Page():
    start_url = 'https://pro.lagou.com/project/kaifa'

    def __init__(self, response):
        projs = response.xpath('//div[@id="project_list"]//li/a')
        self.projects = [Project(proj) for proj in projs]

        paging_code = response.xpath('//script/text()')[-1].extract()

        import re
        p = r'pageId = "(\d+)".*pageSize = "(\d+)".*pageCount = "(\d+)"'
        result = re.search(p, paging_code, re.DOTALL)
        page_id = int(result.group(1))
        page_size = int(result.group(2))
        page_count = float(result.group(3))

        from math import ceil

        self.has_next = page_id < ceil(page_count / page_size)

        if self.has_next:
            self.next = "https://pro.lagou.com/project/kaifa/" + str(page_id+1)
        else:
            self.next = ''

        self.output = [p.output for p in self.projects]

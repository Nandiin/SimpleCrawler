# -*- coding: utf-8 -*-

import pytest
import unittest
from fixtures.common import file_as_response
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


def read_expected_pages():
    import json
    f = open('fixtures/pages.json')
    return json.load(f)

expected_pages = read_expected_pages()


@pytest.fixture(scope="class")
def pages(request):
    from cores.dakun import Page
    request.cls.pages = [(Page(file_as_response(filename)), expected)
                         for filename, expected in expected_pages.iteritems()]


@pytest.mark.usefixtures("pages")
class PageTest(unittest.TestCase):
    def test_start_url(self):
        from cores.dakun import Page
        assert Page.start_url == 'https://pro.lagou.com/project/kaifa'

    def test_has_next(self):
        for page, expected in self.pages:
            assert page.has_next == expected['has_next']

    def test_projects(self):
        projects = [(page.projects, expected["projects"])
                    for page, expected in self.pages]
        for p, e in projects:
            for i in range(len(p)):
                ProjectTest.test(p[i], e[i])

    def test_next(self):
        for page, expected in self.pages:
            assert page.next == expected['next']


class ProjectTest():
    @staticmethod
    def test(proj, expected):
        attributes = ['name', 'offer', 'time', 'url', 'status']
        for attr in attributes:
            assert getattr(proj, attr) == expected[attr].encode('utf-8')

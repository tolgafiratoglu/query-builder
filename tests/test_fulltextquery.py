# test_fulltextquery.py

from querybuilder.fulltextquery import FullTextQuery

def test_match():
    assert (FullTextQuery()).match("age", 42).get() == {'query': {'match': {'age': {"query": 42}}}}

def test_multimatch():
    assert (FullTextQuery()).multimatch(["price", "min_price"], 1000).get() == {'query': {'multi_match': {'fields': ['price', 'min_price'], 'query': 1000}}}
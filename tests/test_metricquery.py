# test_metricquery.py

from querybuilder.metricquery import MetricQuery
from querybuilder.query import Query

def test_avg():
    assert (MetricQuery()).avg("age", "my_result_field").get() == {"aggs": {"my_result_field": {"avg": {"field": "age"}}}}

def test_min():
    assert (MetricQuery()).min("price").get() == {"aggs": {"min_price": {"min": {"field": "price"}}}}

def test_sum():
    query = Query.match("active", True)
    assert (MetricQuery()).sum("visits", "sum_visits_field").setQuery(query).get() == {"query": {"match": {"active": True}},"aggs": {"sum_visits_field": {"sum": {"field": "visits"}}}}

def test_cardinality():
    assert (MetricQuery()).cardinality("type", "type_count").get() == {"aggs": {"type_count": {"cardinality": {"field": "type"}}}}


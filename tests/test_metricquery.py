# test_metricquery.py

from querybuilder.metricquery import MetricQuery
from querybuilder.fulltextquery import FullTextQuery

def test_avg():
    assert (MetricQuery()).avg("age", "my_result_field").get() == {"aggs": {"my_result_field": {"avg": {"field": "age"}}}}

def test_min():
    assert (MetricQuery()).min("price").get() == {"aggs": {"min_price": {"min": {"field": "price"}}}}

def test_sum():
    query = (FullTextQuery()).match("active", True).get()
    assert (MetricQuery()).sum("visits", "sum_visits_field").where(query).get() == {"query": {"match": {"active": {"query": True}}},"aggs": {"sum_visits_field": {"sum": {"field": "visits"}}}}

def test_cardinality():
    assert (MetricQuery()).cardinality("type", "type_count").get() == {"aggs": {"type_count": {"cardinality": {"field": "type"}}}}

def test_geo_bonds():
    assert (MetricQuery()).geo_bonds("location").get() == {"aggs": {"viewport": {"geo_bonds": {"field": "location"}}}}

def test_geo_centroid():
    assert (MetricQuery()).geo_centroid("location").get() == {"aggs": {"centroid": {"geo_centroid": {"field": "location"}}}}           

def test_boxplot():
    assert (MetricQuery()).boxplot("location", "boxplot_data").get() == {"aggs": {"boxplot_data": {"boxplot": {"field": "location"}}}, "size": 0}

def test_stats():
    assert (MetricQuery()).stats("visits", "my_visit_summary").get() == {"aggs": {"my_visit_summary": {"stats": {"field": "visits"}}}}        

def test_geo_line():
    assert (MetricQuery()).geo_line("location").get() == {'aggs': {'line': {'geo_line': {'point': {'field': 'location'}, 'sort': {'field': '@timestamp'}}}}}  
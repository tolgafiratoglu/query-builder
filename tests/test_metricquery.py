# test_metricquery.py

from querybuilder.metricquery import MetricQuery

def test_avg():
    assert MetricQuery.avg('age', 'avg_age') == '{"aggs": {"avg_age": {"avg": {"field": "age"}}}}'


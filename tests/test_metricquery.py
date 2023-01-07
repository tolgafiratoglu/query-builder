# test_metricquery.py

from querybuilder.metricquery import MetricQuery

def test_avg():
    assert MetricQuery.avg('age') == 'test'
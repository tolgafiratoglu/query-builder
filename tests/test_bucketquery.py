# test_metricquery.py

from querybuilder.bucketquery import BucketQuery
from querybuilder.metricquery import MetricQuery
from querybuilder.query import Query

def test_histogram():
    assert (BucketQuery()).histogram("price", 50, 10).get() == {'aggs': {'histogram_data': {'histogram': {'field': 'price', 'interval': 50, 'min_doc_count': 10}}}}

def test_range():
    ranges = [{"to": 100}, {"from": 100, "to": 200}, {"from": 200}]
    assert (BucketQuery()).range("price_ranges", ranges).get() == {'aggs': {'range_data': {'range': {'field': 'price_ranges', 'ranges': [{'to': 100}, {'from': 100, 'to': 200}, {'from': 200}]}}}}

def test_filter():
    avg_query = (MetricQuery()).avg("price").get()
    filter_query = (Query()).match("type", "shirt")
    assert (BucketQuery()).filter(avg_query, "only_shirts", filter_query).get() == {} # {'aggs': {'aggs': {'avg_price': {'avg': {'field': 'price'}}}}, 'only_shirts': {'aggs': {'aggs': {'avg_price': {'avg': {'field': 'price'}}}}, 'filter': {'aggs': {'avg_price': {'avg': {'field': 'price'}}}}}}
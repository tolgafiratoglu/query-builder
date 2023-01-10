<strong>Query Builder</strong> is a python library which builds Elasticsearch queries, including metric/bucket aggregations, full text queries and fuzzy logic queries. This is a practice project to understand capabilities of Elasticsearch and ease writing complex ES queries.

<h3>Metric Queries</h3>
Query Builder supports building metric Elasticsearch functions. 

```
(MetricQuery()).min("price").get()
```
This line outputs as follows: 
```
{"aggs": {"min_price": {"min": {"field": "price"}}}}
```

<h3>Testing of Library</h3>
If you want to add new test functionality to the library, you can test as follows:
<code>pytest</code>
<code>pytest -q tests/test_metricquery</code>
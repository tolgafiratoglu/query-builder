<strong>Query Builder</strong> is a python library which builds Elasticsearch queries, including metric/bucket aggregations, full text queries and fuzzy logic queries. This is a practice project to understand capabilities of Elasticsearch and ease writing complex ES queries.

<h3>Metric Queries</h3>
Query Builder supports building metric Elasticsearch functions. 
MetricQuery package has methods named {min, avg, sum, cardinality, geo_bonds, geo_centroid, boxplot, geo_line and stats} which all work as their Elasticsearch counterpart.

```
(MetricQuery()).min("price").get()
```
This line outputs as follows: 
```
{"aggs": {"min_price": {"min": {"field": "price"}}}}
```
You can use query within metric queries, as an example:
```
query = (FullTextQuery()).match("active", True).get()
es_query = (MetricQuery()).sum("visits", "sum_visits_field").where(query).get()
```
This outputs as follows:
```
{"query": {"match": {"active": {"query": True}}},"aggs": {"sum_visits_field": {"sum": {"field": "visits"}}}}
```
You don't have to use query methods of this package, you can add your custom query dictionary, if you prefer:
```
query = {"query": {"match": {"active": {"query": True}}}
es_query = (MetricQuery()).sum("visits", "sum_visits_field").where(query).get()
```
Would result the same.

<h3>Bucket Queries</h3>
Elasticsearch supports bucketing. Query Builder library supports histogram, range and filter functionalities:

```
es_query = (BucketQuery()).histogram("price", 50, 10).get() 
```

Here's the output of the query:

```
{'aggs': {'histogram_data': {'histogram': {'field': 'price', 'interval': 50, 'min_doc_count': 10}}}}
```
So what does this query do? Elasticsearch creates a histogram of how many docs exist for prices, 50, 100, 150...The final parameter (min_doc_count=10) ensures to show if only there are at least 10 docs. 

Filter method extends the functionality of metric queries:

```
avg_query = (MetricQuery()).avg("price").get()
filter_query = (FullTextQuery()).match("type", "shirt")
es_query = (BucketQuery()).filter(avg_query, "only_shirts", filter_query).get()
```

What does this method do? First line builds a simple query for avarage on price field. Third line builds a second option where only avarage price of shirts are calculated. Here's the expected output:
```
{'aggs': {'aggs': {'avg_price': {'avg': {'field': 'price'}}}}, 'only_shirts': {'aggs': {'aggs': {'avg_price': {'avg': {'field': 'price'}}}}, 'filter': {'aggs': {'avg_price': {'avg': {'field': 'price'}}}}}}
```

<h3>Fulltext Queries</h3>
Match method is the basic matching:

```
(FullTextQuery()).match("age", 42).get()
```

Multi-match:

```
(FullTextQuery()).multimatch(["price", "min_price"], 1000).get()
```

<h3>Fuzzy Logic</h3>
Query builder supports fuzzy logic functionality. Please refer <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-fuzzy-query.html">documentation</a> about the functionality. 

```
(FuzzyQuery("inbox.message", "sponsor")).addSetting("fuzziness", "AUTO").get()
```

Fuzzy functionality can be configured with many options:

```
fq = FuzzyQuery("inbox.message", "sponsor")
    fq.addSetting("fuzziness", "AUTO")
    fq.addSetting("max_expansions", 50)
    fq.addSetting("prefix_length", 0)
    fq.addSetting("transpositions", True)
    es_query = fq.get()
```

All of these options define how deep the fuzziness will be defined in the search query. 

<h3>Geo - Specific Queries</h3>
Bucket and metric queries support geo-calculations:

1. Geobonds calculates bonds of many geographical locations:
```
(MetricQuery()).geo_bonds("location").get()
```

2. Geo-centroid calculates centeroid of multiple locations:
```
(MetricQuery()).geo_centroid("location").get()
```

3. Boxplot calculates geographical boxplot.
```
(MetricQuery()).boxplot("location", "boxplot_data").get()
```

<h3>Testing of Library</h3>
If you want to add new test functionality to the library, you can test as follows:
<code>pytest</code>
<code>pytest -q tests/test_metricquery</code>
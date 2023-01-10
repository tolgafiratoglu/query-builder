from .helpers.dictionarybuilder import multifield_aggregation

class BucketQuery():
    es_query = None
    query = None

    def where(self, query):
        self.query = query
        return self

    def get(self):
        output = self.es_query
        if self.query != None: output["query"] = self.query["query"]
        return output

    def histogram(self, field, interval, min_doc_count = None):
        fields = {
           "field": field,
           "interval": interval
        }
        if min_doc_count != None: fields["min_doc_count"] = min_doc_count
        self.es_query = multifield_aggregation("histogram", fields, "histogram_data")
        return self

    def date_histogram(self, field, calendar_interval = None, fixed_interval = None):
        fields = {
           "field": field,
        }
        if calendar_interval != None: fields["calendar_interval"] = calendar_interval
        if fixed_interval != None: fields["fixed_interval"] = fixed_interval
        self.es_query = multifield_aggregation("date_histogram", fields, "date_histogram_data")
        return self

    def range(self, field, ranges):
        fields = {
           "field": field,
           "ranges": ranges
        }
        self.es_query = multifield_aggregation("range", fields, "range_data")
        return self

    def filter(self, metric_query, filter_key, filter_query):
        es_query = {}
        es_query["aggs"] = metric_query
        es_query[filter_key] = {
            "filter": metric_query,
            "aggs": metric_query
        }
        self.es_query = es_query
        return self
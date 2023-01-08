from .helpers.dictionarybuilder import basic_aggregation;

class MetricQuery():
    es_query = None
    query = None

    def setQuery(self, query):
        self.query = query
        return self

    def get(self):
        output = self.es_query
        if self.query != None: output["query"] = self.query["query"]
        return output

    def geobonds(field, result_field = "viewport", wrap_longitude = None, query = None):
        aggs = basic_aggregation(result_field, "geo_bonds", field, query)
        if wrap_longitude != None: aggs["aggs"][result_field]["geo_bonds"]["wrap_longitude"] = wrap_longitude
        return aggs

    def geo_centroid(field, result_field = "centroid", query = None):
        return basic_aggregation(result_field, "geo_centroid", field, query)

    def geo_line(field, point_field, sort_field="@timestamp", query = None):
        return {
            "aggs": {
                "line": {
                    "geo_line": {
                        "point": {
                            "field": point_field
                        },
                        "sort": {
                            "field": sort_field
                        }
                    }
                }
            }
        }

    def avg(self, field, response_field = None):
        self.es_query = basic_aggregation("avg", field, response_field)
        return self

    def boxplot(field, result_field = None, query = None):
        if result_field == None: result_field = "boxplot_" + field
        aggs = basic_aggregation(result_field, "boxplot", field, query)    
        aggs["size"] = 0
        return aggs

    def min(self, field, response_field = None):
        self.es_query = basic_aggregation("min", field, response_field)
        return self

    def sum(self, field, response_field = None):
        self.es_query = basic_aggregation("sum", field, response_field)
        return self

    def cardinality(self, field, response_field = None):
        self.es_query = basic_aggregation("cardinality", field, response_field)
        return self

    @classmethod
    def stats(self, field):
        if response_field == None: response_field = "stats_" + field
        self.es_query = basic_aggregation(response_field, "stats", field, self.query)
        return self

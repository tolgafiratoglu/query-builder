from .helpers.dictionarybuilder import basic_aggregation, multifield_aggregation

from .aggquery import AggQuery

class MetricQuery(AggQuery):
    def avg(self, field, response_field = None):
        self.es_query = basic_aggregation("avg", field, response_field)
        return self

    def min(self, field, response_field = None):
        self.es_query = basic_aggregation("min", field, response_field)
        return self

    def sum(self, field, response_field = None):
        self.es_query = basic_aggregation("sum", field, response_field)
        return self

    def cardinality(self, field, response_field = None):
        self.es_query = basic_aggregation("cardinality", field, response_field)
        return self    

    def geo_bonds(self, field, response_field = "viewport", wrap_longitude = None):
        aggs = basic_aggregation("geo_bonds", field, response_field)
        if wrap_longitude != None: aggs["aggs"][response_field]["geo_bonds"]["wrap_longitude"] = wrap_longitude
        self.es_query = aggs
        return self

    def geo_centroid(self, field, response_field = "centroid"):
        self.es_query = basic_aggregation("geo_centroid", field, response_field)
        return self

    def geo_line(self, point_field, sort_field="@timestamp"):
        fields = {
           "point": {
                "field": point_field
            },
            "sort": {
                "field": sort_field
            } 
        }
        self.es_query = multifield_aggregation("geo_line", fields, "line")
        return self

    def boxplot(self, field, response_field = None):
        self.es_query = basic_aggregation("boxplot", field, response_field)
        self.es_query["size"] = 0
        return self

    def stats(self, field, response_field = None):
        self.es_query = basic_aggregation("stats", field, response_field)
        return self

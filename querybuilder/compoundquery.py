from .query import Query

class CompoundQuery(Query):
    def boolean(self, criterias, minimum_should_match = None):
        self.es_query = {
            "query": {
                "bool": criterias
            }
        }
        if minimum_should_match != None: self.es_query["minimum_should_match"] = minimum_should_match
        return self
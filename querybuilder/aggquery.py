from .query import Query

class AggQuery(Query):    
    query = None

    def where(self, query):
        self.query = query
        return self

    def get(self):
        output = self.es_query
        if self.query != None: output["query"] = self.query["query"]
        return output    
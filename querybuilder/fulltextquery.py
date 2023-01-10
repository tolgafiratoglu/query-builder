from enum import Enum

from .helpers.dictionarybuilder import basic_query
from .query import Query

class FullTextQuery(Query):
    multi_match_types = {"best_fields", "most_fields", "cross_fields", "phrase", "phrase_prefix", "bool_prefix"}

    def match(self, field, value):
        self.es_query = {
            "query": {
                "match": {
                   field: {
                       "query": value  
                   }
                }
            }
        }
        return self

    def multimatch(self, fields, value, type = None):
        if type != None and type not in self.multi_match_types:
            raise Exception("Type is not a valid multi match type")
        es_query = {
            "query": {
                "multi_match": {
                    "query": value,
                    "fields": fields
                }
            }
        }
        if type != None: es_query["query"]["multi_match"]["type"] = type
        self.es_query = es_query
        return self    
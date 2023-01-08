from .helpers.dictionarybuilder import basic_query

class Query():
    @staticmethod
    def match(field, value):
        return basic_query(field, value, "match")
from .query import Query

class FuzzyQuery(Query):
    valid_params = ["fuzziness", "max_expansions", "prefix_length", "transpositions", "rewrite"]
    
    def __init__(self, field, value):
        self.field = field
        output = {
            "query": {
                "fuzzy": {
                    field: {
                        "value": value
                    }
                }
            } 
        }
        self.es_query = output

    def addSetting(self, setting_key, setting_value):
        if setting_key not in self.valid_params:
            raise Exception("This setting key is not a valid key")
        self.es_query["query"]["fuzzy"][self.field][setting_key] = setting_value 
        return self
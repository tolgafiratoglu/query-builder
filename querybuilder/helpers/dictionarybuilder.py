def basic_aggregation(context, function, field, query = None):
    basic_aggregation = {}
    if query != None: basic_aggregation['query'] = query
    basic_aggregation["aggs"] = {
        context: {
            function: {
                "field": field
            } 
        }
    }
    return basic_aggregation

def basic_query(field, value, context = "match"):
    return {
        "query": {
            context: {
                field: value
            }
        }
    }    
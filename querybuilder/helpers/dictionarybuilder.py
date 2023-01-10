def basic_aggregation(function, field, response_field = None):
    basic_aggregation = {}
    if response_field == None: response_field = function + "_" + field
    basic_aggregation["aggs"] = {
        response_field: {
            function: {
                "field": field
            } 
        }
    }
    return basic_aggregation

def multifield_aggregation(function, fields, response_field):
    basic_aggregation = {}
    basic_aggregation["aggs"] = {
        response_field: {
            function: fields
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
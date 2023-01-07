import json

from .helpers.dictionarybuilder import basic_aggregation;

class MetricQuery():
    @staticmethod
    def avg(field, query = None, result_field = None):
        if result_field != None: result_field = 'avg_' + field
        return json.dumps(basic_aggregation(result_field, 'avg', field, query))

    @staticmethod
    def min(field, query = None, result_field = None):
        if result_field != None: result_field = 'min_' + field
        return json.dumps(basic_aggregation(result_field, 'min', field, query))

    @staticmethod
    def sum(field, query = None, result_field = None):
        if result_field != None: result_field = 'sum_' + field
        return json.dumps(basic_aggregation(result_field, 'sum', field, query))
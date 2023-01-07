import json

class MetricQuery():

    @staticmethod
    def avg(field, result_field = None):
        result_field = 'avg.' + field
        return 'test' # json.dumps('test')

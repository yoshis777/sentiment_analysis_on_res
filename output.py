import pprint

from analyzer import Analyzer
from board import Board


class Output:
    def __init__(self):
        self.board = Board()
        self.analyzer = Analyzer()

    def output(self, thread_key):
        res_list = self.board.get(thread_key)

        def extract_message(res):
            return res['message']
        messages = list(map(extract_message, res_list))

        results = self.analyzer.analyze(messages)

        def combine_results(res, result):
            return {'res': res, 'result': result}

        pprint.pprint(list(map(combine_results, res_list, results)))

    def average(self):
        pprint.pprint('平均: ' + str(self.analyzer.average()))

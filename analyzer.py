from transformers import pipeline
from transformers import AutoModelForSequenceClassification
from transformers import BertJapaneseTokenizer


class Analyzer:
    def __init__(self):
        model = AutoModelForSequenceClassification.from_pretrained('daigo/bert-base-japanese-sentiment')
        tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking',
                                                          mecab_kwargs={"mecab_dic": 'unidic', "mecab_option": None})
        self.nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
        self.results = None

    def analyze(self, messages):
        self.results = self.nlp(messages)
        return self.results

    def average(self):
        if self.results is None:
            return None

        summary = 0.0
        for result in self.results:
            if result['label'] == 'ポジティブ':
                summary += result['score']
            elif result['label'] == 'ネガティブ':
                summary -= result['score']
        summary = summary / len(self.results)

        return summary




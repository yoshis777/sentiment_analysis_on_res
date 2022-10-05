## 前提
* [Transformersのインストール](https://github.com/yoshis777/import_transformers) を行い実行結果が出ていること

## 手順
関連ライブラリのインストール（初回のみ）
```bash
pip install -r requirements.txt
```
実行
```bash
python main.py <掲示板のID>
# 例：https://mevius.5ch.net/test/read.cgi/tech/1635480870/
# python main.py 1635480870
# 対象の掲示板は.envにて指定
```
実行結果
```json
[{'res': {'message': '...  '
                     '...',
          'res_num': '1'},
  'result': {'label': 'ポジティブ', 'score': 0.9402524828910828}},
 {'res': {'message': '...', 'res_num': '2'},
  'result': {'label': 'ポジティブ', 'score': 0.9831962585449219}},
 {'res': {'message': '...', 'res_num': '3'},
  'result': {'label': 'ポジティブ', 'score': 0.9763979911804199}}]
```

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

# ドバドバボール 公開ページ

iOS アプリ「ドバドバボール」のプライバシーポリシーとサポートのページです。アプリのソースとは別の公開リポジトリで管理し、GitHub Pages が `main` ブランチの `docs/` を配信します。

| ページ | URL |
| --- | --- |
| トップ | https://sean-sunagaku.github.io/dobadoba-legal/ |
| プライバシーポリシー | https://sean-sunagaku.github.io/dobadoba-legal/privacy/ |
| サポート | https://sean-sunagaku.github.io/dobadoba-legal/support/ |
| English | https://sean-sunagaku.github.io/dobadoba-legal/en/ |

## 直し方

1. `build.py` の中の文面（`PRIVACY`・`SUPPORT`）を、日本語と英語の両方そろえて直す。
2. 内容を変えたら `UPDATED` の日付も直す。
3. `python3 build.py` を実行して `docs/` を作り直す。
4. コミットして `main` に push する。

ページは JavaScript・外部フォント・解析・広告を使いません。必要なのは Python 3.10 以降だけです。

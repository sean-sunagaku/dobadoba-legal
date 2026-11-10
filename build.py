#!/usr/bin/env python3
"""ドバドバボールの公開ページ（プライバシーポリシー・サポート）を docs/ に書き出す。

日本語と英語を同じ構成で持ち、ここを直して `python3 build.py` を実行すると両方が作り直される。
ページは JavaScript・外部フォント・解析・広告を一切使わない。
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
BASE = "https://sean-sunagaku.github.io/dobadoba-legal"
CONTACT = "sunagaku.dx@gmail.com"
UPDATED = "2026-11-10"

SITE = {
    "ja": {
        "app": "ドバドバボール",
        "tagline": "ゆび1本でねらって、ボールをドバドバ増やすゲーム",
        "home": "トップ",
        "privacy": "プライバシーポリシー",
        "support": "サポート",
        "updated": "最終更新日",
        "other": ("English", "/en"),
        "operator": "運営者: sunagaku",
        "intro": "ドバドバボールは、画面を押しっぱなしにしてボールを流し、ゲートで増やしてバケツに集める iPhone 向けのゲームです。",
    },
    "en": {
        "app": "DobaDoba Ball",
        "tagline": "Aim with one finger and multiply the balls",
        "home": "Home",
        "privacy": "Privacy Policy",
        "support": "Support",
        "updated": "Last updated",
        "other": ("日本語", ""),
        "operator": "Operator: sunagaku",
        "intro": "DobaDoba Ball is an iPhone game: hold the screen to pour balls, multiply them through gates, and collect them in the bucket.",
    },
}

# 各ページ: (見出し, [段落 or ("ul", [項目...])])
PRIVACY = {
    "ja": [
        ("1. 運営者と対象", [
            "sunagaku（ドバドバボールの開発・運営者。以下「運営者」）は、iOS アプリ「ドバドバボール」（以下「本アプリ」）で取り扱う情報について、このプライバシーポリシーを定めます。",
        ]),
        ("2. 運営者が取得する情報", [
            "本アプリにはアカウント登録がありません。氏名、メールアドレス、電話番号、連絡先、写真、正確な位置情報を、運営者が取得することはありません。",
            "ゲームの進み具合（クリアしたステージ、星の数、集めたボールの記録）と設定（音・振動のオン／オフ）は、お使いの端末の中だけに保存されます。運営者のサーバーには送られません。",
        ]),
        ("3. 広告のために第三者が取得する情報", [
            "本アプリは無料で提供するために、Google LLC の広告サービス「Google AdMob」を使って広告を表示します。広告の配信、表示回数の計測、不正の防止のために、Google の SDK が次の情報を取得することがあります。",
            ("ul", [
                "IP アドレス（おおよその地域の推定に使われます）",
                "端末の識別子（広告識別子 IDFA は、トラッキングを許可した場合のみ）",
                "広告の表示・タップなど、広告に対する操作の情報",
                "アプリの動作に関する情報（起動、クラッシュ、処理速度などの診断情報）",
                "端末の種類、OS のバージョン、言語設定などの情報",
            ]),
            "これらの情報の取り扱いは、Google のポリシーに従います。詳しくは <a href=\"https://policies.google.com/privacy\">Google プライバシーポリシー</a> と <a href=\"https://policies.google.com/technologies/partner-sites\">Google のサービスを使用するサイトやアプリから収集した情報の Google による使用</a> をご覧ください。",
        ]),
        ("4. トラッキングの許可と同意", [
            "本アプリは、広告の表示を始める前（最初の 2 ステージをクリアしたあと）に、iOS の機能（App Tracking Transparency）を使って、他社のアプリや Web サイトを横断したトラッキングを許可するかどうかをおたずねします。許可しなくても、ゲームはすべて遊べます。許可しない場合、広告識別子（IDFA）は使われません。",
            "この設定は、iOS の「設定」→「プライバシーとセキュリティ」→「トラッキング」でいつでも変更できます。",
            "欧州経済領域・英国・スイスなど、法令で同意が必要な地域では、広告のためのデータ利用について同意画面を表示します。同意の内容は、本アプリの「せってい」→「こうこくの プライバシーせってい」からいつでも変更できます。",
        ]),
        ("5. 利用目的", [
            ("ul", [
                "広告を表示し、その表示回数や効果を計測するため",
                "不正な広告の表示やタップを防ぐため",
                "アプリの不具合を見つけて直すため",
            ]),
        ]),
        ("6. 第三者への提供", [
            "運営者は、第 3 項に書いた広告事業者による取得を除き、利用者の情報を第三者に提供しません。法令にもとづく場合はこの限りではありません。",
        ]),
        ("7. お子さまの利用について", [
            "本アプリは、特定の年齢のお子さまを主な対象にしたものではなく、広く一般の方に向けたゲームです。表示する広告は、年齢を問わず見られる内容（全年齢向け）に制限しています。",
            "運営者は、13 歳未満（地域の法令でより高い年齢が定められている場合はその年齢未満）のお子さまの個人情報を、それと知りながら取得することはありません。お子さまが利用する場合は、保護者の方の管理のもとでご利用ください。",
        ]),
        ("8. 情報の保存と削除", [
            "端末の中に保存された進み具合は、本アプリの「せってい」→「きろくを けす」、または本アプリの削除によって消すことができます。",
            "Google が取得した情報の保存期間と削除の方法は、Google のポリシーに従います。",
        ]),
        ("9. このポリシーの変更", [
            "内容を変更する場合は、このページでお知らせします。大きな変更があるときは、アプリ内や App Store の説明でもお知らせします。",
        ]),
        ("10. お問い合わせ", [
            f"このポリシーについてのご質問は、<a href=\"mailto:{CONTACT}\">{CONTACT}</a> までご連絡ください。",
        ]),
    ],
    "en": [
        ("1. Operator and scope", [
            "sunagaku (the developer and operator of DobaDoba Ball, the “Operator”) provides this Privacy Policy for the iOS app “DobaDoba Ball” (the “App”).",
        ]),
        ("2. Information the Operator collects", [
            "The App has no account registration. The Operator does not collect your name, email address, phone number, contacts, photos, or precise location.",
            "Your game progress (cleared stages, stars, ball records) and settings (sound and haptics) are stored only on your device. They are not sent to the Operator’s servers.",
        ]),
        ("3. Information collected by third parties for advertising", [
            "To keep the App free, it shows ads using Google AdMob, an advertising service of Google LLC. To deliver ads, measure impressions, and prevent fraud, Google’s SDK may collect the following information.",
            ("ul", [
                "IP address (used to estimate your general location)",
                "Device identifiers (the advertising identifier, IDFA, only if you allow tracking)",
                "Interactions with ads, such as impressions and taps",
                "Information about how the App runs (diagnostics such as launches, crashes, and performance)",
                "Device type, OS version, language setting, and similar information",
            ]),
            "This information is handled under Google’s policies. See the <a href=\"https://policies.google.com/privacy\">Google Privacy Policy</a> and <a href=\"https://policies.google.com/technologies/partner-sites\">How Google uses information from sites or apps that use our services</a>.",
        ]),
        ("4. Tracking permission and consent", [
            "Before it starts showing ads (after you clear the first two stages), the App uses the iOS App Tracking Transparency feature to ask whether you allow tracking across other companies’ apps and websites. The game is fully playable even if you do not allow it. If you do not allow it, the advertising identifier (IDFA) is not used.",
            "You can change this at any time in iOS Settings → Privacy &amp; Security → Tracking.",
            "In regions where the law requires consent, such as the European Economic Area, the United Kingdom, and Switzerland, the App shows a consent screen for the use of data for advertising. You can change your choices at any time from Settings → Ad privacy settings in the App.",
        ]),
        ("5. Purposes of use", [
            ("ul", [
                "To show ads and measure their impressions and effectiveness",
                "To prevent fraudulent ad impressions and taps",
                "To find and fix problems in the App",
            ]),
        ]),
        ("6. Sharing with third parties", [
            "Other than the collection by the advertising provider described in Section 3, the Operator does not share user information with third parties, except where required by law.",
        ]),
        ("7. Children", [
            "The App is a general-audience game and is not directed primarily at children of any particular age. Ads shown in the App are limited to content suitable for all ages.",
            "The Operator does not knowingly collect personal information from children under 13 (or under the higher age set by local law). Children should use the App under the supervision of a parent or guardian.",
        ]),
        ("8. Retention and deletion", [
            "Progress stored on your device can be erased from Settings → Reset progress in the App, or by deleting the App.",
            "The retention period and deletion of information collected by Google follow Google’s policies.",
        ]),
        ("9. Changes to this policy", [
            "Changes will be announced on this page. Significant changes will also be announced in the App or in its App Store description.",
        ]),
        ("10. Contact", [
            f"For questions about this policy, contact <a href=\"mailto:{CONTACT}\">{CONTACT}</a>.",
        ]),
    ],
}

SUPPORT = {
    "ja": [
        ("あそびかた", [
            ("ul", [
                "画面を押しっぱなしにすると、ノズルからボールが出ます。",
                "押したまま指を左右に動かすと、ノズルが指についてきます。",
                "「×2」「×3」などのゲートを通ると、ボールが増えます。",
                "赤い「✕」のゲートを通ると、ボールが消えます。",
                "バケツに入ったボールの数で、星が 1〜3 個もらえます。星 1 個でクリアです。",
                "最初に流してから時間がたつと「タイムアップ」になります。残ったボールは流せません。",
            ]),
        ]),
        ("よくある質問", [
            "<strong>音が鳴りません。</strong><br>端末の消音スイッチがオンになっていないか、音量が 0 になっていないかを確かめてください。アプリの「せってい」で「おと」がオンになっているかもご確認ください。",
            "<strong>記録を最初からやり直したい。</strong><br>「せってい」→「きろくを けす」で、星と記録を消せます。消した記録は元に戻せません。",
            "<strong>機種変更をしたら記録が消えました。</strong><br>記録は端末の中だけに保存しています。iPhone のバックアップから復元した場合は引き継がれますが、アプリを入れ直しただけでは引き継がれません。",
            "<strong>広告について。</strong><br>無料で遊べるように、ホーム画面と結果の画面にバナー広告を、ステージの合間にときどき全画面の広告を表示しています（最初の 2 ステージには広告が出ません）。動画広告は、見るかどうかを自分で選べます。失敗したときに見ると、ボールを足して続きから遊べます。星が 3 つに届かなかったときや、ステージの前にときどき出る「ボーナス チャンス」で見ると、ボールが増えた状態で遊べます。見なくても同じように遊べます。",
            "<strong>対応している端末は？</strong><br>iOS 17.0 以降の iPhone に対応しています。",
        ]),
        ("お問い合わせ", [
            f"不具合のご報告やご質問は、<a href=\"mailto:{CONTACT}\">{CONTACT}</a> までメールでお送りください。お使いの機種、iOS のバージョン、起きたことを書いていただけると、早く確認できます。",
        ]),
    ],
    "en": [
        ("How to play", [
            ("ul", [
                "Hold the screen and balls pour out of the nozzle.",
                "Slide your finger left and right while holding to move the nozzle.",
                "Balls multiply when they pass through gates such as “×2” and “×3”.",
                "Balls disappear when they pass through a red “✕” gate.",
                "You earn 1 to 3 stars depending on how many balls land in the bucket. One star clears the stage.",
                "A timer starts when you first pour. When time is up, the remaining balls cannot be poured.",
            ]),
        ]),
        ("FAQ", [
            "<strong>There is no sound.</strong><br>Check that the silent switch is off and the volume is not zero. Also check that Sound is turned on in Settings in the App.",
            "<strong>I want to start over.</strong><br>Go to Settings → Reset progress to erase your stars and records. This cannot be undone.",
            "<strong>My records disappeared after changing devices.</strong><br>Records are stored only on the device. They carry over when you restore from an iPhone backup, but not when you simply reinstall the App.",
            "<strong>About ads.</strong><br>To keep the game free, banner ads appear on the home and result screens, and full-screen ads occasionally appear between stages (no ads appear during the first two stages). Video ads are always optional. After a failed stage, you can watch one to add balls and continue. When you earn fewer than 3 stars, or on the “Bonus chance” card that sometimes appears before a stage, you can watch one to play with extra balls.",
            "<strong>Which devices are supported?</strong><br>iPhone with iOS 17.0 or later.",
        ]),
        ("Contact", [
            f"To report a problem or ask a question, email <a href=\"mailto:{CONTACT}\">{CONTACT}</a>. Including your device model, iOS version, and what happened helps us check it quickly.",
        ]),
    ],
}

CSS = """
:root { color-scheme: light dark; --bg: #f7f5ff; --card: #ffffff; --ink: #241a4d; --sub: #5b5480; --line: #e4dff5; --accent: #6a35c9; }
@media (prefers-color-scheme: dark) { :root { --bg: #17122e; --card: #221a45; --ink: #f1eeff; --sub: #b9b2dc; --line: #382e66; --accent: #c7a6ff; } }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Noto Sans JP", "Segoe UI", sans-serif; line-height: 1.8; }
.wrap { max-width: 760px; margin: 0 auto; padding: 24px 20px 64px; }
header.site { display: flex; align-items: center; gap: 14px; margin-bottom: 8px; }
header.site img { width: 56px; height: 56px; border-radius: 13px; }
header.site .name { font-weight: 800; font-size: 1.15rem; }
header.site .tag { color: var(--sub); font-size: .9rem; }
nav { display: flex; flex-wrap: wrap; gap: 6px 16px; padding: 12px 0 18px; border-bottom: 1px solid var(--line); margin-bottom: 26px; font-size: .95rem; }
a { color: var(--accent); }
nav a[aria-current="page"] { font-weight: 800; text-decoration: none; color: var(--ink); }
h1 { font-size: 1.7rem; line-height: 1.35; margin: 0 0 6px; }
h2 { font-size: 1.15rem; margin: 34px 0 8px; }
.meta { color: var(--sub); font-size: .9rem; margin: 0 0 22px; }
.card { background: var(--card); border: 1px solid var(--line); border-radius: 18px; padding: 22px 22px 10px; }
ul { padding-left: 1.3em; }
li { margin: 4px 0; }
footer { margin-top: 36px; color: var(--sub); font-size: .85rem; }
.links { display: grid; gap: 12px; margin-top: 18px; }
.links a { display: block; background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 16px 18px; text-decoration: none; font-weight: 700; }
""".strip()


def render_blocks(blocks) -> str:
    out = []
    for block in blocks:
        if isinstance(block, tuple) and block[0] == "ul":
            items = "".join(f"<li>{item}</li>" for item in block[1])
            out.append(f"<ul>{items}</ul>")
        else:
            out.append(f"<p>{block}</p>")
    return "\n".join(out)


def page(lang: str, kind: str, title: str, body: str) -> str:
    site = SITE[lang]
    prefix = "/en" if lang == "en" else ""
    root = f"{BASE}{prefix}"
    other_label, other_prefix = site["other"]
    suffix = "" if kind == "home" else f"/{kind}"
    other_url = f"{BASE}{other_prefix}{suffix}/"
    canonical = f"{root}{suffix}/"

    def nav_link(key: str, href: str) -> str:
        current = ' aria-current="page"' if key == kind else ""
        return f'<a href="{href}"{current}>{escape(site[key])}</a>'

    full_title = site["app"] if kind == "home" else f"{title} | {site['app']}"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(site['tagline'])}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="ja" href="{BASE}{suffix}/">
<link rel="alternate" hreflang="en" href="{BASE}/en{suffix}/">
<link rel="icon" href="{BASE}/assets/icon.png">
<link rel="stylesheet" href="{BASE}/assets/style.css">
</head>
<body>
<div class="wrap">
<header class="site">
<img src="{BASE}/assets/icon.png" alt="" width="56" height="56">
<div><div class="name">{escape(site['app'])}</div><div class="tag">{escape(site['tagline'])}</div></div>
</header>
<nav aria-label="{escape(site['home'])}">
{nav_link('home', root + '/')}
{nav_link('privacy', root + '/privacy/')}
{nav_link('support', root + '/support/')}
<a href="{other_url}" lang="{'ja' if lang == 'en' else 'en'}">{escape(other_label)}</a>
</nav>
<main>
{body}
</main>
<footer>
<p>{escape(site['operator'])} · <a href="mailto:{CONTACT}">{CONTACT}</a></p>
</footer>
</div>
</body>
</html>
"""


def document(lang: str, kind: str, sections) -> str:
    site = SITE[lang]
    title = site[kind]
    parts = [f"<h1>{escape(title)}</h1>", f'<p class="meta">{escape(site["updated"])}: {UPDATED}</p>', '<div class="card">']
    for heading, blocks in sections:
        parts.append(f"<h2>{escape(heading)}</h2>")
        parts.append(render_blocks(blocks))
    parts.append("</div>")
    return page(lang, kind, title, "\n".join(parts))


def home(lang: str) -> str:
    site = SITE[lang]
    prefix = "/en" if lang == "en" else ""
    body = f"""<h1>{escape(site['app'])}</h1>
<p>{escape(site['intro'])}</p>
<div class="links">
<a href="{BASE}{prefix}/privacy/">{escape(site['privacy'])}</a>
<a href="{BASE}{prefix}/support/">{escape(site['support'])}</a>
</div>"""
    return page(lang, "home", site["app"], body)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    write(DOCS / "assets/style.css", CSS + "\n")
    for lang in ("ja", "en"):
        base = DOCS / ("en" if lang == "en" else "")
        write(base / "index.html", home(lang))
        write(base / "privacy/index.html", document(lang, "privacy", PRIVACY[lang]))
        write(base / "support/index.html", document(lang, "support", SUPPORT[lang]))
    write(DOCS / "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    urls = [f"{BASE}{p}{s}/" for p in ("", "/en") for s in ("", "/privacy", "/support")]
    sitemap = "".join(f"<url><loc>{u}</loc><lastmod>{UPDATED}</lastmod></url>" for u in urls)
    write(DOCS / "sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sitemap}</urlset>\n')
    write(DOCS / "404.html", page("ja", "home", "404", f'<h1>404</h1><p>ページが見つかりません。<a href="{BASE}/">トップへ戻る</a> / Page not found. <a href="{BASE}/en/">Back to home</a></p>'))
    print("書き出し:", ", ".join(sorted(str(p.relative_to(DOCS)) for p in DOCS.rglob("*.html"))))


if __name__ == "__main__":
    main()

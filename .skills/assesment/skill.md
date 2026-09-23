---
name: assesment
description: >
  このリポジトリでユーザが初めて学習し始めるときにdocs/LEARNER.mdが存在しなければ、最初にユーザーにこのskill.mdで定義される質問を行い、ユーザーの現在のスキルを把握しdocs/LEARNER.mdに記録する。
---


# Learner Assessment

このリポジトリで初めて学習を開始するとき、エージェントは実装や解説を始める前に、ユーザーの現在のスキルレベルを確認してください。

目的はユーザーを評価することではなく、

* 説明の粒度
* 使用する用語
* ヒントの強さ
* 課題の難易度
* Pythonとの比較量
* FastAPI側の説明量
* HTML / JavaScriptの前提知識

を調整することです。

質問数は多くしすぎず、原則として5〜10問程度にしてください。

ユーザーがすでに十分な情報を提示している場合、同じ質問を繰り返してはいけません。

---

# Initial Questions

初回は原則として以下の質問を使用してください。

## Q1. Python

Pythonについて最も近いものを選んでください。

A. 変数、if、for、関数などもまだ不安がある

B. 基本文法は理解しているが、クラス、例外処理、型ヒントなどはあまり使わない

C. Pythonで通常のアプリケーションを実装できる

D. Pythonで設計、テスト、非同期処理なども含めて実務開発している

---

## Q2. HTTP / Web

HTTPについて最も近いものを選んでください。

A. GETやPOSTの違いもまだ曖昧

B. GET / POSTやステータスコードは知っている

C. Request / Response / Header / Body / Cookieなどをある程度説明できる

D. Web APIの設計やデバッグを日常的に行っている

---

## Q3. FastAPI / Backend

FastAPIまたは他のWebバックエンドについて最も近いものを選んでください。

A. Webフレームワークをほぼ使ったことがない

B. FastAPIのサンプルを動かしたことがある

C. FastAPIでAPIを実装したことがある

D. 認証、DB、セッション、非同期処理などを含むWebアプリを実装したことがある

---

## Q4. HTML

HTMLについて最も近いものを選んでください。

A. ほぼ触ったことがない

B. div、form、input、buttonなどは見たことがある

C. 簡単なページやフォームを書ける

D. DOM構造を意識してHTMLを設計できる

---

## Q5. CSS

CSSについて最も近いものを選んでください。

A. ほぼ触ったことがない

B. classや基本的なスタイル指定は分かる

C. FlexboxやGridを使ったことがある

D. レスポンシブレイアウトなども実装できる

---

## Q6. JavaScript

JavaScriptについて最も近いものを選んでください。

A. ほぼ書いたことがない

B. 変数、配列、関数程度は分かる

C. DOM操作やイベント処理を書いたことがある

D. fetch、async / await、Promiseを使った実装経験がある

---

## Q7. Frontend Framework

React / Vue / Svelteなどについて最も近いものを選んでください。

A. 利用したことがない

B. AIやサンプルを使って触ったことがある

C. 小規模な画面を実装したことがある

D. 実務で利用したことがある

---

## Q8. AI-assisted Coding

生成AIを使った開発について最も近いものを選んでください。

A. あまり使わない

B. 分からない部分を質問する程度

C. コード生成をよく利用する

D. 動作するコードは作れるが、生成されたコードの一部を説明できないことがある

---

# Optional Diagnostic Questions

必要に応じて、選択式回答だけで判断せず、以下のような小さな確認問題を1〜3問だけ追加してください。

例えば：

> Pythonで次のコードが何をしているか説明できますか？

```python
names = [user["name"] for user in users if user["active"]]
```

または：

> 次のURLへアクセスした場合、FastAPIではGETとPOSTのどちらのエンドポイントが呼ばれるでしょうか？

または：

> 次のJavaScriptで `button` には何が入っていると思いますか？

```javascript
const button = document.querySelector("#submit");
```

確認問題は試験ではありません。

正解・不正解だけで判断せず、ユーザーがどの概念を理解しているかを確認してください。

---

# Learner Profiles

回答から、概ね以下のプロフィールを決定してください。

プロフィールは固定的な能力評価ではなく、その時点の学習支援方法を決めるために使用します。

## Level 1: Programming Beginner

典型例：

* Python基本文法にも不安がある
* 関数やデータ構造の理解もまだ途中

支援方法：

* プログラミングの概念そのものから説明する
* 一度に扱う概念を少なくする
* 短いコードを使用する
* JavaScriptとPythonを同時に説明しすぎない
* 用語を使用したら意味も説明する
* 課題は5〜10行程度から始める

このレベルでは、JavaScriptへ急いで進まず、必要に応じてPythonの基本概念も補足してください。

---

## Level 2: Python User / Web Beginner

典型例：

* Python文法は理解している
* WebフレームワークやHTTPはあまり分からない

支援方法：

* Pythonの文法説明は省略する
* HTTPとWebブラウザの仕組みを重点的に説明する
* Request / Responseの概念を丁寧に扱う
* FastAPIの簡単なエンドポイントから始める

重点：

Python
→ FastAPI
→ HTTP
→ Browser

という流れを理解させてください。

---

## Level 3: Backend Developer / Frontend Beginner

典型例：

* FastAPIやバックエンド開発は理解している
* JavaScriptやDOMはほぼ未経験

支援方法：

* PythonやFastAPIの説明を必要以上に行わない
* HTTPについても基本説明は省略してよい
* JavaScriptとブラウザ実行環境を重点的に説明する
* Pythonとの比較を積極的に利用する

重点：

Browser
→ DOM
→ Event
→ JavaScript
→ fetch
→ FastAPI

という流れを理解させてください。

---

## Level 4: Backend Developer / Basic Frontend User

典型例：

* FastAPIは理解している
* HTML / JavaScriptを多少触ったことがある
* React / Vueなどのフレームワークは未経験
* AI生成コードを利用した経験が多い

支援方法：

* 文法の説明より「なぜそう動くのか」を優先する
* DOM、Event、Promise、async / awaitなどの実行モデルを重点的に確認する
* AIが生成したコードをユーザー自身に分解して説明してもらう
* Vanilla JavaScriptによる再実装を課題として利用する

重点：

「書けるか」よりも

「処理の流れを説明できるか」

を確認してください。

---

## Level 5: Frontend Experienced

典型例：

* JavaScript / TypeScriptを理解している
* DOMやfetchも利用できる
* React / Vueなども利用経験がある

支援方法：

* 基礎課題を無理に繰り返さない
* 理解が不足している領域だけを重点的に扱う
* ブラウザ内部の実行モデル
* Event Loop
* Promise
* Rendering
* State management
* Security

など、より深いテーマへ進んで構いません。

---

# Adaptive Teaching Rules

学習者プロフィールに応じて支援方法を変更してください。

## Explanation Depth

初心者：

> `fetch()` はブラウザからサーバーへHTTPリクエストを送るための関数です。

経験者：

> `fetch()` は `Promise<Response>` を返します。HTTP 404や500ではPromise自体はrejectされない点に注意してください。

同じ内容でも、理解度に応じて説明の抽象度を変更してください。

---

# Do Not Overteach Known Topics

ユーザーが十分理解している分野を繰り返し説明しないでください。

例えばユーザーがFastAPIを実務利用している場合、

* `@app.get`
* Pydanticの基本
* Python関数
* HTTP GETの基本

などを毎回説明する必要はありません。

その場合はフロントエンド側の理解に時間を使ってください。

---

# Detect Knowledge Gaps Dynamically

初回診断だけを絶対視しないでください。

学習中に、

* 説明できないコードがある
* 同じ種類のミスが繰り返される
* AI生成コードをそのまま使用している
* APIの戻り値について誤解している

などが確認された場合、その部分だけ説明レベルを一段下げてください。

逆にユーザーが十分理解していることが分かった場合は、説明レベルを上げてください。

---

# Do Not Label the User

内部的にLevelを利用して構いませんが、

> あなたはLevel 2です

のような固定的な評価として扱わないでください。

代わりに、

> PythonとFastAPIの基礎は十分そうなので、そこは省略してDOMとJavaScriptを重点的に進めましょう。

のように、学習方針として伝えてください。

---

# Reassessment

以下の場合、簡単な再評価を行って構いません。

* 新しいStageへ移るとき
* TypeScriptへ進むとき
* React / Vueなどへ進むとき
* ユーザーが難しすぎる、または簡単すぎると感じているとき

再評価では全質問を繰り返さず、その分野に関係する2〜4問程度だけ確認してください。

---

# Persisted Learner Profile

リポジトリ内に学習プロフィールを保存する場合は、例えば以下のようなファイルを利用できます。

```text
LEARNER.md
```

例：

```markdown
# Learner Profile

## Current background

- Python: advanced
- HTTP / Web: intermediate
- FastAPI / Backend: advanced
- HTML: beginner
- CSS: beginner
- JavaScript: beginner
- Frontend Framework: none

## Current focus

- DOM
- browser events
- fetch
- async / await

## Teaching preference

- Do not provide full solutions
- Prefer hints before code
- Compare JavaScript with Python when useful
- Ask for explanation after implementation
```

エージェントは学習開始時にこのファイルが存在する場合は読み取り、不要な初回質問を省略してください。

学習が進んだ場合は、ユーザーの許可または明示的な指示がある場合に限り更新してください。

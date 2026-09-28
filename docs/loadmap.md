はい。むしろ今の段階では、**基本に戻って手で書く価値がかなり大きい**と思います。

生成AIを使ってフロントエンドを作ると、`addEventListener`、`fetch`、`async/await`、DOM操作などが一気に生成されるので、「動くもの」は早くできます。一方で、バックエンドのFastAPIほど「この1行が何をしているか」を追えていない状態になりやすいです。

そこで、FastAPIを軸にして **「ブラウザ → HTTP → FastAPI → HTTP → JavaScript → DOM」** を一周、自分の手で追えることをゴールにするロードマップがよいと思います。

## FastAPI経験者向けフロントエンド学習ロードマップ

目安は6〜8週間ですが、仕事と並行なら期間はあまり気にしなくて構いません。

1. **第1段階：HTMLとブラウザの仕組み**

   まずJavaScriptを書かず、HTMLだけでFastAPIと通信します。

   ```python
   @app.post("/login")
   async def login(username: str = Form()):
       return {"username": username}
   ```

   ```html
   <form action="/login" method="post">
       <input name="username">
       <button type="submit">送信</button>
   </form>
   ```

   ここで理解したいのは、HTMLタグの種類より、

   ```text
   input
     ↓
   form
     ↓
   HTTP POST
     ↓
   FastAPI
     ↓
   HTTP Response
   ```

   という流れです。

   Chrome DevToolsのNetworkタブも必ず使います。Request Method、URL、Headers、Request Payload、Responseを見る癖をつけます。

   この段階では、`form action`と`method`だけで通信できることを確認してください。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | HTML | マークアップ言語 |
   | 要素（Element） | HTML |
   | 属性（Attribute） | HTML |
   | `form` | HTML要素 |
   | `input` | HTML要素 |
   | `button` | HTML要素 |
   | `action` | HTML属性 |
   | `method` | HTML属性 |
   | `name` | HTML属性 |
   | URL | Web |
   | HTTPリクエスト | HTTP |
   | HTTPレスポンス | HTTP |
   | GET | HTTPメソッド |
   | POST | HTTPメソッド |
   | ヘッダー | HTTP |
   | ボディ | HTTP |
   | ステータスコード | HTTP |
   | ページ遷移 | ブラウザ |
   | Networkタブ | Chrome DevTools |
   | `Form` | FastAPI |

2. **第2段階：JavaScriptそのもの**

   DOM操作はまだ最小限にして、JavaScriptという言語を理解します。

   ```javascript
   const user = {
       id: 1,
       name: "Taro"
   };

   const users = [
       { id: 1, name: "Taro" },
       { id: 2, name: "Hanako" }
   ];

   const names = users.map(user => user.name);
   ```

   特に重点を置くのは、

   ```text
   const / let
   object / array
   function
   arrow function
   map / filter / find
   destructuring
   spread syntax
   import / export
   ```

   です。

   Python経験者なら、例えば

   ```javascript
   users.filter(user => user.id > 10)
   ```

   を見たとき、

   ```python
   [user for user in users if user["id"] > 10]
   ```

   と対応させて考えると理解しやすいです。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | JavaScript | プログラミング言語 |
   | 文（Statement） | JavaScript構文 |
   | 式（Expression） | JavaScript構文 |
   | `const` | 変数宣言 |
   | `let` | 変数宣言 |
   | プリミティブ値 | データ型 |
   | オブジェクト | データ構造 |
   | 配列 | データ構造 |
   | 関数 | JavaScript |
   | アロー関数 | JavaScript構文 |
   | 引数 | 関数 |
   | 戻り値 | 関数 |
   | スコープ | JavaScript |
   | コールバック関数 | 関数 |
   | `map()` | 配列メソッド |
   | `filter()` | 配列メソッド |
   | `find()` | 配列メソッド |
   | 分割代入 | JavaScript構文 |
   | スプレッド構文 | JavaScript構文 |
   | `import` / `export` | ES Modules |

3. **第3段階：DOMとイベント**

   ここから「ブラウザ上でJavaScriptを使う」ことを学びます。

   ```html
   <input id="name">
   <button id="button">表示</button>

   <div id="result"></div>
   ```

   ```javascript
   const button = document.querySelector("#button");

   button.addEventListener("click", () => {
       const name = document.querySelector("#name").value;

       document.querySelector("#result").textContent = name;
   });
   ```

   このコードをAIなしで書けるようになるのが一つの目標です。

   このとき、

   ```text
   HTML読み込み
        ↓
   DOM生成
        ↓
   querySelector()
        ↓
   HTMLElement取得
        ↓
   addEventListener()
        ↓
   click発生
        ↓
   callback実行
        ↓
   DOM変更
   ```

   と説明できるようにします。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | DOM | ブラウザAPI |
   | `document` | DOM |
   | DOMツリー | DOM |
   | `Element` | DOMインターフェース |
   | `HTMLElement` | DOMインターフェース |
   | CSSセレクター | CSS |
   | `querySelector()` | DOM API |
   | `value` | DOMプロパティ |
   | `textContent` | DOMプロパティ |
   | `createElement()` | DOM API |
   | `append()` | DOM API |
   | イベント | ブラウザ |
   | `Event` | Web API |
   | `addEventListener()` | EventTarget API |
   | イベントリスナー | イベント |
   | `click` | イベント種別 |
   | `event.target` | イベント |
   | コールバック関数 | 関数 |

4. **第4段階：fetchとFastAPI**

   ここが最重要です。

   FastAPI側：

   ```python
   @app.get("/api/users")
   async def get_users():
       return [
           {"id": 1, "name": "Taro"},
           {"id": 2, "name": "Hanako"},
       ]
   ```

   JavaScript側：

   ```javascript
   async function loadUsers() {
       const response = await fetch("/api/users");

       const users = await response.json();

       console.log(users);
   }
   ```

   ここでは、

   ```text
   fetch()
      ↓
   Promise
      ↓
   await
      ↓
   Response
      ↓
   response.json()
      ↓
   JavaScript Object
   ```

   を説明できることが非常に重要です。

   特に、

   ```javascript
   const response = await fetch(...)
   ```

   と

   ```javascript
   const data = await response.json()
   ```

   がなぜ2段階になっているのかは、一度しっかり理解しておく価値があります。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | Fetch API | ブラウザAPI |
   | `fetch()` | Fetch API |
   | `Request` | Fetch API |
   | `Response` | Fetch API |
   | `Promise` | 非同期処理 |
   | `async` | JavaScript構文 |
   | `await` | JavaScript構文 |
   | `response.json()` | Fetch API |
   | JSON | データ形式 |
   | シリアライズ | データ変換 |
   | デシリアライズ | データ変換 |
   | レスポンスヘッダー | HTTP |
   | レスポンスボディ | HTTP |
   | `Content-Type` | HTTPヘッダー |
   | パスオペレーション | FastAPI |
   | 同一オリジン | Webセキュリティ |

5. **第5段階：CRUD画面を自作する**

   ここまで来たら、小さなユーザー管理画面を作ります。

   FastAPIに、

   ```text
   GET    /api/users
   GET    /api/users/{id}
   POST   /api/users
   PUT    /api/users/{id}
   DELETE /api/users/{id}
   ```

   を用意して、JavaScriptだけで操作します。

   フロント側には、

   ```text
   ユーザー一覧
   ↓
   新規登録
   ↓
   編集
   ↓
   削除
   ```

   を実装します。

   Reactは使いません。

   BootstrapやTailwindも、一度は使わない方がいいです。

   ```text
   HTML
   CSS
   Vanilla JavaScript
   FastAPI
   ```

   だけで作ります。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | CRUD | アプリケーション操作 |
   | REST | API設計 |
   | リソース | REST |
   | エンドポイント | Web API |
   | GET | HTTPメソッド |
   | POST | HTTPメソッド |
   | PUT | HTTPメソッド |
   | PATCH | HTTPメソッド |
   | DELETE | HTTPメソッド |
   | パスパラメータ | HTTP / FastAPI |
   | クエリパラメータ | HTTP / FastAPI |
   | リクエストボディ | HTTP |
   | Pydanticモデル | FastAPI / Pydantic |
   | バリデーション | データ検証 |
   | `JSON.stringify()` | JavaScript API |
   | DOMレンダリング | DOM |

6. **第6段階：非同期処理とエラー処理**

   次に実務で重要になる部分です。

   ```javascript
   async function loadUsers() {
       try {
           const response = await fetch("/api/users");

           if (!response.ok) {
               throw new Error(`HTTP Error: ${response.status}`);
           }

           const users = await response.json();

           renderUsers(users);

       } catch (error) {
           console.error(error);
       }
   }
   ```

   ここで、

   ```text
   Network Error
   HTTP 400
   HTTP 401
   HTTP 403
   HTTP 404
   HTTP 422
   HTTP 500
   ```

   の違いも確認します。

   FastAPIを使っているなら422は特に重要です。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | 非同期処理 | JavaScript |
   | イベントループ | JavaScript実行モデル |
   | `Promise` | 非同期処理 |
   | pending / fulfilled / rejected | Promise状態 |
   | `try` / `catch` | 例外処理 |
   | `throw` | 例外処理 |
   | `Error` | JavaScript組み込みオブジェクト |
   | `response.ok` | Fetch API |
   | `response.status` | Fetch API |
   | ネットワークエラー | 通信エラー |
   | HTTPエラー | HTTP |
   | 4xx | HTTPステータスコード |
   | 5xx | HTTPステータスコード |
   | 422 Unprocessable Content | HTTPステータスコード |
   | ローディング状態 | UI状態 |
   | エラー状態 | UI状態 |

7. **第7段階：フォームをちゃんと理解する**

   次に、

   ```javascript
   FormData
   URLSearchParams
   JSON.stringify()
   Content-Type
   ```

   の違いを理解します。

   例えば、

   ```javascript
   await fetch("/api/users", {
       method: "POST",
       headers: {
           "Content-Type": "application/json"
       },
       body: JSON.stringify({
           name: "Taro"
       })
   });
   ```

   FastAPI側：

   ```python
   class UserCreate(BaseModel):
       name: str


   @app.post("/api/users")
   async def create_user(user: UserCreate):
       ...
   ```

   これで、

   ```text
   JavaScript Object
       ↓
   JSON.stringify
       ↓
   HTTP Body
       ↓
   FastAPI
       ↓
   Pydantic
       ↓
   Python Object
   ```

   という変換を理解します。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | `form` | HTML要素 |
   | `submit` | イベント種別 |
   | `preventDefault()` | Event API |
   | `FormData` | Web API |
   | `URLSearchParams` | Web API |
   | `JSON.stringify()` | JavaScript API |
   | `application/x-www-form-urlencoded` | MIMEタイプ |
   | `multipart/form-data` | MIMEタイプ |
   | `application/json` | MIMEタイプ |
   | `Content-Type` | HTTPヘッダー |
   | リクエストボディ | HTTP |
   | エンコーディング | データ表現 |
   | `BaseModel` | Pydantic |
   | バリデーションエラー | FastAPI / Pydantic |

8. **第8段階：認証・Cookie・セッション**

   ここはFastAPIアプリ開発ではかなり重要です。

   ```text
   Browser
      ↓
   POST /login
      ↓
   FastAPI
      ↓
   Set-Cookie
      ↓
   Browser Cookie
      ↓
   GET /api/...
      ↓
   Cookie自動送信
      ↓
   FastAPI
      ↓
   Session取得
   ```

   Cookie、HttpOnly、Secure、SameSite、CSRFを、このタイミングでまとめて理解するとよいです。

   セッションをValkeyなどに保存する場合も、

   ```text
   Browser
       ↓ session_id
   Cookie
       ↓
   FastAPI
       ↓
   Valkey
       ↓
   User Session
   ```

   と整理すればかなり分かりやすくなります。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | 認証 | セキュリティ |
   | 認可 | セキュリティ |
   | Cookie | HTTP / ブラウザ |
   | `Set-Cookie` | HTTPレスポンスヘッダー |
   | `Cookie`ヘッダー | HTTPリクエストヘッダー |
   | セッション | 認証 |
   | セッションID | 認証 |
   | セッションストア | サーバーサイド |
   | `HttpOnly` | Cookie属性 |
   | `Secure` | Cookie属性 |
   | `SameSite` | Cookie属性 |
   | `Domain` | Cookie属性 |
   | `Path` | Cookie属性 |
   | `Expires` / `Max-Age` | Cookie属性 |
   | CSRF | Webセキュリティ |
   | XSS | Webセキュリティ |
   | Valkey | データストア |

9. **第9段階：TypeScript**

   Vanilla JavaScriptでCRUDが作れるようになってからTypeScriptに進みます。

   ```typescript
   interface User {
       id: number;
       name: string;
   }

   async function getUsers(): Promise<User[]> {
       const response = await fetch("/api/users");

       return await response.json();
   }
   ```

   Pydanticを使い慣れているなら、

   ```text
   FastAPI / Python       Frontend

   Pydantic        ←→     interface / type
   type hint       ←→     TypeScript
   BaseModel       ←→     型定義
   ```

   と見るとかなり理解しやすいはずです。

   **調べる用語**

   | 用語 | カテゴリ |
   | --- | --- |
   | TypeScript | プログラミング言語 |
   | 静的型付け | 型システム |
   | 型推論 | 型システム |
   | 型注釈 | TypeScript構文 |
   | `type` | TypeScript構文 |
   | `interface` | TypeScript構文 |
   | union型 | TypeScript型 |
   | optional property | TypeScript型 |
   | 関数型 | TypeScript型 |
   | ジェネリクス | TypeScript型 |
   | `Promise<T>` | TypeScript型 |
   | `unknown` | TypeScript型 |
   | 型アサーション | TypeScript構文 |
   | コンパイル | 開発工程 |
   | トランスパイル | 開発工程 |
   | `tsconfig.json` | TypeScript設定 |

10. **第10段階：React/Vueへ進む**

    ここまで来て初めてReactを触るくらいでも遅くありません。

    Reactで行われていることも、突き詰めれば、

    ```text
    State変更
       ↓
    Component再評価
       ↓
    Virtual DOM
       ↓
    DOM更新
    ```

    なので、Vanilla JSでDOM操作を経験していると、

    「Reactが何を楽にしているのか」

    が理解できます。

    **調べる用語**

    | 用語 | カテゴリ |
    | --- | --- |
    | フロントエンドフレームワーク | ソフトウェア分類 |
    | コンポーネント | UI設計 |
    | State | UI状態管理 |
    | Props | コンポーネント間通信 |
    | 宣言的UI | UI設計 |
    | 再レンダリング | UI更新 |
    | Virtual DOM | UI更新 |
    | ライフサイクル | コンポーネント |
    | Hooks | React API |
    | Composition API | Vue API |
    | Single File Component | Vue |
    | JSX | JavaScript拡張構文 |
    | リアクティビティ | 状態管理 |
    | クライアントサイドルーティング | Webアプリケーション |

---

### 一つの教材を育てていく方法がおすすめです

毎回違う教材を作るより、例えば

```text
FastAPI User Manager
```

を1つ作り続けます。

最初は、

```text
HTMLフォーム
↓
FastAPI POST
```

だけ。

次に、

```text
fetch GET
↓
一覧表示
```

を追加。

さらに、

```text
POST
PUT
DELETE
```

を追加。

その後、

```text
認証
Cookie
Session
CSRF
Loading
Error handling
TypeScript
```

を追加します。

こうすると一つのアプリを通して、

```text
Browser
Frontend
HTTP
FastAPI
Pydantic
DB
Session
```

が全部つながります。

これはかなり実務に近い学習になります。

### 生成AIは「禁止」する必要はありません

ここは結構重要だと思います。

AIを使わずに全部書くこと自体が目的ではありません。

むしろ、

> **生成させる用途から、理解を補助する用途へ一時的に切り替える**

のがよいです。

例えば、

```text
× 「ユーザー一覧画面を作って」

○ 「このfetchがどのタイミングでPromiseを返すのか説明して」

○ 「このevent.targetは実際には何のオブジェクトか」

○ 「このコードを実行したときの処理順序を説明して」

○ 「この処理を自分で実装したのでレビューして」
```

という使い方です。

特におすすめなのは、**まず自分で10〜30行書いてからAIに見せる**方法です。

AIが100行生成したコードを読むより、自分が書いた20行をAIにレビューしてもらう方が、学習効率はかなり高いです。

そして、自分に対して一つ基準を置くとよいと思います。

> **そのコードを消されても、同等のものをもう一度書けるか。**

完全に暗記している必要はありません。MDNなどを調べながらで構いません。

ただ、

```javascript
button.addEventListener(...)
```

を見て、

「なんとなくAIが書いたイベント処理」

ではなく、

```text
button = HTMLElement
addEventListener = イベント登録
"click" = Event type
callback = イベント発生時に呼ばれる関数
```

まで説明できる状態にします。

最終的には、フロントエンドコードを見て、

```text
これはDOM取得

これはイベント登録

ここでHTTPリクエスト

ここで非同期待ち

ここでレスポンスをJSONに変換

ここでstateを書き換えて

ここでDOMを更新
```

と**処理を分解して読めること**が目標です。

FastAPI側についてかなり具体的な理解を積み上げてきた人であれば、フロントエンドも同じやり方で十分追いつけると思います。今は「技術が難しい」というより、生成AIによって途中の学習段階を何段か飛ばしてしまった状態に近いのではないでしょうか。

その飛ばした部分をVanilla JavaScript + FastAPIで一度埋め直しておくと、その後Reactやdeck.glのようなライブラリを触るときも、「魔法のコード」に見える部分がかなり減ってきます。

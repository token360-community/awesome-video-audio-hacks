<h1 align="center">
  <img src="./assets/banner.png" alt="Awesome Video & Audio Hacks（Token360）" width="800" />
  <br />
  Awesome Video &amp; Audio Hacks
</h1>

<!-- data/catalog.json から scripts/generate_readme.py で生成。手で編集しないこと。 -->

<p align="center">
  <a href="./README.md">EN</a> · <a href="./README.zh-CN.md">简体中文</a> · <strong>日本語</strong>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-42-9633af" alt="entries: 42" />
  <img src="https://img.shields.io/badge/last_verified-2026--10--11-informational" alt="last verified: 2026-10-11" />
  <img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey" alt="License: CC0-1.0" />
</p>

> AI の**動画・音声合成・吹き替え・リップシンク・編集**向けに、オープンソースのワークフロー、エージェントスキル、MCP サーバー、再現できる投稿を厳選したリストです。すべての項目は書面の基準（[コントリビュート](#コントリビュート)）で再確認しており、各カテゴリは最大 5 件です。メンテナンスは [Token360](https://www.token360.ai?utm_source=github&utm_medium=awesome&utm_campaign=avah) 開発者コミュニティ。

**タグ：** `Repo` `Skill` `MCP` `Node` `Post` `Person` `List` · ⛔ リンクのみ（非商用または source-available ライセンス） · ⚠️ 商用利用の前に注記を確認

⚡ は「`base_url` とキーを変えるだけで Token360 で動くことを確認済み」を表します。現時点では未検証のため、⚡ の付いた項目はありません。

<sub>10 カテゴリ・全 42 件 · 最終確認 2026-10-11</sub>

## Token360 クイックスタート

Token360 は OpenAI 互換の `base_url` ひとつで、テキスト・画像・動画モデルを提供しています。

```python
import os
from openai import OpenAI

client = OpenAI(base_url="https://api.token360.ai/v1", api_key=os.environ["TOKEN360_API_KEY"])
resp = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[{"role": "user", "content": "Write a 3-shot storyboard for a 10-second product teaser."}],
)
print(resp.choices[0].message.content)
```

```bash
# Video: create a task, then poll GET /videos/{id} until it completes
curl https://api.token360.ai/v1/videos \
  -H "Authorization: Bearer $TOKEN360_API_KEY" -H "Content-Type: application/json" \
  -d '{"model": "seedance-2.5", "prompt": "A paper-cut crane takes off over a misty lake"}'
```

| モダリティ | エンドポイント                    | モデル ID の例                                                       |
| ---------- | --------------------------------- | -------------------------------------------------------------------- |
| テキスト   | `POST /chat/completions`          | `claude-sonnet-5-5`, `gpt-6-sol`, `deepseek-v4.1-flash`              |
| 画像       | `POST /images/generations`        | `gpt-image-2`, `dola-seedream-5.0-pro`, `nano-banana-2`              |
| 動画       | `POST /videos → GET /videos/{id}` | `seedance-2.5`, `veo-3.1-generate-001`, `wan3.0-video`, `minimax-h3` |
| 音声       | _検証待ち_                        | `seed-audio-1.0`, `glm-asr-2512`                                     |

<sub>モデル ID は 2026-10-11 時点の公開 `GET /v1/models` から取得。キーなしのリクエストには認証エラーを返すことを確認済みですが、このリストの項目はまだ Token360 上でエンドツーエンドに試していません。</sub>

全モデルの一覧とモデルごとのリクエスト例：[token360.ai/models](https://www.token360.ai/models?utm_source=github&utm_medium=awesome&utm_campaign=avah)。

## 目次

- [動画生成とプロンプト](#動画生成とプロンプト) (5)
- [ショートドラマとストーリー](#ショートドラマとストーリー) (5)
- [編集・モーションエージェント](#編集モーションエージェント) (5)
- [音声・TTS・音楽](#音声tts音楽) (5)
- [吹き替えと字幕](#吹き替えと字幕) (4)
- [リップシンクとデジタルヒューマン](#リップシンクとデジタルヒューマン) (3)
- [ComfyUI と MCP コネクタ](#comfyui-と-mcp-コネクタ) (4)
- [ワークフロー解説（投稿）](#ワークフロー解説投稿) (4)
- [注目の作り手](#注目の作り手) (4)
- [関連リスト](#関連リスト) (3)

## 動画生成とプロンプト

- [HKUDS/ViMax](https://github.com/HKUDS/ViMax) - `Repo` · ⭐ 12.6k · MIT · アイデア → 脚本 → 絵コンテ → ショットまでを 1 本でつなぐエージェント型動画生成。監督・脚本・プロデューサー役のエージェントが分担します。
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) - `Skill` · ⭐ 7.6k · MIT · Seedance 2.0 での映像制作向けスキル。テキスト・画像・動画・音声の 4 種類の入力を扱う制作パイプラインです。
- [zhouwei713/seedance-prompt](https://github.com/zhouwei713/seedance-prompt) - `Skill` · ⭐ 327 · MIT · Seedance などのテキスト→動画モデル向けに、実写風の動画プロンプトを書くエージェントスキル。
- [liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) - `Skill` · ⭐ 616 · MIT · Seedance 2.5 の「動画ディレクター」スキル。プロンプト、脚本、人物の固定、続きの生成、編集、トランジションに対応。
- [s1dashu/director](https://github.com/s1dashu/director) - `Skill` · ⭐ 801 · MIT · リサーチ、脚本、ビジュアル開発、ショット設計、素材生成、納品まで、1 本の動画を通しで「監督」するスキル。

## ショートドラマとストーリー

- [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) - `Repo` · ⭐ 17.2k · MIT · セルフホストできるショートドラマ／モーションコミック制作ツール。無限キャンバス上で脚本、絵コンテ、キャラクター・シーン素材、画像・動画生成をエージェントと進めます。
- [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) - `Repo` · ⭐ 4.7k · AGPL-3.0 · 脚本から完成映像までをバッチで回す AI 映像制作ツール。Seedance 2.0 に対応。
- [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) - `Repo` · ⭐ 2k · MIT · ローカル優先のショートドラマ制作ツール。ストーリー → 絵コンテ → 動画まで、プロジェクトデータは手元のマシンに残ります。
- [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) - `Skill` · ⭐ 2.7k · MIT · Claude Code / Codex 向けの AI ショートドラマ用スキル集。脚本、キャラクター素材、絵コンテ、画像・動画プロンプト、レビューまで。
- [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) - `Skill` · ⭐ 4.4k · Apache-2.0 · ショートドラマのプリプロダクション向けエージェントスキル。キャラクター設定、構成案、美術設定、脚本、絵コンテ。

## 編集・モーションエージェント

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) - `Repo` · ⭐ 66.9k · AGPL-3.0 · AI コーディングアシスタントを動画制作パイプラインに変えるエージェント型システム。既製のパイプラインとツールを多数収録。
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) - `Repo` · ⭐ 60.9k · Apache-2.0 · HTML を書けば動画にレンダリングできるモーションフレームワーク。エージェントから扱う前提で設計されています。
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - `Skill` · ⭐ 11.3k · Apache-2.0 · Remotion でシネマティックな製品動画を作る Claude Code / Codex スキル。ショットのレシピカード、モーションプレビュー、制作用テンプレート付き。 ⚠️ レンダリングに Remotion を使用。Remotion 本体のライセンスは一部の企業利用で有償ライセンスが必要です。
- [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit) - `Skill` · ⭐ 2.2k · MIT · Claude Code 向けの AI ネイティブな動画制作ツールキット。
- [luoluoluo22/jianying-editor-skill](https://github.com/luoluoluo22/jianying-editor-skill) - `Skill` · ⭐ 3.9k · MIT · 剪映（CapCut 中国版）のプロジェクト下書きを書き換えて編集を自動化するエージェントスキル。

## 音声・TTS・音楽

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - `Repo` · ⭐ 62.7k · MIT · 少量サンプルでの声のクローンと TTS。約 1 分の参照音声で声を学習できます。
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) - `Repo` · ⭐ 39k · Apache-2.0 · トークナイザー不要の多言語 TTS。ボイスデザインと声のクローンに対応。
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - `Repo` · ⭐ 26.9k · MIT · Resemble AI によるオープンソースの TTS モデル。
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) - `Repo` · ⭐ 23.9k · Apache-2.0 · 多言語の音声生成モデル。推論・学習・デプロイのコード一式付き。
- [remsky/Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI) - `Repo` · ⭐ 5.5k · Apache-2.0 · Kokoro-82M を OpenAI 互換の音声 API として Docker で動かすサーバー。CPU / GPU 対応、字幕タイムスタンプ出力付き。

## 吹き替えと字幕

- [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) - `Repo` · ⭐ 18.8k · Apache-2.0 · 字幕の分割・翻訳・タイミング調整から吹き替えまでを自動でつなぐパイプライン。
- [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans) - `Repo` · ⭐ 19.3k · GPL-3.0 · 動画を別の言語に翻訳し、吹き替え音声と字幕を付けます。
- [buxuku/SmartSub](https://github.com/buxuku/SmartSub) - `Repo` · ⭐ 5.6k · MIT · Windows / macOS / Linux 対応のデスクトップアプリ。ローカル文字起こし、字幕翻訳、AI 吹き替え、字幕の焼き込み。
- [m-bain/whisperX](https://github.com/m-bain/whisperX) - `Repo` · ⭐ 24.5k · BSD-2-Clause · 単語単位のタイムスタンプと話者分離付きの音声認識。

## リップシンクとデジタルヒューマン

- [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) - `Repo` · ⭐ 8k · Apache-2.0 · 音声駆動で長さ制限のないトーキング動画を生成。画像からも既存動画からも作れます。
- [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) - `Repo` · ⭐ 19.2k · MIT · ドライビング動画に合わせて静止画のポートレートを動かします。 ⚠️ コードは MIT ですが、同梱の InsightFace 検出モデルは非商用限定です。商用利用では差し替えが必要です。
- [Jingyi-Wu-Richael/rachel-digital-human-production](https://github.com/Jingyi-Wu-Richael/rachel-digital-human-production) - `Skill` · ⭐ 1.1k · MIT · 許諾を得たトーキングヘッド動画を作る Codex スキル。素材チェック、短いプレビュー、承認後に本番レンダリングという流れです。

## ComfyUI と MCP コネクタ

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - `Repo` · ⭐ 136.9k · GPL-3.0 · 画像・動画・音声の拡散モデルをノードグラフで組むエンジンと GUI。
- [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) - `Node` · ⭐ 1.2k · GPL-3.0 · MiniMax H3 のクリップをつなぎ、つなぎ目でも動きと音声が続くようにする ComfyUI ノード。サンプルワークフロー付き。
- [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) - `MCP` · ⭐ 811 · MIT · MCP サーバーとサイドバーエージェントで、LLM から ComfyUI の画像・動画・音声ワークフローを組み立て・実行・編集できます。 ⚠️ README によると現在は限定的なメンテナンス（重大な修正のみ）です。
- [pireel/pireel](https://github.com/pireel/pireel) - `MCP` · ⭐ 1.3k · AGPL-3.0 · キャンバスとタイムラインを備えたオープンソースの動画エディター。AI エージェントから MCP で操作できます。

## ワークフロー解説（投稿）

- [@GeekCatX — 4 ステップで作る Vox 風解説動画](https://x.com/GeekCatX/status/2078488413045747814) - `Post` · 2026-07 · 動画生成 · 4 ステップ：Codex と vox-style スキルで絵コンテのプロンプトを作り、画像モデルでコマを生成、動画モデルで動かし、最後に自動編集。
- [@newbeeyu — Codex + Remotion で作る唐代風切り絵アニメ](https://x.com/newbeeyu/status/2076530524110369070) - `Post` · 2026-07 · 編集・モーション · X の長文記事。Codex と Remotion でコードから作る唐代風の切り絵レイヤーアニメ。レイヤー分け、タイミング、レイヤーごとの効果音を解説。
- [@EXM7777 — Claude Code で組む AI 動画制作パイプライン](https://x.com/EXM7777/status/2082107255449919582) - `Post` · 2026-07 · 編集・モーション · X の長文記事。Claude Code を動画制作パイプラインとして組む手順と、ショット設計で参照する資料サイトを紹介。
- [@Pluvio9yte — Codex + Hyperframes + HeyGen + 声のクローンの全工程](https://x.com/Pluvio9yte/status/2081580929492131947) - `Post` · 2026-07 · 音声・TTS · X の長文記事（中国語）。Codex を司令塔に、Hyperframes でモーション、HeyGen でアバター、IndexTTS で音声を作るショート動画の全工程。

## 注目の作り手

- [@HeyAbhishek](https://x.com/HeyAbhishek) - `Person` · EN · Seedance アニメのプロンプト · シネマティックな AI アニメ動画の完全なプロンプトを公開しています。例: [投稿](https://x.com/HeyAbhishek/status/2106369769956065518)。
- [@liyue_ai](https://x.com/liyue_ai) - `Person` · 中文 · Seedance 監督スキル · GitHub（liyue-aigc）で Seedance 用の監督スキルをオープンソース公開しています。例: [投稿](https://x.com/liyue_ai/status/2093592225162960982)。
- [@Pluvio9yte](https://x.com/Pluvio9yte) - `Person` · 中文 · エージェント駆動の動画制作 · Codex + Hyperframes の動画パイプラインと、その裏のスキルを長文で解説しています。例: [投稿](https://x.com/Pluvio9yte/status/2081648099680743554)。
- [@GeekCatX](https://x.com/GeekCatX) - `Person` · 中文 · 低コストの解説動画ワークフロー · エージェントと画像・動画モデルで低コストに解説動画を作る手順を発信しています。例: [投稿](https://x.com/GeekCatX/status/2078488413045747814)。

## 関連リスト

- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) - `List` · ⭐ 2k · MIT · Seedance 2.5 / 2.0 のプロンプト集。元投稿をたどれる事例、テンプレート、インストールできる動画スキル付き。
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - `List` · ⭐ 2.7k · MIT · Seedance 2.0 のプロンプト、ガイド、動画生成ワークフローのまとめ。
- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) - `List` · ⭐ 34.3k · MIT · GPT Image 2 / 2.5 のプロンプトと事例集（テンプレート付き）。動画化前のキーフレームや絵コンテ作りに。

## コントリビュート

`data/catalog.json` だけを編集し（README は直接編集しない）、`python3 scripts/generate_readme.py` を実行してから PR を出してください。先に [CONTRIBUTING.ja.md](./CONTRIBUTING.ja.md) の基準を読んでください。基準に満たない項目はマージせずにクローズします。

---

<sub>リストの内容は [CC0 1.0](./LICENSE) で公開しています。リンク先のプロジェクト・投稿・商標は各権利者に帰属し、掲載は権利者や Token360 による推奨を意味しません。</sub>

<sub>※ この日本語版は機械翻訳による下書きで、ネイティブスピーカーのレビュー前です。誤りに気づいたら Issue でお知らせください。</sub>

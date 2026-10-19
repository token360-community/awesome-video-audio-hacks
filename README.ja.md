<h1 align="center">
  <img src="./assets/banner.webp" alt="Awesome Video & Audio Hacks（Token360）" width="800" />
  <br />
  Awesome Video &amp; Audio Hacks
</h1>

<!-- data/catalog.json から scripts/generate_readme.py で生成。手で編集しないこと。 -->

<p align="center">
  <a href="./README.md">EN</a> · <a href="./README.zh-CN.md">简体中文</a> · <strong>日本語</strong>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-96-9633af" alt="entries: 96" />
  <img src="https://img.shields.io/badge/last_verified-2026--10--11-informational" alt="last verified: 2026-10-11" />
  <img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey" alt="License: CC0-1.0" />
</p>

> AI の**動画・音声合成・音楽・吹き替え・リップシンク・編集**向けに、オープンソースのワークフロー、エージェントスキル、MCP サーバー、再現できる投稿を厳選したリストです。すべての項目は書面の基準（[コントリビュート](#コントリビュート)）を満たす必要があり、少なくとも 30 日ごとに再確認しています。メンテナンスは [Token360](https://www.token360.ai?utm_source=github&utm_medium=awesome&utm_campaign=avah) 開発者コミュニティ。

**タグ：** `Repo` `Skill` `MCP` `Node` `Post` `Person` `List` · ⛔ リンクのみ（非商用または source-available ライセンス） · ⚠️ 商用利用の前に注記を確認

⚡ = Token360 上でエンドツーエンドに動作確認済みで、公開ガイドあり。⚡ のない項目は未検証です。🔷 Token360 版 = Token360 コミュニティが保守する fork で、検証済みの Token360 クイックスタートを追加したもの。成果・クレジット・ライセンスは元の作者に帰属し、⭐ は元リポジトリのスター数です。

<sub>11 カテゴリ・全 96 件 · 最終確認 2026-10-11</sub>

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

<sub>モデル ID は 2026-10-11 時点の公開 `GET /v1/models` から取得。キーなしのリクエストには認証エラーを返します。⚡ の付いた項目は Token360 上でエンドツーエンドに確認済み（各ガイド参照）で、それ以外はまだ試していません。</sub>

全モデルの一覧とモデルごとのリクエスト例：[token360.ai/models](https://www.token360.ai/models?utm_source=github&utm_medium=awesome&utm_campaign=avah)。

## 目次

- [動画生成とプロンプト](#動画生成とプロンプト) (10)
- [ショートドラマとストーリー](#ショートドラマとストーリー) (9)
- [編集・モーションエージェント](#編集モーションエージェント) (17)
- [音声・TTS・音楽](#音声tts音楽) (14)
- [吹き替えと字幕](#吹き替えと字幕) (8)
- [リップシンクとデジタルヒューマン](#リップシンクとデジタルヒューマン) (6)
- [広告・マーケティング動画](#広告マーケティング動画) (4)
- [ComfyUI と MCP コネクタ](#comfyui-と-mcp-コネクタ) (10)
- [ワークフロー解説（投稿）](#ワークフロー解説投稿) (10)
- [注目の作り手](#注目の作り手) (4)
- [関連リスト](#関連リスト) (4)

## 動画生成とプロンプト

- [HKUDS/ViMax](https://github.com/HKUDS/ViMax) - `Repo` · ⭐ 12.6k · MIT · アイデア → 脚本 → 絵コンテ → ショットまでを 1 本でつなぐエージェント型動画生成。監督・脚本・プロデューサー役のエージェントが分担します。
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - `Repo` · ⭐ 130.2k · MIT · テーマやキーワードからショート動画を自動生成。台本、素材、ナレーション、字幕、BGM までを 1 つのワークフローで仕上げます。
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) - `Skill` · ⭐ 7.6k · MIT · Seedance 2.0 での映像制作向けスキル。テキスト・画像・動画・音声の 4 種類の入力を扱う制作パイプラインです。
- [liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) - `Skill` · ⭐ 623 · MIT · Seedance 2.5 の「動画ディレクター」スキル。プロンプト、脚本、人物の固定、続きの生成、編集、トランジションに対応。
- [s1dashu/director](https://github.com/s1dashu/director) - `Skill` · ⭐ 801 · MIT · リサーチ、脚本、ビジュアル開発、ショット設計、素材生成、納品まで、1 本の動画を通しで「監督」するスキル。
- [krillinai/OpenCreator](https://github.com/krillinai/OpenCreator) - `Repo` · ⭐ 12.8k · Apache-2.0 · 台本から生成・吹き替え・ローカライズまでを一つで行うデスクトップ AI 動画スタジオ。エージェントスキル内蔵。
- [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) - `Skill` · ⭐ 4.3k · MIT · ざっくりしたアイデアから、そのまま使える Seedance 2.x 用の動画プロンプトを書くエージェントスキル。
- [token360-community/seedance-prompt-skill](https://github.com/token360-community/seedance-prompt-skill) - `Skill` ⚡ · 🔷 Token360 版（元: [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill)） · ⭐ 4.3k · MIT · Dex による Seedance プロンプト作成スキルに、Token360 上の Seedance 2.5 でプロンプトをそのまま動画にする標準ライブラリだけの Python スクリプトとサンプル動画を加えたもの。
- [FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo) - `Repo` · ⭐ 1.8k · Apache-2.0 · オープンな MiniMax H3 音声付き動画モデルを一般向け GPU や Mac で動かすローカル推論ツール。GPU ごとのコミュニティ実測あり。 ⚠️ コードは Apache-2.0 ですが、MiniMax H3 の重みは独自の MiniMax H3 Community License（米国・EU・英国・韓国のユーザーは申請が必要）です。商用利用の前に確認してください。
- [edenfunf/reelmimic](https://github.com/edenfunf/reelmimic) - `Repo` · ⭐ 2.4k · MIT · 好きな動画を渡すと、Claude Code や Codex 上のマルチエージェント班が同じスタイルの新しい動画を一緒に設計・制作・レビューします。

## ショートドラマとストーリー

- [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) - `Repo` · ⭐ 17.4k · MIT · セルフホストできるショートドラマ／モーションコミック制作ツール。無限キャンバス上で脚本、絵コンテ、キャラクター・シーン素材、画像・動画生成をエージェントと進めます。
- [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) - `Repo` · ⭐ 4.7k · AGPL-3.0 · 脚本から完成映像までをバッチで回す AI 映像制作ツール。Seedance 2.0 に対応。
- [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) - `Repo` · ⭐ 2k · MIT · ローカル優先のショートドラマ制作ツール。ストーリー → 絵コンテ → 動画まで、プロジェクトデータは手元のマシンに残ります。
- [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) - `Skill` · ⭐ 2.8k · MIT · Claude Code / Codex 向けの AI ショートドラマ用スキル集。脚本、キャラクター素材、絵コンテ、画像・動画プロンプト、レビューまで。
- [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) - `Skill` · ⭐ 4.5k · Apache-2.0 · ショートドラマのプリプロダクション向けエージェントスキル。キャラクター設定、構成案、美術設定、脚本、絵コンテ。
- [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) - `Repo` · ⭐ 5.5k · AGPL-3.0 · 小説や脚本からキャラクター・シーン素材、絵コンテ、一貫性のあるショット、剪映（CapCut）ドラフトまで作るセルフホスト型エージェントワークスペース。費用トラッキング付き。
- [FireRedTeam/FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline) - `Repo` · ⭐ 3.5k · Apache-2.0 · 自然言語で指示するだけで手作業の編集を「演出」に変える動画編集エージェント。MCP とエージェントスキルに対応。
- [alibaba/lumenx](https://github.com/alibaba/lumenx) - `Repo` · ⭐ 1.4k · MIT · 小説のテキストをアニメ調ショートドラマにする Alibaba のオープンソーススタジオ。脚本分析、キャラクター設定、絵コンテ、動画合成まで対応。
- [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama) - `Repo` ⛔ · ⭐ 16.1k · CC-BY-NC-SA-4.0 · 脚本から絵コンテ、生成エピソードまでを扱う、中国語圏で最もスターの多い AI ショートドラマ制作パイプライン。カテゴリの参照先として掲載。

## 編集・モーションエージェント

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) - `Repo` · ⭐ 67.5k · AGPL-3.0 · AI コーディングアシスタントを動画制作パイプラインに変えるエージェント型システム。既製のパイプラインとツールを多数収録。
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) - `Repo` · ⭐ 61.7k · Apache-2.0 · HTML を書けば動画にレンダリングできるモーションフレームワーク。エージェントから扱う前提で設計されています。
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - `Skill` · ⭐ 11.5k · Apache-2.0 · Remotion でシネマティックな製品動画を作る Claude Code / Codex スキル。ショットのレシピカード、モーションプレビュー、制作用テンプレート付き。 ⚠️ レンダリングに Remotion を使用。Remotion 本体のライセンスは一部の企業利用で有償ライセンスが必要です。
- [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) - `Repo` · ⭐ 93.8k · MIT · Web・デスクトップ・モバイルで使える無料のオープンソース動画エディター。CapCut の代替として開発されています。
- [luoluoluo22/jianying-editor-skill](https://github.com/luoluoluo22/jianying-editor-skill) - `Skill` · ⭐ 3.9k · MIT · 剪映（CapCut 中国版）のプロジェクト下書きを書き換えて編集を自動化するエージェントスキル。
- [browser-use/video-use](https://github.com/browser-use/video-use) - `Repo` · ⭐ 28.8k · MIT · browser-use チームによる、コーディングエージェントが単語単位の文字起こしから素材を完成動画に編集するツール。字幕の焼き込みにも対応。
- [linyqh/NarratoAI](https://github.com/linyqh/NarratoAI) - `Repo` · ⭐ 11.4k · MIT · 映画やドラマの解説動画をワンクリックで作成。LLM がナレーション原稿を書き、音声と編集まで自動で仕上げます。
- [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) - `Repo` · ⭐ 9.4k · MIT · ポッドキャストやインタビュー、講座などの長尺動画を、字幕・サムネイル・投稿文付きのショート動画に自動で切り出します。
- [GuanYixuan/pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) - `Repo` · ⭐ 4.5k · Apache-2.0 · 剪映（中国版 CapCut）のドラフトを Python で生成・書き出すライブラリ。多くの自動編集パイプラインの土台です。
- [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) - `Skill` · ⭐ 3.1k · Apache-2.0 · Claude Code スキルで作るトーキングヘッド動画の編集エージェント。言いよどみや間を詰め、字幕を付けて書き出します。
- [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) - `Skill` · ⭐ 4.3k · MIT · SRT 字幕ファイルから、温かみのある紙の上に一筆ずつ描かれるホワイトボード手描きアニメを作るスキル。
- [jub0t/concat](https://github.com/jub0t/concat) - `Repo` · ⭐ 5k · AGPL-3.0 · ネイティブ Rust エンジンのクロスプラットフォーム動画エディタ。オフライン Whisper の自動字幕、TTS と音声クローン、背景除去を備え、JSON-RPC・gRPC・MCP API からエージェントでも編集できます。 ⚠️ 作者はまだベータと明記しています。README には無関係なプロキシサービスのアフィリエイトコード付き有料スポンサー枠があります。
- [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) - `Skill` · ⭐ 3.6k · MIT · アート調のアニメーションをコードで書くエージェントスキル。35 の画風、9 種類のナレーション文法、8 種類のパラメトリック素材、ナレーション付き完成作のリファレンスコードを同梱し、npx 一行で導入できます。
- [nateherkai/hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit) - `Skill` · ⭐ 1.4k · MIT · 文字起こしから Reels や YouTube Shorts を編集する Codex / Claude Code スキル 14 本。406 枚のモーショングラフィックスカードと HyperFrames テンプレート、素材も API キーも不要で描画できるフィクスチャ付き。 ⚠️ 作者自身の構成では ElevenLabs Scribe と Kie.ai のモデル API を使いますが、どちらも任意で（ローカル Whisper や既存の文字起こしでも可）、生成素材も必須ではありません。
- [glanderness/BeefTV](https://github.com/glanderness/BeefTV) - `Repo` · ⭐ 1.1k · MIT · ローカルファーストの軽量な動画制作ワークスペース。無限キャンバス上でプロンプト・モデル・素材をつなぎ、人とエージェントが同じボードで反復できます。
- [Barty-Bart/motion-graphics](https://github.com/Barty-Bart/motion-graphics) - `Skill` · ⭐ 634 · MIT · Claude Code と Codex 向けのモーショングラフィックススキル集。フォント同梱の b-roll エンジンを含み、毎日更新されています。
- [hypit-ai/hypit](https://github.com/hypit-ai/hypit) - `Repo` ⛔ · ⭐ 23.9k · Modified Apache-2.0 · バズった動画を、素材・字幕・B ロール・エフェクトを単語単位で揃えた編集可能なワークフローとしてエージェントに複製させ、多数のバリエーションを書き出せるスキルと CLI。カテゴリの参照先として掲載。 ⚠️ ソース公開型：改変版 Apache-2.0 で、マルチテナント / SaaS としての提供と商用再配布は禁止です（生成物はユーザーのもの）。ドキュメントは Hypit 自社のホスティング HypiHub と提携モデル API（一部は紹介リンク）を既定としていますが、ローカルや自前のプロバイダーも使えます。

## 音声・TTS・音楽

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - `Repo` · ⭐ 62.7k · MIT · 少量サンプルでの声のクローンと TTS。約 1 分の参照音声で声を学習できます。
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) - `Repo` · ⭐ 39.2k · Apache-2.0 · トークナイザー不要の多言語 TTS。ボイスデザインと声のクローンに対応。
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - `Repo` · ⭐ 26.9k · MIT · Resemble AI によるオープンソースの TTS モデル。
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) - `Repo` · ⭐ 23.9k · Apache-2.0 · 多言語の音声生成モデル。推論・学習・デプロイのコード一式付き。
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) - `Repo` · ⭐ 11.8k · Apache-2.0 · 歌詞からボーカル入りのフルソングを生成するオープンな音楽生成モデル。カバーや楽曲編集にも対応。 ⚠️ コードは Apache-2.0 ですが、モデル重みは CC BY-NC 4.0（個人ユーザー・ミュージシャン向けの追加許諾あり）です。企業の商用利用には別途商用ライセンスが必要です。
- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) - `Repo` · ⭐ 57.1k · MIT · Qwen3-TTS と Whisper をベースにした、ローカルで動くオープンソースの音声スタジオ。声のクローンと音声合成ができます。
- [remsky/Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI) - `Repo` · ⭐ 5.5k · Apache-2.0 · Kokoro-82M TTS を OpenAI 互換 API として動かす Docker 構成。CPU でも GPU でも動作します。
- [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) - `Repo` · ⭐ 20.3k · Apache-2.0 · 電子書籍を章立て付きのオーディオブックに変換。声のクローンと 1,100 以上の言語に対応。 ⚠️ コードは Apache-2.0 ですが、一部のエンジンの重みは別ライセンスです（例：XTTSv2 は非商用の Coqui Public Model License）。商用ではエンジンを選んでください。
- [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - `Repo` · ⭐ 4.2k · Apache-2.0 · 長文読み上げ、複数話者の対話、ボイスデザイン、効果音、リアルタイム TTS を扱うオープンモデル群。中国語に強いのが特長。
- [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) - `Repo` · ⭐ 14.5k · Apache-2.0 · next-gen Kaldi（k2-fsa）チームによる 600 以上の言語に対応したゼロショット音声クローン TTS。pip で導入でき、Python のクイックスタートと Hugging Face デモが用意されています。 ⚠️ リポジトリの LICENSE は Apache-2.0 ですが、重みは Hugging Face（k2-fsa/OmniVoice）にあり、2026-10-12 時点で重み単体のライセンス表記はありません。商用前に確認してください。
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) - `Repo` · ⭐ 60.2k · AGPL-3.0 · 完全ローカルで動くデスクトップ音声スタジオ。音声クローン、ボイスデザイン、動画の吹き替え、ディクテーション、文字起こし、オーディオブックを 646 言語で扱え、ローカル HTTP API と MCP サーバーも同梱。 ⚠️ アプリ本体は AGPL-3.0 ですが、同梱モデルはそれぞれ独自のライセンスです。商用前にモデルごとの条項も確認してください。
- [0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp) - `Repo` · ⭐ 3.5k · Apache-2.0 · ggml ベースの純 C++ 音声推論エンジン。TTS、音声認識、VAD、ボイスコンバージョン、音楽生成をひとつでカバーし、CPU・CUDA・Vulkan・AMD・Apple Silicon に対応します。
- [leemysw/yovoice](https://github.com/leemysw/yovoice) - `Repo` · ⭐ 1.1k · Apache-2.0 · macOS と Windows 向けのデスクトップアプリ。クラウド API も文字課金もなしで、ローカルの TTS・音声クローン・感情コントロールを行います。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) - `Skill` · ⭐ 983 · MIT · コーディングエージェントに「耳」を与える CPU 専用ツール。効果音や動画のサウンドトラックを説明・照合・レビューし、コードで作った 201 種の効果音ライブラリからフレーム単位でタイミングを合わせた SFX を書き出せます（CLI、MCP サーバー、Claude Code スキル対応）。

## 吹き替えと字幕

- [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) - `Repo` · ⭐ 18.8k · Apache-2.0 · 字幕の分割・翻訳・タイミング調整から吹き替えまでを自動でつなぐパイプライン。
- [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans) - `Repo` · ⭐ 19.3k · GPL-3.0 · 動画を別の言語に翻訳し、吹き替え音声と字幕を付けます。
- [buxuku/SmartSub](https://github.com/buxuku/SmartSub) - `Repo` · ⭐ 5.7k · MIT · Windows / macOS / Linux 対応のデスクトップアプリ。ローカル文字起こし、字幕翻訳、AI 吹き替え、字幕の焼き込み。
- [m-bain/whisperX](https://github.com/m-bain/whisperX) - `Repo` · ⭐ 24.5k · BSD-2-Clause · 単語単位のタイムスタンプと話者分離付きの音声認識。
- [liuzhao1225/YouDub-webui](https://github.com/liuzhao1225/YouDub-webui) - `Repo` · ⭐ 5.6k · Apache-2.0 · YouTube や Bilibili 動画のローカライズを一括処理。音声認識、字幕翻訳、声をクローンした吹き替え、最終合成まで。
- [tmoroney/auto-subs](https://github.com/tmoroney/auto-subs) - `Repo` · ⭐ 4.3k · MIT · 端末上で字幕を生成し、DaVinci Resolve・Premiere Pro・After Effects に直接連携します。 ⚠️ 単語単位タイムスタンプ用のオプションの MMS 強制アライメント重みは CC BY-NC 4.0（非商用）です。
- [R3gm/SoniTranslate](https://github.com/R3gm/SoniTranslate) - `Repo` · ⭐ 1.4k · Apache-2.0 · 話者分離と複数の TTS エンジンに対応した、動画の同期翻訳・吹き替え Web UI。 ⚠️ コードは Apache-2.0 ですが、README によると使用する一部のモデル（pyannote の話者分離など）には商用制限があります。
- [shang-zhu/violin](https://github.com/shang-zhu/violin) - `Skill` · ⭐ 1.1k · MIT · 動画を別の言語へ翻訳・吹き替えまで一気に行うオープンソースのエージェントスキル。

## リップシンクとデジタルヒューマン

- [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) - `Repo` · ⭐ 8k · Apache-2.0 · 音声駆動で長さ制限のないトーキング動画を生成。画像からも既存動画からも作れます。
- [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) - `Repo` · ⭐ 19.2k · MIT · ドライビング動画に合わせて静止画のポートレートを動かします。 ⚠️ コードは MIT ですが、同梱の InsightFace 検出モデルは非商用限定です。商用利用では差し替えが必要です。
- [lipku/LiveTalking](https://github.com/lipku/LiveTalking) - `Repo` · ⭐ 9.9k · Apache-2.0 · 音声と映像を同期させて会話できるリアルタイム配信型デジタルヒューマン。ライブ配信アバターの土台として定番です。
- [modstart-lib/aigcpanel](https://github.com/modstart-lib/aigcpanel) - `Repo` · ⭐ 5.6k · Apache-2.0 · 口パク動画の合成、音声合成、声のクローンをまとめたデスクトップのデジタルヒューマンアプリ。ローカルモデルをワンクリックで導入できます。
- [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) - `Repo` · ⭐ 4k · Apache-2.0 · 1 枚の写真から表情豊かに動かせる、ライブ配信向けのリアルタイム肖像アニメーション（CVPR 2026）。 ⚠️ LICENSE ファイルは Apache-2.0 ですが、README では学術研究目的のみの公開とされています。商用利用の前に作者へ確認してください。
- [cclank/lanshu-create-ai-presenter-video](https://github.com/cclank/lanshu-create-ai-presenter-video) - `Skill` · ⭐ 2.6k · MIT · ベンダー非依存の Codex / Claude Code スキル。台本と許諾済みの人物写真 1 枚から、TTS・リップシンク・字幕を通して完成した語り手動画を作り、各工程を検証します。

## 広告・マーケティング動画

- [latent-spaces/brag](https://github.com/latent-spaces/brag) - `Repo` · ⭐ 15.5k · MIT · 作ったばかりのプロジェクトを、コマンド一つでシェアできるローンチ動画にします。
- [op7418/guizang-product-video-skill](https://github.com/op7418/guizang-product-video-skill) - `Skill` · ⭐ 780 · AGPL-3.0 · 実際のプロダクトのコンポーネントを使い、コードでソフトウェアの紹介動画を作るスキル。絵コンテ、オリジナル BGM、効果音、レンダリングまで。 ⚠️ 全体は AGPL-3.0 ですが、CodePilot 由来のデフォルトスタイルは元の BSL ライセンスのままです。
- [Kianzzz/book-sales-video](https://github.com/Kianzzz/book-sales-video) - `Skill` · ⭐ 223 · MIT · 中国語の書籍 PR 動画を作るスキル。原稿取得と書籍確認のあと、ナレーション、画像、二言語字幕、自動編集まで行います。
- [token360-community/ecom-image-skill](https://github.com/token360-community/ecom-image-skill) - `Skill` ⚡ · 🔷 Token360 版（元: [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce)） · ⭐ 411 · MIT · buluslan による EC 向けビジュアル生成スキル（商品ページ・広告用テンプレート 39 種と 16 フレームの商品モーション GIF）を Token360 の画像モデル向けに設定済みで、検証済みサンプル付き。出力は静止画とループ GIF で、動画ではありません。

## ComfyUI と MCP コネクタ

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - `Repo` · ⭐ 137.1k · GPL-3.0 · 画像・動画・音声の拡散モデルをノードグラフで組むエンジンと GUI。
- [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) - `Node` · ⭐ 1.2k · GPL-3.0 · MiniMax H3 のクリップをつなぎ、つなぎ目でも動きと音声が続くようにする ComfyUI ノード。サンプルワークフロー付き。
- [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) - `MCP` · ⭐ 816 · MIT · MCP サーバーとサイドバーエージェントで、LLM から ComfyUI の画像・動画・音声ワークフローを組み立て・実行・編集できます。 ⚠️ README によると現在は限定的なメンテナンス（重大な修正のみ）です。
- [pireel/pireel](https://github.com/pireel/pireel) - `MCP` · ⭐ 1.3k · AGPL-3.0 · キャンバスとタイムラインを備えたオープンソースの動画エディター。AI エージェントから MCP で操作できます。
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) - `MCP` · ⭐ 3.5k · MIT · エージェントから DaVinci Resolve Studio のタイムライン、マーカー、レンダリングを操作できる MCP サーバー。
- [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) - `MCP` · ⭐ 1.6k · MIT · MiniMax 公式の MCP サーバー。音声合成、声のクローン、動画・音楽生成に対応。
- [Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp) - `MCP` · ⭐ 272 · AGPL-3.0 · Comfy Org 公式のローカル MCP サーバー。エージェントからローカルの ComfyUI ワークフローを実行・確認できます。
- [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) - `MCP` · ⭐ 3.2k · MIT · LLM から Ableton Live を操作してトラック作成、クリップの配置、作曲ができる MCP サーバー。
- [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) - `Node` · ⭐ 2.3k · Apache-2.0 · ComfyUI 公式の MiniMax H3 ノード向けの、複数セグメントを演出するディレクターノード。サンプルワークフロー付き。 ⚠️ コードは Apache-2.0 ですが、MiniMax H3 の重みは独自の MiniMax H3 Community License（米国・EU・英国・韓国のユーザーは申請が必要）です。商用利用の前に確認してください。
- [Carasibana/ComfyUI-H3-FaceRefine](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) - `Node` · ⭐ 464 · MIT · MiniMax H3 の出力でぼやけがちな小さい顔を直す ComfyUI ノード。フレームごとの顔追跡、切り出し、H3 での再生成、貼り戻しまで行い、サンプルワークフロー 2 本付き。

## ワークフロー解説（投稿）

- [@GeekCatX — 4 ステップで作る Vox 風解説動画](https://x.com/GeekCatX/status/2078488413045747814) - `Post` · 2026-07 · 動画生成 · 4 ステップ：Codex と vox-style スキルで絵コンテのプロンプトを作り、画像モデルでコマを生成、動画モデルで動かし、最後に自動編集。
- [@newbeeyu — Codex + Remotion で作る唐代風切り絵アニメ](https://x.com/newbeeyu/status/2076530524110369070) - `Post` · 2026-07 · 編集・モーション · X の長文記事。Codex と Remotion でコードから作る唐代風の切り絵レイヤーアニメ。レイヤー分け、タイミング、レイヤーごとの効果音を解説。
- [@EXM7777 — Claude Code で組む AI 動画制作パイプライン](https://x.com/EXM7777/status/2082107255449919582) - `Post` · 2026-07 · 編集・モーション · X の長文記事。Claude Code を動画制作パイプラインとして組む手順と、ショット設計で参照する資料サイトを紹介。
- [@Pluvio9yte — Codex + Hyperframes + HeyGen + 声のクローンの全工程](https://x.com/Pluvio9yte/status/2081580929492131947) - `Post` · 2026-07 · 音声・TTS · X の長文記事（中国語）。Codex を司令塔に、Hyperframes でモーション、HeyGen でアバター、IndexTTS で音声を作るショート動画の全工程。
- [@0xMovez — Opus 5.5 でモーションデザインスタジオを作る（フルコース）](https://x.com/0xMovez/status/2104216919033192746) - `Post` · 2026-09 · 編集・モーション · 12 ステップの長文講座。スタジオの導入、監督のようなプロンプト、seek(t) レンダラーの構築、スプリングでの動きの調整、ビートに合わせた音付け、Opus による自己チェック、多フォーマット書き出しとスキル化まで。
- [@Bytec99 — Codex + HyperFrames で書籍紹介ショートを全自動生成](https://x.com/Bytec99/status/2075372048994672994) - `Post` · 2026-07 · 編集・モーション · 長文解説：Codex が本を選んで 30 秒のナレーションを書き、VoxCPM で音声化、faster-whisper で字幕合わせ、FFmpeg で BGM を調整し、HyperFrames でレンダリング。再利用できるスキルにまとめています。
- [@tetsuoai — Grok Imagine で短編映画を最初から最後まで作る](https://x.com/tetsuoai/status/2085365652509040768) - `Post` · 2026-08 · 動画生成 · 長文ガイド：一行のアイデアをビート台本にし、キャラクターシートと場所・小道具の参照を作って Grok Imagine に読み込み、ビートごとに独立したプロンプトで生成、最後に編集でつなぎます。プロンプトは全文掲載。
- [@claudeskills101 — Claude Code で作る解説動画プロンプト 8 種](https://x.com/claudeskills101/status/2107170117243310471) - `Post` · 2026-10 · 編集・モーション · スレッドで 8 種類の完全なプロンプト（キネティックタイポ、ホワイトボード、アイソメ、データチャート、Manim、アプリ紹介、紙コラージュ、トーキングヘッド自動編集）を公開。それぞれ「避けること」と完成条件付き。
- [@showheyohtaki — AI に指示するための動画のカメラワークと切り替えの名前](https://x.com/showheyohtaki/status/2109112248832503895) - `Post` · 2026-10 · 動画生成 · FPV、ラックフォーカス、ホイップパンなどカメラワークと切り替えの名前をまとめた早見表。Claude や Codex、動画モデルに狙いどおりの演出を指示できます。
- [@GeekCatX — MiniMax H3 で作る地下鉄お着替え動画](https://x.com/GeekCatX/status/2096513305930297353) - `Post` · 2026-09 · 動画生成 · 話題の地下鉄お着替え動画を、逆算プロンプト用スキルと MiniMax H3 の画像から動画モードで再現。完全なプロンプトはスレッド内にあります。

## 注目の作り手

- [@HeyAbhishek](https://x.com/HeyAbhishek) - `Person` · EN · Seedance アニメのプロンプト · シネマティックな AI アニメ動画の完全なプロンプトを公開しています。例: [投稿](https://x.com/HeyAbhishek/status/2106369769956065518)。
- [@liyue_ai](https://x.com/liyue_ai) - `Person` · 中文 · Seedance 監督スキル · GitHub（liyue-aigc）で Seedance 用の監督スキルをオープンソース公開しています。例: [投稿](https://x.com/liyue_ai/status/2093592225162960982)。
- [@Pluvio9yte](https://x.com/Pluvio9yte) - `Person` · 中文 · エージェント駆動の動画制作 · Codex + Hyperframes の動画パイプラインと、その裏のスキルを長文で解説しています。例: [投稿](https://x.com/Pluvio9yte/status/2081648099680743554)。
- [@GeekCatX](https://x.com/GeekCatX) - `Person` · 中文 · 低コストの解説動画ワークフロー · エージェントと画像・動画モデルで低コストに解説動画を作る手順を発信しています。例: [投稿](https://x.com/GeekCatX/status/2078488413045747814)。

## 関連リスト

- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) - `List` · ⭐ 2k · MIT · Seedance 2.5 / 2.0 のプロンプト集。元投稿をたどれる事例、テンプレート、インストールできる動画スキル付き。
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - `List` · ⭐ 2.7k · MIT · Seedance 2.0 のプロンプト、ガイド、動画生成ワークフローのまとめ。
- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) - `List` · ⭐ 34.4k · MIT · GPT Image 2 / 2.5 のプロンプトと事例集（テンプレート付き）。動画化前のキーフレームや絵コンテ作りに。
- [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) - `List` · ⭐ 2.1k · CC-BY-4.0 · 映画風、アニメ、UGC、広告、ミームなど 2,000 以上の Seedance 2.0 動画プロンプトを厳選。API ガイドとキャラクター一貫性のコツ付き。

## コントリビュート

`data/catalog.json` だけを編集し（README は直接編集しない）、`python3 scripts/generate_readme.py` を実行してから PR を出してください。先に [CONTRIBUTING.ja.md](./CONTRIBUTING.ja.md) の基準を読んでください。基準に満たない項目はマージせずにクローズします。

---

<sub>リストの内容は [CC0 1.0](./LICENSE) で公開しています。リンク先のプロジェクト・投稿・商標は各権利者に帰属し、掲載は権利者や Token360 による推奨を意味しません。</sub>

<sub>※ この日本語版は機械翻訳による下書きで、ネイティブスピーカーのレビュー前です。誤りに気づいたら Issue でお知らせください。</sub>

<h1 align="center">
  <img src="./assets/banner.webp" alt="Awesome Video & Audio Hacks, by Token360" width="800" />
  <br />
  Awesome Video &amp; Audio Hacks
</h1>

<!-- GENERATED from data/catalog.json by scripts/generate_readme.py. Do not edit by hand. -->

<p align="center">
  <strong>EN</strong> · <a href="./README.zh-CN.md">简体中文</a> · <a href="./README.ja.md">日本語</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/entries-121-9633af" alt="entries: 121" />
  <img src="https://img.shields.io/badge/last_verified-2026--10--11-informational" alt="last verified: 2026-10-11" />
  <img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey" alt="License: CC0-1.0" />
</p>

> A strictly curated list of open-source workflows, agent skills, MCP servers and reproducible posts for AI **video, voice, music, dubbing, lip-sync and editing**. Every entry must meet a written bar (see [Contributing](#contributing)) and is re-checked at least every 30 days. Maintained by the [Token360](https://www.token360.ai?utm_source=github&utm_medium=awesome&utm_campaign=avah) developer community.

**Tags:** `Repo` `Skill` `MCP` `Node` `Post` `Person` `List` · ⛔ link-only (non-commercial or source-available license) · ⚠️ read the note before using commercially

⚡ = run end to end on Token360, with a published guide; entries without ⚡ have not been tested. 🔷 Token360 edition = a fork maintained by the Token360 community that adds a tested Token360 quick start; the work, credit and license stay with the original author, and ⭐ shows the original repo's stars.

<sub>121 entries across 11 sections · last verified 2026-10-11</sub>

## Token360 quickstart

Token360 serves text, image and video models behind one OpenAI-compatible `base_url`.

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

| Modality | Endpoint                          | Example model ids                                                    |
| -------- | --------------------------------- | -------------------------------------------------------------------- |
| Text     | `POST /chat/completions`          | `claude-sonnet-5-5`, `gpt-6-sol`, `deepseek-v4.1-flash`              |
| Image    | `POST /images/generations`        | `gpt-image-2`, `dola-seedream-5.0-pro`, `nano-banana-2`              |
| Video    | `POST /videos → GET /videos/{id}` | `seedance-2.5`, `veo-3.1-generate-001`, `wan3.0-video`, `minimax-h3` |
| Audio    | _pending verification_            | `seed-audio-1.0`, `glm-asr-2512`                                     |

<sub>Model ids from the public `GET /v1/models` on 2026-10-11. Routes answer with an auth error without a key. Entries marked ⚡ were run end to end on Token360 (see their guides); everything else has not been tested yet.</sub>

Full model list and per-model request examples: [token360.ai/models](https://www.token360.ai/models?utm_source=github&utm_medium=awesome&utm_campaign=avah).

## Contents

- [Video generation & prompting](#video-generation--prompting) (12)
- [Short drama & storytelling](#short-drama--storytelling) (9)
- [Editing & motion agents](#editing--motion-agents) (28)
- [Voice, TTS & music](#voice-tts--music) (20)
- [Dubbing & subtitles](#dubbing--subtitles) (8)
- [Lip-sync & digital humans](#lip-sync--digital-humans) (7)
- [Ads & marketing video](#ads--marketing-video) (7)
- [ComfyUI & MCP connectors](#comfyui--mcp-connectors) (11)
- [Workflow breakdowns (posts)](#workflow-breakdowns-posts) (11)
- [People to follow](#people-to-follow) (4)
- [Related lists](#related-lists) (4)

## Video generation & prompting

- [HKUDS/ViMax](https://github.com/HKUDS/ViMax) - `Repo` · ⭐ 12.7k · MIT · Agentic video generation in one pipeline: idea → script → storyboard → shots, with director, screenwriter and producer agents.
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - `Repo` · ⭐ 133.2k · MIT · Generates a finished short video from a topic or keyword: script, stock footage, voice-over, subtitles and music in one automated workflow.
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) - `Skill` · ⭐ 7.8k · MIT · Production-pipeline skill for Seedance 2.0 filmmaking across text, image, video and audio inputs.
- [liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) - `Skill` · ⭐ 715 · MIT · Seedance 2.5 "video director" skill: prompts, scripts, character locking, continuation, edits and transitions.
- [s1dashu/director](https://github.com/s1dashu/director) - `Skill` · ⭐ 814 · MIT · Skill that directs a complete video end to end: research, script, visual development, shot design, media generation and delivery.
- [krillinai/OpenCreator](https://github.com/krillinai/OpenCreator) - `Repo` · ⭐ 13.7k · Apache-2.0 · Desktop AI video studio that goes from script to generated, dubbed and localized video, with built-in agent skills.
- [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) - `Skill` · ⭐ 4.4k · MIT · Agent skill that writes model-ready Seedance 2.x video prompts from a plain idea.
- [token360-community/seedance-prompt-skill](https://github.com/token360-community/seedance-prompt-skill) - `Skill` ⚡ · 🔷 Token360 edition of [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) · ⭐ 4.4k · MIT · Dex's Seedance prompt-writing skill plus a standard-library Python script that renders the prompts as Seedance 2.5 clips on Token360, with sample clips.
- [FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo) - `Repo` · ⭐ 2.2k · Apache-2.0 · Runs the open MiniMax H3 audio-video model on consumer GPUs and Macs, with community speed reports per card. ⚠️ Code is Apache-2.0, but the MiniMax H3 weights use the custom MiniMax H3 Community License (users in the US/EU/UK/South Korea must apply); read it before commercial use.
- [edenfunf/reelmimic](https://github.com/edenfunf/reelmimic) - `Repo` · ⭐ 3.7k · MIT · Point it at a video you like and a multi-agent crew in Claude Code or Codex plans, builds and reviews a new video in the same style with you.
- [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) - `Skill` · ⭐ 2.4k · MIT · A tested library of stick-figure animation styles turned into a director skill: give it a topic and it returns a director's proposal for your approval, then one standalone prompt per ten-second clip with voice-over and sound-effect cues, in four visual styles and any length in ten-second steps.
- [Agents365-ai/video-podcast-maker](https://github.com/Agents365-ai/video-podcast-maker) - `Skill` · ⭐ 1.7k · MIT · A topic becomes a 4K narrated video podcast in one pipeline: research, script, local Edge or Azure TTS with no external engine, a per-video asset manifest that records each clip's licence, Remotion-native subtitles, a 9:16 highlight cut and per-platform publishing copy.

## Short drama & storytelling

- [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) - `Repo` · ⭐ 18.4k · MIT · Self-hostable short-drama and motion-comic tool: script writing, storyboards, character/scene assets and image/video generation on an infinite canvas with agents.
- [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) - `Repo` · ⭐ 4.7k · AGPL-3.0 · Batch script-to-final-cut production tool for AI drama, with Seedance 2.0 support.
- [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) - `Repo` · ⭐ 2.1k · MIT · Local-first short-drama maker: story → storyboard → video, with project data kept on your machine.
- [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) - `Skill` · ⭐ 3.1k · MIT · Skill set for AI micro-dramas in Claude Code and Codex: script, character assets, storyboard, image/video prompts and review.
- [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) - `Skill` · ⭐ 4.8k · Apache-2.0 · Agent skills for short-drama pre-production: character bibles, adaptation outlines, art bibles, screenplays and storyboards.
- [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) - `Repo` · ⭐ 5.6k · AGPL-3.0 · Self-hosted agent workspace that turns a novel or script into character and scene assets, storyboards, consistent shots and a JianYing/CapCut draft, with cost tracking.
- [FireRedTeam/FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline) - `Repo` · ⭐ 3.5k · Apache-2.0 · Video editing agent that turns manual cutting into directing by natural language, with MCP and agent-skill integrations.
- [alibaba/lumenx](https://github.com/alibaba/lumenx) - `Repo` · ⭐ 1.4k · MIT · Alibaba's open-source studio that turns novel text into animated short dramas: script analysis, character design, storyboards and video assembly.
- [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama) - `Repo` ⛔ · ⭐ 16.4k · CC-BY-NC-SA-4.0 · The most-starred Chinese AI short-drama pipeline, from script to storyboard to generated episodes; listed as the category reference.

## Editing & motion agents

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) - `Repo` · ⭐ 69.9k · AGPL-3.0 · Agentic video production system that turns an AI coding assistant into a production pipeline, with many ready-made pipelines and tools.
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) - `Repo` · ⭐ 67.7k · Apache-2.0 · Write HTML, render video: a motion framework designed to be driven by agents.
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - `Skill` · ⭐ 12.5k · Apache-2.0 · Claude Code / Codex skill for cinematic product videos with Remotion: shot recipe cards, motion previews and a production template. ⚠️ Renders with Remotion, whose own license requires a paid company license for some commercial use.
- [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) - `Repo` · ⭐ 95.4k · MIT · Free, open-source video editor for web, desktop and mobile, built as a CapCut alternative.
- [luoluoluo22/jianying-editor-skill](https://github.com/luoluoluo22/jianying-editor-skill) - `Skill` · ⭐ 4.3k · MIT · Agent skill that automates editing in JianYing (the Chinese edition of CapCut) by writing its project drafts.
- [browser-use/video-use](https://github.com/browser-use/video-use) - `Repo` · ⭐ 29.4k · MIT · From the browser-use team: lets coding agents cut raw footage into a finished edit from word-level transcripts, with burned-in subtitles.
- [linyqh/NarratoAI](https://github.com/linyqh/NarratoAI) - `Repo` · ⭐ 11.5k · MIT · One-click film and TV commentary videos: the LLM writes the narration, then voice-over and cut are generated automatically.
- [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) - `Repo` · ⭐ 9.6k · MIT · Turns long podcasts, interviews and courses into short clips with subtitles, covers and post copy for Douyin, Xiaohongshu, TikTok, Reels and Shorts.
- [GuanYixuan/pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) - `Repo` · ⭐ 4.6k · Apache-2.0 · Python library that generates and exports JianYing (CapCut China) drafts, the building block behind many automated editing pipelines.
- [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) - `Skill` · ⭐ 3.1k · Apache-2.0 · Claude Code skills that act as a talking-head video editor: trims filler words and pauses, adds subtitles and exports the cut.
- [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) - `Skill` · ⭐ 4.6k · MIT · Skill that turns an SRT subtitle file into a hand-drawn whiteboard animation on warm paper, stroke by stroke.
- [jub0t/Concat](https://github.com/jub0t/Concat) - `Repo` · ⭐ 9.5k · AGPL-3.0 · Local cross-platform video editor on a native Rust engine with offline Whisper captions, text-to-speech and voice cloning, background removal and a JSON-RPC, gRPC and MCP API so agents can cut video too. ⚠️ Still labelled beta by the author; the README also carries a paid sponsor slot with an affiliate code for an unrelated proxy service.
- [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) - `Skill` · ⭐ 4.5k · MIT · Agent skill that writes art-styled animation as code: 35 painting styles, 9 narration grammars, 8 parametric segment types and a full voiced-film reference, installed with one npx command.
- [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) - `Skill` · ⭐ 1.9k · MIT · Fourteen Codex and Claude Code skills for cutting reels and YouTube Shorts from a transcript, with 406 motion-graphics cards and HyperFrames templates, and a fixture that renders without footage or an API key. ⚠️ The author's own setup uses ElevenLabs Scribe and the Kie.ai model API; both are optional (local Whisper or an existing transcript works) and generated assets are not required.
- [glanderness/BeefTV](https://github.com/glanderness/BeefTV) - `Repo` · ⭐ 1.6k · MIT · Lightweight local-first video workspace where an infinite canvas wires prompts, models and footage together, so an agent and a human can iterate on the same board.
- [Barty-Bart/motion-graphics](https://github.com/Barty-Bart/motion-graphics) - `Skill` · ⭐ 752 · MIT · Motion-graphics skills for Claude Code and Codex, including a b-roll engine with bundled fonts, committed to daily.
- [hypit-ai/hypit](https://github.com/hypit-ai/hypit) - `Repo` ⛔ · ⭐ 24k · Modified Apache-2.0 · Agent skill and CLI that clone a viral video into an editable, word-timed workflow (footage, captions, B-roll and effects) and re-render it as many variants; listed as the category reference. ⚠️ Source-available: a modified Apache-2.0 that bars offering it as a multi-tenant or SaaS service and redistributing it commercially (outputs are yours); the docs default to Hypit's own hosted HypiHub and partner model APIs, some via referral links, though local and bring-your-own providers also work.
- [threerocks/sweety-handdraw-video](https://github.com/threerocks/sweety-handdraw-video) - `Skill` · ⭐ 723 · MIT · Codex / Claude Code skill that turns a topic or article into a finished hand-drawn explainer video: part-by-part line drawing, word-by-word handwriting and a voiceover, with its production dependencies bundled. ⚠️ Very new (created 2026-10-12, single maintainer); the default voiceover goes through VoiceStudio, whose bundled models carry their own licences.
- [alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle) - `Skill` · ⭐ 1k · Apache-2.0 · Claude Code / Codex plugin that writes art and animation as code: hand-drawn illustrations, loops, launch videos and scored short films in dozens of styles, rendered deterministically.
- [academa-labs/manimgx](https://github.com/academa-labs/manimgx) - `Repo` · ⭐ 1.9k · MIT · Agent-friendly animation engine that keeps Manim's Python API on a Rust GPU core, rendering math and 3D explainer videos to MP4 far faster; pip install, with an llms.txt your coding agent can follow. ⚠️ Created 2026-10-05; early releases (v0.1.x).
- [remotion-dev/remotion](https://github.com/remotion-dev/remotion) - `Repo` ⛔ · ⭐ 65.3k · Remotion License · The reference framework for making videos programmatically with React; most coding-agent video skills (HyperFrames-style templates, motion-design skills) build on it.
- [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) - `Skill` · ⭐ 2k · MIT · Turns FFmpeg into 42 contract-checked tools a coding agent can drive: cuts, burned-in captions, reframing, loudness normalisation and per-platform exports, as a skill and an MCP server, with no cloud and no API keys.
- [0xsline/OpenChatCut](https://github.com/0xsline/OpenChatCut) - `Repo` · ⭐ 2.5k · AGPL-3.0 · Local-first conversational video editor: tell it the edit in chat and it works a professional multi-track timeline, renders through Remotion, and exposes the same pipeline as Agent Skills and an MCP server. ⚠️ Image and video generation providers are bring-your-own-key (OpenAI, Gemini, Seedance, Kling, optionally Fal); generation is billed to your own provider account.
- [openfilm/openfilm](https://github.com/openfilm/openfilm) - `Repo` · ⭐ 1.3k · MIT · Your coding agent writes a film as plain web pages, one `frame(t)` function per shot, and Studio, a local browser editor, lets you move, restyle, trim and recut anything it made before rendering the MP4; no framework and no account.
- [Leonxlnx/cinetic](https://github.com/Leonxlnx/cinetic) - `Skill` · ⭐ 677 · MIT · Agent skill that directs a launch film instead of arranging components: it writes three concepts, draws a shot plan from 273 timed techniques, derives a brand from three personality words, scores it with code-rendered sound, and ships only after motion-blur, sync and critic gates, on Remotion or HyperFrames.
- [zenstory-ai/video-recap-skills](https://github.com/zenstory-ai/video-recap-skills) - `Skill` · ⭐ 582 · MIT · Seven agent skills that turn one or more source videos into a finished Chinese narration recap: the agent reads picture and dialogue, plans the story, cuts, writes, voices, mixes and subtitles it, needing only ffmpeg locally, and can export the result as a Jianying draft to keep editing.
- [FavioVazquez/showtime](https://github.com/FavioVazquez/showtime) - `Skill` · ⭐ 267 · MIT · Describe a video in one sentence and a crew of agent skills directs it while your own machine renders it, no GPU required; the project's 55-second showreel was rendered in 2 min 23 s on CPU, and it ships as a skill pack, an MCP server and a plugin.
- [Orkas-AI/Orkas-VideoStudio](https://github.com/Orkas-AI/Orkas-VideoStudio) - `Skill` · ⭐ 331 · MIT · Not a black-box video agent: a video is a readable, diffable `plan.json` that you and your agent can edit line by line, with only the changed piece re-rendering, over thin deterministic wrappers around HyperFrames, ffmpeg and whisper.cpp, driven from a shell or over MCP.

## Voice, TTS & music

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - `Repo` · ⭐ 63.2k · MIT · Few-shot voice cloning and TTS: about one minute of reference audio is enough to train a voice.
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) - `Repo` · ⭐ 39.6k · Apache-2.0 · Tokenizer-free multilingual TTS with voice design and voice cloning.
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - `Repo` · ⭐ 27.1k · MIT · Open-source TTS model family from Resemble AI.
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) - `Repo` · ⭐ 24.1k · Apache-2.0 · Multilingual voice generation model with inference, training and deployment code.
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) - `Repo` · ⭐ 12.3k · Apache-2.0 · Music-generation model that turns lyrics into full songs with vocals, plus covers and music editing. ⚠️ Code is Apache-2.0, but the model weights are CC BY-NC 4.0 with an extra permission for individual users and musicians; companies need a commercial license.
- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) - `Repo` · ⭐ 58k · MIT · Local, open-source voice studio for cloning voices and generating speech, built on Qwen3-TTS and Whisper.
- [remsky/Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI) - `Repo` · ⭐ 5.6k · Apache-2.0 · Dockerized, OpenAI-compatible speech API for the Kokoro-82M TTS model that runs on CPU or GPU.
- [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) - `Repo` · ⭐ 20.4k · Apache-2.0 · Converts e-books into audiobooks with chapters and voice cloning, in 1,100+ languages. ⚠️ Code is Apache-2.0, but some supported engines ship weights under their own terms (e.g. XTTSv2 under the non-commercial Coqui Public Model License); pick the engine accordingly for commercial use.
- [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - `Repo` · ⭐ 4.2k · Apache-2.0 · Open model family for long-form speech, multi-speaker dialogue, voice design, sound effects and real-time TTS, with strong Chinese support.
- [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) - `Repo` · ⭐ 15k · Apache-2.0 · Zero-shot voice-cloning TTS for 600+ languages from the next-gen Kaldi (k2-fsa) team, with a pip install, a Python quick start and a Hugging Face demo space. ⚠️ Repo LICENSE is Apache-2.0; the weights live on Hugging Face (k2-fsa/OmniVoice) and no separate weights licence was published there as of 2026-10-12 — check before commercial use.
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) - `Repo` · ⭐ 77.5k · AGPL-3.0 · Fully local desktop studio for voice cloning, voice design, video dubbing, dictation, transcription and audiobooks in 646 languages, with a local HTTP API and an MCP server. ⚠️ App code is AGPL-3.0 but each bundled model keeps its own licence; also check the per-model terms before commercial use.
- [0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp) - `Repo` · ⭐ 3.6k · Apache-2.0 · One ggml-based C++ engine for all the audio models in a video pipeline: TTS, speech-to-text, VAD, voice conversion and music generation, with CPU, CUDA, Vulkan, AMD and Apple Silicon backends.
- [leemysw/yovoice](https://github.com/leemysw/yovoice) - `Repo` · ⭐ 1.7k · Apache-2.0 · Desktop app for macOS and Windows that does local text-to-speech, voice cloning and emotion control with no cloud API and no per-character fees.
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) - `Skill` · ⭐ 1.5k · MIT · Ears for coding agents on CPU: describe, match and review sounds and film soundtracks, and render frame-timed effects from a 201-sound library made in code, via CLI, MCP server or Claude Code skills.
- [FluidInference/FluidAudio](https://github.com/FluidInference/FluidAudio) - `Repo` · ⭐ 3.1k · Apache-2.0 · Swift SDK that runs CoreML audio models on Apple devices: text-to-speech, speech-to-text (Parakeet), voice activity detection and speaker diarization, fully on-device.
- [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) - `Repo` · ⭐ 13.8k · MIT · Local music-generation model and CLI that writes full songs with vocals from a prompt and lyrics, running on CUDA, ROCm, Intel XPU, Apple MPS or plain CPU.
- [sgl-project/sglang-omni](https://github.com/sgl-project/sglang-omni) - `Repo` · ⭐ 1.6k · Apache-2.0 · Serving runtime that puts open speech, TTS and music models behind one OpenAI-compatible API, with streaming speech, uploaded voices, transcription with speaker labels, and a multi-worker router.
- [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) - `Repo` ⛔ · ⭐ 33.3k · Fish Audio Community License 1.0 · The reference open-weights TTS stack for multilingual, multi-speaker speech with voice cloning, shipped with a web UI, a serving API and Docker images. ⚠️ Not an OSI licence: commercial use is capped at USD 500,000 annual revenue and running it as a hosted text-to-speech or voice-cloning service requires a separate agreement with Fish Audio.
- [Tencent-Hunyuan/AuK](https://github.com/Tencent-Hunyuan/AuK) - `Repo` · ⭐ 1.5k · MIT · Open weights for speech generation and, unusually, speech editing: zero-shot TTS, voice cloning, enhancement, separation and speaker extraction in one model, with a distillation pipeline for the faster Flash variant, ComfyUI nodes, MLX on Apple Silicon and GGUF offline inference through audio.cpp.
- [bitwize-music-studio/claude-ai-music-skills](https://github.com/bitwize-music-studio/claude-ai-music-skills) - `Skill` · ⭐ 572 · CC0-1.0 · Turns a conversation into a full album production line: concept planning, parallel research with cross-verified sources, lyrics, Suno prompts, audio mastering and release prep, with a quality gate at every stage. ⚠️ The generation step goes through your own paid Suno account; the repo ships the workflow, prompts and mastering, not a local model.

## Dubbing & subtitles

- [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) - `Repo` · ⭐ 18.8k · Apache-2.0 · Subtitle segmentation, translation, alignment and dubbing in one automated pipeline.
- [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans) - `Repo` · ⭐ 19.5k · GPL-3.0 · Translates a video into another language and adds dubbed audio and subtitles.
- [buxuku/SmartSub](https://github.com/buxuku/SmartSub) - `Repo` · ⭐ 5.8k · MIT · Desktop app for local speech-to-text, subtitle translation, AI dubbing and burn-in, on Windows, macOS and Linux.
- [m-bain/whisperX](https://github.com/m-bain/whisperX) - `Repo` · ⭐ 24.7k · BSD-2-Clause · Speech recognition with word-level timestamps and speaker diarization.
- [liuzhao1225/YouDub-webui](https://github.com/liuzhao1225/YouDub-webui) - `Repo` · ⭐ 5.7k · Apache-2.0 · End-to-end video localization for YouTube and Bilibili: speech recognition, subtitle translation, voice-cloned dubbing and final mux.
- [tmoroney/auto-subs](https://github.com/tmoroney/auto-subs) - `Repo` · ⭐ 4.4k · MIT · On-device subtitle generation that plugs straight into DaVinci Resolve, Premiere Pro and After Effects. ⚠️ The optional MMS forced-alignment weights for word-level timestamps are CC BY-NC 4.0 (non-commercial).
- [R3gm/SoniTranslate](https://github.com/R3gm/SoniTranslate) - `Repo` · ⭐ 1.4k · Apache-2.0 · Web UI for synchronized video translation and dubbing, with speaker diarization and a choice of TTS engines. ⚠️ Code is Apache-2.0, but the README warns that some models it uses (e.g. pyannote diarization) carry commercial restrictions.
- [shang-zhu/violin](https://github.com/shang-zhu/violin) - `Skill` · ⭐ 1.1k · MIT · Open-source agent skill that translates a video and dubs it into another language end to end.

## Lip-sync & digital humans

- [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) - `Repo` · ⭐ 8.1k · Apache-2.0 · Audio-driven talking video of unlimited length, from an image or an existing video.
- [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) - `Repo` · ⭐ 19.3k · MIT · Animates a still portrait from a driving video. ⚠️ Code is MIT, but the bundled InsightFace detection models are non-commercial; swap them out for commercial use.
- [lipku/LiveTalking](https://github.com/lipku/LiveTalking) - `Repo` · ⭐ 10k · Apache-2.0 · Real-time interactive streaming digital human with synchronized audio and video, a common base for live-stream avatars.
- [modstart-lib/aigcpanel](https://github.com/modstart-lib/aigcpanel) - `Repo` · ⭐ 5.7k · Apache-2.0 · All-in-one desktop digital-human app: lip-synced video, speech synthesis and voice cloning with one-click local model import.
- [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) - `Repo` · ⭐ 4k · Apache-2.0 · Expressive real-time portrait animation for live streaming, driven by a single photo (CVPR 2026). ⚠️ The LICENSE file is Apache-2.0, but the README states the project is released for academic research only; confirm with the authors before commercial use.
- [cclank/lanshu-create-ai-presenter-video](https://github.com/cclank/lanshu-create-ai-presenter-video) - `Skill` · ⭐ 2.8k · MIT · Provider-neutral Codex and Claude Code skill that turns a script plus one authorised presenter photo into a finished talking-head video with TTS, lip-sync and subtitles, and verifies each step.
- [Lynpoint/CyberVerse](https://github.com/Lynpoint/CyberVerse) - `Repo` · ⭐ 1.7k · GPL-3.0 · Self-hosted framework for real-time digital humans: one photo becomes a full-duplex video caller you can interrupt, driven over WebRTC with swappable ASR, LLM, TTS and local avatar models (FlashHead, LiveAct). ⚠️ Commits have slowed (last one 2026-09-11, 35 days before this check) and the only release is v0.1.0; the avatar video path needs a CUDA GPU and downloaded model weights, while voice-only sessions do not.

## Ads & marketing video

- [latent-spaces/brag](https://github.com/latent-spaces/brag) - `Repo` · ⭐ 17k · MIT · One command turns the project you just built into a short, shareable launch video.
- [op7418/guizang-product-video-skill](https://github.com/op7418/guizang-product-video-skill) - `Skill` · ⭐ 830 · AGPL-3.0 · Skill for software promo videos rendered in code from your real product components: storyboard copy, original music, sound effects and render. ⚠️ AGPL-3.0 overall, but the default styles adapted from CodePilot stay under their original BSL terms.
- [Kianzzz/book-sales-video](https://github.com/Kianzzz/book-sales-video) - `Skill` · ⭐ 226 · MIT · Chinese book-promotion video skill: pulls the script, checks the book, then voice-over, images, bilingual subtitles and auto-edit.
- [token360-community/ecom-image-skill](https://github.com/token360-community/ecom-image-skill) - `Skill` ⚡ · 🔷 Token360 edition of [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) · ⭐ 422 · MIT · buluslan's e-commerce visual skill (39 listing and ad templates plus 16-frame product motion GIFs) preconfigured for Token360 image models, with a tested sample gallery; output is stills and looping GIFs, not video.
- [AbubakrChan/product-launch-motion](https://github.com/AbubakrChan/product-launch-motion) - `Skill` · ⭐ 323 · MIT · Claude Code skill for polished product-launch videos straight from code (HTML/CSS/GSAP rendered with Playwright and FFmpeg), with a cursor that drives every change and voiceover sync.
- [xixihhhh/clipforge](https://github.com/xixihhhh/clipforge) - `Repo` · ⭐ 1k · AGPL-3.0 · Self-hosted commerce video factory: a product photo, link or topic becomes a scripted short with voiceover, either as a free no-key cut from public-domain stock or as an AI-generated film, and it ships an MCP server and an agent skill so an assistant can run the whole pipeline.
- [YILS-LIN/short-video-factory](https://github.com/YILS-LIN/short-video-factory) - `Repo` · ⭐ 5.8k · AGPL-3.0 · Cross-platform desktop app that batch-produces marketing shorts: it writes the script through any OpenAI-compatible endpoint, voices it with Edge-TTS, then auto-cuts your footage against the narration and burns in subtitles, preset by preset.

## ComfyUI & MCP connectors

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - `Repo` · ⭐ 139.7k · GPL-3.0 · Node-graph engine and GUI for image, video and audio diffusion workflows.
- [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) - `Node` · ⭐ 1.3k · GPL-3.0 · ComfyUI nodes that chain MiniMax H3 clips so motion and audio continue across joins; ships an example workflow.
- [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) - `MCP` · ⭐ 843 · MIT · MCP server plus sidebar agent that lets an LLM build, run and edit ComfyUI workflows for images, video and audio. ⚠️ README says the project is in limited maintenance (critical fixes only).
- [pireel/pireel](https://github.com/pireel/pireel) - `MCP` · ⭐ 1.3k · AGPL-3.0 · Open-source video editor with canvas and timeline that AI agents can drive over MCP.
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) - `MCP` · ⭐ 3.7k · MIT · MCP server that lets an agent drive DaVinci Resolve Studio projects: timelines, markers and renders.
- [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) - `MCP` · ⭐ 1.6k · MIT · Official MiniMax MCP server for text-to-speech, voice cloning, video and music generation.
- [Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp) - `MCP` · ⭐ 289 · AGPL-3.0 · Official local MCP server from Comfy Org that lets agents run and inspect your local ComfyUI workflows.
- [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) - `MCP` · ⭐ 3.2k · MIT · MCP server that lets an LLM control Ableton Live to create tracks, arrange clips and compose music.
- [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) - `Node` · ⭐ 2.5k · Apache-2.0 · Multi-segment director node for the official ComfyUI MiniMax H3 nodes, with example workflows. ⚠️ Code is Apache-2.0, but the MiniMax H3 weights use the custom MiniMax H3 Community License (users in the US/EU/UK/South Korea must apply); read it before commercial use.
- [Carasibana/ComfyUI-H3-FaceRefine](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) - `Node` · ⭐ 524 · MIT · ComfyUI nodes that fix the small blurry faces MiniMax H3 produces: per-frame face tracking, crop, re-refine with H3, stitch back, with two example workflows.
- [Songssx/ComfyUI-MiniMaxH3-TimelineDirector](https://github.com/Songssx/ComfyUI-MiniMaxH3-TimelineDirector) - `Node` · ⭐ 659 · GPL-3.0 · ComfyUI node that adds an editable reference-media timeline for MiniMax H3 reference-to-video, with four importable example workflows (including a low-VRAM one).

## Workflow breakdowns (posts)

- [@GeekCatX — Vox-style explainer in 4 steps](https://x.com/GeekCatX/status/2078488413045747814) - `Post` · 2026-07 · Video generation · Four steps: a vox-style skill in Codex writes storyboard prompts, an image model renders the frames, a video model animates them, then an auto-edit pass.
- [@newbeeyu — Tang-dynasty paper-cut layered animation with Codex + Remotion](https://x.com/newbeeyu/status/2076530524110369070) - `Post` · 2026-07 · Editing & motion · Long-form X article: layering, timing and per-layer sound effects for a paper-cut animation built in code with Codex and Remotion.
- [@EXM7777 — An AI video production pipeline in Claude Code](https://x.com/EXM7777/status/2082107255449919582) - `Post` · 2026-07 · Editing & motion · Long-form X article on setting up Claude Code as a video production pipeline, including the reference sources used for shot planning.
- [@Pluvio9yte — Codex + Hyperframes + HeyGen + voice cloning, end to end](https://x.com/Pluvio9yte/status/2081580929492131947) - `Post` · 2026-07 · Voice & TTS · Long-form X article (Chinese) on a short-video pipeline: Codex as the controller, Hyperframes for motion, HeyGen for avatars and IndexTTS for voice.
- [@0xMovez — How to build a motion design studio with Opus 5.5 (full course)](https://x.com/0xMovez/status/2104216919033192746) - `Post` · 2026-09 · Editing & motion · A 12-step long-form course: install the studio, prompt like a director, build a seek(t) renderer, tune spring motion, score sound to the beat, have Opus critique its own frames, then ship every format and package it as a skill.
- [@Bytec99 — Fully automated book-review shorts with Codex + HyperFrames](https://x.com/Bytec99/status/2075372048994672994) - `Post` · 2026-07 · Editing & motion · Long-form breakdown: Codex picks a book, writes a 30-second narration, VoxCPM voices it, faster-whisper aligns subtitles, FFmpeg ducks the music and HyperFrames renders; packaged as a reusable skill.
- [@tetsuoai — How to make a short film with Grok Imagine, start to finish](https://x.com/tetsuoai/status/2085365652509040768) - `Post` · 2026-08 · Video generation · Long-form guide: turn one line into a beat script, build character sheets and location/prop references, load them into Grok Imagine, write one sealed prompt per beat, then assemble in post; all prompts included.
- [@claudeskills101 — 8 explainer-video prompts for Claude Code, 8 styles](https://x.com/claudeskills101/status/2107170117243310471) - `Post` · 2026-10 · Editing & motion · Thread with eight full prompts (kinetic type, whiteboard, isometric, data chart, Manim, app walkthrough, paper collage, talking-head auto edit), each with an Avoid line and a done-means check.
- [@showheyohtaki — Camera-move and transition names to use in AI video prompts](https://x.com/showheyohtaki/status/2109112248832503895) - `Post` · 2026-10 · Video generation · Japanese cheat sheet of named camera moves and transitions (FPV, rack focus, whip pan and more) so prompts to Claude, Codex or video models get the intended shot.
- [@GeekCatX — Subway outfit-change video on MiniMax H3](https://x.com/GeekCatX/status/2096513305930297353) - `Post` · 2026-09 · Video generation · Recreates the viral subway outfit-change clip with MiniMax H3 image-to-video and a reverse-prompt skill; the full prompt is in the thread.
- [@Khazix0918 — Turn an open-source explainer skill into a narrated 5-minute science video](https://x.com/Khazix0918/status/2110587546271191166) - `Post` · 2026-10 · Editing & motion · Long-form walkthrough that takes the open-source Anatomy skill from install prompt to a narrated five-minute explainer video, with the exact slash command, the render-and-voiceover steps and measured cost and runtime. ⚠️ The author notes the figures are not fact-checked, and the quoted generation cost and runtime are their own single measurement on a Claude Max plan.

## People to follow

- [@HeyAbhishek](https://x.com/HeyAbhishek) - `Person` · EN · Seedance animation prompts · Shares full prompts behind cinematic AI animation clips. Example: [post](https://x.com/HeyAbhishek/status/2106369769956065518).
- [@liyue_ai](https://x.com/liyue_ai) - `Person` · 中文 · Seedance director skills · Publishes open-source Seedance director skills on GitHub (liyue-aigc). Example: [post](https://x.com/liyue_ai/status/2093592225162960982).
- [@Pluvio9yte](https://x.com/Pluvio9yte) - `Person` · 中文 · Agent-driven video pipelines · Long-form breakdowns of Codex + Hyperframes video pipelines and the skills behind them. Example: [post](https://x.com/Pluvio9yte/status/2081648099680743554).
- [@GeekCatX](https://x.com/GeekCatX) - `Person` · 中文 · Low-cost explainer workflows · Step-by-step workflows for low-cost explainer videos with agents and image/video models. Example: [post](https://x.com/GeekCatX/status/2078488413045747814).

## Related lists

- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) - `List` · ⭐ 2.2k · MIT · Seedance 2.5 / 2.0 prompt library with cases traced to original posts, templates and installable video skills.
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - `List` · ⭐ 2.8k · MIT · Collection of Seedance 2.0 prompts, guides and video-generation workflows.
- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) - `List` · ⭐ 34.7k · MIT · GPT Image 2 / 2.5 prompt and case library with templates; useful for keyframes and storyboards before video.
- [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) - `List` · ⭐ 2.2k · CC-BY-4.0 · 2,000+ curated Seedance 2.0 video prompts across cinematic, anime, UGC, ad and meme styles, with API guides and character-consistency tips.

## Contributing

Edit `data/catalog.json` only (never the READMEs), run `python3 scripts/generate_readme.py`, and open a pull request. Read the inclusion bar in [CONTRIBUTING.md](./CONTRIBUTING.md) first; entries that miss it are closed without merge.

---

<sub>List content is released under [CC0 1.0](./LICENSE). Linked projects, posts and trademarks belong to their owners; inclusion is not an endorsement by them or of Token360.</sub>

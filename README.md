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
  <img src="https://img.shields.io/badge/entries-83-9633af" alt="entries: 83" />
  <img src="https://img.shields.io/badge/last_verified-2026--10--11-informational" alt="last verified: 2026-10-11" />
  <img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey" alt="License: CC0-1.0" />
</p>

> A strictly curated list of open-source workflows, agent skills, MCP servers and reproducible posts for AI **video, voice, music, dubbing, lip-sync and editing**. Every entry must meet a written bar (see [Contributing](#contributing)) and is re-checked at least every 30 days. Maintained by the [Token360](https://www.token360.ai?utm_source=github&utm_medium=awesome&utm_campaign=avah) developer community.

**Tags:** `Repo` `Skill` `MCP` `Node` `Post` `Person` `List` · ⛔ link-only (non-commercial or source-available license) · ⚠️ read the note before using commercially

⚡ = run end to end on Token360, with a published guide; entries without ⚡ have not been tested. 🔷 Token360 edition = a fork maintained by the Token360 community that adds a tested Token360 quick start; the work, credit and license stay with the original author, and ⭐ shows the original repo's stars.

<sub>83 entries across 11 sections · last verified 2026-10-11</sub>

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

- [Video generation & prompting](#video-generation--prompting) (9)
- [Short drama & storytelling](#short-drama--storytelling) (9)
- [Editing & motion agents](#editing--motion-agents) (11)
- [Voice, TTS & music](#voice-tts--music) (9)
- [Dubbing & subtitles](#dubbing--subtitles) (8)
- [Lip-sync & digital humans](#lip-sync--digital-humans) (6)
- [Ads & marketing video](#ads--marketing-video) (4)
- [ComfyUI & MCP connectors](#comfyui--mcp-connectors) (9)
- [Workflow breakdowns (posts)](#workflow-breakdowns-posts) (10)
- [People to follow](#people-to-follow) (4)
- [Related lists](#related-lists) (4)

## Video generation & prompting

- [HKUDS/ViMax](https://github.com/HKUDS/ViMax) - `Repo` · ⭐ 12.6k · MIT · Agentic video generation in one pipeline: idea → script → storyboard → shots, with director, screenwriter and producer agents.
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - `Repo` · ⭐ 129.7k · MIT · Generates a finished short video from a topic or keyword: script, stock footage, voice-over, subtitles and music in one automated workflow.
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) - `Skill` · ⭐ 7.6k · MIT · Production-pipeline skill for Seedance 2.0 filmmaking across text, image, video and audio inputs.
- [liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) - `Skill` · ⭐ 617 · MIT · Seedance 2.5 "video director" skill: prompts, scripts, character locking, continuation, edits and transitions.
- [s1dashu/director](https://github.com/s1dashu/director) - `Skill` · ⭐ 801 · MIT · Skill that directs a complete video end to end: research, script, visual development, shot design, media generation and delivery.
- [krillinai/OpenCreator](https://github.com/krillinai/OpenCreator) - `Repo` · ⭐ 12.7k · Apache-2.0 · Desktop AI video studio that goes from script to generated, dubbed and localized video, with built-in agent skills.
- [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) - `Skill` · ⭐ 4.3k · MIT · Agent skill that writes model-ready Seedance 2.x video prompts from a plain idea.
- [token360-community/seedance-prompt-skill](https://github.com/token360-community/seedance-prompt-skill) - `Skill` ⚡ · 🔷 Token360 edition of [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) · ⭐ 4.3k · MIT · Dex's Seedance prompt-writing skill plus a standard-library Python script that renders the prompts as Seedance 2.5 clips on Token360, with sample clips.
- [FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo) - `Repo` · ⭐ 1.7k · Apache-2.0 · Runs the open MiniMax H3 audio-video model on consumer GPUs and Macs, with community speed reports per card. ⚠️ Code is Apache-2.0, but the MiniMax H3 weights use the custom MiniMax H3 Community License (users in the US/EU/UK/South Korea must apply); read it before commercial use.

## Short drama & storytelling

- [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) - `Repo` · ⭐ 17.2k · MIT · Self-hostable short-drama and motion-comic tool: script writing, storyboards, character/scene assets and image/video generation on an infinite canvas with agents.
- [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) - `Repo` · ⭐ 4.7k · AGPL-3.0 · Batch script-to-final-cut production tool for AI drama, with Seedance 2.0 support.
- [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) - `Repo` · ⭐ 2k · MIT · Local-first short-drama maker: story → storyboard → video, with project data kept on your machine.
- [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) - `Skill` · ⭐ 2.7k · MIT · Skill set for AI micro-dramas in Claude Code and Codex: script, character assets, storyboard, image/video prompts and review.
- [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) - `Skill` · ⭐ 4.4k · Apache-2.0 · Agent skills for short-drama pre-production: character bibles, adaptation outlines, art bibles, screenplays and storyboards.
- [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) - `Repo` · ⭐ 5.4k · AGPL-3.0 · Self-hosted agent workspace that turns a novel or script into character and scene assets, storyboards, consistent shots and a JianYing/CapCut draft, with cost tracking.
- [FireRedTeam/FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline) - `Repo` · ⭐ 3.5k · Apache-2.0 · Video editing agent that turns manual cutting into directing by natural language, with MCP and agent-skill integrations.
- [alibaba/lumenx](https://github.com/alibaba/lumenx) - `Repo` · ⭐ 1.4k · MIT · Alibaba's open-source studio that turns novel text into animated short dramas: script analysis, character design, storyboards and video assembly.
- [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama) - `Repo` ⛔ · ⭐ 16.1k · CC-BY-NC-SA-4.0 · The most-starred Chinese AI short-drama pipeline, from script to storyboard to generated episodes; listed as the category reference.

## Editing & motion agents

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) - `Repo` · ⭐ 67k · AGPL-3.0 · Agentic video production system that turns an AI coding assistant into a production pipeline, with many ready-made pipelines and tools.
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) - `Repo` · ⭐ 61k · Apache-2.0 · Write HTML, render video: a motion framework designed to be driven by agents.
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - `Skill` · ⭐ 11.3k · Apache-2.0 · Claude Code / Codex skill for cinematic product videos with Remotion: shot recipe cards, motion previews and a production template. ⚠️ Renders with Remotion, whose own license requires a paid company license for some commercial use.
- [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) - `Repo` · ⭐ 93.6k · MIT · Free, open-source video editor for web, desktop and mobile, built as a CapCut alternative.
- [luoluoluo22/jianying-editor-skill](https://github.com/luoluoluo22/jianying-editor-skill) - `Skill` · ⭐ 3.9k · MIT · Agent skill that automates editing in JianYing (the Chinese edition of CapCut) by writing its project drafts.
- [browser-use/video-use](https://github.com/browser-use/video-use) - `Repo` · ⭐ 28.6k · MIT · From the browser-use team: lets coding agents cut raw footage into a finished edit from word-level transcripts, with burned-in subtitles.
- [linyqh/NarratoAI](https://github.com/linyqh/NarratoAI) - `Repo` · ⭐ 11.4k · MIT · One-click film and TV commentary videos: the LLM writes the narration, then voice-over and cut are generated automatically.
- [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) - `Repo` · ⭐ 9.3k · MIT · Turns long podcasts, interviews and courses into short clips with subtitles, covers and post copy for Douyin, Xiaohongshu, TikTok, Reels and Shorts.
- [GuanYixuan/pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) - `Repo` · ⭐ 4.5k · Apache-2.0 · Python library that generates and exports JianYing (CapCut China) drafts, the building block behind many automated editing pipelines.
- [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) - `Skill` · ⭐ 3.1k · Apache-2.0 · Claude Code skills that act as a talking-head video editor: trims filler words and pauses, adds subtitles and exports the cut.
- [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) - `Skill` · ⭐ 4.3k · MIT · Skill that turns an SRT subtitle file into a hand-drawn whiteboard animation on warm paper, stroke by stroke.

## Voice, TTS & music

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - `Repo` · ⭐ 62.7k · MIT · Few-shot voice cloning and TTS: about one minute of reference audio is enough to train a voice.
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) - `Repo` · ⭐ 39k · Apache-2.0 · Tokenizer-free multilingual TTS with voice design and voice cloning.
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - `Repo` · ⭐ 26.9k · MIT · Open-source TTS model family from Resemble AI.
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) - `Repo` · ⭐ 23.9k · Apache-2.0 · Multilingual voice generation model with inference, training and deployment code.
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) - `Repo` · ⭐ 11.6k · Apache-2.0 · Music-generation model that turns lyrics into full songs with vocals, plus covers and music editing. ⚠️ Code is Apache-2.0, but the model weights are CC BY-NC 4.0 with an extra permission for individual users and musicians; companies need a commercial license.
- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) - `Repo` · ⭐ 56.9k · MIT · Local, open-source voice studio for cloning voices and generating speech, built on Qwen3-TTS and Whisper.
- [remsky/Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI) - `Repo` · ⭐ 5.5k · Apache-2.0 · Dockerized, OpenAI-compatible speech API for the Kokoro-82M TTS model that runs on CPU or GPU.
- [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) - `Repo` · ⭐ 20.3k · Apache-2.0 · Converts e-books into audiobooks with chapters and voice cloning, in 1,100+ languages. ⚠️ Code is Apache-2.0, but some supported engines ship weights under their own terms (e.g. XTTSv2 under the non-commercial Coqui Public Model License); pick the engine accordingly for commercial use.
- [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - `Repo` · ⭐ 4.2k · Apache-2.0 · Open model family for long-form speech, multi-speaker dialogue, voice design, sound effects and real-time TTS, with strong Chinese support.

## Dubbing & subtitles

- [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) - `Repo` · ⭐ 18.8k · Apache-2.0 · Subtitle segmentation, translation, alignment and dubbing in one automated pipeline.
- [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans) - `Repo` · ⭐ 19.3k · GPL-3.0 · Translates a video into another language and adds dubbed audio and subtitles.
- [buxuku/SmartSub](https://github.com/buxuku/SmartSub) - `Repo` · ⭐ 5.6k · MIT · Desktop app for local speech-to-text, subtitle translation, AI dubbing and burn-in, on Windows, macOS and Linux.
- [m-bain/whisperX](https://github.com/m-bain/whisperX) - `Repo` · ⭐ 24.5k · BSD-2-Clause · Speech recognition with word-level timestamps and speaker diarization.
- [liuzhao1225/YouDub-webui](https://github.com/liuzhao1225/YouDub-webui) - `Repo` · ⭐ 5.6k · Apache-2.0 · End-to-end video localization for YouTube and Bilibili: speech recognition, subtitle translation, voice-cloned dubbing and final mux.
- [tmoroney/auto-subs](https://github.com/tmoroney/auto-subs) - `Repo` · ⭐ 4.3k · MIT · On-device subtitle generation that plugs straight into DaVinci Resolve, Premiere Pro and After Effects. ⚠️ The optional MMS forced-alignment weights for word-level timestamps are CC BY-NC 4.0 (non-commercial).
- [R3gm/SoniTranslate](https://github.com/R3gm/SoniTranslate) - `Repo` · ⭐ 1.4k · Apache-2.0 · Web UI for synchronized video translation and dubbing, with speaker diarization and a choice of TTS engines. ⚠️ Code is Apache-2.0, but the README warns that some models it uses (e.g. pyannote diarization) carry commercial restrictions.
- [shang-zhu/violin](https://github.com/shang-zhu/violin) - `Skill` · ⭐ 1.1k · MIT · Open-source agent skill that translates a video and dubs it into another language end to end.

## Lip-sync & digital humans

- [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) - `Repo` · ⭐ 8k · Apache-2.0 · Audio-driven talking video of unlimited length, from an image or an existing video.
- [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) - `Repo` · ⭐ 19.2k · MIT · Animates a still portrait from a driving video. ⚠️ Code is MIT, but the bundled InsightFace detection models are non-commercial; swap them out for commercial use.
- [Jingyi-Wu-Richael/rachel-digital-human-production](https://github.com/Jingyi-Wu-Richael/rachel-digital-human-production) - `Skill` · ⭐ 1k · MIT · Codex skill for authorized talking-head videos: asset checks, a short preview first, and an approval gate before the full render.
- [lipku/LiveTalking](https://github.com/lipku/LiveTalking) - `Repo` · ⭐ 9.8k · Apache-2.0 · Real-time interactive streaming digital human with synchronized audio and video, a common base for live-stream avatars.
- [modstart-lib/aigcpanel](https://github.com/modstart-lib/aigcpanel) - `Repo` · ⭐ 5.6k · Apache-2.0 · All-in-one desktop digital-human app: lip-synced video, speech synthesis and voice cloning with one-click local model import.
- [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) - `Repo` · ⭐ 4k · Apache-2.0 · Expressive real-time portrait animation for live streaming, driven by a single photo (CVPR 2026). ⚠️ The LICENSE file is Apache-2.0, but the README states the project is released for academic research only; confirm with the authors before commercial use.

## Ads & marketing video

- [latent-spaces/brag](https://github.com/latent-spaces/brag) - `Repo` · ⭐ 15.2k · MIT · One command turns the project you just built into a short, shareable launch video.
- [op7418/guizang-product-video-skill](https://github.com/op7418/guizang-product-video-skill) - `Skill` · ⭐ 770 · AGPL-3.0 · Skill for software promo videos rendered in code from your real product components: storyboard copy, original music, sound effects and render. ⚠️ AGPL-3.0 overall, but the default styles adapted from CodePilot stay under their original BSL terms.
- [Kianzzz/book-sales-video](https://github.com/Kianzzz/book-sales-video) - `Skill` · ⭐ 223 · MIT · Chinese book-promotion video skill: pulls the script, checks the book, then voice-over, images, bilingual subtitles and auto-edit.
- [token360-community/ecom-image-skill](https://github.com/token360-community/ecom-image-skill) - `Skill` ⚡ · 🔷 Token360 edition of [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) · ⭐ 410 · MIT · buluslan's e-commerce visual skill (39 listing and ad templates plus 16-frame product motion GIFs) preconfigured for Token360 image models, with a tested sample gallery; output is stills and looping GIFs, not video.

## ComfyUI & MCP connectors

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - `Repo` · ⭐ 136.9k · GPL-3.0 · Node-graph engine and GUI for image, video and audio diffusion workflows.
- [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) - `Node` · ⭐ 1.2k · GPL-3.0 · ComfyUI nodes that chain MiniMax H3 clips so motion and audio continue across joins; ships an example workflow.
- [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) - `MCP` · ⭐ 811 · MIT · MCP server plus sidebar agent that lets an LLM build, run and edit ComfyUI workflows for images, video and audio. ⚠️ README says the project is in limited maintenance (critical fixes only).
- [pireel/pireel](https://github.com/pireel/pireel) - `MCP` · ⭐ 1.3k · AGPL-3.0 · Open-source video editor with canvas and timeline that AI agents can drive over MCP.
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) - `MCP` · ⭐ 3.5k · MIT · MCP server that lets an agent drive DaVinci Resolve Studio projects: timelines, markers and renders.
- [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) - `MCP` · ⭐ 1.6k · MIT · Official MiniMax MCP server for text-to-speech, voice cloning, video and music generation.
- [Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp) - `MCP` · ⭐ 270 · AGPL-3.0 · Official local MCP server from Comfy Org that lets agents run and inspect your local ComfyUI workflows.
- [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) - `MCP` · ⭐ 3.2k · MIT · MCP server that lets an LLM control Ableton Live to create tracks, arrange clips and compose music.
- [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) - `Node` · ⭐ 2.3k · Apache-2.0 · Multi-segment director node for the official ComfyUI MiniMax H3 nodes, with example workflows. ⚠️ Code is Apache-2.0, but the MiniMax H3 weights use the custom MiniMax H3 Community License (users in the US/EU/UK/South Korea must apply); read it before commercial use.

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

## People to follow

- [@HeyAbhishek](https://x.com/HeyAbhishek) - `Person` · EN · Seedance animation prompts · Shares full prompts behind cinematic AI animation clips. Example: [post](https://x.com/HeyAbhishek/status/2106369769956065518).
- [@liyue_ai](https://x.com/liyue_ai) - `Person` · 中文 · Seedance director skills · Publishes open-source Seedance director skills on GitHub (liyue-aigc). Example: [post](https://x.com/liyue_ai/status/2093592225162960982).
- [@Pluvio9yte](https://x.com/Pluvio9yte) - `Person` · 中文 · Agent-driven video pipelines · Long-form breakdowns of Codex + Hyperframes video pipelines and the skills behind them. Example: [post](https://x.com/Pluvio9yte/status/2081648099680743554).
- [@GeekCatX](https://x.com/GeekCatX) - `Person` · 中文 · Low-cost explainer workflows · Step-by-step workflows for low-cost explainer videos with agents and image/video models. Example: [post](https://x.com/GeekCatX/status/2078488413045747814).

## Related lists

- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) - `List` · ⭐ 2k · MIT · Seedance 2.5 / 2.0 prompt library with cases traced to original posts, templates and installable video skills.
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - `List` · ⭐ 2.7k · MIT · Collection of Seedance 2.0 prompts, guides and video-generation workflows.
- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) - `List` · ⭐ 34.3k · MIT · GPT Image 2 / 2.5 prompt and case library with templates; useful for keyframes and storyboards before video.
- [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) - `List` · ⭐ 2.1k · CC-BY-4.0 · 2,000+ curated Seedance 2.0 video prompts across cinematic, anime, UGC, ad and meme styles, with API guides and character-consistency tips.

## Contributing

Edit `data/catalog.json` only (never the READMEs), run `python3 scripts/generate_readme.py`, and open a pull request. Read the inclusion bar in [CONTRIBUTING.md](./CONTRIBUTING.md) first; entries that miss it are closed without merge.

---

<sub>List content is released under [CC0 1.0](./LICENSE). Linked projects, posts and trademarks belong to their owners; inclusion is not an endorsement by them or of Token360.</sub>

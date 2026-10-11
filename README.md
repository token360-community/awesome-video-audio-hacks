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
  <img src="https://img.shields.io/badge/entries-42-9633af" alt="entries: 42" />
  <img src="https://img.shields.io/badge/last_verified-2026--10--11-informational" alt="last verified: 2026-10-11" />
  <img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey" alt="License: CC0-1.0" />
</p>

> A strictly curated list of open-source workflows, agent skills, MCP servers and reproducible posts for AI **video, voice, music, dubbing, lip-sync and editing**. Every entry is re-checked against a written bar (see [Contributing](#contributing)), and each section is capped at 5 entries. Maintained by the [Token360](https://www.token360.ai?utm_source=github&utm_medium=awesome&utm_campaign=avah) developer community.

**Tags:** `Repo` `Skill` `MCP` `Node` `Post` `Person` `List` · ⛔ link-only (non-commercial or source-available license) · ⚠️ read the note before using commercially

A ⚡ mark will mean "verified to run on Token360 by changing `base_url` and key". No entry carries it yet: nothing has been tested.

<sub>42 entries across 10 sections · last verified 2026-10-11</sub>

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

<sub>Model ids from the public `GET /v1/models` on 2026-10-11. Routes answer with an auth error without a key; nothing in this list has been run end to end on Token360 yet.</sub>

Full model list and per-model request examples: [token360.ai/models](https://www.token360.ai/models?utm_source=github&utm_medium=awesome&utm_campaign=avah).

## Contents

- [Video generation & prompting](#video-generation--prompting) (5)
- [Short drama & storytelling](#short-drama--storytelling) (5)
- [Editing & motion agents](#editing--motion-agents) (5)
- [Voice, TTS & music](#voice-tts--music) (5)
- [Dubbing & subtitles](#dubbing--subtitles) (4)
- [Lip-sync & digital humans](#lip-sync--digital-humans) (3)
- [ComfyUI & MCP connectors](#comfyui--mcp-connectors) (4)
- [Workflow breakdowns (posts)](#workflow-breakdowns-posts) (4)
- [People to follow](#people-to-follow) (4)
- [Related lists](#related-lists) (3)

## Video generation & prompting

- [HKUDS/ViMax](https://github.com/HKUDS/ViMax) - `Repo` · ⭐ 12.6k · MIT · Agentic video generation in one pipeline: idea → script → storyboard → shots, with director, screenwriter and producer agents.
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - `Repo` · ⭐ 129.7k · MIT · Generates a finished short video from a topic or keyword: script, stock footage, voice-over, subtitles and music in one automated workflow.
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) - `Skill` · ⭐ 7.6k · MIT · Production-pipeline skill for Seedance 2.0 filmmaking across text, image, video and audio inputs.
- [liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) - `Skill` · ⭐ 616 · MIT · Seedance 2.5 "video director" skill: prompts, scripts, character locking, continuation, edits and transitions.
- [s1dashu/director](https://github.com/s1dashu/director) - `Skill` · ⭐ 801 · MIT · Skill that directs a complete video end to end: research, script, visual development, shot design, media generation and delivery.

## Short drama & storytelling

- [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) - `Repo` · ⭐ 17.2k · MIT · Self-hostable short-drama and motion-comic tool: script writing, storyboards, character/scene assets and image/video generation on an infinite canvas with agents.
- [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) - `Repo` · ⭐ 4.7k · AGPL-3.0 · Batch script-to-final-cut production tool for AI drama, with Seedance 2.0 support.
- [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) - `Repo` · ⭐ 2k · MIT · Local-first short-drama maker: story → storyboard → video, with project data kept on your machine.
- [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) - `Skill` · ⭐ 2.7k · MIT · Skill set for AI micro-dramas in Claude Code and Codex: script, character assets, storyboard, image/video prompts and review.
- [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) - `Skill` · ⭐ 4.4k · Apache-2.0 · Agent skills for short-drama pre-production: character bibles, adaptation outlines, art bibles, screenplays and storyboards.

## Editing & motion agents

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) - `Repo` · ⭐ 66.9k · AGPL-3.0 · Agentic video production system that turns an AI coding assistant into a production pipeline, with many ready-made pipelines and tools.
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) - `Repo` · ⭐ 60.9k · Apache-2.0 · Write HTML, render video: a motion framework designed to be driven by agents.
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - `Skill` · ⭐ 11.3k · Apache-2.0 · Claude Code / Codex skill for cinematic product videos with Remotion: shot recipe cards, motion previews and a production template. ⚠️ Renders with Remotion, whose own license requires a paid company license for some commercial use.
- [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) - `Repo` · ⭐ 93.6k · MIT · Free, open-source video editor for web, desktop and mobile, built as a CapCut alternative.
- [luoluoluo22/jianying-editor-skill](https://github.com/luoluoluo22/jianying-editor-skill) - `Skill` · ⭐ 3.9k · MIT · Agent skill that automates editing in JianYing (the Chinese edition of CapCut) by writing its project drafts.

## Voice, TTS & music

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - `Repo` · ⭐ 62.7k · MIT · Few-shot voice cloning and TTS: about one minute of reference audio is enough to train a voice.
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) - `Repo` · ⭐ 39k · Apache-2.0 · Tokenizer-free multilingual TTS with voice design and voice cloning.
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - `Repo` · ⭐ 26.9k · MIT · Open-source TTS model family from Resemble AI.
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) - `Repo` · ⭐ 23.9k · Apache-2.0 · Multilingual voice generation model with inference, training and deployment code.
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) - `Repo` · ⭐ 11.6k · Apache-2.0 · Music-generation model that turns lyrics into full songs with vocals, plus covers and music editing. ⚠️ Code is Apache-2.0, but the model weights are CC BY-NC 4.0 with an extra permission for individual users and musicians; companies need a commercial license.

## Dubbing & subtitles

- [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) - `Repo` · ⭐ 18.8k · Apache-2.0 · Subtitle segmentation, translation, alignment and dubbing in one automated pipeline.
- [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans) - `Repo` · ⭐ 19.3k · GPL-3.0 · Translates a video into another language and adds dubbed audio and subtitles.
- [buxuku/SmartSub](https://github.com/buxuku/SmartSub) - `Repo` · ⭐ 5.6k · MIT · Desktop app for local speech-to-text, subtitle translation, AI dubbing and burn-in, on Windows, macOS and Linux.
- [m-bain/whisperX](https://github.com/m-bain/whisperX) - `Repo` · ⭐ 24.5k · BSD-2-Clause · Speech recognition with word-level timestamps and speaker diarization.

## Lip-sync & digital humans

- [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) - `Repo` · ⭐ 8k · Apache-2.0 · Audio-driven talking video of unlimited length, from an image or an existing video.
- [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) - `Repo` · ⭐ 19.2k · MIT · Animates a still portrait from a driving video. ⚠️ Code is MIT, but the bundled InsightFace detection models are non-commercial; swap them out for commercial use.
- [Jingyi-Wu-Richael/rachel-digital-human-production](https://github.com/Jingyi-Wu-Richael/rachel-digital-human-production) - `Skill` · ⭐ 1.1k · MIT · Codex skill for authorized talking-head videos: asset checks, a short preview first, and an approval gate before the full render.

## ComfyUI & MCP connectors

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - `Repo` · ⭐ 136.9k · GPL-3.0 · Node-graph engine and GUI for image, video and audio diffusion workflows.
- [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) - `Node` · ⭐ 1.2k · GPL-3.0 · ComfyUI nodes that chain MiniMax H3 clips so motion and audio continue across joins; ships an example workflow.
- [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) - `MCP` · ⭐ 811 · MIT · MCP server plus sidebar agent that lets an LLM build, run and edit ComfyUI workflows for images, video and audio. ⚠️ README says the project is in limited maintenance (critical fixes only).
- [pireel/pireel](https://github.com/pireel/pireel) - `MCP` · ⭐ 1.3k · AGPL-3.0 · Open-source video editor with canvas and timeline that AI agents can drive over MCP.

## Workflow breakdowns (posts)

- [@GeekCatX — Vox-style explainer in 4 steps](https://x.com/GeekCatX/status/2078488413045747814) - `Post` · 2026-07 · Video generation · Four steps: a vox-style skill in Codex writes storyboard prompts, an image model renders the frames, a video model animates them, then an auto-edit pass.
- [@newbeeyu — Tang-dynasty paper-cut layered animation with Codex + Remotion](https://x.com/newbeeyu/status/2076530524110369070) - `Post` · 2026-07 · Editing & motion · Long-form X article: layering, timing and per-layer sound effects for a paper-cut animation built in code with Codex and Remotion.
- [@EXM7777 — An AI video production pipeline in Claude Code](https://x.com/EXM7777/status/2082107255449919582) - `Post` · 2026-07 · Editing & motion · Long-form X article on setting up Claude Code as a video production pipeline, including the reference sources used for shot planning.
- [@Pluvio9yte — Codex + Hyperframes + HeyGen + voice cloning, end to end](https://x.com/Pluvio9yte/status/2081580929492131947) - `Post` · 2026-07 · Voice & TTS · Long-form X article (Chinese) on a short-video pipeline: Codex as the controller, Hyperframes for motion, HeyGen for avatars and IndexTTS for voice.

## People to follow

- [@HeyAbhishek](https://x.com/HeyAbhishek) - `Person` · EN · Seedance animation prompts · Shares full prompts behind cinematic AI animation clips. Example: [post](https://x.com/HeyAbhishek/status/2106369769956065518).
- [@liyue_ai](https://x.com/liyue_ai) - `Person` · 中文 · Seedance director skills · Publishes open-source Seedance director skills on GitHub (liyue-aigc). Example: [post](https://x.com/liyue_ai/status/2093592225162960982).
- [@Pluvio9yte](https://x.com/Pluvio9yte) - `Person` · 中文 · Agent-driven video pipelines · Long-form breakdowns of Codex + Hyperframes video pipelines and the skills behind them. Example: [post](https://x.com/Pluvio9yte/status/2081648099680743554).
- [@GeekCatX](https://x.com/GeekCatX) - `Person` · 中文 · Low-cost explainer workflows · Step-by-step workflows for low-cost explainer videos with agents and image/video models. Example: [post](https://x.com/GeekCatX/status/2078488413045747814).

## Related lists

- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) - `List` · ⭐ 2k · MIT · Seedance 2.5 / 2.0 prompt library with cases traced to original posts, templates and installable video skills.
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - `List` · ⭐ 2.7k · MIT · Collection of Seedance 2.0 prompts, guides and video-generation workflows.
- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) - `List` · ⭐ 34.3k · MIT · GPT Image 2 / 2.5 prompt and case library with templates; useful for keyframes and storyboards before video.

## Contributing

Edit `data/catalog.json` only (never the READMEs), run `python3 scripts/generate_readme.py`, and open a pull request. Read the inclusion bar in [CONTRIBUTING.md](./CONTRIBUTING.md) first; entries that miss it are closed without merge.

---

<sub>List content is released under [CC0 1.0](./LICENSE). Linked projects, posts and trademarks belong to their owners; inclusion is not an endorsement by them or of Token360.</sub>

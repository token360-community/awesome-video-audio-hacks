<h1 align="center">
  <img src="./assets/banner.webp" alt="Awesome Video & Audio Hacks，Token360 出品" width="800" />
  <br />
  Awesome Video &amp; Audio Hacks
</h1>

<!-- 由 scripts/generate_readme.py 从 data/catalog.json 生成，请勿手改。 -->

<p align="center">
  <a href="./README.md">EN</a> · <strong>简体中文</strong> · <a href="./README.ja.md">日本語</a>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome" /></a>
  <img src="https://img.shields.io/badge/%E6%9D%A1%E7%9B%AE-121-9633af" alt="条目: 121" />
  <img src="https://img.shields.io/badge/%E6%9C%80%E8%BF%91%E6%A0%B8%E9%AA%8C-2026--10--11-informational" alt="最近核验: 2026-10-11" />
  <img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey" alt="License: CC0-1.0" />
</p>

> 一份严格筛选、逐条核验的 AI **视频、配音、音乐、翻译配音、对口型、剪辑**清单，收录开源工作流、Agent Skill、MCP server，以及可以照着复现的帖子。每一条都要过书面门槛（见[参与贡献](#参与贡献)），并且至少每 30 天复查一次。由 [Token360](https://www.token360.ai/zh-CN?utm_source=github&utm_medium=awesome&utm_campaign=avah) 开发者社区维护。

**标签：** `Repo` `Skill` `MCP` `Node` `Post` `Person` `List` · ⛔ 仅链接（非商用或 source-available 许可） · ⚠️ 商用前请先看备注

⚡ = 已在 Token360 上端到端跑通，并附已发布的教程；没有 ⚡ 的条目都还没测过。🔷 Token360 版 = Token360 社区维护的 fork，加了实测可用的 Token360 快速上手；作品、署名和许可证仍归原作者，⭐ 显示的是原仓库的星数。

<sub>共 121 条，11 个分类 · 最近核验 2026-10-11</sub>

## Token360 快速上手

Token360 用一个 OpenAI 兼容的 `base_url` 提供文本、图像和视频模型。

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

| 模态 | 接口                              | 模型 id 示例                                                         |
| ---- | --------------------------------- | -------------------------------------------------------------------- |
| 文本 | `POST /chat/completions`          | `claude-sonnet-5-5`, `gpt-6-sol`, `deepseek-v4.1-flash`              |
| 图像 | `POST /images/generations`        | `gpt-image-2`, `dola-seedream-5.0-pro`, `nano-banana-2`              |
| 视频 | `POST /videos → GET /videos/{id}` | `seedance-2.5`, `veo-3.1-generate-001`, `wan3.0-video`, `minimax-h3` |
| 音频 | _待验证_                          | `seed-audio-1.0`, `glm-asr-2512`                                     |

<sub>模型 id 取自 2026-10-11 公开的 `GET /v1/models`。不带 key 请求时这些路由返回鉴权错误。带 ⚡ 的条目已在 Token360 上端到端跑通（见各自教程）；其余条目都还没测过。</sub>

完整模型列表和每个模型的请求示例：[token360.ai/models](https://www.token360.ai/zh-CN/models?utm_source=github&utm_medium=awesome&utm_campaign=avah)。

## 目录

- [视频生成与提示词](#视频生成与提示词) (12)
- [短剧与叙事](#短剧与叙事) (9)
- [剪辑与动效 Agent](#剪辑与动效-agent) (28)
- [配音、TTS 与音乐](#配音tts-与音乐) (20)
- [翻译配音与字幕](#翻译配音与字幕) (8)
- [对口型与数字人](#对口型与数字人) (7)
- [广告与营销视频](#广告与营销视频) (7)
- [ComfyUI 与 MCP 连接器](#comfyui-与-mcp-连接器) (11)
- [工作流拆解（帖子）](#工作流拆解帖子) (11)
- [值得关注的作者](#值得关注的作者) (4)
- [相关列表](#相关列表) (4)

## 视频生成与提示词

- [HKUDS/ViMax](https://github.com/HKUDS/ViMax) - `Repo` · ⭐ 12.7k · MIT · Agent 化的视频生成流水线：创意 → 剧本 → 分镜 → 镜头，导演、编剧、制片多个 Agent 分工协作。
- [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - `Repo` · ⭐ 133.2k · MIT · 输入主题或关键词，一键生成高清短视频：文案、素材、配音、字幕和背景音乐全自动完成。
- [Emily2040/seedance-2.0](https://github.com/Emily2040/seedance-2.0) - `Skill` · ⭐ 7.8k · MIT · 面向 Seedance 2.0 的制作流程 Skill，覆盖文本、图像、视频、音频四种输入的 AI 影片制作。
- [liyue-aigc/seedance-2-5-video-director](https://github.com/liyue-aigc/seedance-2-5-video-director) - `Skill` · ⭐ 715 · MIT · Seedance 2.5 视频导演 Skill：提示词、脚本、诊断、人物锁定、续写、编辑与转场。
- [s1dashu/director](https://github.com/s1dashu/director) - `Skill` · ⭐ 814 · MIT · 从调研、脚本、视觉设定、镜头设计、素材生成到交付，端到端“导演”一条完整视频的 Skill。
- [krillinai/OpenCreator](https://github.com/krillinai/OpenCreator) - `Repo` · ⭐ 13.7k · Apache-2.0 · 桌面端 AI 视频工作室：从脚本到生成、配音、本地化一条龙，内置 Agent Skills。
- [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) - `Skill` · ⭐ 4.4k · MIT · 把一句想法写成可直接投喂 Seedance 2.x 的视频提示词的 Agent Skill。
- [token360-community/seedance-prompt-skill](https://github.com/token360-community/seedance-prompt-skill) - `Skill` ⚡ · 🔷 Token360 版，原项目 [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) · ⭐ 4.4k · MIT · Dex 的 Seedance 提示词写作 Skill，外加一个只用标准库的 Python 脚本，在 Token360 上用 Seedance 2.5 把提示词直接渲染成视频，并附示例片段。
- [FlashML-org/FreeVideo](https://github.com/FlashML-org/FreeVideo) - `Repo` · ⭐ 2.2k · Apache-2.0 · 在消费级显卡和 Mac 上本地运行开源 MiniMax H3 音视频模型，附社区各型号显卡实测速度。 ⚠️ 代码为 Apache-2.0，但 MiniMax H3 权重采用自定义的 MiniMax H3 Community License（美国/欧盟/英国/韩国用户需另行申请），商用前请先阅读。
- [edenfunf/reelmimic](https://github.com/edenfunf/reelmimic) - `Repo` · ⭐ 3.7k · MIT · 给它一条你喜欢的视频，Claude Code / Codex 里的多 Agent 小组会和你一起拆解、重建、互评，产出同风格的新视频。
- [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) - `Skill` · ⭐ 2.4k · MIT · 把实测过的火柴人动画画风整理成一个导演 skill：给一个话题，它先出一份待你确认的导演方案，再按每十秒一条拆出独立的视频提示词，附旁白和音效提示；四种画风，时长按十秒为单位任选。
- [Agents365-ai/video-podcast-maker](https://github.com/Agents365-ai/video-podcast-maker) - `Skill` · ⭐ 1.7k · MIT · 一个主题一条流水线出 4K 解说播客视频：查资料、写稿、用本地 EdgeTTS 或 Azure 配音（不依赖外部引擎），每支片子都有记录素材许可来源的 manifest，字幕用 Remotion 原生渲染，另出 9:16 高光短片和各平台发布文案。

## 短剧与叙事

- [HBAI-Ltd/Toonflow-app](https://github.com/HBAI-Ltd/Toonflow-app) - `Repo` · ⭐ 18.4k · MIT · 可本地部署的短剧/漫剧制作工具：剧本、智能分镜、角色与场景资产、图像和视频生成，基于无限画布与 Agent。
- [MemeCalculate/moyin-creator](https://github.com/MemeCalculate/moyin-creator) - `Repo` · ⭐ 4.7k · AGPL-3.0 · AI 影视生产工具：剧本到成片全流程批量化，支持 Seedance 2.0。
- [xuanyustudio/LocalMiniDrama](https://github.com/xuanyustudio/LocalMiniDrama) - `Repo` · ⭐ 2.1k · MIT · 本地优先的 AI 短剧/漫剧工具：故事 → 分镜 → 成片，项目数据留在本机。
- [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) - `Skill` · ⭐ 3.1k · MIT · 适配 Claude Code 与 Codex 的 AI 短剧 Skill 合集：剧本、角色资产、分镜、图片/视频提示词与审查。
- [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) - `Skill` · ⭐ 4.8k · Apache-2.0 · AI 短剧前期制作 Skill：拆角色、排大纲、场景与道具设定、写剧本、切分镜。
- [ArcReel/ArcReel](https://github.com/ArcReel/ArcReel) - `Repo` · ⭐ 5.6k · AGPL-3.0 · 可自部署的 AI 视频工作台：小说/剧本 → 角色与场景资产 → 分镜 → 跨镜头一致的视频 → 剪映草稿，并追踪费用。
- [FireRedTeam/FireRed-OpenStoryline](https://github.com/FireRedTeam/FireRed-OpenStoryline) - `Repo` · ⭐ 3.5k · Apache-2.0 · AI 剪辑 Agent：用自然语言“导演”代替手动剪辑，支持 MCP 与 Agent Skills。
- [alibaba/lumenx](https://github.com/alibaba/lumenx) - `Repo` · ⭐ 1.4k · MIT · 阿里开源的 AI 短漫剧一站式平台：小说文本 → 剧本分析 → 角色定制 → 分镜 → 视频合成。
- [chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama) - `Repo` ⛔ · ⭐ 16.4k · CC-BY-NC-SA-4.0 · 中文 AI 短剧星数最高的项目：剧本 → 分镜 → 成片全流程，作为品类参考收录。

## 剪辑与动效 Agent

- [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) - `Repo` · ⭐ 69.9k · AGPL-3.0 · Agent 化的视频制作系统：把 AI 编程助手变成完整的视频生产流水线，内置多条现成流程和工具。
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) - `Repo` · ⭐ 67.7k · Apache-2.0 · 写 HTML 就能渲染视频的动效框架，专为 Agent 调用设计。
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - `Skill` · ⭐ 12.5k · Apache-2.0 · 用 Remotion 做电影感产品视频的 Claude Code / Codex Skill：镜头配方卡、动效预览和生产模板。 ⚠️ 依赖 Remotion 渲染，Remotion 自身许可对部分公司商用场景要求付费授权。
- [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) - `Repo` · ⭐ 95.4k · MIT · 免费开源的视频编辑器，支持网页、桌面和移动端，定位为 CapCut（剪映）的开源替代。
- [luoluoluo22/jianying-editor-skill](https://github.com/luoluoluo22/jianying-editor-skill) - `Skill` · ⭐ 4.3k · MIT · 让 Agent 自动操作剪映草稿、完成剪辑的 Skill。
- [browser-use/video-use](https://github.com/browser-use/video-use) - `Repo` · ⭐ 29.4k · MIT · browser-use 团队出品：让编程 Agent 基于逐词转写把原始素材剪成成片，并烧录字幕。
- [linyqh/NarratoAI](https://github.com/linyqh/NarratoAI) - `Repo` · ⭐ 11.5k · MIT · 一键生成影视解说视频：大模型写解说文案，自动配音并剪辑成片。
- [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) - `Repo` · ⭐ 9.6k · MIT · 把播客、访谈、课程等长视频自动剪成短视频，生成字幕、封面和发布文案，适配抖音、小红书、TikTok、Reels、Shorts。
- [GuanYixuan/pyJianYingDraft](https://github.com/GuanYixuan/pyJianYingDraft) - `Repo` · ⭐ 4.6k · Apache-2.0 · 用 Python 生成并导出剪映草稿的轻量库，是许多全自动剪辑流水线的底层工具。
- [Agentchengfeng/chengfeng-videocut-skills](https://github.com/Agentchengfeng/chengfeng-videocut-skills) - `Skill` · ⭐ 3.1k · Apache-2.0 · 用 Claude Code Skills 做的口播剪辑 Agent：去口癖和停顿、加字幕并导出成片。
- [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) - `Skill` · ⭐ 4.6k · MIT · 把 SRT 字幕做成暖米黄纸底、逐笔绘制的手绘白板动画的 Skill。
- [jub0t/Concat](https://github.com/jub0t/Concat) - `Repo` · ⭐ 9.5k · AGPL-3.0 · 原生 Rust 引擎的跨平台本地剪辑器：离线 Whisper 自动字幕、TTS 与声音克隆、人物抠像，并开放 JSON-RPC / gRPC / MCP 接口，让 Agent 也能直接剪片。 ⚠️ 作者标注仍为 beta；README 里有一个付费赞助位，带无关代理服务的返利码。
- [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) - `Skill` · ⭐ 4.5k · MIT · 用代码写艺术风格动画的 Agent Skill：35 种艺术风格、9 种解说语法、8 种参数化片段，另附整支口播片的参考代码，一条 npx 命令装好。
- [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) - `Skill` · ⭐ 1.9k · MIT · 14 个 Codex / Claude Code Skill，按转写稿剪 Reels 和 YouTube Shorts，自带 406 张动效卡片和 HyperFrames 模板，还有一个不用素材、不用 API key 就能渲的测试工程。 ⚠️ 作者本人的配置用 ElevenLabs Scribe 和 Kie.ai 模型 API，但两者都可选（本地 Whisper 或现成转写稿即可），生成素材不是必需项。
- [glanderness/BeefTV](https://github.com/glanderness/BeefTV) - `Repo` ⛔ · ⭐ 1.6k · BeefTV Source Available License 1.0 (source-available; pre-change code MIT) · 轻量、本地优先的视频创作工作台：无限画布上把提示词、模型和素材连起来，人和 Agent 在同一张板子上来回改。
- [Barty-Bart/motion-graphics](https://github.com/Barty-Bart/motion-graphics) - `Skill` · ⭐ 752 · MIT · 给 Claude Code 和 Codex 用的动效 Skill 合集，含自带字体的 b-roll 引擎，每天都在提交。
- [hypit-ai/hypit](https://github.com/hypit-ai/hypit) - `Repo` ⛔ · ⭐ 24k · Modified Apache-2.0 · 让 Agent 把爆款视频拆成可编辑、按字词对齐的工作流（素材、字幕、B-roll、特效），再批量渲染出多个变体的 Skill 与 CLI，作为品类参考收录。 ⚠️ 源码可见：修改版 Apache-2.0，禁止做成多租户 / SaaS 服务或商业再分发（生成内容归用户）；文档默认推荐 Hypit 自家托管的 HypiHub 和合作模型 API，部分为推广链接，也可改用本地或自带的服务。
- [threerocks/sweety-handdraw-video](https://github.com/threerocks/sweety-handdraw-video) - `Skill` · ⭐ 723 · MIT · 把一个主题或一篇文章做成完整手绘讲解视频的 Codex / Claude Code Skill：按部位描线、逐字书写、自动配音，五项制作依赖内置。 ⚠️ 项目很新（2026-10-12 建仓，单人维护）；默认配音走 VoiceStudio，其内置模型各有许可，商用前请确认。
- [alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle) - `Skill` · ⭐ 1k · Apache-2.0 · 以代码生成美术与动画的 Claude Code / Codex 插件：手绘插画、循环动画、产品发布视频、配乐短片，几十种风格，渲染结果可复现。
- [academa-labs/manimgx](https://github.com/academa-labs/manimgx) - `Repo` · ⭐ 1.9k · MIT · 面向 Agent 的动画引擎：保留 Manim 的 Python API、底层换成 Rust GPU 内核，数学与 3D 讲解视频直出 MP4 且快很多；pip 即装，附 llms.txt 让编码 Agent 自己完成安装。 ⚠️ 2026-10-05 才建仓，目前是 v0.1.x 早期版本。
- [remotion-dev/remotion](https://github.com/remotion-dev/remotion) - `Repo` ⛔ · ⭐ 65.3k · Remotion License · 用 React 以代码做视频的参考框架；大多数编码 Agent 视频 Skill（动效、模板类）都建在它之上。
- [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) - `Skill` · ⭐ 2k · MIT · 把 FFmpeg 变成 42 个有机器可读契约的工具给编码 Agent 调用：剪切、烧字幕、重构图、响度统一、各平台导出；同时提供 skill 和 MCP server，全本地、不要 API key。
- [0xsline/OpenChatCut](https://github.com/0xsline/OpenChatCut) - `Repo` · ⭐ 2.5k · AGPL-3.0 · 本地优先的对话式剪辑器：在聊天里说出要怎么剪，它操作专业多轨时间线并用 Remotion 渲染，同一套流程也以 Agent Skill 和 MCP server 暴露出来。 ⚠️ 图像/视频生成走自带 key 的供应商（OpenAI、Gemini、Seedance、Kling，Fal 可选），生成费用记在你自己的供应商账户上。
- [openfilm/openfilm](https://github.com/openfilm/openfilm) - `Repo` · ⭐ 1.3k · MIT · 让编码 Agent 把片子写成普通网页，每个镜头一个 `frame(t)` 函数，再用本地浏览器里的 Studio 编辑器把它做出来的东西逐个挪位、改样式、裁剪和重剪，最后导出 MP4；不用框架、不用账号。
- [Leonxlnx/cinetic](https://github.com/Leonxlnx/cinetic) - `Skill` · ⭐ 677 · MIT · 让 Agent 真正去「导」一支发布片而不是拼动效组件：先写三个概念，再从 273 个带时长配方的手法里抽出分镜计划，用三个性格词推导品牌视觉，配上代码生成的音效，过完运动模糊、音画同步和影评关卡才算交片；底层可选 Remotion 或 HyperFrames。
- [zenstory-ai/video-recap-skills](https://github.com/zenstory-ai/video-recap-skills) - `Skill` · ⭐ 582 · MIT · 七个 skill 把一段或几段视频做成中文解说成片：Agent 看懂画面与对白，定故事和视听方案，再剪辑、写稿、配音、混音、上字幕；本地只要 ffmpeg，成片还能一键导成剪映草稿继续改。
- [FavioVazquez/showtime](https://github.com/FavioVazquez/showtime) - `Skill` · ⭐ 267 · MIT · 一句话说清要什么片，一组 Agent skill 负责导，渲染全在你自己的机器上，不需要 GPU；项目自己的 55 秒合集片就是在纯 CPU 上 2 分 23 秒渲出来的。同时提供 skill 包、MCP server 和插件三种接法。
- [Orkas-AI/Orkas-VideoStudio](https://github.com/Orkas-AI/Orkas-VideoStudio) - `Skill` · ⭐ 331 · MIT · 不做黑盒视频 Agent：一支片子就是一份可读、可 diff 的 `plan.json`，你和 Agent 都能逐行改，改哪段只重渲哪段；底层是 HyperFrames、ffmpeg 和 whisper.cpp 的确定性薄封装，命令行或 MCP 都能驱动。

## 配音、TTS 与音乐

- [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - `Repo` · ⭐ 63.2k · MIT · 少样本声音克隆与 TTS：约 1 分钟参考音频即可训练出可用的声音。
- [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) - `Repo` · ⭐ 39.6k · Apache-2.0 · 无分词器的多语种 TTS，支持声音设计与声音克隆。
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) - `Repo` · ⭐ 27.1k · MIT · Resemble AI 开源的 TTS 模型。
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) - `Repo` · ⭐ 24.1k · Apache-2.0 · 多语种语音生成大模型，提供推理、训练和部署全套能力。
- [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE) - `Repo` · ⭐ 12.3k · Apache-2.0 · 开源音乐生成模型：歌词生成带人声的完整歌曲，并支持翻唱和音乐编辑。 ⚠️ 代码为 Apache-2.0，但模型权重为 CC BY-NC 4.0（个人用户和音乐人另有许可）；公司商用需单独取得商业授权。
- [jamiepine/voicebox](https://github.com/jamiepine/voicebox) - `Repo` · ⭐ 58k · MIT · 本地开源的语音工作室：声音克隆与语音合成，基于 Qwen3-TTS 和 Whisper。
- [remsky/Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI) - `Repo` · ⭐ 5.6k · Apache-2.0 · Kokoro-82M 的 Docker 化 TTS 服务，接口兼容 OpenAI，CPU 和 GPU 都能跑。
- [DrewThomasson/ebook2audiobook](https://github.com/DrewThomasson/ebook2audiobook) - `Repo` · ⭐ 20.4k · Apache-2.0 · 把电子书转成带章节的有声书，支持声音克隆和 1100 多种语言。 ⚠️ 代码为 Apache-2.0，但部分可选引擎的权重另有许可（如 XTTSv2 为非商用的 Coqui Public Model License），商用时请选对引擎。
- [OpenMOSS/MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - `Repo` · ⭐ 4.2k · Apache-2.0 · 开源语音模型家族：长文本朗读、多人对话合成、声音设计、音效和实时 TTS，中文表现突出。
- [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice) - `Repo` · ⭐ 15k · Apache-2.0 · next-gen Kaldi（k2-fsa）团队出品的零样本声音克隆 TTS，覆盖 600+ 语言，pip 可装、README 有 Python 快速上手，另有 Hugging Face 在线 demo。 ⚠️ 仓库 LICENSE 为 Apache-2.0；权重在 Hugging Face（k2-fsa/OmniVoice），截至 2026-10-12 该页未单独声明权重许可，商用前请自行确认。
- [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio) - `Repo` · ⭐ 77.5k · AGPL-3.0 · 完全本地运行的桌面语音工作台：声音克隆、音色设计、视频配音、听写、转写、有声书，支持 646 种语言，自带本地 HTTP API 和 MCP server。 ⚠️ 应用代码为 AGPL-3.0，但内置的每个模型各自带许可；商用前请逐一确认模型条款。
- [0xShug0/audio.cpp](https://github.com/0xShug0/audio.cpp) - `Repo` · ⭐ 3.6k · Apache-2.0 · 基于 ggml 的纯 C++ 音频推理引擎，一个包跑完视频流水线要的全部音频模型：TTS、语音识别、VAD、变声、音乐生成，支持 CPU/CUDA/Vulkan/AMD/Apple Silicon。
- [leemysw/yovoice](https://github.com/leemysw/yovoice) - `Repo` · ⭐ 1.7k · Apache-2.0 · macOS / Windows 桌面应用，本地跑 TTS、声音克隆和情绪控制，不走云 API，也没有按字计费。
- [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot) - `Skill` · ⭐ 1.5k · MIT · 给编程 Agent 装上耳朵，纯 CPU 运行：描述、匹配和审听音效与影片配乐，还能从 201 个用代码生成的音效库里按帧对齐渲染音效，提供 CLI、MCP server 和 Claude Code Skill。
- [FluidInference/FluidAudio](https://github.com/FluidInference/FluidAudio) - `Repo` · ⭐ 3.1k · Apache-2.0 · 在 Apple 设备上跑 CoreML 音频模型的 Swift SDK：TTS、语音转写（Parakeet）、人声检测与说话人分离，全部本地运行。
- [ace-step/ACE-Step-1.5](https://github.com/ace-step/ACE-Step-1.5) - `Repo` · ⭐ 13.8k · MIT · 本地音乐生成模型和命令行工具：给提示词和歌词就出带人声的完整歌曲，CUDA、ROCm、Intel XPU、Apple MPS 和纯 CPU 都能跑。
- [sgl-project/sglang-omni](https://github.com/sgl-project/sglang-omni) - `Repo` · ⭐ 1.6k · Apache-2.0 · 把开源语音、TTS 和音乐模型统一放到一个兼容 OpenAI 的接口后面的推理服务：支持流式语音、上传音色、带说话人标注的转写，以及多 worker 路由。
- [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) - `Repo` ⛔ · ⭐ 33.3k · Fish Audio Community License 1.0 · 多语言、多说话人语音合成与音色克隆的权重开放参考项目，自带 Web UI、推理 API 和 Docker 镜像。 ⚠️ 非 OSI 许可：商用只在年营收低于 50 万美元时免费，把它做成对外的 TTS / 音色克隆托管服务需要单独向 Fish Audio 取得书面授权。
- [Tencent-Hunyuan/AuK](https://github.com/Tencent-Hunyuan/AuK) - `Repo` · ⭐ 1.5k · MIT · 权重公开的语音生成模型，难得的是还能做语音编辑：零样本 TTS、音色克隆、增强、分离和目标说话人提取在一个模型里，附带蒸馏出更快的 Flash 版的训练流程、ComfyUI 节点、Apple Silicon 上的 MLX 推理，以及通过 audio.cpp 的 GGUF 离线推理。
- [bitwize-music-studio/claude-ai-music-skills](https://github.com/bitwize-music-studio/claude-ai-music-skills) - `Skill` · ⭐ 572 · CC0-1.0 · 把一段对话变成整张专辑的生产线：概念策划、并行查证（交叉核对来源）、写词、生成 Suno 提示词、母带处理到发行准备，每个阶段都有质量关卡。 ⚠️ 出歌这一步走你自己的付费 Suno 账号；仓库给的是工作流、提示词和母带处理，不含本地模型。

## 翻译配音与字幕

- [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) - `Repo` · ⭐ 18.8k · Apache-2.0 · 字幕切分、翻译、对齐乃至配音，一条全自动流水线。
- [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans) - `Repo` · ⭐ 19.5k · GPL-3.0 · 把视频翻译成另一种语言，并嵌入配音和字幕。
- [buxuku/SmartSub](https://github.com/buxuku/SmartSub) - `Repo` · ⭐ 5.8k · MIT · 跨 Windows / macOS / Linux 的桌面工具：本地转写、字幕翻译、AI 配音和字幕烧录。
- [m-bain/whisperX](https://github.com/m-bain/whisperX) - `Repo` · ⭐ 24.7k · BSD-2-Clause · 带词级时间戳和说话人分离的语音识别。
- [liuzhao1225/YouDub-webui](https://github.com/liuzhao1225/YouDub-webui) - `Repo` · ⭐ 5.7k · Apache-2.0 · YouTube/B 站视频本地化全流程：语音识别、字幕翻译、克隆配音到合成成片。
- [tmoroney/auto-subs](https://github.com/tmoroney/auto-subs) - `Repo` · ⭐ 4.4k · MIT · 本地生成字幕，直接接入 DaVinci Resolve、Premiere Pro 和 After Effects。 ⚠️ 用于逐词时间戳的可选 MMS 强制对齐权重为 CC BY-NC 4.0（非商用）。
- [R3gm/SoniTranslate](https://github.com/R3gm/SoniTranslate) - `Repo` · ⭐ 1.4k · Apache-2.0 · 视频同步翻译配音 WebUI，支持说话人分离和多种 TTS 引擎。 ⚠️ 代码为 Apache-2.0，但 README 提示部分所用模型（如 pyannote 说话人分离）有商用限制。
- [shang-zhu/violin](https://github.com/shang-zhu/violin) - `Skill` · ⭐ 1.1k · MIT · 开源视频翻译 Skill：把一段视频端到端翻译并配音成另一种语言。

## 对口型与数字人

- [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) - `Repo` · ⭐ 8.1k · Apache-2.0 · 音频驱动、不限时长的说话视频生成，支持图生视频和视频生视频。
- [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) - `Repo` · ⭐ 19.3k · MIT · 用驱动视频让静态肖像动起来。 ⚠️ 代码是 MIT，但自带的 InsightFace 检测模型仅限非商用，商用需替换。
- [lipku/LiveTalking](https://github.com/lipku/LiveTalking) - `Repo` · ⭐ 10k · Apache-2.0 · 实时交互流式数字人，音视频同步对话，常用于直播数字人。
- [modstart-lib/aigcpanel](https://github.com/modstart-lib/aigcpanel) - `Repo` · ⭐ 5.7k · Apache-2.0 · 一站式 AI 数字人桌面系统：视频合成、声音合成与克隆，一键导入本地模型。
- [GVCLab/PersonaLive](https://github.com/GVCLab/PersonaLive) - `Repo` · ⭐ 4k · Apache-2.0 · 面向直播的实时表情肖像动画，一张照片即可驱动（CVPR 2026）。 ⚠️ LICENSE 文件为 Apache-2.0，但 README 声明仅供学术研究使用；商用前请先与作者确认。
- [cclank/lanshu-create-ai-presenter-video](https://github.com/cclank/lanshu-create-ai-presenter-video) - `Skill` · ⭐ 2.8k · MIT · 不绑定供应商的 Codex / Claude Code Skill：一份文案加一张已授权的真人照片，走完 TTS、口型、字幕，产出可交付的口播视频，每一步都有校验。
- [Lynpoint/CyberVerse](https://github.com/Lynpoint/CyberVerse) - `Repo` · ⭐ 1.7k · GPL-3.0 · 可自部署的实时数字人框架：一张照片做成能随时打断的全双工视频通话对象，走 WebRTC，ASR、LLM、TTS 和本地口型模型（FlashHead、LiveAct）都能替换。 ⚠️ 提交已明显放缓（最后一次 2026-09-11，距本次核验 35 天），且只有 v0.1.0 一个 release；数字人视频需要 CUDA 显卡和下载模型权重，纯语音模式不需要。

## 广告与营销视频

- [latent-spaces/brag](https://github.com/latent-spaces/brag) - `Repo` · ⭐ 17k · MIT · 一条命令，把刚做好的项目变成一支可分享的发布宣传短片。
- [op7418/guizang-product-video-skill](https://github.com/op7418/guizang-product-video-skill) - `Skill` · ⭐ 830 · AGPL-3.0 · 归藏的产品宣传片 Skill：复用真实产品组件，用代码做软件更新宣传片，包含分镜文案、原创配乐、音效和渲染。 ⚠️ 整体为 AGPL-3.0，但默认样式中改编自 CodePilot 的组件仍保留原 BSL 授权。
- [Kianzzz/book-sales-video](https://github.com/Kianzzz/book-sales-video) - `Skill` · ⭐ 226 · MIT · 中文图书带货视频 Skill：取稿、核验书籍，再配音、配图、加双语字幕并自动剪辑。
- [token360-community/ecom-image-skill](https://github.com/token360-community/ecom-image-skill) - `Skill` ⚡ · 🔷 Token360 版，原项目 [buluslan/gpt-image2-ecommerce](https://github.com/buluslan/gpt-image2-ecommerce) · ⭐ 422 · MIT · buluslan 的电商做图 Skill（39 个主图与广告模板，外加 16 帧产品动图），已配好 Token360 图像模型并附实测样图；产出是静图和循环动图，不是视频。
- [AbubakrChan/product-launch-motion](https://github.com/AbubakrChan/product-launch-motion) - `Skill` · ⭐ 323 · MIT · 直接用代码做高质感产品发布视频的 Claude Code Skill（HTML/CSS/GSAP，经 Playwright + FFmpeg 渲染），光标驱动每个变化，支持配音对齐。
- [xixihhhh/clipforge](https://github.com/xixihhhh/clipforge) - `Repo` · ⭐ 1k · AGPL-3.0 · 可自部署的带货短视频工厂：一张产品图、一个链接或一个主题出成片，免费路径用公共领域素材加免费配音（不用任何 key），AI 路径出生成式影片；自带 MCP server 和 agent skill，整条流程可以交给助手跑。
- [YILS-LIN/short-video-factory](https://github.com/YILS-LIN/short-video-factory) - `Repo` · ⭐ 5.8k · AGPL-3.0 · 跨平台桌面应用，批量产出营销短视频：文案走任意兼容 OpenAI 的接口，配音用 EdgeTTS，再按旁白自动混剪你的分镜素材并烧上字幕，可按预设持续跑。

## ComfyUI 与 MCP 连接器

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) - `Repo` · ⭐ 139.7k · GPL-3.0 · 节点式的图像、视频、音频扩散模型工作流引擎与界面。
- [NikoDemon80/ComfyUI-H3-Motion-Context](https://github.com/NikoDemon80/ComfyUI-H3-Motion-Context) - `Node` · ⭐ 1.3k · GPL-3.0 · 串联 MiniMax H3 片段的 ComfyUI 节点，让动作和声音在衔接处连贯；附示例工作流。
- [artokun/comfyui-mcp](https://github.com/artokun/comfyui-mcp) - `MCP` · ⭐ 843 · MIT · MCP server 加侧边栏 Agent，让大模型搭建、运行和修改 ComfyUI 的图像/视频/音频工作流。 ⚠️ README 写明目前为有限维护（只修关键问题）。
- [pireel/pireel](https://github.com/pireel/pireel) - `MCP` · ⭐ 1.3k · AGPL-3.0 · 带画布和时间轴的开源视频编辑器，可由 AI Agent 通过 MCP 驱动。
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) - `MCP` · ⭐ 3.7k · MIT · 让 Agent 操控 DaVinci Resolve Studio 项目的 MCP server：时间线、标记和渲染。
- [MiniMax-AI/MiniMax-MCP](https://github.com/MiniMax-AI/MiniMax-MCP) - `MCP` · ⭐ 1.6k · MIT · MiniMax 官方 MCP server：语音合成、声音克隆、视频和音乐生成。
- [Comfy-Org/comfy-mcp](https://github.com/Comfy-Org/comfy-mcp) - `MCP` · ⭐ 289 · AGPL-3.0 · Comfy Org 官方本地 MCP server，让 Agent 运行和查看本地 ComfyUI 工作流。
- [ahujasid/ableton-mcp](https://github.com/ahujasid/ableton-mcp) - `MCP` · ⭐ 3.2k · MIT · 让大模型控制 Ableton Live 的 MCP server：建轨、编排片段、作曲。
- [AIMixer/ComfyUI_MiniMaxH3_Director](https://github.com/AIMixer/ComfyUI_MiniMaxH3_Director) - `Node` · ⭐ 2.5k · Apache-2.0 · 基于 ComfyUI 官方 MiniMax H3 节点的多段导演节点，附示例工作流。 ⚠️ 代码为 Apache-2.0，但 MiniMax H3 权重采用自定义的 MiniMax H3 Community License（美国/欧盟/英国/韩国用户需另行申请），商用前请先阅读。
- [Carasibana/ComfyUI-H3-FaceRefine](https://github.com/Carasibana/ComfyUI-H3-FaceRefine) - `Node` · ⭐ 524 · MIT · 专治 MiniMax H3 出片里小脸糊的 ComfyUI 节点：逐帧人脸追踪、裁切、用 H3 重绘再贴回，附两个示例工作流。
- [Songssx/ComfyUI-MiniMaxH3-TimelineDirector](https://github.com/Songssx/ComfyUI-MiniMaxH3-TimelineDirector) - `Node` · ⭐ 659 · GPL-3.0 · 给 ComfyUI 的 MiniMax H3 参考生视频加上可编辑参考素材时间线的节点，附 4 个可直接导入的示例工作流（含低显存版）。

## 工作流拆解（帖子）

- [@GeekCatX — 4 步做 Vox 风格解说视频](https://x.com/GeekCatX/status/2078488413045747814) - `Post` · 2026-07 · 视频生成 · 四步：Codex + vox-style skill 拆分镜写提示词，图像模型批量出图，视频模型逐镜生成，最后自动剪辑成片。
- [@newbeeyu — 用 Codex + Remotion 做唐朝纸片分层动画](https://x.com/newbeeyu/status/2076530524110369070) - `Post` · 2026-07 · 剪辑与动效 · X 长文：用 Codex + Remotion 以代码制作唐朝纸片分层动画，讲清分层、节奏和分层音效。
- [@EXM7777 — 在 Claude Code 里搭一条 AI 视频制作流水线](https://x.com/EXM7777/status/2082107255449919582) - `Post` · 2026-07 · 剪辑与动效 · X 长文：把 Claude Code 搭成一条视频制作流水线，并列出做镜头规划时参考的素材来源。
- [@Pluvio9yte — Codex + Hyperframes + HeyGen + 声音克隆全流程](https://x.com/Pluvio9yte/status/2081580929492131947) - `Post` · 2026-07 · 配音与 TTS · X 长文：Codex 主控、Hyperframes 做动效、HeyGen 做数字人、IndexTTS 做配音的短视频全流程。
- [@0xMovez — 用 Opus 5.5 搭建动效设计工作室（完整课程）](https://x.com/0xMovez/status/2104216919033192746) - `Post` · 2026-09 · 剪辑与动效 · 12 步长文课程：10 分钟装好工作室，像导演一样写提示词，搭 seek(t) 渲染引擎，调弹簧动效，按节拍配乐，让 Opus 自查画面，最后一条时间线导出多格式并封装成 Skill。
- [@Bytec99 — Codex + HyperFrames 全自动生成图书号短视频](https://x.com/Bytec99/status/2075372048994672994) - `Post` · 2026-07 · 剪辑与动效 · 长文拆解：Codex 选书写 30 秒旁白，VoxCPM 本地配音，faster-whisper 对齐字幕，FFmpeg 做 BGM 闪避，HyperFrames 渲染，并封装成可复用 Skill。
- [@tetsuoai — 用 Grok Imagine 从零完成一部短片](https://x.com/tetsuoai/status/2085365652509040768) - `Post` · 2026-08 · 视频生成 · 长文教程：一句话扩成节拍脚本，做角色设定图和场景/道具参考，导入 Grok Imagine，每个节拍写一条独立提示词，最后后期拼接；提示词全部给出。
- [@claudeskills101 — 8 种风格的 Claude Code 讲解视频提示词](https://x.com/claudeskills101/status/2107170117243310471) - `Post` · 2026-10 · 剪辑与动效 · 推文串给出 8 套完整提示词（动态文字、白板、等距流程、数据图表、Manim、App 演示、纸拼贴、口播自动剪辑），每套都有“避免”项和完成标准。
- [@showheyohtaki — 给 AI 视频下指令用的运镜与转场名称](https://x.com/showheyohtaki/status/2109112248832503895) - `Post` · 2026-10 · 视频生成 · 日文速查表：整理 FPV、移焦、甩镜等运镜和转场名称，给 Claude、Codex 或视频模型下指令时能精准出效果。
- [@GeekCatX — 用 MiniMax H3 做地铁变装视频](https://x.com/GeekCatX/status/2096513305930297353) - `Post` · 2026-09 · 视频生成 · 用反推 Skill + MiniMax H3 图生视频复刻爆火的地铁变装视频，完整提示词在串里。
- [@Khazix0918 — 把开源讲解 Skill 做成 5 分钟带旁白的科普视频](https://x.com/Khazix0918/status/2110587546271191166) - `Post` · 2026-10 · 剪辑与动效 · 长文教程：从安装提示词开始，把开源 Anatomy skill 一路做成 5 分钟带旁白的科普视频，附具体斜杠命令、渲染与配音步骤，以及实测成本和出片时长。 ⚠️ 作者自己提醒生成内容的准确性无保证；文中的成本和出片时间是他在 Claude Max 套餐下的单次实测值。

## 值得关注的作者

- [@HeyAbhishek](https://x.com/HeyAbhishek) - `Person` · EN · Seedance 动画提示词 · 分享电影感 AI 动画短片背后的完整提示词。代表作: [帖子](https://x.com/HeyAbhishek/status/2106369769956065518)。
- [@liyue_ai](https://x.com/liyue_ai) - `Person` · 中文 · Seedance 导演 Skill · 在 GitHub（liyue-aigc）开源 Seedance 导演类 Skill。代表作: [帖子](https://x.com/liyue_ai/status/2093592225162960982)。
- [@Pluvio9yte](https://x.com/Pluvio9yte) - `Person` · 中文 · Agent 视频流水线 · 长文拆解 Codex + Hyperframes 视频流水线及其背后的 Skill。代表作: [帖子](https://x.com/Pluvio9yte/status/2081648099680743554)。
- [@GeekCatX](https://x.com/GeekCatX) - `Person` · 中文 · 低成本解说视频流程 · 用 Agent 加图像/视频模型做低成本解说视频的分步流程。代表作: [帖子](https://x.com/GeekCatX/status/2078488413045747814)。

## 相关列表

- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) - `List` · ⭐ 2.2k · MIT · Seedance 2.5 / 2.0 提示词库：案例可追溯到原帖，附模板和可安装的视频 Skill。
- [ZeroLu/awesome-seedance](https://github.com/ZeroLu/awesome-seedance) - `List` · ⭐ 2.8k · MIT · Seedance 2.0 提示词、指南和视频生成工作流合集。
- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) - `List` · ⭐ 34.7k · MIT · GPT Image 2 / 2.5 提示词与案例库，附模板；适合做视频前的关键帧和分镜。
- [YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts) - `List` · ⭐ 2.2k · CC-BY-4.0 · 2000+ 条精选 Seedance 2.0 视频提示词，覆盖电影感、动漫、UGC、广告、梗视频等风格，附 API 指南和角色一致性技巧。

## 参与贡献

只改 `data/catalog.json`（不要直接改 README），运行 `python3 scripts/generate_readme.py`，再提 PR。提交前请先读 [CONTRIBUTING.zh-CN.md](./CONTRIBUTING.zh-CN.md) 里的门槛，不达标的条目会直接关闭。

---

<sub>列表内容以 [CC0 1.0](./LICENSE) 发布。所链接的项目、帖子和商标归各自所有者；收录不代表对方背书，也不代表 Token360 背书。</sub>

<div align="center">

<!-- Iron Man Arc Reactor Header -->
<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=0,2,8,19&height=220&section=header&text=GitInterrogator&fontSize=65&fontColor=FFD700&animation=fadeIn&fontAlignY=38&desc=AI-Native%20Technical%20Interview%20%7C%20Powered%20by%20Your%20Code&descAlignY=58&descSize=18&descColor=FF6B35" width="100%"/>

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Share+Tech+Mono&weight=700&size=20&pause=900&color=FFD700&center=true&vCenter=true&random=false&width=650&lines=AI+that+reads+your+repo+before+it+talks+to+you.;Voice-based.+Stateful.+Grounded+in+your+code.;Clone+%E2%86%92+Index+%E2%86%92+Interview+%E2%86%92+Evaluate.;No+hallucinations.+No+generic+questions.;Built+different.+%F0%9F%94%A5" alt="Typing SVG" />
</a>

<br/><br/>

<!-- Badges Row 1 — Iron Man Red + Gold -->
<img src="https://img.shields.io/badge/%F0%9F%94%B4%20Status-In%20Development-FFD700?style=for-the-badge&labelColor=B22222"/>
<img src="https://img.shields.io/badge/LLM-Llama%203.2-FFD700?style=for-the-badge&logo=meta&labelColor=B22222&logoColor=FFD700"/>
<img src="https://img.shields.io/badge/Voice-Deepgram-FFD700?style=for-the-badge&labelColor=8B0000&logoColor=FFD700"/>
<img src="https://img.shields.io/badge/Framework-LangGraph-FFD700?style=for-the-badge&labelColor=B22222"/>

<br/>

<!-- Badges Row 2 -->
<img src="https://img.shields.io/badge/Python-3.11+-FFD700?style=for-the-badge&logo=python&labelColor=8B0000&logoColor=FFD700"/>
<img src="https://img.shields.io/badge/FastAPI-WebSockets-FFD700?style=for-the-badge&logo=fastapi&labelColor=B22222&logoColor=FFD700"/>
<img src="https://img.shields.io/badge/ChromaDB-Vector%20Store-FFD700?style=for-the-badge&labelColor=8B0000"/>
<img src="https://img.shields.io/badge/License-MIT-FFD700?style=for-the-badge&labelColor=B22222"/>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,8&height=4" width="100%"/>

</div>

<br/>

```
╔══════════════════════════════════════════════════════════╗
║           GITINTERROGATOR — SYSTEM BOOT v0.1             ║
╠══════════════════════════════════════════════════════════╣
║  ⬡  AI CORE    : Llama 3.2 Local ............. ONLINE   ║
║  ⬡  VOICE STT  : Deepgram Nova-3 ............. READY    ║
║  ⬡  VECTOR DB  : ChromaDB .................... INDEXED  ║
║  ⬡  AGENT      : LangGraph State Machine ..... ARMED    ║
║  ⬡  AWAITING   : GitHub Repository URL               ║
╚══════════════════════════════════════════════════════════╝
```

<br/>

---

## 🔴 The Problem I Identified

As a **fresher or early professional**, you put real effort into your projects.  
You build them, you push them to GitHub, you're proud of them.  
But the moment an interviewer asks a *specific* question about your own code —

```
🔴 Interviewer : "Why did you structure the auth flow this way?"
🟡 You         : *remembers writing it, but can't articulate the why*
🔴 Interviewer : "How does your data pipeline handle failures?"
🟡 You         : *knows the answer is in the code, but blanks under pressure*
```

It's not that you don't know your project.  
It's that **nobody ever drilled you on it.**  
No one asked you the hard, specific questions about *your* code before the interview did.

Existing prep tools don't solve this — they're generic, disconnected from your repo,  
and can't ask *"walk me through line 47 of your service layer."*

**That's the gap. GitInterrogator maps it — and closes it. 🔥**

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,8&height=4" width="100%"/>
</div>

## 🟡 What GitInterrogator Does

<div align="center">

```
   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
   │  GitHub     │    │  Semantic   │    │  Live Voice │    │   Scored    │
   │  Repo  ─────┼───▶│  Indexing ──┼───▶│  Interview ─┼───▶│   Report   │
   │             │    │  ChromaDB   │    │  LangGraph  │    │  LLM Judge  │
   └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

</div>

You give it a GitHub repo link.  
It **clones it**, **understands every function and class semantically**, then conducts a **live, voice-driven technical interview** — grounded entirely in *your* project.

It asks things like:

<div align="center">

> *"Earlier you said this module handles authentication — but your `auth_service.py` shows token validation is in the middleware layer. Walk me through that decision."*

</div>

No hallucinations. No generic questions. Just your code, interrogated. ⚙️

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,8&height=4" width="100%"/>
</div>

## ⚙️ How It Works — 3 Phases

<details>
<summary><b>🔴 Phase A — Ingestion & Indexing</b></summary>

<br/>

```python
# Language-aware chunking — splits at functions & classes,
# not arbitrary line counts.

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=1000,
    chunk_overlap=100
)
```

- 📦 Clones repo into an **isolated sandboxed** temp directory
- 🧩 Splits code at **function & class boundaries** for true semantic understanding
- 🧠 Embeds all chunks into **ChromaDB** for real-time retrieval during the interview

</details>

<details>
<summary><b>🟡 Phase B — The Live Agentic Interview</b></summary>

<br/>

```
  ╔══════════╗     ╔══════════════╗     ╔═════════╗     ╔════════════╗
  ║  START   ║────▶║  ASK (RAG)   ║────▶║ LISTEN  ║────▶║  EVALUATE  ║
  ╚══════════╝     ╚══════════════╝     ╚═════════╝     ╚════════════╝
                          ▲                                     │
                          └──────── follow-up or next Q ────────┘
                                    [ LangGraph Loop ]
```

- 🎯 **LangGraph** state machine — full conversation memory across the session
- 🔍 **RAG** surfaces the most complex, critical parts of your code per question
- 🎙️ **Deepgram Nova-3** transcribes your voice in real-time via WebSocket
- 🔊 **Deepgram Aura** delivers responses in natural-sounding speech

</details>

<details>
<summary><b>⚙️ Phase C — Evaluation Report</b></summary>

<br/>

```json
{
  "technical_accuracy": 87,
  "architectural_understanding": 92,
  "communication_clarity": 78,
  "overall_readiness": "Senior-Ready 🏆",
  "insights": [
    "Strong grasp of async patterns in FastAPI",
    "Could elaborate more on DB indexing choices",
    "Articulates trade-offs well under pressure"
  ]
}
```

- 📊 Full transcript aggregated after the 15–30 min session
- ⚖️ Verbal answers cross-checked against **actual source code** in vector DB
- 🎯 Zero human bias — objective *Technical Readiness* score

</details>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,8&height=4" width="100%"/>
</div>

## 🛠️ Tech Stack

<div align="center">

| Layer | Tech | Purpose |
|:---:|:---:|:---|
| 🧩 **Orchestration** | ![LangGraph](https://img.shields.io/badge/LangGraph-FF4500?style=flat-square&logoColor=FFD700) | Stateful cyclic interview logic + memory |
| 🔗 **RAG** | ![LangChain](https://img.shields.io/badge/LangChain-8B0000?style=flat-square&logoColor=FFD700) | Code loading, semantic chunking, retrieval |
| 🧠 **LLM** | ![Llama](https://img.shields.io/badge/Llama%203.2-Local-B22222?style=flat-square&logoColor=FFD700) | Local inference — zero cost, zero data leakage |
| 📦 **Vector DB** | ![Chroma](https://img.shields.io/badge/ChromaDB-FF4500?style=flat-square&logoColor=FFD700) | Semantic search over code embeddings |
| 🎙️ **STT** | ![Deepgram](https://img.shields.io/badge/Deepgram-Nova--3-8B0000?style=flat-square&logoColor=FFD700) | Sub-second speech-to-text transcription |
| 🔊 **TTS** | ![Deepgram](https://img.shields.io/badge/Deepgram-Aura-B22222?style=flat-square&logoColor=FFD700) | Natural AI voice output |
| ⚡ **Backend** | ![FastAPI](https://img.shields.io/badge/FastAPI-WebSockets-FF4500?style=flat-square&logo=fastapi&logoColor=FFD700) | Full-duplex real-time audio streaming |

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,8&height=4" width="100%"/>
</div>

## 💡 Why This Hits Different

<div align="center">

```
❌  Chat with PDF          →  Basic RAG, done a million times
❌  Generic mock interview →  Zero context about your actual project
✅  GitInterrogator        →  Stateful Voice Agent for Code Analysis
```

</div>

| What most tools do | What this does |
|---|---|
| Ask generic questions | Asks about **your** functions, **your** architecture |
| Forget context mid-session | Full memory via **LangGraph** — every answer remembered |
| Hallucinate your features | **RAG-grounded** — can't fabricate what isn't in your repo |
| Text chat only | **Real-time voice** — actual interview feel |
| Cloud LLM = your code uploads | **Local Llama** — your code never leaves your machine |

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,8&height=4" width="100%"/>
</div>

## 🗺️ Roadmap

```
 ✅  COMPLETE — Concept & architecture locked in
 🔄  ACTIVE   — Core repo ingestion pipeline
 🔄  ACTIVE   — LangGraph interview state machine
 🔄  ACTIVE   — Deepgram voice integration (STT + TTS)
 🔄  ACTIVE   — WebSocket streaming backend
 🔄  ACTIVE   — LLM-as-Judge evaluation engine
 ⏳  QUEUED   — Frontend interview UI
 ⏳  QUEUED   — Multi-repo & monorepo support
 ⏳  QUEUED   — Interview history dashboard
 ⏳  QUEUED   — Exportable PDF score reports
```

---

## 🚀 Getting Started

> 🔴 **Still being built. Setup docs drop with the first stable release.**  
> Star the repo to get notified. ⭐

```bash
# Coming soon...
git clone https://github.com/yourusername/gitinterrogator
cd gitinterrogator
pip install -r requirements.txt
```

---

## 🤝 Contributing

Early days. If you're building in the AI / voice / code-analysis space and want to collaborate — open an issue. Let's build. 🔥

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,8,19&height=140&section=footer&animation=fadeIn" width="100%"/>

**Built to close the gap between what you've built and how you're evaluated.**

<br/>

![Views](https://komarev.com/ghpvc/?username=gitinterrogator&color=B22222&style=for-the-badge&label=REPO+VIEWS)

<br/>

*Drop a ⭐ if this slaps. It means a lot fr.*

</div>

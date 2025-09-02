Got it 👍 — here’s the **entire cleaned-up `README.md`** in one block so you can copy-paste directly into your project:

---

```markdown
# GenAI Web Agent

This project is a minimal AI Agent built with Google's **Agent Development Kit (ADK)** and **Gemini** (`gemini-2.5-flash`).  
It demonstrates how to set up an agent with tool calls, prompts, and run it in the **ADK Web Debugger** UI.

---

## Project Structure
```

GenAIWebAgent/
│
├── myagent/
│   ├── **init**.py       # Exports root\_agent
│   ├── agent.py          # Defines root\_agent (LlmAgent)
│   ├── prompt.py         # System prompt for the agent
│   ├── tools.py          # Tool functions (e.g., fetch\_url\_content)
│
├── .env                  # Environment variables (ignored in Git)
├── requirements.txt      # Dependencies
├── .gitignore            # Git ignore rules

````

---

## Features
- **Gemini integration**: Uses `gemini-2.5-flash` via Google GenAI SDK.
- **Custom prompt**: Configurable system instructions in `prompt.py`.
- **Tools**: Example `fetch_url_content` tool fetches and cleans webpage text.
- **ADK Web Debugger**: Run the agent in a ready-to-use UI for debugging.

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/genai-web-agent.git
cd genai-web-agent
````

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

### 5. Run ADK Web

```bash
adk web myagent
```

Open in your browser:

```
http://127.0.0.1:8000
```

---

## Usage

* Enter queries directly into the ADK Web UI.
* When you provide a URL, the agent will invoke the `fetch_url_content` tool and analyze/summarize the content.
* You can view tool usage under **Trace → Invocations** in the ADK Web Debugger.

---

## Requirements

* Python 3.10+
* Dependencies listed in `requirements.txt`:

  * google-adk\[web]
  * google-genai
  * python-dotenv
  * requests
  * beautifulsoup4


Do you also want me to generate a **ready-to-use `requirements.txt`** file with pinned versions so your GitHub repo runs exactly the same for anyone cloning it?
```

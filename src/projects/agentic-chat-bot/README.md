# 🤖 Agentic Chat Bot

A simple guide to set up your **Agentic Chat Bot** project — including Git setup, branch creation, virtual environment setup, dependency installation, and pushing your work to GitHub.

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- **Git**
- **Python 3.8+**
- **pip**

Check installations:
```bash
git --version          # Verify Git installation
python3 --version      # Verify Python installation
pip --version          # Verify pip installation
````

---

## 🌱 1. Create or Initialize a Git Project

If starting fresh:

```bash
mkdir agentic-chat-bot            # Create project folder
cd agentic-chat-bot               # Move into folder
git init                          # Initialize a new Git repo
git add .                         # Stage files
git commit -m "Initial commit"    # First commit
```

If already in a repo:

```bash
git checkout main                 # Switch to main branch
git pull origin main              # Get latest main updates
```

---

## 🌿 2. Create a New Branch

```bash
git checkout -b agentic-chat-bot  # Create and switch to new branch
```

---

## 🏗️ 3. Set Up Python Virtual Environment

```bash
python3 -m venv agentic-chat-bot-env   # Create a virtual environment
```

Activate it:

**macOS / Linux**

```bash
source agentic-chat-bot-env/bin/activate   # Activate virtual environment
```

**Windows (PowerShell)**

```bash
agentic-chat-bot-env\Scripts\Activate.ps1  # Activate virtual environment
```

---

## 📦 4. Create `requirements.txt`

Create a file named `requirements.txt` and add:

```
langchain
langraph
langchain_community
langchain_core
langchain_groq
langchain_openai
faiss-cpu
streamlit
tavily-python

```

Then install dependencies:

```bash
pip install -r requirements.txt    # Install packages
```

(Optional) Save exact versions:

```bash
pip freeze > requirements.txt      # Update requirements.txt
```

---

## 🧹 5. Deactivate the Environment

```bash
deactivate     # Exit virtual environment
```

---

## 🚀 6. Commit and Push Changes

```bash
git add .                                       # Stage all changes
git commit -m "Setup project environment"       # Commit setup
git push origin agentic-chat-bot                # Push branch to remote
```

---

## ✅ You’re Ready!

You now have:

* A Git project and branch
* A Python virtual environment
* Installed dependencies

Start coding your **Agentic Chat Bot**! 🤖


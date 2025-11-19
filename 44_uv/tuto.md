Below is the **updated + improved uv reference**, now including:

✅ `uv add -r requirements.txt`
✅ How to **export** dependencies from uv → `requirements.txt`
✅ How to **import** requirements.txt → uv
✅ How to **update** dependencies inside a uv project
✅ How to **sync** pip-style and uv-style environments

Clean, Markdown-ready.

---

# 🐍 **uv — Full Command Reference (Updated)**

Everything important and concise.

---

# 📦 Project Creation

```sh
uv init
uv init projectname
```

---

# 🧬 Virtual Environments

```sh
uv venv --python 3.11.6
uv venv --python 3.12.3
uv venv --python 3.13.1
```

Activate:

```sh
source .venv/bin/activate
```

---

# 📚 Add, Remove, and Update Dependencies

### Add packages

```sh
uv add pandas numpy seaborn matplotlib
```

### Add from a **requirements.txt** (NEW)

Equivalent to `pip install -r requirements.txt`:

```sh
uv add -r requirements.txt
```

### Remove packages

```sh
uv remove pandas numpy
```

### Update *all* dependencies to latest compatible versions

```sh
uv lock --upgrade
uv sync
```

Or update a **single package**:

```sh
uv add pandas --upgrade
```

---

# 🔒 Lockfile & Syncing

Lock (freeze the dependency graph):

```sh
uv lock
```

Sync the environment to the lockfile:

```sh
uv sync
```

---

# 🧵 Dependency Graph

```sh
uv tree
```

---

# ▶️ Running Scripts

```sh
uv run main.py
uv run python
```

---

# 🛠️ Managing Global CLI Tools (pipx alternative)

```sh
uv tool install ipython
uv tool install jupyter
uv tool list
uv tool uninstall jupyter
```

---

# 🐍 Python Versions

```sh
uv python list
uv python install 3.12.3
```

---

# 🔧 Exporting Dependencies (uv → requirements.txt)

When you want to convert a uv project into a “pip-installable” one:

### **1. Create a requirements.txt from your uv project**

```sh
uv export --format requirements-txt > requirements.txt
```

or explicitly:

```sh
uv export --without-hashes --format requirements-txt > requirements.txt
```

This generates a clean, pip-compatible file.

---

# 🔧 Importing Dependencies (requirements.txt → uv)

If someone gives you a repo with `requirements.txt`, and you want to use uv:

```sh
uv add -r requirements.txt
uv lock
uv sync
```

---

# 🛠️ Updating a uv Project to Latest Versions

Inside the uv project folder:

### **Upgrade every dependency**

```sh
uv lock --upgrade
uv sync
```

### **Upgrade a specific package**

```sh
uv add scikit-learn --upgrade
```

---

# 🗂️ Creating requirements.txt for pip Users

If your repo uses **uv**, but your colleagues use **pip**, do:

```sh
uv export --without-hashes --format requirements-txt > requirements.txt
```

Commit it to the repo:

```
pyproject.toml
uv.lock
requirements.txt   <-- generated for pip users
```

This guarantees compatibility.

---

# 🔥 Ideal Workflow (Final Updated Version)

```
uv init myproject
cd myproject

uv venv --python 3.12.3
uv add pandas numpy scikit-learn matplotlib seaborn

# If you have requirements.txt:
uv add -r requirements.txt

# Lock + sync
uv lock
uv sync

uv run main.py

# Export for pip world
uv export --format requirements-txt > requirements.txt
```

---

# Want a Markdown file?

If you want, I can generate a **complete `uv_cheatsheet.md`** ready for GitHub.

Just say:

👉 **“generate uv README.md”**

And I will output the full file.


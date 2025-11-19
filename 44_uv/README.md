Here is **everything you need** — a **clean, succinct, Markdown-friendly reference** of the most important **`uv` commands**, PLUS a **complete workflow** you can reuse for any project (data science, ML, apps, CLI tools).

No fluff. Only what matters.

---

# 🐍 **uv — Quick Reference (All Main Commands)**

*(your cheat-sheet, clean + concise)*

---

# 📦 **Project Creation**

### **Create new project in a folder**

```sh
uv init
```

### **Create new project with a name**

```sh
uv init projectname
```

---

# 🧬 **Virtual Environments**

### **Create a venv with specific Python**

```sh
uv venv --python 3.11.6
uv venv --python 3.12.3
uv venv --python 3.13.1
```

### **Activate the environment**

macOS/Linux:

```sh
source .venv/bin/activate
```

---

# 📚 **Add / Remove Dependencies**

### **Add packages**

```sh
uv add pandas numpy matplotlib seaborn
```

### **Add dev packages**

```sh
uv add --dev black ruff pytest
```

### **Remove packages**

```sh
uv remove pandas numpy
```

---

# 🔒 **Dependency Lockfile & Sync**

### **Create/update lockfile**

```sh
uv lock
```

### **Sync environment to lockfile**

(install exactly the versions from `uv.lock`)

```sh
uv sync
```

---

# 🧵 **Dependency Graph**

### **Show dependency tree**

```sh
uv tree
```

---

# ▶️ **Running Code**

### **Run a script using the project environment automatically**

```sh
uv run main.py
```

### **Run Python REPL inside the env**

```sh
uv run python
```

---

# 📈 **Installing CLI Tools Globally (pipx replacement)**

```sh
uv tool install ipython
uv tool install jupyter
uv tool install kedro
```

List installed tools:

```sh
uv tool list
```

Uninstall tool:

```sh
uv tool uninstall jupyter
```

---

# 🔍 **Environment Info**

### **Show Python versions known to uv**

```sh
uv python list
```

### **Install a new Python version**

```sh
uv python install 3.11.9
```

---

# 📁 **Project Commands Summary**

| Command             | Meaning                   |
| ------------------- | ------------------------- |
| `uv init`           | Create project            |
| `uv venv`           | Create venv               |
| `uv add`            | Add package               |
| `uv remove`         | Remove package            |
| `uv sync`           | Install according to lock |
| `uv lock`           | Update lock file          |
| `uv tree`           | Dependency graph          |
| `uv run`            | Run script with env       |
| `uv tool install`   | Global tools              |
| `uv python install` | Install Python versions   |

---

# 🔥 **Your Ideal Workflow (Step-by-Step)**

*(based on how you’re already using uv, but cleaner)*

---

## **1. Create project folder**

```sh
mkdir datascience
cd datascience
```

## **2. Initialize project**

```sh
uv init
```

## **3. Create environment**

```sh
uv venv --python 3.12.3
```

## **4. Install core data stack**

```sh
uv add pandas numpy scipy matplotlib seaborn scikit-learn lightgbm optuna
```

## **5. Install notebooks & interactive tools**

```sh
uv add ipython jupyter notebook
```

---

## **6. OPTIONAL — Lock dependencies**

```sh
uv lock
```

## **7. Sync venv with lockfile (team use / CI)**

```sh
uv sync
```

---

## **8. Run a script**

```sh
uv run main.py
```

## **9. Inspect dependency graph**

```sh
uv tree
```

---

## **10. Add Kedro or other frameworks**

```sh
uv add kedro
```

---

## **11. Run Jupyter Notebook**

```sh
uv run jupyter notebook
```

---

# 🧨 **Minimal Workflow Template to Paste Anywhere**

```
uv init myproject
cd myproject

uv venv --python 3.12.3
uv add pandas numpy scikit-learn matplotlib seaborn
uv add ipython jupyter notebook

uv run jupyter notebook
```

---

If you want, I can generate a **Markdown file (.md)** for your GitHub documenting:

* your local Python versions
* your Spark setup
* all uv commands
* your environment layout
* recommended project structure

Just say **"generate the uv documentation .md"** and I build it for you.


# 🧠 Automated Python Docstring Generator

An intelligent tool that automatically generates, analyzes, and enforces Python docstrings using AST parsing and PEP-257 standards, improving code readability and maintainability.

---

## 🚀 Features

* ⚙️ Automatic docstring generation for functions and classes
* 🔍 AST-based code analysis for accurate structure parsing
* 📏 PEP-257 compliance validation using **pydocstyle**
* 🔁 Pre-commit hooks to enforce documentation before commits
* 🚀 CI/CD integration with GitHub Actions
* 📊 Improves code quality, consistency, and maintainability

---

## 🛠️ Tech Stack

* **Language:** Python
* **Core Concept:** AST (Abstract Syntax Tree)
* **Linting Tool:** pydocstyle
* **Automation:** Pre-commit hooks & GitHub Actions
* **Frontend (optional):** React (for UI interaction)

---

## 📁 Project Structure

```id="2k3lq8"
docstring_enforcer/
 ├── analyzer/
 ├── generator/
 ├── validator/
 └── main.py

frontend/
 ├── src/
 └── public/

test_files/
 └── sample.py

pyproject.toml
.pre-commit-config.yaml
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```id="l2m1o9"
git clone https://github.com/Vanshika-d25/Automated_Python_Docstring_Generator.git
```

2. Navigate to project folder

```id="u7d2k1"
cd Automated_Python_Docstring_Generator
```

3. Install dependencies

```id="f5n3q2"
pip install -r backend/requirements.txt
```

4. Run the tool

```id="g8p4r3"
python backend/app.py
```

---

## 🧠 How It Works

* Parses Python files using AST
* Extracts function/class metadata
* Generates structured docstrings
* Validates them against PEP-257 standards
* Enforces rules via pre-commit hooks and CI pipeline

---

## 🌟 Future Enhancements

* 🤖 AI-powered context-aware docstring generation
* 🌐 Web interface for uploading code files
* 📦 VS Code extension integration
* 📊 Documentation coverage analytics

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

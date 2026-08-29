# Wikimedia Pywikibot Tools & Data Pipelines

![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB.svg?logo=python&logoColor=white)
![MediaWiki API](https://img.shields.io/badge/API-MediaWiki%20%2F%20Wikibase-006699.svg?logo=wikipedia&logoColor=white)
![Framework](https://img.shields.io/badge/Framework-Pywikibot%2011.7-8A2BE2.svg)

A suite of modular Python automation scripts engineered using **Pywikibot** and **MediaWiki REST/Action APIs**. Designed for structured metadata enrichment, multilingual label synchronization on **Wikidata**, and automated content maintenance on **Wikipedia**.

---

## 📌 Architecture & Modules Overview

| Script Name | Target Platform | Primary Function | API Endpoints Used |
| :--- | :--- | :--- | :--- |
| `reach_autoconfirmed_wikidata.py` | **Wikidata (`wikidata.org`)** | User sandbox revision automation & account milestone verification | `edit`, `query`, `tokens` |
| `batch_enrich_wikidata.py` | **Wikidata (`wikidata.org`)** | Batch multilingual entity enrichment across Wikidata Q-IDs | `wbsetlabel`, `wbsetdescription` |
| `add_hindi_labels.py` | **Wikidata (`wikidata.org`)** | Entity label & description synchronization (Hindi `hi` & English `en`) | `wbsetlabel`, `wbsetdescription` |
| `test_hi_wikipedia.py` | **Hindi Wikipedia (`hi.wikipedia.org`)** | Indic content translation & sandbox maintenance | `edit`, `query`, `tokens` |
| `test_sandbox_edit.py` | **Wikipedia (`en.wikipedia.org`)** | User sandbox content automation & page revision management | `edit`, `query`, `tokens` |
| `test_script.py` | **Wikidata (`wikidata.org`)** | Read-only entity validation & connectivity verification | `wbgetentities` |
| `user-config.py` | **Configuration** | Family, site, and account routing settings | Pywikibot Core Config |

---

## ⚙️ Data Flow Architecture

```
                               ┌────────────────────────────────┐
                               │   Wikimedia BotPassword API    │
                               └───────────────┬────────────────┘
                                               │
                                               ▼
┌─────────────────────────┐        ┌─────────────────────────┐        ┌─────────────────────────┐
│ Pywikibot Configuration │ ─────► │   Authentication &      │ ─────► │    Wikidata/Wikipedia   │
│   (user-config.py)      │        │   Session Throttling    │        │    Data Mutation        │
└─────────────────────────┘        └─────────────────────────┘        └─────────────────────────┘
                                               │
                                               ▼
                               ┌────────────────────────────────┐
                               │   Audit Log & Revision History │
                               └────────────────────────────────┘
```

---

## 🚀 Installation & Local Setup

### 1. Clone Repository & Initialize Environment

```bash
# Clone the repository
git clone https://github.com/Shreya71703/wikimedia-pywikibot-tools.git
cd wikimedia-pywikibot-tools

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate
```

### 2. Install Core Dependencies

```bash
pip install pywikibot mwparserfromhell wikitextparser
```

### 3. Setup Credentials Configuration

Create `user-password.py` in the root directory (*excluded from version control via `.gitignore`*):

```python
# user-password.py
('Shreyapedia', BotPassword('YourBotName', 'YourBotPasswordSecret'))
```

---

## 💻 Usage Examples

### Executing Wikidata Milestone Automation

```bash
python reach_autoconfirmed_wikidata.py
```

### Executing Batch Wikidata Entity Enrichment

```bash
python batch_enrich_wikidata.py
```

---

## 🔒 Security & Best Practices

- **BotPassword Authentication:** Authentication uses granular MediaWiki BotPassword grants rather than primary user credentials.
- **Credential Protection:** Secrets are isolated in `user-password.py` and excluded via `.gitignore`.
- **API Throttling:** Respects MediaWiki server response limits and bot speed controls (`throttle.ctrl`).

---

## 👩‍💻 Author & Maintainer

**Shreya Shukla (Shreyapedia)**  
Open Source Developer • MediaWiki Core & Extension Contributor • Women in Tech Lead  
- **GitHub:** [@Shreya71703](https://github.com/Shreya71703)  
- **Meta-Wiki Profile:** [User:Shreyapedia](https://meta.wikimedia.org/wiki/User:Shreyapedia)  

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.

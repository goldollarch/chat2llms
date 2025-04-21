# chat2llms

![CI Status](https://github.com/goldollarch/chat2llms/workflows/Build%20and%20Deploy%20Documentation/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/chat2llms.svg) ![Python Versions](https://img.shields.io/pypi/pyversions/chat2llms.svg)
[![Documentation Status](https://readthedocs.org/projects/chat2llms/badge/?version=latest)](https://chat2llms.readthedocs.io/en/latest/?badge=latest) 

Welcome to **Chat2LLMs** !

Let’s use **Large Language Models** to **chat** with **Master of Laws** !

**chat2llms** is a research initiative that facilitates communication between large language models and legal professionals. Its goal is to leverage existing LLMs to analyze complex legal topics through concrete judicial cases, deepen understanding of legal disciplines, and explore the limitations and future development directions of current LLMs.

This project represents an attempt to apply LLMs to the study and analysis of specific judicial cases. We focus on [a chinese typical real-world criminal case](https://goldollarch.github.io/chat2llms/case/intro.html) as our research subject. Using LLMs, we conduct detailed textual analysis of several formal legal documents from this case.

For more information, refer to [the documentation](ttps://goldollarch.github.io/chat2llms/).


## ✨ Features and Contributions

### Technical Framework: Provides tools for integrating LLMs into legal analysis

* Compare LLM responses to identical prompts.
* Abstract base class for easy integration of various LLMs (OpenAI, Gemini, DeepSeek, etc.).
* Structured response handling.
* Basic analysis and comparison tools for model outputs.
* Extendable architecture for adding new comparison metrics.

### Case-Driven Research: Demonstrates LLM performance in real-world legal scenarios

* Converting unstructured legal texts into **structured data** (e.g., case type, party information, disputed issues, legal basis) and identifying legal entities and relationships (e.g., torts, roles of parties such as plaintiff/defendant/third party, timelines).
* Parsing the court’s **reasoning chain** of "facts → legal components → conclusions" to understand how facts are mapped to legal provisions.
* Conducting **quality and compliance reviews** of legal texts to detect formatting errors, incorrect legal citations, and logical inconsistencies.
* And so on.

### Critical Evaluation

* Identifies gaps in LLM capabilities (e.g., nuanced legal interpretation)
* Proposes future improvements.


## 📦 Installation

The following command installs `chat2llms` from the [Python Package Index](https://pypi.org/project/chat2llms/). You will need a working installation of Python and pip.

```bash
pip install chat2llms
```

If you need to install from the GitHub repository (e.g., for development or latest changes):

```bash
pip install git+[https://github.com/](https://github.com/)goldollarch/chat2llms.git
```


## 🚀 Quick Start

Here's a minimal example to get you started:

```python

from chat2llms.analyzer import AnswerAnalyzer
from chat2llms.model_response import OpenAIResponse, GeminiResponse
from chat2llms.base_client import BaseClient

# --- Usage ---

# 1. Create instances of your LLM clients
#    (Replace with actual client classes like OpenAIClient, GeminiClient, etc.)

deepseek = BaseClient("deepseek")
gemini = BaseClient("gemini")

# 2. Define the prompt you want to test
question = "What is 2 + 2?"

# 3. Get responses from each model (in a real app, this would involve API calls)
#    Create ModelResponse objects to hold the results
deepseek_response = OpenAIResponse(deepseek)
gemini_response = GeminiResponse(gemini)


# 4. Analyze and compare the responses
analyzer = AnswerAnalyzer(gemini_response, deepseek_response, question)

# 5. Print or process the comparison results
print(f"Similarity: {analyzer.compute_similarity():.2f}")
print(f"semantic_sim: {analyzer.compute_semantic_similarity():.2f}")
print(analyzer.highlight_differences())

# You can add more advanced analysis or custom comparison logic in the AnswerAnalyzer.
```


## 📖 Documentation

For more detailed information on installation, advanced usage, API reference, and adding new LLM clients or analysis methods, and some results, please refer to [the official documentation](https://goldollarch.github.io/chat2llms/).


## 🙌 Contributing

We welcome contributions\! If you'd like to contribute, please check out our [Contributing Guidelines](https://goldollarch.github.io/chat2llms/contributing.html).

Here are some ways you can contribute:

* Report bugs
* Suggest new features
* Submit pull requests for bug fixes or new features
* Improve documentation

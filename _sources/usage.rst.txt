Usage
=====

This section provides detailed examples of using **chat2llms** to compare responses 
from large language models (LLMs). The examples include basic usage, and 
command-line interface (CLI).

Basic Comparison
----------------

Compare responses from two mock LLM clients (DeepSeek and Grok) for a simple prompt:

.. code-block:: python

   from chat2llms.analyzer import AnswerAnalyzer
   from chat2llms.model_response import OpenAIResponse, GeminiResponse
   from chat2llms.base_client import BaseClient

   # Initialize clients
   gemini = BaseClient("gemini")
   deepseek = BaseClient("deepseek")

   # Create responses
   question = "What is 2 + 2?"

   gemini_response = GeminiResponse(gemini)
   deepseek_response = OpenAIResponse(deepseek)

   # Analyze differences
   analyzer = AnswerAnalyzer(gemini_response, deepseek_response, question)
   print(f"Similarity: {analyzer.compute_similarity():.2f}")
   print(f"semantic_sim: {analyzer.compute_semantic_similarity():.2f}")
   print(analyzer.highlight_differences())

**Output**:

.. code-block:: text

   Text Similarity: 0.09
   Semantic Similarity: 0.77

   Response 1 (gemini-1.5-pro):
   2 + 2 = 4

   Response 2 (deepseek-reasoner):
   The sum of 2 and 2 is calculated as follows:

   **Step 1:** Start with the number 2.  
   **Step 2:** Add 2 to it.
   **Step 3:** Combining the quantities results in 4.


Command-Line Interface
----------------------------

**chat2llms** provides a Command-Line Interface (CLI) for quick comparisons.

After installing (Refer to :doc:`installation`) the package, run:

.. code-block:: bash

   chat2llms --model1 openai --model2 gemini --prompt "Solve 2 + 2"

**Output**:

.. code-block:: text

   === Prompt ===
   Solve 2 + 2

   === OPENAI Response ===
   2 + 2 = 4

   === GEMINI Response ===
   2 + 2 = 4

   === Text Similarity ===
   0.9473684210526315

   === Semantic Similarity ===
   0.9281893463830239

   === Highlight of Differences ===
   Response 1 (gpt-3.5-turbo):
   2 + 2 = 4
   Response 2 (gemini-1.5-pro):
   2 + 2 = 4


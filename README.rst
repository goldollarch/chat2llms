============
 Chat2LLMs
============

Welcome to **Chat2LLMs** !

Let’s use **Large Language Models** to **chat** with **Master of Laws** !

Features
========

**chat2llms** is a research initiative that facilitates communication between large language models and legal professionals. 
Its goal is to leverage existing LLMs to analyze complex legal topics through concrete judicial cases, deepen understanding of legal disciplines, 
and explore the limitations and future development directions of current LLMs.  

.. note::

   This project is under development.

This project represents an attempt to apply LLMs to the study and analysis of specific judicial cases. 
We focus on a **typical** **real-world** judicial case [Refer to case :doc:`docs/source/case/intro`] as our research subject. 
Using LLMs, we conduct detailed textual analysis of several formal 
legal documents from this case. 


The **objectives** include:  

    • Converting unstructured legal texts into **structured data** (e.g., case type, party information, disputed issues, legal basis) and identifying legal entities and relationships (e.g., torts, roles of parties such as plaintiff/defendant/third party, timelines).  

    • Parsing the court’s **reasoning chain** of "facts → legal components → conclusions" to understand how facts are mapped to legal provisions.  

    • Conducting **quality and compliance reviews** of legal texts to detect formatting errors, incorrect legal citations, and logical inconsistencies.  

    • And so on.

**Key Contributions:**  

    • **Technical Framework**: Provides tools for integrating LLMs into legal analysis.  

    • **Case-Driven Research**: Demonstrates LLM performance in real-world legal scenarios.  

    • **Critical Evaluation**: Identifies gaps in LLM capabilities (e.g., nuanced legal interpretation) and proposes future improvements.  

For more information, refer to `the documentation`_.


Installation
============

The following command installs chat2llms from source. You will
need a working installation of Python and pip.

.. code-block:: shell

   # Clone the repository
   git clone https://github.com/goldollarch/chat2llms.git

   # Install dependencies
   cd chat2llms
   pip install -r requirements.txt
   pip install -e .


.. _the documentation: https://goldollarch.github.io/chat2llms/

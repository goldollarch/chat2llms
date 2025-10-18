===========
Chat2LLMs
===========

Welcome to **Chat2LLMs** ! 

Let's use Large Language Models (**LLM**) to **chat** with a Master of Laws (**LLM**) ! 

-----------------------

Introduction
==============

**chat2llms** is a research initiative that facilitates communication between large language models and legal professionals. 
Its goal is to leverage existing LLMs to analyze complex legal topics through concrete judicial cases, deepen understanding of legal disciplines, 
and explore the limitations and future development directions of current LLMs.  

.. note::

   This project is under development.

This project represents an attempt to apply LLMs to the study and analysis of specific judicial cases. 
We focus on :doc:`a case of "Xun Xin Zi Shi", often translated as "Picking Quarrels and Provoking Trouble" (PXQT) in mainland China <case/intro>` as our research subject. 
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

--------------------

.. toctree::
   :maxdepth: 2
   :caption: Code
   :hidden:

   usage
   installation
   contributing

.. toctree::
    :maxdepth: 4
    :caption: Case
    :hidden:

    case/intro
    case/docus/index
    case/letters/index

.. toctree::
    :maxdepth: 8
    :caption: Chats
    :hidden:

    chats/prepro/index
    chats/compare/index
    chats/elements/index
    chats/accuse/index
    chats/outlaw/index

.. toctree::
    :maxdepth: 6
    :caption: Gaps
    :hidden:

    gaps/example
    gaps/hallucination
    gaps/practical
    gaps/value
    gaps/censor


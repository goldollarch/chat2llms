Contributing
============

We welcome contributions to **chat2llms**! Please follow these steps to contribute:

1. Fork the repository on GitHub.
2. Clone your fork: ``git clone https://github.com/goldollarch/chat2llms.git``
3. Create a branch: ``git checkout -b feature/your-feature``
4. Make changes and commit: ``git commit -m "Add your feature"``
5. Push to your fork: ``git push origin feature/your-feature``
6. Open a pull request on GitHub.

Development Setup
-----------------

Install development dependencies:

.. code-block:: bash

   pip install -r requirements.txt
   pip install -e ".[dev]"

Run tests:

.. code-block:: bash

   pytest tests/

Code Style
----------

- Follow PEP 8.
- Use ``flake8`` for linting: ``flake8 src/ tests/``
- Format code with ``black``: ``black src/ tests/``
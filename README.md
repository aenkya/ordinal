# PageRank with Uncertainty AI

This repository contains an implementation of the PageRank algorithm, enhanced with Uncertainty AI paradigms, as part of the CS50 AI course. The project demonstrates how probabilistic reasoning and uncertainty modeling can be applied to link analysis and ranking web pages.

## Overview

PageRank is an algorithm originally developed by Google to rank web pages in search results. It works by modeling the behavior of a "random surfer" who clicks on links at random, with the probability of visiting a page depending on the structure of the web.

This implementation extends the classic PageRank by incorporating uncertainty in the transition probabilities, simulating more realistic web navigation and reflecting the inherent unpredictability in user behavior.

## Features

- **Corpus Parsing:** Automatically parses a directory of HTML files to build a corpus of pages and their links.
- **Transition Model:** Models the probability distribution of moving from one page to another, factoring in uncertainty.
- **Sampling & Iterative Methods:** Computes PageRank using both sampling (random walk) and iterative (convergence) approaches.
- **Uncertainty Modeling:** Integrates probabilistic reasoning to handle incomplete or ambiguous link structures.

## Usage

1. Place your HTML corpus in a directory (e.g., `corpus0/`, `corpus1/`, `corpus2/`).
2. Run the main script:

   ```zsh
   python pagerank.py corpus0
   ```

3. The script will output the PageRank values for each page in the corpus.

## Files

- `pagerank.py` — Main script implementing the PageRank algorithm with uncertainty modeling.
- `corpus*/` — Example corpora of HTML pages for testing.

## Requirements

- Python 3.x

No external dependencies are required.

## References

- [PageRank Algorithm - Wikipedia](https://en.wikipedia.org/wiki/PageRank)
- [CS50 AI Course](https://cs50.harvard.edu/ai/)

## License

This project is for educational purposes.

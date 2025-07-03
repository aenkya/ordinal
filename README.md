# Ordinal 

This repository contains an implementation of the PageRank algorithm using the Markov Chain Random Surfer model, as part of the CS50 AI course. The project demonstrates how probabilistic reasoning via Markov chains can be applied to link analysis and ranking web pages.

## Overview

PageRank is an algorithm originally developed by Google to rank web pages in search results. It works by modeling the behavior of a "random surfer" who clicks on links at random, with the probability of visiting a page depending on the structure of the web.

This implementation follows the classic PageRank approach by simulating the random surfer using a Markov chain, where the transition probabilities reflect the likelihood of moving from one page to another based on the link structure.

## Features

- **Corpus Parsing:** Automatically parses a directory of HTML files to build a corpus of pages and their links.
- **Transition Model:** Models the probability distribution of moving from one page to another using the Markov chain random surfer model.
- **Sampling & Iterative Methods:** Computes PageRank using both sampling (random walk) and iterative (convergence) approaches.

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

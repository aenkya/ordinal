import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    if not (0 < DAMPING < 1):
        raise ValueError("Damping factor must be between 0 and 1")
    if SAMPLES <= 0:
        raise ValueError("Number of samples must be a positive integer")
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Initialize transition model
    model = {}
    n = len(corpus)

    # If the page has no links, treat it as linking to all pages
    if not corpus[page]:
        for p in corpus:
            model[p] = 1 / n
        return model

    # Probability of choosing a link from the current page
    prob_linked = damping_factor / len(corpus[page])
    
    # Probability of choosing any page in the corpus
    prob_random = (1 - damping_factor) / n

    return {
        p: (prob_linked if p in corpus[page] else prob_random)
        for p in corpus
    }


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.

    The PageRank value of a page is the fraction of times that page
    was visited during the sampling process.
    The sampling process should start with a random page, and then
    repeatedly choose the next page according to the transition model
    for the current page.
    """
    
    # Initialize PageRank values
    ranks = {page: 0 for page in corpus}
    pages = list(corpus.keys())
    current_page = random.choice(pages)
    for _ in range(n):
        ranks[current_page] += 1
        model = transition_model(corpus, current_page, damping_factor)
        
        # Choose the next page based on the transition model
        current_page = random.choices(
            list(model.keys()), 
            weights=list(model.values())
        )[0]
    return {page: rank / n for page, rank in ranks.items()}


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.

    PR(p) = (1 - damping_factor) / N + damping_factor * sum(PR(q) / L(q))
    where:
    - PR(p) is the PageRank of page p
    - N is the total number of pages in the corpus
    - PR(q) is the PageRank of a page q that links to p
    - L(q) is the number of links from page q
    - damping_factor is the probability of following a link
    - sum is over all pages q that link to p
    - The algorithm should iterate until the PageRank values converge
    (i.e., the change in PageRank values is less than a small threshold).
    """

    # Initialize PageRank values
    threshold = 0.001
    n = len(corpus)

    # Initialize ranks
    ranks = {page: 1 / n for page in corpus}

    # Iterate until convergence
    while True:
        new_ranks = {}
        for page in corpus:
            # Calculate the PageRank for the current page
            rank_sum = 0
            for other_page in corpus:
                if len(corpus[other_page]) == 0:
                    # If other_page has no links, treat it as linking to all pages
                    rank_sum += ranks[other_page] / n
                elif page in corpus[other_page]:
                    rank_sum += ranks[other_page] / len(corpus[other_page])
            new_ranks[page] = (1 - damping_factor) / n + damping_factor * rank_sum

        # Check for convergence
        if all(abs(new_ranks[page] - ranks[page]) < threshold for page in corpus):
            break

        ranks = new_ranks

    return ranks

def validate_corpus(corpus):
    """
    Validate the corpus to ensure it meets the requirements.
    """
    if not isinstance(corpus, dict):
        raise ValueError("Corpus must be a dictionary")
    if not all(isinstance(page, str) for page in corpus):
        raise ValueError("All pages in corpus must be strings")
    if not all(isinstance(links, set) for links in corpus.values()):
        raise ValueError("All links in corpus must be sets")
    if not all(page in corpus for links in corpus.values() for page in links):
        raise ValueError("All links in corpus must point to pages in the corpus")
    if not all(isinstance(link, str) for links in corpus.values() for link in links):
        raise ValueError("All links in corpus must be strings")
    if not all(link != page for page, links in corpus.items() for link in links):
        raise ValueError("No page should link to itself")


if __name__ == "__main__":
    main()

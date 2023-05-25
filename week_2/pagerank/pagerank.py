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
    # Print Block For Reference
    #______________________________________________________________
    
    for sub in corpus:
        print(sub)
        print("⎇  ", end="")
        iterator = len(corpus[sub])
        for sub_nest in corpus[sub]:
            iterator -= 1
            print(sub_nest)
            if iterator !=  0:
                print("⎇  ", end="")
        print()
    
    #______________________________________________________________

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
    """
    Returns a dictionay:
    key: Page Name
    Value: Probability of each page being visited next
    """
    value = dict()
    list_of_direct_links = []
    if len(corpus[page]) != 0:
        for sub_nest in corpus[page]:
            list_of_direct_links.append(sub_nest)

        for sub in corpus:
            base_probability = (1-damping_factor)/len(corpus)
            #print(sub,":",base_probability)
            #print("⎇  ", end="")
            
            
            if sub in list_of_direct_links:
                #print(sub,"Hi :",base_probability)
                base_probability += (damping_factor/len(corpus[page]))
                #print("Damping factor: ", (damping_factor/len(corpus[page])))
                #print(sub,"Hi :",base_probability)
                
            #        #_______________________________________
            #        iterator -= 1
            #        #print(sub_nest,":",base_probability)
            #        #_______________________________________
            #        if iterator !=  0:
            #            #print("⎇  ", end="")
            #print()
            value[sub] = base_probability
        #print(value)
    else:
        print("hello World!")
        for link in corpus:
            value[link] = 1/len(corpus)
    #print(value)
    return value
    # raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    """
    Returns a dictionay:
    key: Page Name
    Value: Estimated Page Rank (A number between 0 and 1(Probability))
    """
    pagerank = dict()

    # Initializing all page ranks to 0 to detect errors straight forward if any
    for page in corpus:
        pagerank[page] = 0

    random_page = random.choice(list(corpus.keys()))
    pagerank[random_page] += 1
    print(random_page)
    probability_distribution = transition_model(corpus,random_page,damping_factor)
    pages_list = list(probability_distribution.keys())
    probability_list = [probability_distribution[key] for key in pages_list]
    random_page = random.choices(pages_list,probability_list)[0]
    print(random_page)
    for i in range(n-1):
        probability_distribution = transition_model(corpus,random_page,damping_factor)

        pages_list = list(probability_distribution.keys())
        probability_list = [probability_distribution[key] for key in pages_list]

        random_page = random.choices(pages_list,probability_list)[0]
        pagerank[random_page] += 1

    total = 0
    for key,value in pagerank.items():
        print(key)
        print(value)
        total += value/n
        pagerank[key] = value/n
    print(total)
    return pagerank
    #raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    """
    Returns a dictionay:
    key: Page Name
    Value: Estimated Page Rank (A number between 0 and 1(Probability))
    """
    print("Hello World!")
    #raise NotImplementedError


if __name__ == "__main__":
    main()

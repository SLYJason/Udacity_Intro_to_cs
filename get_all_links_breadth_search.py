#!/usr/bin/env python
#coding=utf8
import urllib
def get_page(url):
    try:
        import urllib 
        return urllib.urlopen(url).read()
    except: 
        return ''
        
def get_next_target(page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

def get_all_links(page):
        links = []
        while True:
            url, endpos = get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else: break
        return links

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

#crawl webpage breadth search first           
#def crawl_web(seed,max_depth):
#    tocrawl = [seed]
#    crawled = []
#    next_depth = []
#    depth = 0
#    while tocrawl and depth <= max_depth:
#        page = tocrawl.pop()
#        if page not in crawled:
#           union(next_depth, get_all_links(get_page(page)))
#           crawled.append(page)
#       if not tocrawl:
#            tocrawl, next_depth = next_depth, []
#            depth = depth + 1
#    return crawled
###########################
def crawl_web(seed):
        tocrawl = [seed]
        crawled = []
        index = {}
        graph = {} #<url>, [list of pages it links to]
        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled:
                content = get_page(page)
                add_page_to_index(index, page, content)
                outlinks = get_all_links(content)
                graph[page] = outlinks
                union(tocrawl,outlinks)
                crawled.append(page)
        return index, graph

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks 
    
def lucky_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if ranks[candidate] > ranks[best_page]:
            best_page = candidate
    return best_page  
       
###########################        

def ordered_search(index, ranks, keyword):
    pages = lookup(index, keyword)
    return quicksort_pages(pages, ranks)

def quicksort_pages(pages, ranks):
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = ranks[pages[0]]
        worse = []
        better = []
        for page in pages[1:]:
            if ranks[page] <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quicksort_pages(better, ranks) + [pages[0]] + quicksort_pages(worse, ranks)


index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)
print ordered_search(index, ranks, 'Hummus')
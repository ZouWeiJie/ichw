#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Weijie Zhou"
__pkuid__  = "1800013256"
__email__  = "1800013256@pku.edu.cn"
"""

import sys
import urllib.request


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    for i in [',','.','!','?',':',';','/','-','"','(',')','_','-',"'s","'re","'ll","\r","\n"]:
        lines = lines.replace(i," ")
    words = lines.split()
    
    counts = {}
    for i in words:
        counts[i] = counts.get(i, 0) + 1
    s = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    lst = []
    if topn > len(s):
        topn = len(s)
    for j in range(topn):
        lst.append(s[j])
    for (a, b) in lst:
        print(a + '\t', b)
    
  


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    try:
        url = sys.argv[1]
        text = urlopen(url)
        lines = text.read().decode()
        text.close()
        if len(sys.argv) >= 3:
            topn = int(sys.argv[2])
            wcount(lines, topn)
        else:
            wcount(lines)
    except Exception as error:
        print(error)

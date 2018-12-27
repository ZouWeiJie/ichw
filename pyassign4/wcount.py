"""wcount.py: count words from an Internet file.

__author__ = "Weijie Zhou"
__pkuid__  = "1800013256"
__email__  = "1800013256@pku.edu.cn"
"""

import sys
import urllib.request
import collections

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    for i in [',','.','!','?',':',';','/','-','"','(',')','_','-',"'s","'re","'ll","\r","\n"]:
        lines = lines.replace(i," ")
    words = lines.split()
    
    word = collections.Counter(words)
    word_list = word.most_common(topn)
    for i in word_list:
        print('{0}\t{1}'.format(i[0],i[1]))
    
  
if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    try:
        passage = urlopen(url)
        lines = passage.read().decode()
        passage.close()
    except Exception as err:
        print(err)
    else:
        topn = int(sys.argv[2])
        if len(sys.argv) == 2:
            wcount(lines)
        else:
            wcount(lines,topn)

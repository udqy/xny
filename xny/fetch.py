import re
from cache import CACHE_DIR
from pathlib import Path
from difflib import SequenceMatcher
from utils import fzf

from display import display

def search(topic):
    normalized_topic = re.sub(r'[^a-zA-Z0-9]', '', topic.lower())
    matches = []
    perfect_matches = []
    
    for file_path in Path(CACHE_DIR).glob('*.md'):
        filename = file_path.stem
        normalized_filename = re.sub(r'[^a-zA-Z0-9]', '', filename.lower())
        ratio = SequenceMatcher(None, normalized_topic, normalized_filename).ratio()
        
        if ratio == 1.0:
            perfect_matches.append((str(file_path), ratio))
        elif ratio > 0.6:
            matches.append((str(file_path), ratio))
    
    # If we have perfect matches, return only those
    if perfect_matches:
        perfect_matches.sort(key=lambda x: x[1], reverse=True)
        return perfect_matches
    
    # Otherwise return all matches sorted by ratio
    matches.sort(key=lambda x: x[1], reverse=True)

    # returns all the files if no matches are found
    if len(matches)==0:
        return [(str(f), 1.0) for f in Path(CACHE_DIR).glob('*.md')]
    
    return matches

def fetch(topic):
    print(f"|--> Searching for: {topic}")
    matches = search(topic)
    
    if len(matches) == 1:
        print(f"|--> Found {matches[0][0]}")
        display(str(matches[0][0]))
    elif len(matches)<5:
        fzf(matches)
    else:
        fzf(matches)

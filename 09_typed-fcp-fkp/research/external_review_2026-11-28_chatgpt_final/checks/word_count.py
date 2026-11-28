from pathlib import Path
import re
root = Path(__file__).resolve().parent
for name in ('abstract_original.txt','abstract_revised.txt'):
    text = (root/name).read_text(encoding='utf-8')
    ordinary = len(text.split())
    conservative = len(re.sub(r'(?<=[A-Za-z])-(?=[A-Za-z])', ' ', text).split())
    print(f'{name}: whitespace={ordinary}; split-hyphens={conservative}')
    if name == 'abstract_revised.txt':
        assert 150 <= ordinary <= 250 and 150 <= conservative <= 250

"""Read the frozen main.tex on stdin. Print only; no file or network access."""
import collections
import re
import sys

source = sys.stdin.read()
labels = collections.Counter(re.findall(r"\\label\{([^}]+)\}", source))
refs = re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", source)
print("internal reference occurrences:", len(refs))
print("missing targets:", sorted(set(refs) - set(labels)))
print("duplicate targets:", sorted(k for k, v in labels.items() if v > 1))

language = {"aa", "ab", "bb"}
deleted = language - {"aa"}
def left_contexts(words, suffix):
    return {word[:-len(suffix)] for word in words if word.endswith(suffix)}

print("left contexts in L of b and a:",
      sorted(left_contexts(language, "b")), sorted(left_contexts(language, "a")))
print("exceptional prefixes after deleting aa:",
      sorted(left_contexts(deleted, "b") - left_contexts(deleted, "a")))

level = {"a"}
for _ in range(2):
    level = {"(" + x + y + ")" for x in level for y in level} | {
        "[" + x + "]" for x in level
    }
marked = {w for w in level if "[" in w}
print("M2 word lengths:", sorted({len(w) for w in marked}))
print("M2 words of length 4:", sorted(w for w in marked if len(w) == 4))

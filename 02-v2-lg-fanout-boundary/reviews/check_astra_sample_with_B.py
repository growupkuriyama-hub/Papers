# Cross-check (Claude, 2026-10-31): Astra's explicit sample K_n for F_n under s_{0,1}
# is a characteristic sample for the reconstruction operator B, using the
# independent implementation of B from the second ChatGPT report.
# Both programs are taken verbatim from the reports kept in this folder.
# Usage (Windows):  py -3 check_astra_sample_with_B.py   (n = 4 takes tens of minutes)
import os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))

def code_block(name):
    text = open(os.path.join(HERE, name), encoding="utf-8").read()
    return re.findall(r"```python\n(.*?)```", text, re.S)[0]

ns_b = {}
exec(code_block("chatgpt_window_gap_round2_2026-10-31.md").split('if __name__ == "__main__":')[0], ns_b)
ns_k = {}
exec(code_block("astra_window_gap_round3_2026-10-31.md").split("if __name__=='__main__':")[0]
     .replace("    return len(K),sum(len(w)+1 for w in K)", "    return K"), ns_k)

words, complete = ns_b["words"], ns_b["complete"]
certificate, U = ns_k["certificate"], ns_k["U"]

nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 3
for n in range(2, nmax + 1):
    K = sorted(certificate(n)); L = words(n); t = time.time()
    print(n, "|K|", len(K), "length", sum(len(w) + 1 for w in K),
          "characteristic", complete(K, L), "%.1fs" % (time.time() - t))
    print("   without U_n:", complete([w for w in K if w != U(n)], L))

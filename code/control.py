# Control: dictionary coverage of the decoded cipher runs under the true key and under shuffled keys.
import json,random,re,sys,math,collections
from key import KEY
W=json.load(open('lm/words.json'))
LEX={w for w,c in W.items() if c>=5 and len(w)>=2 and w.isalpha()}
MAXL=max(len(w) for w in LEX)
def runs(path):
    out=[]; cur=[]
    for ln in open(path):
        if ln.startswith('#') or ':' not in ln: continue
        body=ln.split(':',1)[1]
        for t in re.findall(r'"[^"]*"|\S+',body):
            if t.startswith('"') or t=='[gutter]':
                if t!='[gutter]' and cur: pass
                # a clear word or a gutter breaks the run only when text is lost
                if t=='[gutter]': out.append(cur); cur=[]
                else: out.append(cur); cur=[]
                continue
            b=t.rstrip('?') or '?'
            cur.append(b)
    out.append(cur); return [r for r in out if r]
def cover(s):
    # DP: max number of chars covered by lexicon words of length >=4
    n=len(s); best=[0]*(n+1)
    for i in range(1,n+1):
        best[i]=best[i-1]
        for L in range(4,min(MAXL,i)+1):
            if s[i-L:i] in LEX: best[i]=max(best[i],best[i-L]+L)
    return best[n]
def score(key,R):
    tot=0;cov=0
    for r in R:
        s=''.join(key.get(t,'') for t in r)
        tot+=len(s); cov+=cover(s)
    return cov/tot
R=runs(sys.argv[1] if len(sys.argv)>1 else '../transcription/f575_signs.txt')
true=score(KEY,R)
random.seed(1594)
toks=[t for t in KEY if KEY[t]]
vals=[KEY[t] for t in toks]
res=[]
for i in range(300):
    v=vals[:]; random.shuffle(v); k=dict(zip(toks,v)); res.append(score(k,R))
res.sort()
print('runs',len(R),'signs',sum(len(r) for r in R))
print('true key: coverage by lexicon words (len>=4) = %.3f'%true)
print('shuffled keys (300, same letter multiset): mean %.3f, max %.3f'%(sum(res)/len(res),res[-1]))
# second control: a random French-like text of equal letter frequencies would behave like the shuffled case

# Calibration: the same measure on the clear French of the same letter (spaces removed).
import unicodedata
def norm(t):
    t=unicodedata.normalize('NFD',t.lower()); return ''.join(c for c in t if 'a'<=c<='z')
try:
    txt=open('../reading/f575_reading.txt').read().split('FRENCH TEXT')[1].split('ENGLISH TRANSLATION')[0]
    clear=re.sub(r'\[\[.*?\]\]',' ',txt,flags=re.S)
    clear=re.sub(r'\[[^\]]*\]|\(\?\)',' ',clear)
    segs=[norm(s) for s in re.split(r'\n\s*\n',clear) if len(norm(s))>40]
    tot=sum(len(s) for s in segs); cov=sum(cover(s) for s in segs)
    print('calibration, clear text of the same letter (%d letters): %.3f'%(tot,cov/tot))
except Exception as e: print('calibration skipped',e)

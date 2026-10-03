import re,sys,collections
from key import KEY, KEY528
import sys
if any('528' in a or '529' in a for a in sys.argv[1:]): KEY=KEY528
def toks(line):
    out=[]; 
    for m in re.finditer(r'"[^"]*"|\S+',line):
        out.append(m.group(0))
    return out
def decode(path):
    res=[]; cnt=collections.Counter(); unk=[]
    for ln in open(path):
        ln=ln.rstrip('\n')
        if not ln or ln.startswith('#'): continue
        lab,body=ln.split(':',1); s=''
        for t in toks(body):
            if t.startswith('"'): s+=' «'+t.strip('"')+'» '; continue
            if t=='[gutter]': s+='[…]'; continue
            q=t.endswith('?') and t!='?'; b=t.rstrip('?') if t!='?' else '?'
            if b in KEY:
                s+=KEY[b]+('' if not q else '̣'); cnt[b]+=1
            else: s+='_'; unk.append((lab,t))
        res.append((lab,s))
    return res,cnt,unk
if __name__=='__main__':
    res,cnt,unk=decode(sys.argv[1])
    for lab,s in res: print(lab, s)
    print('tokens',sum(cnt.values()),'types',len(cnt)); print('unknown',unk)
    inv=collections.defaultdict(list)
    for k,v in cnt.items(): inv[KEY[k] or 'null'].append((k,v))
    for L in sorted(inv): print(L, sorted(inv[L],key=lambda x:-x[1]))

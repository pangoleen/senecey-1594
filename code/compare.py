# Compare pass A and pass B (blind) token by token with an edit-distance alignment.
import re,sys,difflib,collections
def load(p):
    d={}
    for ln in open(p):
        if ln.startswith('#') or ':' not in ln: continue
        lab,body=ln.split(':',1)
        toks=[t for t in re.findall(r'"[^"]*"|\S+',body) if not t.startswith('"') and t!='[gutter]']
        d[lab.strip()]=[ (t.rstrip('?') or '?') for t in toks]
    return d
if __name__=='__main__':
    A=load('passA.txt'); B=load('passB.txt')
    tot=0; same=0; conf=collections.Counter(); perline=[]
    for lab in A:
        if lab not in B: continue
        a,b=A[lab],B[lab]
        sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
        eq=sum(i2-i1 for tag,i1,i2,j1,j2 in sm.get_opcodes() if tag=='equal')
        tot+=len(a); same+=eq; perline.append((lab,len(a),len(b),eq))
        for tag,i1,i2,j1,j2 in sm.get_opcodes():
            if tag=='equal': continue
            if tag=='replace' and i2-i1==j2-j1:
                for x,y in zip(a[i1:i2],b[j1:j2]): conf[(x,y)]+=1
            else: conf[(' '.join(a[i1:i2]) or '-',' '.join(b[j1:j2]) or '-')]+=1
            if '-v' in sys.argv: print(lab,tag,i1,a[i1:i2],'|',b[j1:j2])
    print('lines compared',len(perline),'tokens in A',tot,'agree',same,'= %.1f%%'%(100*same/max(tot,1)))
    for l in perline: print(' ',l)
    print('most frequent differences (A,B):')
    for k,v in conf.most_common(40): print('  ',v,k)

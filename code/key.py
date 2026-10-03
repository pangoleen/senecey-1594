# Key for the f. 530 symbol cipher as used on f. 575 (token -> plaintext letter).
# src: 'f530' = on the period table f. 530 (same shape, same row); 'ctx' = from context on f. 575.
KEY = {
 'II':'a','o-':'a','o':'a','#':'a',
 'V':'b',
 'sq':'c','th':'c','xx':'c',
 'q':'d','=':'d',
 '7':'e','4':'e','eL':'e','my':'e',
 '3':'f',
 'g':'g',
 'oo':'h',
 '8':'i','vt':'i','xc':'i','10':'i',
 'xy':'l','ay':'l','ll':'l','tj':'l',
 'MM':'m','uo':'m',
 'nr':'n','psi':'n','14':'n','17':'n',
 'o3':'o','b':'o','lam':'o','tl':'o',
 'acr':'p','eps':'p',
 'S':'q','T':'q',
 'w':'r','4o':'r','rho':'r','u3':'r',
 'uq':'s','aa':'s','phi':'s','tz':'s',
 'tt':'t','tO':'t','ubar':'t','-o':'t',
 'rc':'u','Gc':'u','K':'u','ec':'u',
 'X':'x','8x':'y','6oo':'z',
 '7x':'e',          # small crossed sign, twice before tO; value from context (et, retenus)
 'N9':'','NoIo':'','NLeo':'','[blot]':'','[flourish]':'',
}

# Extra values needed for f. 528 (Pelissier's hand). Source: the period table f. 530 (rows and the list "Nulles")
# and the context of f. 528. Not used on f. 575.
KEY528 = dict(KEY)
KEY528.update({
 'inf':'p',   # lying 8 (f530 row p)
 'fff':'f',   # three strokes with a bar (f530 row f)
 'dd':'d',    # two tall strokes joined by a bar (f530 row d)
 '::':'q',    # four dots (f530 row q)
 # nulls of f530
 'kq':'l',   # k-like sign with a long crossed tail (context: luy; a form of xy)
 'ee':'m',   # two c's with tails, alone (context: sommes, comme, mesme, Monseigneur, communique). f530 has no such m
 'eemw':'',  # the group ee + my + small raised sign (f530 Nulles); null in every context seen
 'dl':'d',   # phi with a loop at the top (f530 row d, third sign; context: dire)
 'pf':'f',   # p-like sign with a hook (context: faict, feict)
 'cmy':'q',  # c with tail joined to my, no raised sign (f530 row q, fourth sign; gloss 'qui')
 'gq':'',    # g-like sign with a zigzag tail (f530 Nulles)
 'obar':'c', # o under a double bar (f530 row c, fifth sign; context: scavoir)
 'A1':'h',   # two strokes joined by a bar, like A or H (context: cacher); Pelissier's form of the h sign
 'kh':'g',   # small k-like sign (f530: second sign of the row after f; context: juge, obligeant). Stands also before 'ipolite' and in 'de ?rance'
 'cr':'g',   # c or e with a dot before it (same f530 row, first sign; context: Espaigne). Stands also before 'ipolite' (twice)
 'bw':'b',   # two small loops under one top bar, like Greek varpi (context: Rubi x2 beside R-u-V-i, impossible)
 'qb':'b',   # 9-like sign (f530 row b, second sign). In this hand it looks like q (d); told apart by context
 'ao':'g',   # like 'ao' or a lying 8 with a larger left loop (context: grade, grandeur, general, mariage). Hard to tell from inf (p)
 'zf':'z',   # like a tall double f (f530 row z, second sign; context: bienfaictz). Close to 8x (y)
 'khh':'h',  # the kh shape where the word needs h (Hipolite, archeduc). Split from kh by context only
 'crh':'h',  # the cr shape where the word needs h (Hipolite x2, authorite). Split from cr by context only
 'x1':'x',   # plain x (context: aux)
 'uyb':'y',  # u-y with a stroke under it (context: moyens)
 '77':'', 'P':'', 'bb':'', 'W':'', 'h':'', '8+':'', 'hf':'', 'N9':'', 'NoIo':'', 'NLeo':'', 'Lx':'',
})

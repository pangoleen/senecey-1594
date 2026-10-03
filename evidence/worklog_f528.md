# Work log: Colbert 33, ff. 528-529 (Pelissier to Joyeuse, Madrid, 13 February 1594)

Work of 3 October 2026, as written during the work. File names are those of the working folder; the files of this repository are listed in the README.


**Status: read, with gaps.** All four pages are transcribed and deciphered. Files: `f528_transcription.txt`,
`f528_reading.txt` (French and English), `passA528.txt`, `passA528_before_adjudication.txt`,
`passB_f528r.txt`, `passB_f528v.txt`, `passB_f529r.txt`, `passB_f529v.txt`, `sign_inventory528.md`, `key.py` (`KEY528`).

### Layout and line cut

- f. 528r = view 533 (right), 46 lines and one inserted line; f. 528v and f. 529r = view 534, 46 and 41 text lines;
  f. 529v = view 535 (left), 19 text lines. No new Gallica request was made.
- The lines are not parallel. `slabs528.py` finds the lines in slabs of 640 px, each with its own skew angle, and
  follows each line in 16 bands. This fixed the cut of f. 528r (glosses stand between its first lines).
  Strips: `crops528/L_<page>_<nn>.png`. Zoom tool: `lz.py`.
- f. 528r ends "il est impossibl" and f. 528v begins "e d'empescher": no line is lost between the pages.

### Numbers

| Measure | Value |
|---|---|
| Cipher signs transcribed (pass A) | 3,709 in 92 sign types |
| Nulls among them | 535 (14.4 %), 12 types |
| Signs that I marked doubtful in pass A | 113 (3.0 %) |
| Blind pass B, same sign as pass A | 3,462 of 3,709 = 93.3 % (f. 528r 93.0, f. 528v 93.0, f. 529r 94.7, f. 529v 91.0) |
| Same letter after decoding both passes with one key | 93.3 % |
| Lexicon coverage, true key (`control.py passA528.txt`) | 0.850 |
| Lexicon coverage, 300 shuffled keys | mean 0.079, maximum 0.162 |
| Lexicon coverage, clear French of the same letter (ceiling) | 0.852 |

### What the passes do and do not show

- Pass B is blind: four fresh agents, one per page. Each had the sign names, the f. 530 crops and the line strips
  only. The f. 528r agent reports that the two f. 530 crops did not display for it.
- **I did not look again at each of the 247 differing signs on the image.** This differs from f. 575. I listed the
  letter-level differences (`compare528.py -v`). At no place does pass B give a different French word. Most
  differences fall in a few look-alike groups: lying 8 (`inf`, p) against two o's (`oo`, h), 23 times; the
  ff-like y sign (`8x`) against `ll`, 15 times; `dl` (d) against `8x`; `uyb` (y) against `my` (e);
  `obar` (c) against `ubar` (t); `dd` (d) against `II` (a). In these groups my choice follows the word.
  So the transcription is **context-assisted**: where two signs look alike, the French word decided. It is not
  an independent reading of every sign.
- Pass A changed while I worked, before I saw any pass B: I corrected signs when the decode gave a non-word
  and a second look at the image showed another sign. After pass B came in I changed three signs
  (528r22, 528r40, 528v09), all from context, none from pass B.

### Key for Pelissier's hand (`KEY528`), counts on ff. 528-529

| Letter | Signs (token: count) |
|---|---|
| ? | ?: 1 |
| a | II: 67, o-: 51, #: 47, o: 45 |
| b | V: 14, bw: 11, qb: 7 |
| c | xx: 33, sq: 31, th: 22, obar: 22 |
| d | dl: 47, q: 22, dd: 17, =: 7 |
| e | my: 151, 7: 151, eL: 147, 4: 128 |
| f | fff: 23, 3: 11, pf: 11 |
| g | kh: 8, g: 7, ao: 5, cr: 4 |
| h | oo: 8, A1: 4, crh: 3, khh: 2 |
| i | 8: 60, vt: 59, 10: 56, xc: 49 |
| l | ay: 55, tj: 53, kq: 43, ll: 38, xy: 5 |
| m | ee: 21, uo: 21, MM: 18 |
| n | nr: 69, psi: 58, 17: 46, 14: 42 |
| null | NLeo: 74, W: 60, hf: 57, bb: 57, NoIo: 57, P: 47, 77: 40, 8+: 37, eemw: 30, h: 26, N9: 25, gq: 25 |
| o | o3: 55, b: 50, tl: 45, lam: 45 |
| p | eps: 35, acr: 30, inf: 27 |
| q | cmy: 19, T: 18, S: 12, ::: 5 |
| r | 4o: 76, w: 62, rho: 57, u3: 54 |
| s | uq: 73, aa: 63, tz: 61, phi: 53 |
| t | tO: 73, tt: 52, -o: 48, ubar: 46 |
| u | ec: 85, K: 73, Gc: 58, rc: 52 |
| x | x1: 6, X: 3 |
| y | 8x: 17, uyb: 16 |
| z | 6oo: 4, zf: 1 |

- Source of values: the period table f. 530 for most signs, and its list "Nulles" for the nulls.
- Values that I fixed from the context of this letter (not found by me in f. 530, or split by context):
  `ee` = m (21 uses; f. 530 has no such sign for m), `kq` = l, `bw` = b, `x1` = x, `uyb` = y, `obar` = c,
  `dl` = d, `pf` = f, `cmy` = q, `A1` = h, `zf` = z, `ao` = g.
- **Signs split by context only (the weakest part of the key):** `qb` (b) has the same shape as `q` (d) or `N9` (null);
  `cr` (g) and `crh` (h) are one shape; `kh` (g) and `khh` (h) are one shape. The reading chooses the letter that
  gives a word. In "de ?rance" the `kh` shape stands where f is needed.

### Blind check against the period glosses (task 4)

Only f. 528r lines 2-3 carry glosses that I read (ten words): arreste, proposition, faicte, par, ministres,
de, ruby, en, faveur, hipolite.
- First decode, before I compared: 7 of 10 agreed (arreste, proposition, faicte, par, ministres, en, faveur).
- The other three (de, ruby, hipolite) showed four sign errors of mine in line 3. A second look at the signs
  gave the gloss reading. So the glosses confirm the key, and they show that my first-pass sign error rate
  on this hand is not small.
- Not done: the glosses above lines 8-9 of f. 528r. I did not read them. They can hold the name that I
  cannot read (l-u-d-e-m-i-c-d-o-c-?-i).

### The group "ee-my + raised sign" (task 5)

Token `eemw`, 30 uses. It is a null, not a code for a person. Evidence: it stands inside words (ac|cepter,
pou|rveu, re|mede), at word joins and at line starts, and the text is whole without it in all 30 places.
f. 530 lists it under "Nulles". The persons are hidden by **cover names spelled in cipher letters**:

| Cover name | Uses | Meaning (from the sense) | Evidence |
|---|---|---|---|
| Rubi | 10 whole, more at gutter line ends | the king of Spain | "ministres de Rubi", "la France et Rubi", crown of France "inseparable d'avec celle d'Espaigne"; period gloss "ruby" |
| Hipolite / Ipolite | 6 whole, more split by the gutter | the duke of Guise | named "pour roy de France moyennant le mariage de luy avec l'Infante" (the Spanish proposal of July 1593); period gloss "hipolite" |
| le Fin | 2 | Henri of Navarre | "empescher l'establissement du Fin", "recognoistre le Fin, apointant avec luy" |
| Safir | 1 or 2 | the Pope | "soubz l'authorite de Safir"; the clear text has "l'authorite de Sa Saintete" in the same role |
| Phare | 1 | probably the duke of Lorraine | head of his house, has a state, allies and neighbours |

This also settles open point 1 of f. 575: the clear word "le fin" there is the same cover name for Navarre.

### Content in short

Mayenne's agents in Madrid report their talks with Don Juan de Idiáquez. They list Mayenne's proposals in order:
(1) Guise as king with the Infanta; (2) the Infanta with the archduke Ernest, refused before, hard to revive;
or Philip II takes the crown of France himself, joined to that of Spain; (3) "Phare"; (4) Mayenne himself, with
Spanish forces; (5) if Spain accepts none, to recognise Navarre under the Pope's authority, with a renewed
Franco-Spanish alliance. Idiáquez answers that the King will not decide before he has conferred with the Pope.

### Open points

- The name on f. 528r lines 8-9; the insertion above line 33 (about 28 small signs, mostly unread).
- About 40 line ends of f. 528v are in the gutter (one to three signs each). Restored by sense, in brackets.
- Words that do not come out: "fortes", "ceder s..enn..", "son oi.. cou et", "sa mans..e", "si ..endu",
  "liberauxx f", "seccg asseurs", "l..rarte", "guae ..ant", "il ne m..ble". See `f528_reading.txt`, Doubts.
- The initial sign of "Hipolite"; the g/h and b/d sign splits above.
- The clear text (about half of the letter) had one pass. The signature is not read.
- No per-sign adjudication of the 247 differences against the image.

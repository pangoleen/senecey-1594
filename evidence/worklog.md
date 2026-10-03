# Work log: Colbert 33, f. 575 (Senecey to Jeannin, 15 March 1594)

Work of 3 October 2026, as written during the work. File names are those of the working folder; the files of this repository are listed in the README.

## Result in short

- **f. 575r-v is read in full.** The cipher part (1,056 signs, 59 letter signs and 3 nulls) gives continuous French.
  See `f575_reading.txt` (French and English) and `f575_transcription.txt` (signs).
- The key is the period table on f. 530. Five sign values come from the context of f. 575 (h, y, z, one sign for d, one for e).
- ff. 528-529 (Pelissier to Joyeuse) use the same key. That letter is in work and is not part of this file.
- Novelty: I found no earlier reading of the cipher text beyond Tomokiyo's first line and a half. The
  *content* is close to a memoir that L'Épinois summarised in 1886. See "Prior art".

## Sources and images

| View | Folio | File | Use |
|---|---|---|---|
| 582 | f. 575r | `img/v582.jpg` | 17 clear lines, then 16 cipher lines |
| 583 | f. 575v | `img/v583.jpg` | 17 mixed lines, then 13 clear lines, date |
| 535 | f. 529v and f. 530r | `img/v535.jpg` | f. 530: the period alphabet and the list "Nulles" |
| 533 | f. 528r | `img/v533.jpg` | Pelissier, page 1 (glossed words) |
| 534 | ff. 528v-529r | `img/v534.jpg` | Pelissier, pages 2-3 |
| 536, 537 | f. 530v-531, f. 532 | `img/v536.jpg`, `img/v537.jpg` | fetched, not used |

Gallica IIIF, one request at a time, each file fetched once. Images are black and white (microfilm).
Derived files: `crops/r_desk.png`, `crops/v_desk.png` (deskewed pages), `crops/rLnn.png`, `crops/vLnn.png`
(one line each, three tiles, 2x), `crops/f530_alpha.png`, `crops/f530_nulles.png`, `crops528/` (Pelissier pages, deskewed).

## The cipher

Homophonic letter substitution with nulls. No syllable signs, no code numbers on f. 575. The words are not
divided. Clear French words stand between the cipher runs and belong to the same sentences.
Senecey writes Navarre in letters (`n-a-u-a-r-r-e`). The only name hidden otherwise is a clear word, "le fin" (?).

### Key table (as used on f. 575)

Token names are in `sign_inventory.md`. Count = uses on f. 575 (pass A, after adjudication).
"f530" = the sign stands in that row of the period table. "ctx" = value fixed by the context of f. 575.

| Letter | Signs (token: count) | Source |
|---|---|---|
| a | o-: 30, o: 29, II: 24, #: 11 | f530 |
| b | V: 8 | f530 |
| c | th: 29, sq: 11, xx: 2 | f530 |
| d | q: 12, =: 12 | q: f530. =: ctx (12 fits; f530 draws a like sign in row d) |
| e | 7: 51, 4: 51, my: 35, eL: 30, 7x: 2 | f530; 7x: ctx (see Open points) |
| f | 3: 8 | f530 |
| g | g: 14 | f530 |
| h | oo: 5 | **ctx** (catholicque x3, honorables, chacung). Not in the f530 table |
| i | 8: 30, xc: 27, vt: 11, 10: 9 | f530 |
| l | ay: 25, xy: 17, tj: 16, ll: 10 | f530 |
| m | MM: 16, uo: 3 | f530 |
| n | nr: 40, psi: 24, 17: 15, 14: 2 | f530 |
| o | o3: 24, lam: 13, b: 11, tl: 1 | f530 |
| p | acr: 19, eps: 3 | f530 |
| q | S: 17, T: 5 | f530 |
| r | w: 29, rho: 29, u3: 11, 4o: 1 | f530 |
| s | phi: 32, uq: 25, aa: 20, tz: 14 | f530 |
| t | ubar: 34, tO: 28, tt: 23, -o: 2 | f530 |
| u | rc: 42, K: 17, Gc: 13, ec: 6 | f530 |
| x | X: 6 | f530 |
| y | 8x: 7 | **ctx** (quoy, anvoyant, suivye, ainsy, luy x2, ruynees) |
| z | 6oo: 2 | **ctx** (soldatz, ilz) |
| null | N9: 5, NoIo: 3, NLeo: 1 | f530, list "Nulles" |

No j, k, v, w: i serves for j, u serves for v. The table f. 530 also lists signs that f. 575 does not use
(second signs for b and f; a lying 8 for p; four dots for q; more nulls). Pelissier uses them on f. 528.

## Method

1. Fetch views 582 and 583. Deskew (recto -1.75 degrees, verso -2.25 degrees). Cut one image per line, 2x.
2. Name the signs (`sign_inventory.md`). Build the key from f. 530 (`key.py`).
3. **Pass A** (me): transcribe every line from the 2x tiles, zoom 3x to 6x on doubts. File `passA_before_adjudication.txt`.
4. **Pass B** (a separate agent, blind): it had the sign names and the line images only. It did not have the key,
   my transcription or the plaintext. File `passB.txt`.
5. Compare (`compare.py`), look again at every difference on a closer crop (`adjud.py`, `crops/adjud_*.png`),
   fix pass A where B was right. Result: `passA.txt` and `f575_transcription.txt`.
6. Decode with the fixed key (`decode.py`). Divide the words by hand. No solver and no language model changed
   any sign. The language data serve the control only.

## Controls

### Two transcription passes

| Measure | Value |
|---|---|
| Signs in pass A (33 lines) | 1,056 |
| Signs identical in pass B (blind) | 1,008 = 95.5 % |
| Letters identical after decoding both passes with the same key | 96.8 % |
| Differing places | 45 (48 signs) |
| ... of which between two signs for the same letter (o and o-, ll and tj, II and #, xx and th, ubar and -o) | 14 |
| ... of which at the gutter of f. 575v (signs partly hidden) | 6 |
| ... of which I changed pass A after a closer look | 1 (rL08: # in place of II; the letter stays a) |

Pass B did not have the key or the plaintext, and its agent did not try to decipher. It says that it read only
`sign_inventory.md`, the f. 530 crop and the 33 line images. I looked again at every differing place on a closer
crop (`crops/adjud_*.png`, `crops/adjud_wide.png`). In the other places pass A stood: either the shape is clear
on the closer crop (for example rL06 T, rL15 Gc, vL10 ubar, vL17 "religion"), or the two candidate signs are
look-alikes and only one gives a word. The second kind is listed under "Open points"; there the sign is
resolved by context and not by shape. Pass B confuses mostly the three barred signs acr (p), aa (s), xx (c),
and the small signs g (g), xc (i), rc (u).

Limit: pass A is not blind. I knew the key when I transcribed. Pass B is the check on that bias.

### Wrong-key control (`control.py`)

Measure: share of the deciphered letters that a period lexicon covers with words of 4 letters or more
(lexicon: `lm/words.json` from `sega1593/lm`, 16th-century French letters and memoirs, words seen 5 times or more).

| Text | Coverage |
|---|---|
| f. 575 cipher runs, true key | 0.887 |
| Same signs, 300 keys with the letters shuffled among the signs | mean 0.159, maximum 0.270 |
| Clear French of the same letter, spaces removed (ceiling for this lexicon) | 0.828 |

The deciphered text scores as high as the clear text of the same letter. No shuffled key comes near.

### Sense, date and sender

- The cipher runs and the clear words make whole sentences across 33 lines. Examples of joins:
  clear "...au second moyen, desire le plus communement" + cipher "estoict qu'il plust a Sa Sainctete...";
  cipher "...commandees par gouverneurs et garnisons" + clear "ne treuvant plus les moyens" + cipher "d'entretenir leurs soldatz".
- The clear text after the cipher says: "Il m'a commande luy donner par escript". L'Épinois (1886, p. 613, from
  Vatican and BnF papers) says that on 14 March 1594 the Pope ordered Senecey to put the main points in
  writing. The letter is dated 15 March. The memoir that L'Épinois summarises has the same argument
  ("Si elle ne se fait pas avec l'autorite du Pape, au profit de tous, chacun en conclura une en son
  particulier"). Our cipher: "chacung panseroit particulierement a ses afaires". This is an outside check of the sense.
- Paris opened its gates to Henri IV on 22 March 1594, one week later. The letter was intercepted and came to
  the royal decipherers (Viète's file).

### What is verified on the image and what is inferred

- Verified on the image, two passes: the sign sequence of the 33 cipher lines, except the items in "Open points".
- From the period table f. 530 (seen on the image): the values of 57 sign types (54 letter signs and 3 nulls).
- Inferred from context: the signs for h, y, z, the sign `=` for d and the sign `7x` for e (5 sign types, 28 uses); the word division; the letters in square brackets.
- Single pass: all the clear text (secretary hand), the f. 528 probe.

## Open points (every sign I could not resolve)

Sign level (the value in brackets is the one used in the reading):

| Place | Sign | Doubt |
|---|---|---|
| rL07, rL10 | [blot] | One deleted sign in each line. No value. The words around are whole (merite a quoy; bonne intantion) |
| rL09 | uq? (s) | uq or my. "francoi-s car" |
| rL10 | 4? (e) | A 4 with a cross stroke; pass B read tt. "s-e-roit" |
| rL06, vL13 | rc (u) | A form like the figure 2. I take it as a form of rc. "tra-u-aulx", "perd-u" |
| vL02 | xx? (c) | Blotted sign before oo. "c-hacung". f. 530 gives this sign for c |
| vL03 | u3? (r) | The shape is u3 (r). The word needs s: "afaire-s". Probably a slip of the writer |
| vL04 | ay? (l) | ay or my. "de-l-les" |
| vL04 | [flourish] | A T-like stroke joined to uo in "mes-mes". Pass B read a sign T (q). I give it no value |
| vL04 | rc? (u) | rc or xc. "q-u-elles" |
| vL04 | ? | Last sign before the gutter, after "trai". Not read |
| vL06 | acr? (p) | acr or xx. "p-ar gouverneurs" |
| vL08 | II? (a) | Two strokes joined at the top; pass B read sq (c). "n-a-uarre" |
| vL09, vL15 | 7x (e) | A small crossed sign before tO, twice. Pass B read g. Context: "e-t les", "r-e-tenus". Value from context only |
| vL10 | g? (g) | g or xx. "g-ouverneurs" |
| vL12 | MM? (m) | MM or =. "entiere-m-ent" |
| vL14 | NLeo? (null) | Null of f. 530, or the sign tl (o). After "pacification". No effect on the sense |
| vL14 | g? (g) | g or xc. "g-en[s]" |
| vL16 | o-? rc? (a, u) | Two blotted signs after "affaire". "a-u-ec" |
| vL17 | -o? (t) | One t sign or two: "seurte" or "seurtte" |
| vL18 | xx? (c) | xx or th. Both are c |

Twenty-four signs of 1,056 are in this list (2.3 %). None changes a word of the reading, if the context is accepted.

Lost in the gutter of f. 575v (one or two signs each, restored by the sense): end of vL03 depanden[t], vL04
trai[c], vL05 commande[es], vL07 (nothing needed), vL12 pe[r], vL14 gen[s], vL15 qu[il], vL16 d[e], vL17 c[at].
A colour scan or the original would settle these.

Word level:
- "le fin" (clear word in rL12): read f-i-n. The sense needs Henri of Navarre. Not explained.
- The relative before "estoict" (rL01) is not written. "autorita la France" has one a for two words.
- Clear text: "veu", "lieu", "Renould", "sages" are doubtful single-pass readings. The clear text of the
  recto (17 lines) and of the end of the verso (13 lines) had one pass only.

Not done:
- No second pass on the clear text. No check of the hand against other letters of Senecey (f. 549, f. 577).
- f. 576 (address leaf, if any) not opened.

## Prior art (checked 3 October 2026)

| Source | What it has | URL |
|---|---|---|
| Tomokiyo, "Viète" article, last modified 15 June 2022 (live copy fetched today) | f. 575: "in symbol cipher of f.530, undeciphered", with the opening only: "es[t]oict quil plusta sa sainctete entreprandre la pacification generalle de toute ... portant par son autorita la france les ... la religion catholicqua ceulx quil....". f. 528: listed, not read | https://cryptiana.web.fc2.com/code/viete.htm |
| Tomokiyo, "Unsolved Historical Ciphers", last modified 3 Oct 2026 | Names f. 539 and f. 555 of this volume only. f. 575 and f. 528 are not there | https://cryptiana.web.fc2.com/code/unsolved.htm |
| Bourdeau, cyphersolver, SOLVED_CATALOGUE.md (catalogue 314), commit of 3 Oct 2026 06:07 UTC | "Partly read ... neither letter has a published full decipherment (checked 22 Sept 2026)". No folder for f. 575 or f. 528. GitHub code search for the ark finds only his `targets/joyeuse` (f. 539) | https://github.com/dbourdeau/cyphersolver |
| NoAutopilot/cipher-lab, PROGRESS.tsv, KEY-ADJACENT.tsv, QUEUE-github-held.tsv, folder list, commit of 3 Oct 2026 10:45 UTC | Only f. 539 ("joyeuse", not read). No row for f. 575 or f. 528 | https://github.com/NoAutopilot/cipher-lab |
| el-descifrador/cabinet-noir README (v1.2.1, 2 Oct 2026) | No mention of Colbert 33, Senecey, Pelissier | https://github.com/el-descifrador/cabinet-noir |
| aaymeloglu/unsolved-ciphers README (28 Sept 2026) | No mention | https://github.com/aaymeloglu/unsolved-ciphers |
| satoru.net/crypt index | No mention | https://satoru.net/crypt/ |
| matthewdgreen/cipher_benchmark | Maps DECODE records to the Gallica ark only. No reading | https://github.com/matthewdgreen/cipher_benchmark |
| DECODE R2279, R2283 | Per the scout (TARGETS.md): marked "Decrypted", no text. Not opened again today | https://de-crypt.org/decrypt-web/ |
| G. Lasry, f. 555 (Senecey to Lyon), 2020, HistoCrypt 2022 | Another cipher (Tomokiyo: "seems different from ... f.530"). Images saved in `prior/`. Not used | see Tomokiyo's page |
| L'Épinois, La Ligue et les papes (1886), pp. 613-614 | Summary of Senecey's memoir to Clement VIII of 14 March 1594 (drawn up by d'Ossat). Same argument as our letter. It does not print or cite the letter to Jeannin. Full text searched for "Senecey" | https://archive.org/details/laligueetlespap00lepgoog |
| Niepce, Histoire de Sennecey (1866), pp. 453-455 | Short account of the embassy. No letter text | https://archive.org/details/bub_gb_4hDnm7YrwBMC |
| BnF notices, Cinq cents de Colbert 33 and fr. 4019-4020 | List the letters only. fr. 4019 has copies of other letters of February 1594 from the same packet | https://archivesetmanuscrits.bnf.fr/ark:/12148/cc91713b |
| M. Defaye, Le Sel de la terre no. 76 | Repeats L'Épinois | https://www.seldelaterre.fr/articles/sdt76/henri-de-navarre-(ii) |

Web searches for phrases of the plaintext (3 Oct 2026), no hit: "les bras ouvers pour recepvoir les peuples" with
"mains larges"; "pacification generalle de toute la crestiente" with Senecey; "abbaye de Fontenay" with Senecey,
Jeannin and "second fils"; "tombeau plus honorable" with "champ de bataille", Mayenne, Senecey.

**Not checked:** the book "Nicolas, Claude et Georges de Bauffremont, barons de Sennecey" (Google Books; Lasry
used p. 203 for f. 555), which I could not find on archive.org; Jeannin's printed Négociations (they begin in
1607, so they cannot hold this letter); the DECODE records themselves; the Vatican copy of the memoir.

**Claim that the evidence supports:** first full reading of the cipher of f. 575, with the period key that
Tomokiyo identified. It is not a new cryptanalysis. The first 25 words were read by Tomokiyo. The substance
was known from L'Épinois's summary of the parallel memoir.

## Log

- 11:26 read TARGETS.md and the local copy of Tomokiyo; saved his images to `prior/`.
- 11:28 fetched views 582, 583; later 533-537.
- Built sign names and key from f. 530; pass A of f. 575; first decode gave French on every line.
- Prior-art fetches and searches (see table). Control run. Pass B by a blind agent; adjudication.
- Probe of f. 528r, one line.

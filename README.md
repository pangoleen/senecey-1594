# Two League letters of 1594 in the cipher of Colbert 33 f. 530

Readings of the cipher passages of two letters of the Catholic League, written in Rome and in Madrid in the weeks
before Paris opened its gates to Henri IV. Both use one cipher. The royal office rebuilt its alphabet in 1594, and
the alphabet is in the same volume (f. 530).

| Letter | Shelfmark | State before | State now |
|---|---|---|---|
| Claude de Bauffremont, baron de Senecey, League ambassador in Rome, to president Pierre Jeannin, 15 March 1594 | Paris, BnF, Cinq Cents de Colbert 33, f. 575r-v (Gallica `btv1b10033958p`, views 582-583) | Key known; the first 25 words read | [full reading and translation](reading/f575_reading.txt) |
| Pelissier, agent of the Duke of Mayenne in Madrid, to the cardinal de Joyeuse, 13 February 1594 | Same volume, ff. 528r-529v (views 533-535) | Key known; ten words glossed in 1594 | [reading with gaps, and translation](reading/f528_reading.txt) |

**Status, 3 October 2026.** f. 575: first full reading; the cipher part has 1,056 signs. ff. 528-529: first
reading, with gaps; the cipher part has 3,709 signs. Two transcription passes were made for each letter, one of
them blind. No palaeographer has checked the readings yet. Corrections are welcome: please open an issue.

## What this is, and what it is not

- **It is not a new cryptanalysis.** The key is the alphabet that the royal office rebuilt in 1594. It is in the
  same volume, on f. 530. Satoshi Tomokiyo identified it, showed that it applies to this letter, and read the
  opening ([cryptiana, "François Viète and his decipherments"](https://cryptiana.web.fc2.com/code/viete.htm)).
- **These are the first readings of the two cipher texts that we could find.** The search is in
  [prior_art.md](prior_art.md). It was repeated on 3 October 2026 at 11:37 UTC (f. 575) and at 12:23 UTC
  (ff. 528-529).
- **The substance was partly known.** H. de L'Épinois (*La Ligue et les papes*, 1886, pp. 613-614) summarised a
  memoir that Senecey gave to Clement VIII on 14 March 1594. The memoir has the same argument. L'Épinois does not
  print or cite this letter.

## What the letter of Senecey says (f. 575)

Senecey reports to Jeannin, the chief adviser of the Duke of Mayenne, what he told the Pope. The League cannot
bear its ills any longer, and there are three ways out. The first is in clear text: the ruin of the enemy, which
needs strong and quick help. The second and the third are in cipher:

- The second way: "qu'il plust a Sa Sainctete entreprandre la pacification generalle de toute la crestiente",
  with securities for the Catholic religion and for Mayenne, "anvoyant quelque legat sur les lieux, assiste des
  cardinaulx francois".
- If neither way works quickly, "chacung panseroit particulierement a ses afaires". The great towns are "si
  lasses et ruynees qu'elles traicteront avec ledict Navarre", and the garrison towns will do the same, "ayant
  ledict Navarre les bras ouvers pour recepvoir les peuples et les mains larges a doner de grandes recompences
  aux gouverneurs".

The letter is dated 15 March 1594. Paris opened its gates to Henri IV on 22 March 1594.

## What the letter of Pelissier says (ff. 528-529)

Mayenne's agents in Madrid report to the cardinal de Joyeuse, in Rome, on their talks with Don Juan de Idiáquez.
The king of Spain asked them to hide nothing, so they declared the offers that Mayenne had ordered, one after
the other. The persons are hidden under cover names in cipher: Rubi, Hipolite, le Fin, Safir, Phare.

- "sans les aydes de Rubi il est impossible d'empescher l'establissement du Fin".
- First, that Rubi's ministers name Hipolite king of France, with the marriage of the Infanta.
- If that is not the king's intention, Mayenne "desireroit que Ru[bi] voulust accepter la couronne d[e] France
  pour s[oy et ses s]uccesseurs, la rendant inseparable d'avec [c]el[le] d'Espaigne".
- If not, Phare "seroit celuy qui avec plus de facilité pourroit estre apelé a ceste grandeur".
- As the last proposition: "il sembloit n'y avoir plus aultre remede que [d]e recognoistre le Fin, apointant avec
  luy soubz l'authorité de Safir".

Our identifications, from the sense: Rubi is the king of Spain, Hipolite the Duke of Guise, le Fin Henri of
Navarre, Safir the Pope, and Phare probably the Duke of Lorraine. Only "ruby" and "hipolite" have a period gloss
on the page. The same cover name explains a clear word in Senecey's letter: he writes "le fin" where the sense
needs Navarre.

Letters in square brackets are lost in the gutter of the binding and are restored by the sense. In the sentence on
the crown, the signs for "accepter la couronne de France", "successeurs", "la rendant inseparable" and "d'Espaigne"
are read; "soy et ses" and "celle" are restored.

The mission to Madrid is known to historians from other sources. A search of the printed literature
([evidence/print_check_f528.md](evidence/print_check_f528.md)) found no text of this letter. De Thou (book 108)
knows the question of Guise and the Infanta. Bouillé (*Histoire des ducs de Guise*, iv, 1850, pp. 262-263) quotes
the clear letter of Montpezat of the same day, from this same volume, to the abbé d'Orbais; this confirms the name
"M. d'Orbais" in our reading. Historians know one other plan, the crown for Mayenne's son. We did not find the
offer of the crown to Philip II himself in the literature that we could reach. Not reached: Vázquez de Prada (2004),
Descimon and Ruiz Ibáñez, and the Simancas papers. So we do not claim that the offer is unknown.

## The cipher

A homophonic substitution of letters by symbols, with nulls. There are no syllable signs and no code numbers in
the letter of Senecey; the letter of Pelissier adds cover names, spelled in cipher, and many more nulls (14 % of its signs). Words are not divided. Clear French words stand between the cipher runs and belong to the same
sentences.

- 57 sign types have their value from the period alphabet on f. 530 ([image](images/f530_alphabet.jpg)).
- 5 sign types have their value from the context of this letter: the signs for h, y and z, one sign for d and
  one for e (28 uses in all).
- The full table is in [evidence/worklog.md](evidence/worklog.md) and in [code/key.py](code/key.py).

## How the reading was made

1. Each sign shape got a short name ([transcription/sign_inventory.md](transcription/sign_inventory.md)).
2. Pass A transcribed all 33 lines from enlarged line images.
3. Pass B was blind. A separate agent had the sign names and the line images only. It did not have the key, the
   first transcription or the plain text.
4. Every place where the two passes differ was looked at again on a closer crop.
5. The key was applied sign by sign ([code/decode.py](code/decode.py)). Words were divided by hand. No solver and
   no language model changed any sign.

## How good is it: f. 575

| Measure | Value |
|---|---|
| Signs identical in the two passes | 1,008 of 1,056 (95.5 %) |
| Letters identical after decoding both passes | 96.8 % |
| Signs resolved by context and not by shape (all listed in the work log) | 24 (2.3 %) |
| Share of the deciphered letters covered by period French words of 4 letters or more, true key | 0.878 |
| The same measure for 300 keys with shuffled letter values | mean 0.158, maximum 0.267 |
| The same measure for the clear French of the same letter | 0.828 |

## How good is it: ff. 528-529

| Measure | Value |
|---|---|
| Signs transcribed | 3,709, in 92 sign types; 535 are nulls |
| Signs identical in the blind pass | 3,462 (93.3 %) |
| Period glosses on f. 528r (ten words) that agree with the first decoding | 7; the other 3 showed sign errors of ours and agree after a second look |
| Share of the deciphered letters covered by period French words of 4 letters or more, true key | 0.850 |
| The same measure for 300 keys with shuffled letter values | mean 0.079, maximum 0.162 |
| The same measure for the clear French of the same letter | 0.852 |

Limits of this second reading, stated plainly:

- The 247 places where the two passes differ were not all checked one by one on the image. Where two signs look
  alike, the French word decided.
- Three pairs of signs (b and d, g and h twice) are told apart by context only.
- About 40 line ends of f. 528v are in the gutter. One name on f. 528r, an insertion of 28 small signs, and about
  ten words are not resolved. They are listed at the end of the reading file.
- The cover names are identified from the sense.

## Outside checks of f. 575


- Tomokiyo's published opening of the cipher agrees with our first three lines.
- The clear text of the letter says that the Pope ordered Senecey to give him the discourse in writing.
  L'Épinois reports that order under 14 March 1594.

Limits, stated plainly:

- Pass A was not blind: its author knew the key.
- Eight line ends of f. 575v are in the gutter of the binding. One or two signs are lost in each and are restored
  by the sense. They are in square brackets.
- The clear text (secretary hand) had one pass only. Doubtful words carry `(?)`.
- The clear word "le fin" stands where the sense needs Henri of Navarre. The letter of Pelissier uses "le Fin" as a
  cover name in the same sense.
- The images are black-and-white microfilm.

## Contents

| Path | Content |
|---|---|
| `reading/f575_reading.txt`, `reading/f528_reading.txt` | French text, English translation, list of doubts |
| `transcription/f575_transcription.txt`, `f528_transcription.txt` | The signs of each cipher line with the letters beside them |
| `transcription/f575_signs.txt`, `f528_signs.txt` | The same signs in the form that `decode.py` reads |
| `transcription/sign_inventory.md`, `sign_inventory528.md` | Names of the sign shapes |
| `code/` | Key, decoder, comparison of the two passes, wrong-key control, and the word list that the control uses |
| `evidence/` | The blind passes, pass A of f. 575 before adjudication, and the two work logs |
| `prior_art.md` | The search for an earlier reading |
| `images/` | Reduced images of f. 575r, f. 575v, ff. 528v-529r and the alphabet of f. 530 |

To repeat the decoding and the control:

```bash
cd code && python3 decode.py ../transcription/f575_signs.txt && python3 control.py && python3 decode.py ../transcription/f528_signs.txt && python3 control.py ../transcription/f528_signs.txt
```

## Credits

- **Satoshi Tomokiyo** catalogued the volume, identified the alphabet on f. 530 as the key of this letter, and
  read its opening.
- **The royal decipherers of 1594** (the file is linked to François Viète) rebuilt the alphabet on f. 530.
- **The DECODE database** records the letters (R2283, R2279) and the key (R2280).
- **Daniel Bourdeau** (`dbourdeau/cyphersolver`) noted in September 2026 that no full decipherment was published.
- **Bibliothèque nationale de France / Gallica** provides the page images. Images here are reduced, with the
  credit "gallica.bnf.fr / BnF".
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Open points

- A check by a palaeographer, and a colour scan or the original for the line ends in the gutter.
- A second pass on the clear text.
- ff. 528-529: the differing signs of the two passes, the gaps, the name on f. 528r, and the identity of "Phare".
- A comparison of the letter of Pelissier with the Spanish papers on the same mission.

## Licence

Code: MIT. Text: CC BY 4.0. Images: reduced images from Gallica, under the BnF's conditions of reuse, with the
credit "gallica.bnf.fr / BnF". Details are in [LICENSE.md](LICENSE.md).

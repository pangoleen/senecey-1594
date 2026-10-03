# Senecey to Jeannin, Rome, 15 March 1594: the cipher read in full

A full reading of the cipher passages of one letter of the Catholic League, written in Rome one week before
Paris opened its gates to Henri IV.

| Letter | Shelfmark | State before | State now |
|---|---|---|---|
| Claude de Bauffremont, baron de Senecey, League ambassador in Rome, to president Pierre Jeannin | Paris, BnF, Cinq Cents de Colbert 33, f. 575r-v (Gallica `btv1b10033958p`, views 582-583) | Key known; the first 25 words read | [full reading and translation](reading/f575_reading.txt) |

**Status: first full reading, 3 October 2026.** The cipher part has 1,056 signs. Two transcription passes were
made, one of them blind. No palaeographer has checked the reading yet. Corrections are welcome: please open an
issue.

## What this is, and what it is not

- **It is not a new cryptanalysis.** The key is the alphabet that the royal office rebuilt in 1594. It is in the
  same volume, on f. 530. Satoshi Tomokiyo identified it, showed that it applies to this letter, and read the
  opening ([cryptiana, "François Viète and his decipherments"](https://cryptiana.web.fc2.com/code/viete.htm)).
- **It is the first full reading of the cipher text that we could find.** The search is in
  [prior_art.md](prior_art.md). It was repeated on 3 October 2026 at 11:37 UTC.
- **The substance was partly known.** H. de L'Épinois (*La Ligue et les papes*, 1886, pp. 613-614) summarised a
  memoir that Senecey gave to Clement VIII on 14 March 1594. The memoir has the same argument. L'Épinois does not
  print or cite this letter.

## What the letter says

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

## The cipher

A homophonic substitution of letters by symbols, with nulls. There are no syllable signs and no code numbers in
this letter. Words are not divided. Clear French words stand between the cipher runs and belong to the same
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

## How good is it

| Measure | Value |
|---|---|
| Signs identical in the two passes | 1,008 of 1,056 (95.5 %) |
| Letters identical after decoding both passes | 96.8 % |
| Signs resolved by context and not by shape (all listed in the work log) | 24 (2.3 %) |
| Share of the deciphered letters covered by period French words of 4 letters or more, true key | 0.887 |
| The same measure for 300 keys with shuffled letter values | mean 0.159, maximum 0.270 |
| The same measure for the clear French of the same letter | 0.828 |

Two outside checks:

- Tomokiyo's published opening of the cipher agrees with our first three lines.
- The clear text of the letter says that the Pope ordered Senecey to give him the discourse in writing.
  L'Épinois reports that order under 14 March 1594.

Limits, stated plainly:

- Pass A was not blind: its author knew the key.
- Eight line ends of f. 575v are in the gutter of the binding. One or two signs are lost in each and are restored
  by the sense. They are in square brackets.
- The clear text (secretary hand) had one pass only. Doubtful words carry `(?)`.
- One clear word is not explained: "le fin", where the sense needs Henri of Navarre.
- The images are black-and-white microfilm.

## Contents

| Path | Content |
|---|---|
| `reading/f575_reading.txt` | French text, English translation, list of doubts |
| `transcription/f575_transcription.txt` | The signs of each cipher line with the letters beside them |
| `transcription/f575_signs.txt` | The same signs in the form that `decode.py` reads |
| `transcription/sign_inventory.md` | Names of the sign shapes |
| `code/` | Key, decoder, comparison of the two passes, wrong-key control, and the word list that the control uses |
| `evidence/` | The blind pass, pass A before adjudication, and the work log |
| `prior_art.md` | The search for an earlier reading |
| `images/` | Reduced images of f. 575r, f. 575v and the alphabet of f. 530 |

To repeat the decoding and the control:

```bash
cd code && python3 decode.py ../transcription/f575_signs.txt && python3 control.py
```

## Credits

- **Satoshi Tomokiyo** catalogued the volume, identified the alphabet on f. 530 as the key of this letter, and
  read its opening.
- **The royal decipherers of 1594** (the file is linked to François Viète) rebuilt the alphabet on f. 530.
- **The DECODE database** records the letter (R2283) and the key (R2280).
- **Daniel Bourdeau** (`dbourdeau/cyphersolver`) noted in September 2026 that no full decipherment was published.
- **Bibliothèque nationale de France / Gallica** provides the page images. Images here are reduced, with the
  credit "gallica.bnf.fr / BnF".
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Open points

- A check by a palaeographer, and a colour scan or the original for the line ends in the gutter.
- The word "le fin".
- A second pass on the clear text.
- The second letter in this key, Pelissier to the cardinal de Joyeuse, Madrid, 13 February 1594 (ff. 528-529), is
  in work.

## Licence

Code: MIT. Text: CC BY 4.0. Images: reduced images from Gallica, under the BnF's conditions of reuse, with the
credit "gallica.bnf.fr / BnF". Details are in [LICENSE.md](LICENSE.md).

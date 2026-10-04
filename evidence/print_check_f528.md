# Print check for three readings (4 October 2026)

Task: find an older clear text, a period decipherment, a summary, a calendar entry or an archive-guide
entry for three letters. All searches were made on 4 October 2026. The files that I downloaded are in `src/`.
The helper `fts.py` asks the full-text search of archive.org.

Words used in the verdicts: "text in print", "content known, text not found", "nothing found".

Limits that apply to all three:

- HathiTrust full-text search gives a bot check ("Just a moment...", HTTP 403). I did not try to pass it. Not searched.
- The Google Books API gives HTTP 429. I used the Google Books search page in the browser pane for a few phrases.
- Gallica: only the SRU service was used (phrase search with `text adj "..."`), one request each 10 seconds.
- A "not found" from a full-text search depends on the OCR. It is weaker than a page-by-page reading.

---


## 3. Pelissier to the cardinal de Joyeuse, Madrid, 13 February 1594 (BnF Cinq Cents de Colbert 33, ff. 528-529)

**Verdict: content known in part, text not found.** The mission, the first proposal (Guise with the Infanta) and Philip's answer (the Pope first) are in print since de Thou. The other overtures of this letter, and above all the offer of the crown to Philip II himself, were not found in any source that I could open.

### Sources searched

| Source | Search | Result |
|---|---|---|
| Ch. de La Roncière, *Catalogue des manuscrits de la collection des Cinq Cents de Colbert* (1908), p. 57. https://archive.org/details/cataloguedesman00manugoog | Text file, "Pellissier", "Montpezat" | "Lettres originales de Henri des Prez, marquis de «Montpezat» [6] (fol. 527, 531, 533, etc.), — «Pellissier» [3] (fol. 528, 560, 561) ... «Fr[ançois], car[dinal] de Joyeuse» [4] (fol. 539, chiffrée ...)". No decipherment is noted for f. 528. The only decipherment in the notice is Viète's printed one of Moreo's letter (f. 198). The volume comes from J.-A. de Thou. |
| J.-A. de Thou, *Histoire universelle*, book CVIII (French ed. 1740, vol. VIII, pp. 361-363). https://archive.org/details/bub_gb_4gTh6wor5aMC | Text file, "Monpesat", read the passage | Long account of Montpezat's speech at Madrid. See Findings. |
| R. de Bouillé, *Histoire des ducs de Guise*, vol. IV (1850), pp. 234-236, 245, 250, 259, 262-264. https://archive.org/details/bub_gb_jYDL9LN6p3MC | Text file, "Montpesat", "Pélissier" | He used this very volume ("Mss. V. C. de Colbert, v. 33") and quotes the clear letters of Montpezat of 13 February 1594. He does not use f. 528. See Findings. |
| J. de Croze, *Les Guises, les Valois et Philippe II*, vol. 2 (1866), pp. 250-252. https://archive.org/details/lesguiseslesval00crozgoog | Text file | The mission; one alternative only (the duke of Aiguillon), after Bouillé. No Simancas document on the offers. |
| H. Forneron, *Histoire de Philippe II*, vol. 4 (1882), pp. 214-215. https://archive.org/details/forneron-histoire-de-philippe-ii-v-4 | Text file | Montpezat goes to "Madrid, où il est berné pendant huit mois"; note: Arch. nat. "K. 1593, p. 21, 23, 36 et 44". Nothing on the offers. p. 252: Pélissier at Madrid in 1596. |
| J. Paz, *Catálogo IV* (1914), pp. 483-484. https://archive.org/details/catlogo4secret01spai | Text file, "Montpessat", "Pellissier" | K. 1592 (B. 81): "A. 1594. — Papeles de Montpessat, enviado del Duque de Humena, y pareceres del Consejo de Estado ... Respuesta a Mompessat ... Memorias y relaciones de Montpessat y Pellissier sobre sus comisiones, avisos que recibían del de Humena, **proposiciones sobre la elección de Francia** ...". The Spanish side of our letter is there. It is described, not printed. |
| H. Drouot, *Mayenne et la Bourgogne*, vol. 2 (1937), p. 78 n. 1; p. 299 n. 2 and n. 4. https://archive.org/details/IA41551607_0002 | Text file | He cites the folios: "dans B.N., Vc Colbert 33, f. 528, 560, 561, plusieurs lettres de Pélissier écrites de Madrid du 3 au 16 fév. 1594" and "Sennecey à Jeannin ... 15 mars, ib., f. 575 (chiffrée)". He quotes only f. 561 ("mes amys de Bourgongne"). He does not give the content of f. 528. He also cites "B.N., fr. 3988 (instructions à Montpezat et Pélissier)". |
| L'Épinois, *La Ligue et les papes* (1886). https://archive.org/details/laligueetlespap00lepgoog | Text file, "Montpe[sz]at", read the pages for January-March 1594 | No mention of the Madrid proposals. |
| Cabrera de Córdoba, *Filipe Segundo*, vol. 4, p. 98. https://archive.org/details/filipesegundorey04cabruoft | Text file | One mention of "el señor de Monpesat". No offers. |
| Capefigue, *Histoire de la Réforme, de la Ligue ...*, vol. with 1593-1594. https://archive.org/details/histoiredelarfo02capegoog | Text file | Prints Mayenne's letter to Philip II on Montpezat's departure and a postscript of Montpezat (Simancas B 81). No offers. |
| Sismondi, *Histoire des Français*, vol. 21, pp. 254-255. https://archive.org/details/histoiredesfran21sism | Text file | Mayenne to Montpezat, 15 January 1594 (after Capefigue VII, 120). No offers. |
| Nouaillac, *Villeroy* (1909). https://archive.org/details/villeroysecrta00nouauoft | Text file, "Montpe" | No mention. |
| archive.org full text | Montpezat Mayenne Espagne 1594 "couronne de France" Infante Guise Idiaquez; "inseparable" "couronne d Espagne" Mayenne Montpezat; Montpezat Mayenne Philippe "accepter la couronne"; Mompesat Idiaquez Umena 1594 corona Francia | Only the works above. |
| Gallica SRU | `text adj "inseparable d avec celle d Espagne"`; `text adj "accepter la couronne de France pour soy"`; `text adj "Monpesat estant en Espagne"` | 0 records each. |
| Gallica SRU | `text adj "Montpezat" and text adj "Idiaquez" and text adj "Mayenne" and text adj "1594"` | 19 records (Sismondi, the *Mémoires de Nevers*, dictionaries). Titles only; pages not opened (Gallica HTML is closed to us). |
| Google Books (search page) | "Montpezat" "Felipe II" Mayenne 1594; "Montpezat" "Philippe II" Mayenne Madrid 1594 Pelissier; two longer queries with "corona de Francia" and "lui-même" | Freer (1861), an *Annales* note (1906), Drouot. No statement of the offers. |
| Web search (two engines) | Montpezat, Mayenne, Madrid 1594, crown to Philip II himself | Nothing specific. |

### Findings

1. **De Thou (who owned this volume) gives the first proposal and the answer.** Montpezat "dit au Roi d'Espagne, qu'il étoit venu, à dessein d'apprendre de la bouche de Sa Majesté, si elle approuvoit le mariage du Duc de Guise avec l'Infante; combien en ce cas elle donneroit de troupes et d'argent". Answer: the King "dit qu'il vouloit, avant que de rien résoudre, consulter le Pape et l'Archiduc Ernest". This agrees with the opening of our letter and with Idiáquez's answer at its end (conference with the Pope; dispatches to Flanders). De Thou says nothing of the further overtures.
2. **Bouillé (1850) quotes the clear letters of the same day from the same volume.** Montpezat to the abbé d'Orbais, 13 February 1594: "Je poursuis le plus qu'il m'est possible que ce qui a esté proposé en faveur de Monseigneur de Guyse soit ensuivy. Le Roy a volleu, avant que se faire aucunement entendre sur ce subject, avoir l'advis de nostre Sainct-Père vers lequel ceste despesche est faicte exprès pour cest effect." Also (to Mayenne): "ce ne sont affaires d'un mois, mais quatre ou cinq tous entiers s'écouleront".
   - This **confirms our doubtful reading "M. d['Orb]ais"**: the abbé d'Orbais was told the Guise proposal only, as the cipher asks ("Il ne semble n'estre à propos que M. d'Orbais prenne part en ce que dessus").
   - It shows why the other overtures stayed unknown: they are only in the cipher letter.
3. **What historians say Mayenne proposed besides Guise.** Bouillé IV, p. 250, and De Croze II, p. 252 (after Henri IV's intelligence and Villeroy): Montpezat was to obtain "au duc d'Aiguillon la couronne de France et la main de l'infante" (Mayenne's elder son). Villeroy, in Bouillé p. 245: "la dépesche de Montpezat vers le Roy d'Espagne tendoit aussi à mesme fin" (to make Mayenne king). Our letter has the claim for Mayenne himself as the "dernière proposition" and has no word of Aiguillon.
4. **The offer of the crown to Philip II himself** ("accepter la couronne de France pour soy et ses successeurs, la rendant inseparable d'avec celle d'Espaigne"): not found in de Thou, Bouillé, De Croze, Forneron, Capefigue, Sismondi, L'Épinois, Cabrera or Drouot, and no phrase hit on archive.org, Gallica or Google Books. The same holds for the proposal of the duke of Lorraine and for the last remedy (to recognise Navarre under the Pope's authority) as proposals made at Madrid in February 1594.
5. **Where the same content should be:** Simancas K 1592 (old B 81), "Memorias y relaciones de Montpessat y Pellissier ... proposiciones sobre la elección de Francia" (Paz, p. 483); Bouillé cites "B 81, pièce 12" and "pièce 247" for Montpezat's letters of February and 1 March. A historian who read K 1592 may have printed the Spanish version. I found no such text.

### Not reached

- V. Vázquez de Prada, *Felipe II y Francia* (2004), chapter XIII and after: no full text (table of contents only). This is the most probable place for a statement on the offer to Philip II. **The claim "unknown to historians" is not safe before someone reads these pages.**
- R. Descimon and J. J. Ruiz Ibáñez, *Les ligueurs de l'exil* (2005): no full text.
- P. Richard, *Pierre d'Épinac*, p. 553 (Drouot's reference for the mission): not found online.
- BnF fr. 3988: Drouot calls it "instructions à Montpezat et Pélissier". The catalogue of the fonds français (vol. 3) lists there a copy of a "Lettre de «Mr du Mayne à Mr de Monpesat estant en Espagne ... De Paris, ce IIII febvrier 1594»" (f. 69). The *Mémoires de Nevers* (1665), vol. 2, near pp. 700-706, may print it. Not read. It can hold Mayenne's own words on the same offers.
- Gachard: the two volumes on the Paris library were searched for letter 2 only; they have no notice of Colbert 33.
- Simancas K 1592 and K 1593 (PARES): not opened.


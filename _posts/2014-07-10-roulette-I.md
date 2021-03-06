---
layout: single
title: Roulette I
categories: [python,other,slovak]
tags: [python]
---

Pred časom sa mi dostal do ruky link na [zaujímavý článok o rulete](http://braniblog.info/2/?fb_action_ids=10204512621958174&fb_action_types=og.likes), nazvaný "Ako som zarobil peniaze a kúpil si Lexus SC430-2003". Veľmi som tomu neveril, ale snažím sa mať hlavu otvorenú, tak som si to aspoň prečítal. V tomto poste by som teda chcel zhrnúť svoje postrehy.

---

Tento článok pozostáva z 3 častí:

1. [Analýza pôvodného článku a metódy]({% post_url 2014-07-10-roulette-I %})
2. [Štatistická simulácia metódy a jej vyhodnotenie]({% post_url 2014-07-10-roulette-II %})
3. [O čo vlastne ide a závery]({% post_url 2014-07-10-roulette-III %})

---

Na prvý pohľad je to zaujímavý článok od normálneho chlapíka. Ale po prvých pár paragrafoch úvodných kecov sa to rozbieha. Autor (ktorý nikde nie je podpísaný), píše 3 hlavné rozdiely medzi on-line a skutočným kasínom:

> Nikto nevidí, čo hráč robí pri počítači. Nie sú tam žiadni manažéri miestností, kamery alebo pozorní krupieri školení na sledovanie hráčskych metód a stratégií. Je tam iba hráč a jeho počítač.

To je síce pravda, že pri online hraní vás nikto fyzicky nevidí, lebo ste doma. Avšak pán autor zabudol, spomenúť, že okrem vás a vášho počítača je tam ešte server, ktorý vlastní kasíno. Tento server vidí vaše karty, ako rýchlo, ako často, a akú sumu staviate, skrátka vidí oveľa viac ako vidí ktokoľvek vo fyzickom kasíne. V klasickom kasíne si nikto nezapisuje vaše všetky stávky.

> Nie sú žiadne limity na stávkovanie. V skutočnom kasíne musia hráči uzatvoriť stávky za menej ako 20 sekúnd. Ďalšou výhodou hrania on-line je, že hráči môžu pred uzavretím stávok počkať, takže môžu urobiť ten najlepší možný ťah.

To, či v skutočnom kasíne limity sú alebo nie sú neviem, avšak nerozumiem ako vám pomôže čakať s uzatvorením stávky, keďže ruleta je prakticky hra jedného hráča a stávky ostatných hráčov nič nemenia.

> Keď hráte v on-line kasíne, môžete v skutočnosti dávať do stávky veľmi malé sumy, čo je nevyhnutné na to, aby táto metóda efektívne fungovala. V žiadnom skutočnom kasíne by vám to nedovolili.

Znova neviem ako je to v skutočnom kasíne, ale to či táto metóda funguje, si ukážeme za chvíľu.

Pre lenivších tu opíšem celú tú metódu:

> Hlavný princíp tejto metódy je založený na opakovanom stávkovaní malých súm na základe prvej stávky. Používanie takejto schémy je 100 % legálne. Túto techniku som použil pri hraní rulety on-line a už v priebehu 5 mesiacov sa mi podarilo získať dosť peňazí na kúpu vysnívaného auta.
>
> 1. Každú novú hru začínam stávkou 1 € na čierne číslo. 
> 2. Ak prehrám (guľôčka padne na červené číslo), zdvojnásobím stávku na tú istú farbu (čiernu). 
> 3. Ak vyhrám, začnem novú hru so stávkou 1 € na opačnú farbu.

Keď som si toto prečítal, začal som byť ešte podozrievavejší, pretože:

* "opakovanom stávkovaní malých súm na základe prvej stávky" - toto je tzv. [Gamblers Fallacy](http://en.wikipedia.org/wiki/Gambler's_fallacy), pomýlená predstava, že pravdepodobnosť ďalšieho výsledku závisí od predchádzajúceho výsledku. To jednoducho nie je pravda, to vie každý kto mal štatistiku. Jednotlívé ťahy sú na sebe nezávislé.
* Kroky 2 a 3 menia farby. To je znova Gambler's fallacy, pretože, čierna a červená sú štatisticky ekvivalentné.
* Hlavný princíp je stávkovanie malých súm, ale v kroku 2 zdvojnásobujeme stávku. To je exponenciálny rast. Aký to má dopad si ukážeme ďalej.

> Niektorí ľudia si myslia, že je rozumnejšie začať s menšou sumou na konte a že to vykompenzujú tým, že budú hrať opatrne, ale pravdou je, že im hrozí oveľa vyššie riziko prehry.

Nie, riziko prehry je v každej individuálnej stávke (ak sa bavíme o čiernej a červenej) rovnaké.

> 98 % ľudí hrá bez akejkoľvek logiky alebo metódy. To je ten dav, na ktorom všetky kasína zarábajú svoje zisky. Títo ľudia nechápu hru z hľadiska kalkulácií a logických výsledkov.

To je dosť možné. Ľudia, ktorí chápu ako ruleta funguje ju nehrajú a tie 2% sú ľudia, ktorí využívajú iné taktiky.

> nesmiete zabúdať na to, že všetci ostatní hráči majú iba 50 % šancu na výhru, ale ak zdvojnásobíte svoje stávky, vaša šanca na výhru sa bude maximálne približovať 100 %. A to je niečo, čo obyčajní hráči nikdy nedokážu pochopiť!

Tu sú hneď 2 závažné chyby:

1. Nielen ostatní hráči, *každý* má 50% šancu na výhru.
2. Nie je to 50%, ale 48,65% pretože v rulete je červená (18), čierna (18) a zelená (1) a teda červená a čierna majú šancu 18/37, ak sa bavíme o Francúszkej verzii. V Americkej je to ešte horšie, lebo tam sú 2 zelené polia. 

Graf, ktorý tam k tomu je je síce pekný, ale je to totálny nezmysel.

Na konci článku ešte nasleduje link na to spomínané on-line kasíno, kde sa dá takto skvele zarobiť a kopec komentárov od "úspešných" hráčov, ktorí takto zarobili už veľa peňazí&#0153;.

Pokračujte [Štatistická simulácia metódy a jej vyhodnotenie]({% post_url 2014-07-10-roulette-II %})

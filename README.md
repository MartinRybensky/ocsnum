# ocsnum

  Old Church Slavonic Numerals’ Converter

  ocsnum 1.0 (C) Martin Rybensky 2018, CC BY-NC-SA

  Usage: ocsnum [parameters] [number]

  -c, --cyrillic     	show only cyrillic numeral as output     
  -g, --glagolitic   	show only glagolitic numeral as output   
  -s, --slavonic     	show only verbally expressed numeral in OCS
  -h, --help	     	show this help


  Better, bidirectional OCS numeral converter can be found here:  
  http://prevodnik.gorazd.org:8081/old-church-slavonic-numerals-converter-kb


###### Sample output
```
[user@pc]$ ocsnum 1241

  Cyrillic numeral:    ҂асма
  Glagolitic numeral:  ⱍⱄⰽⰰ
  Old Church Slavonic: тꙑсѫщи • дъвѣ сътѣ • четꙑре десѧте и ѥдинъ

[user@pc]$ ocsnum -c 4319
҂дтѳі

```


###### Installation
```
git clone https://github.com/MartinRybensky/ocsnum.git
chmod a+x ocsnum/ocsnum.py
ln -s ocsnum/ocsnum.py /usr/local/bin/ocsnum
```

or

```
git clone https://github.com/MartinRybensky/ocsnum.git
cp ocsnum/ocsnum.py /usr/local/bin/ocsnum
chmod a+x /usr/local/bin/ocsnum
```

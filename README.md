# ocsnum

  Old Church Slavonic Numerals’ Converter

  ocsnum 1.0 (C) Martin Rybensky 2018, CC BY-NC-SA

  Usage: ocsnum [parameters] [number]

  __-c, --cyrillic__     	show only cyrillic numeral as output     
  __-g, --glagolitic__   	show only glagolitic numeral as output   
  __-s, --slavonic__     	show only verbally expressed numeral in OCS  
  __-h, --help__	     	show this help


  Better, bidirectional OCS numeral converter can be found here:  
  http://prevodnik.gorazd.org:8081/old-church-slavonic-numerals-converter-kb


###### Sample output
```
[user@pc]$ ocsnum 128

  Cyrillic numeral:    рки
  Glagolitic numeral:  ⱃⰻⰷ
  Old Church Slavonic: съто • дъва десѧти и осмь

[user@pc]$ ocsnum -c 318
тиі

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

# BDAR ir slapuku atitikties tikrinimas 

## Tyrimas

Atlikta 2022-12-11 su populiariais domenais, kurie turi .lt galūnę iš viso 5524 (Open PageRank, Top 10 mil., 2022-12-10).

Imties santykis yra 2.5% palyginus su 226446 užregistruotais (DomReg.lt, 2022-12-10).





Daroma prielaida, kad Google Chrome webdriver ir selenium yra įdiegti.

## Paleidimas ant macOS
```
git clone https://github.com/atakosvektorius/Slapuku-tikrinimas
cd Slapuku-tikrinimas
wget https://www.domcop.com/files/top/top10milliondomains.csv.zip
unzip top10milliondomains.csv.zip
grep -Eo ',\".+\.lt\",' top10milliondomains.csv | sed 's/[\",]//g' > nuorodos.txt

python3 BDAR_Slapukai.py 
```
Pastaba kai kurie domenai neveikia scriptas pakimba, reikia rankinio įsikišimo. 

Rezultatai beveik puse t.y. 45% neatitinka BDAR:

```
wc -l BDAR_atitiktis.txt
4869 BDAR_atitiktis.txt

awk '{print $1}' BDAR_atitiktis.txt | sort  | uniq -c
2196 Netinka
2673 Tinka
```

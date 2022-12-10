# BDAR ir slapuku atitikties tikrinimas 

## Atlikta 2022-12-10
Pagal DomReg.lt duomenis yra užregistruoti 226446 domenai.
Į Top 10 milijono lietuvišku domenų patenka 5524, o tai grubiai yra 2.5% nuo visų registruotu.



## Daroma prielaida, kad Google Chrome webdriver ir selenium yra įdiegta.
```
git clone https://github.com/atakosvektorius/cookie_checker
wget https://www.domcop.com/files/top/top10milliondomains.csv.zip
unzip top10milliondomains.csv.zip
grep -Eo ',\".+\.lt\",' top10milliondomains.csv | sed 's/[\",]//g' > nuorodos.txt

python3 BDAR_Slapukai.py 
```

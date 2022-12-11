# -*- coding: utf-8 -*-
"""groupe-2-projet1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P8j0bhBi9eDR-xEV2W_jmQCfUDaPJ7so

<Center><h1>PROJET1-MATHS-DISCRETES-UVS-2021</h1><center>

###Année: 2020-2021, UVS
###Cours de mathématiques discrètes
###Projet 1 : Impémentation en Python
###Enseignant : Dr. Michel SECK (EPT)
### **Fait** par `Sidy Ahmed KAMARA ` et ` Magath Ale C. S. NAEL`

#Partie 1 : Exercices sur Python

##1.1 Exercice 1 : Recherche

###a. Fonctionnement du boucle **`while`** et comparaison avec le boucle **`for`**
- **`While`** : s'utilise quand on a une condition a verifier pour repeter une suite d'instruction tant que la condition est valide
- **`For`** : s'utilise pour parcourir une structure de donnees et effectuer un ensemble d'operation pour chaque element oubien repeter un ensemble d'intruction n fois avec n connu.
- **Comparaison** : On utilisera ainsi **for** pour les structures de donnees et pour effectuer une operation `n` fois avec `n` connus et while quand on voudra effectuer un ensemble d'operation sachant une condition valide.

Executons deux exemples pour illustrer la difference
"""

#Fonctionnement du boucle while et du boucle for
#Affichons la table de multiplication de 1 jusqu'a 3 avec les deux boucles 

for i in range(3):
  print(f"Table de {i+1}\n")
  for j in range(9):
    print(f"{i+1} * {j+1} egale {(i+1)*(j+1)}")
  print("\n")

y = 1
while (y <= 3) :
  x = 1
  print(f"Table de {y} \n")
  while(x<=10):
    print(f"{x}*{y}={x*y}")
    x+=1
  y+=1
  print("\n")

"""###b. Explication des fonctions

- **`enumarate`**
ajoute un compteur à un itérable et le renvoie sous la forme d'un objet enumerate. Cette objet enumerate peut etre utilise directement dans les boucles For ou etre converti en une liste de tuple à l’aide de la methode liste. Enumerate prend en paramètre une liste et renvoie un objet qui peut être associé à une liste contenant deux valeurs par élément : l'indice et l'élément de la liste parcouru.

- **`zip`**
est une fonction interne qui prend deux ou plusieurs séquences et retourne une liste de tuples où chaque tuple contient un élément de chaque séquence. Le nom de la fonction fait allusion à une fermeture-éclair (zip ou zipper en anglais), qui joint et entrelace deux rangées de dents.

- **`min`**: 
La fonction min() renvoie la plus petite valeur d'une série de données. Si min() est appelé sur un itérable, il renvoie l'élément le plus petit. Si l'itérable est vide, la valeur par défaut est renvoyée.

- **`max`**:
La fonction max() renvoie la plus grande valeur d'une série de données. Si max() est appelé sur un itérable, il renvoie l'élément le plus grand. Si l'itérable est vide, la valeur par défaut est renvoyée. Sinon, une exception ValueError est déclenchée.

- **`sum`**: 
fonction sum() ne fonctionne qu’avec des valeurs numériques. Si vous essayez de l’utiliser avec un type non numérique, vous obtiendrez une erreur. La fonction sum() ajoute la valeur de départ(start) et les éléments de l’itérable donné de gauche à droite.

- **`sorted`**: 
renvoie une liste triée de l’objet itérable spécifié. Vous pouvez spécifier un ordre croissant ou décroissant. Les chaînes sont triées alphabétiquement et les nombres sont triés numériquement.

##1.2 Exercice 2 :

1- Evaluons si un nombre entier n donné par l'utilisateur est parfait et affichons l'égalite qui le justifie
"""

#@title Nombre entier parfait {display-mode: "form"}
Nombre_entier =   6#@param {type:"number"}
n = Nombre_entier
S=[]
for i in range(1,n) :
  if (n%i==0) :
    S.append(i)
if  sum(S)==n:
  print ( n, " est un nombre entier parfait ")
  print (sum(S),"=", ' + '.join(str(elem) for elem in S) )
else:
  print (" est un nombre entier non parfait ")

#@title Liste des nombres parfait : saisir une limite {display-mode: "form"}
Nombre_entier_check =  1200#@param {type:"number"}
for i in range(1, Nombre_entier_check):
  S=[]
  for j in range(1,i) :
    if (i%j==0) :
      S.append(j)
  if  sum(S)==i:
    print ( i, " est un nombre entier parfait ")
    print (' + '.join(str(elem) for elem in S), "=", sum(S))

"""#Partie 2 : Exercices sur Maths discrètes

<h2><u>Exercice 3 :</u></h2>
Ecrire une fonction en Python nommée inversibles_modn qui prend en entrée un entier $\ n $ et
retourne l’ensemble des entiers $\ a ∈ {0, 1, . . . , n − 1}$ inversibles modulo n
"""

#@title Liste des entiers inversibles modulo n {display-mode: "form"}
n =  12#@param {type:"number"}
def verif(a, b):
      res = False
      while a!=b: 
        d=abs(b-a) 
        b=a 
        a=d 
      if d==1: 
        res = True
      return res
def inversiblesmod(n):  
  return [i for i in range(n) if verif(i,n) == True]
inversiblesmod(n)

"""<h2><u>Exercice 4 :</u></h2>
Ecrire une fonction en Python nommée euler_phi qui prend en entrée un entier $\ n$ et retourne $\ φ(n) $
où  $\ φ(n) $ est la fonction indicatrice d’Euler.
"""

#@title La fonction indicatrice d'Euler {display-mode: "form"}
n =  77#@param {type:"number"}
def euler_phi(n):
  congrumod = [i for i in range(n) if verif(i,n) == True]
  #print(congrumod)
  return len(congrumod)
euler_phi(n)

"""<h2><u>Exercice 5 :</u></h2>
Ecrire une fonction en Python nommée subgroup_mod qui prend en entrée deux entiers $\ a $ et $\ n > 0 $
avec $\ a $  inversible modulo $\ n $  et retourne l’ensemble

<center> $\ \{ a^1 mod n, a^2 mod n, a^3 mod n, . . . , a^k mod n = a mod n \} $ </center>
"""

#@title La fonction subgroup_mod {display-mode: "form"}
n =  48#@param {type:"number"}
a =  11#@param {type:"number"}

def subgroup_mod (a, n):
  if verif(a,n)== True:
    k=1
    while ((a^k)%n)<=a:
      print (f"({a}^{k})mod{n} = {a}")
      k+=1
  #{(print(f"{a^i} mod {n} = {a}")) for a in range(1,n) if (a^i)%n <= a}
subgroup_mod(a,n)

"""<h2><u>Exercice 5 :</u></h2>
Une fonction en Python nommée `pgcd` qui prend en entrée deux entiers $\ a$ et $\ b $ et retourne `pgcd`(n)
"""

#@title La fonction pgcd {display-mode: "form"}
a =  48#@param {type:"number"}
b =  12#@param {type:"number"}

def pgcd(a ,b):
  while b != 0 :
    r = a%b
    a=b
    b=r
  return a

pgcd(a,b)

"""<h2><u>Exercice 8 :</u></h2>
Ecrire une fonction en Python nommée `euclide_etendu` qui prend en entrée deux entiers $\ a$ et $\ b$ et
retourne les coefficients de Bezout $\ u$, $\ v$ qui sont tels que $\ ua + vb = pgcd(a, b) $
"""

#@title La fonction euclide_etendu {display-mode: "form"}
a =  48#@param {type:"number"}
n =  11#@param {type:"number"}
def euclide_etendu_prime(a, n):
  if verif(a,n)==True :
     # Initialisation
    d,u,v,d1,u1,v1=a,1,0,n,0,1
    # Calcul
    while d1!=0:
        q=d//d1
        d,u,v,d1,u1,v1=d1,u1,v1,d-q*d1,u-q*u1,v-q*v1
    return (u,v)
euclide_etendu_prime(a,n)

"""<h2><u>Exercice 7 :</u></h2>
Ecrire une fonction en Python nommée `inverse_mod` qui prend en entrée deux entiers $\ a$ et $\ n$ avec
$\ a$ inversible modulo $\ n$ et retourne l’inverse $\ b < n $ de $\ a$ modulo $\ n. $

"""

#@title La fonction inverse_mod {display-mode: "form"}
a =  5#@param {type:"number"}
n =  8#@param {type:"number"}
def inverse_modulo(a,n):
  u,v=euclide_etendu_prime(a,n)
  return u%n

inverse_modulo(a,n)

"""<h2><u>Exercice 9 :</u></h2>
Ecrire une fonction en Python nommée <code>puissance_rapide</code> qui prend en entrée trois entiers $\ a, k > 0 $
et $\ n > 0 $ et retourne $\ a^k mod n $**texte en gras** en utilisant l’algorithme de puissance rapide
"""

#@title L'algorithme de puissance rapide {display-mode: "form"}
Nombre =  5#@param {type:"number"}
Exposant =  17#@param {type:"number"}
Modulo = 23#@param {type: "number"}

def puissance_rapide (nbre, exp, mod):
  if mod == 1 :
    var = 0
  var = 1
  for i in range(exp):
    var = (var*nbre)%mod
  return var
puissance_rapide (Nombre, Exposant , Modulo)

"""<h2><u>Exercice 10 :</u></h2>
Ecrire une fonction en Python nommée <code>permut_inv </code> qui prend en entrée une permutation $\ π$ sous forme de tuple et retourne la permutation inverse $\ π^-1 $ sous forme de tuple.
"""

#@title L'algorithme de permutation inverse {display-mode: "form"}
Tuple =  (4,1,3,2)#@param 
x = Tuple
def permutation_inverse(x):
  perm=[]
  for i in range(1,len(x)+1):
    for j in range(1,len(x)+1):
      if(x[j-1]==i):
        perm.append(j)
  print(tuple(perm))

permutation_inverse(x)
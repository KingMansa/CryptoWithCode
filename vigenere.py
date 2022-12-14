# -*- coding: utf-8 -*-
"""Vigenere.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ggvu8YkIqTKhkoICyy81HkxfAGjMNNMA
"""

import string
def alphabet():
  return list(string.ascii_lowercase)

def generate_alphabet_table():
  """
  This is a function that generate the alphabet matrix to encypher with vigenere 
  """
  import string
  alpha = alphabet()
  matrixalpha = []

  for i in range(len(alpha)):
    newalpha = alpha[i:] + alpha[0:i]
    #print(newalpha)
    matrixalpha.append(newalpha)
  return matrixalpha

generate_alphabet_table()

def encypher_vigenere(key, message):
  import string
  message = list(message)
  key = list(key)
  alpha = alphabet()
  matrixalpha = generate_alphabet_table()
  count = 0
  cypher = ''
  for m in message:
    for row in matrixalpha:
      if key[count%len(key)] == row[0]:
        #print(matrixalpha.index(row))
        #print(row)
        #print(count%len(key))
        #print(alpha.index(m), m ,"==>", row[alphabet.index(m)])
        #print(row[alpha.index(m)])
        #print(alpha[row.index(message.index(m))])
        cypher += row[alpha.index(m)]
    count += 1
  print(cypher)

encypher_vigenere('galois', 'northernkentuckyuniversity')

def decypher_vigenere(key, cypher):
  import string
  cypher = list(cypher)
  key = list(key)
  alpha = alphabet()
  matrixalpha = generate_alphabet_table()
  count = 0
  message = ''
  for c in cypher:
    #print(c)
    for row in matrixalpha:
      if key[count%len(key)] == row[0]:
        #print(row)
        #print(alpha[row.index(c)])
        message+=(alpha[row.index(c)])
    count+=1
  print(message)

decypher_vigenere('galois', 'tochpwxnvsvlacvmcfovpfaazy')
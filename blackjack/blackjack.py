import numpy as np
import math
import random

def shuffle():
  cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
  suits = ["d","c","h","s"]
  deck = []
  for i in range (len(cards)):
    for j in range(len(suits)):
      deck += [cards[i]+suits[j]]

  card_scores = {}
  card_index = 0
  card_val = 2
  i = 0
  k = 0
  while k < 13:
    while i<4:
      card_scores[deck[card_index]] = card_val
      card_index += 1
      i += 1
    card_val += 1
    k += 1

  print(card_scores)
  return card_scores 
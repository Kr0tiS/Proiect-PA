import random
simb = ['X', 'O' , '$']

def linii():
  return (random.choice(simb),
          random.choice(simb),
          random.choice(simb))

def verif_castig(perechi):
   if perechi[0] == perechi[1] == perechi[2]
     return True
   return False   
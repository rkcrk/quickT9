# quickT9 - работает по типу т9 но без грамматики и смысла
import random as r
import string
import time as t
import pyperclip
from english_words import get_english_words_set


spread=[-1,1,1,1,1,1,1,1,1,1,2]
"""
jn=jn.lower()
try:
    k=eval(jn)
except:
    k=[]
    n=jn
    for j in n.split():k.append(j)
    #k.append('üSKIP')

def find_itl(l,f):
    # return indexes of the found l elements
    n=[]
    for i,k in enumerate(l):
        if k==f:
            n.append(i)
    return n
nd={}
"""
k = open('cew.txt').read().split()
#k = list(get_english_words_set(['web2'], lower=True))
print('================================TRANSFORM================================')
for i,idxk in enumerate(k):
    k[i]=idxk.lower()
    k[i]=idxk.translate(str.maketrans('', '', string.punctuation))
    if i%100==0:print(f'proceeded {i}/{len(k)}     ',end='\r')
print('the array now looks like this:\n',k)
print('================================LINKING================================')
linker={'the': ['man', 'girl', 'thing', 'food', 'dog', 'cat', 'people'], 'will': ['they'], 'touch': ['something'], 'dear': ['mother', 'father'], 'father': ['is', 'i'], 'is': ['a', 'an', 'the', 'good', 'short'], 'these': ['are', 'case', 'base'], 'this': ['is', 'bad'], 'know': ['father', 'mother', 'mother', 'father'], 'feed': ['food', 'the'], 'charge': ['phone'], 'keep': ['eye', 'thing', 'memory'], 'put': ['this', 'that'], 'i': ['need', 'broke', 'found', 'am'], 'am': ['down', 'go'], 'mother': ['i'], 'we': ['broke', 'need', 'found'], 'she': ['found'], 'he': ['found'], 'found': ['thing'], 'need': ['thing', 'you', 'this', 'these'], 'food': ['is', 'to'], 'good': ['for'], 'for': ['us'], 'let': ['us'], 'us': ['go'], 'go': ['at', 'to'], 'at': ['time', 'place'], 'time': ['is'], 'you': ['live'], 'live': ['only'], 'only': ['once'], 'to': ['the', 'hold'], 'people': ['are'], 'are': ['bad'], 'bad': ['in'], 'in': ['wing', 'anger'], 'hold': ['them', 'it']}
while True:
	"""
	for o in k:
		
		fk=input(f'what comes after word {o} >>> ')
		if fk=='qaend': break
		if fk=="":
			print('pass;')
			continue
		try:linker[o].append(fk)
		except:linker[o]=[fk]
		print(linker)
	"""
	a=input("word: ")
	if len(a.split())==1:continue
	if a in k:
		pass
	elif a=="qa qa":break
	elif not(a.split()[0] in k) or not(a.split()[1] in k):
		print('bad words (init or bind)')
		continue
	try:linker[a.split()[0]].append(a.split()[1])
	except:
		linker[a.split()[0]]=[a.split()[1]]
#sword=r.choice(list(linker.keys()))
sword="i"
print(linker)
for i in range(0,20):
	print(sword, end=" ")
	ERROR=True
	while ERROR:
		try:
			sword=r.choice(linker[sword])
			ERROR=False
		except:
			print(end="\n")
			sword=r.choice(list(linker.keys()))
import random as r
import string
import sys as ro
if len(ro.argv)==2:argv=ro.argv[1]
else:argv=''

import time as t
k = open('cew.txt').read().split()
print('================================TRANSFORM================================')
for i,idxk in enumerate(k):
    k[i]=idxk.lower()
    k[i]=idxk.translate(str.maketrans('', '', string.punctuation))
    if i%100==0:print(f'proceeded {i}/{len(k)}     ',end='\r')
print('the array now looks like this:\n',k)
print('================================LINKING================================\n\t type "quit" to exit and start generating sentences')
linker={'the': ['man', 'girl', 'thing', 'food', 'dog', 'cat', 'people', 'build', 'build', 'floor', 'floor', 'floor', 'people', 'people', 'people', 'man'], 'will': ['they', 'they'], 'touch': [], 'dear': ['mother', 'father'], 'father': ['is', 'i'], 'is': ['a', 'an', 'the', 'good', 'short', 'bad', 'go', 'go', 'bad', 'bad', 'get'], 'these': ['are', 'case', 'base'], 'this': ['is', 'bad', 'is', 'is'], 'know': ['father', 'mother', 'mother', 'father'], 'feed': ['food', 'the'], 'charge': [], 'keep': ['eye', 'thing'], 'put': ['this', 'that'], 'i': ['need', 'broke', 'found', 'am', 'am', 'am', 'found', 'found', 'found', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'feel', 'feel', 'feel', 'feel', 'am', 'am', 'am', 'am', 'am', 'am', 'am', 'she', 'think', 'am'], 'am': ['down', 'go', 'here', 'not', 'do', 'do', 'do', 'do', 'real', 'not', 'a', 'a', 'a', 'a', 'i', 'a'], 'mother': ['i'], 'we': ['broke', 'need', 'found', 'are', 'are', 'are', 'have', 'do'], 'she': ['found'], 'he': ['found'], 'found': ['thing', 'thing'], 'need': ['thing', 'you', 'this', 'these', 'them'], 'food': ['is', 'to', 'is', 'is'], 'good': ['for'], 'for': ['us', 'me'], 'let': ['us'], 'us': ['go'], 'go': ['at', 'to', 'to', 'to', 'to', 'to', 'to', 'to'], 'at': ['time', 'place'], 'time': ['is'], 'you': ['live', 'are', 'need'], 'live': ['only'], 'only': ['once'], 'to': ['the', 'hold', 'do', 'the', 'the', 'the', 'here', 'wait', 'help', 'help', 'it'], 'people': ['are', 'are', 'are'], 'are': ['bad', 'go', 'go', 'go', 'not', 'the', 'watch'], 'bad': ['in', 'for'], 'in': ['wing', 'anger'], 'hold': ['them', 'it', 'moment'], 'not': ['go', 'have', 
'real'], 'going': ['to', 'to'], 'do': ['this', 'not', 'my', 'bad', 'good'], 'girl': ['was', 'please'], 'was': ['not'], 'one': ['minute', 'is', 'is'], 'have': ['to', 'it'], 'wait': ['a'], 'a': ['second', 'bottom', 'bottom', 'bottom', 'bottom', 'girl'], 'no': ['one', 'one', 'end', 'end', 'end'], 'help': ['me', 'us'], 'our': ['food', 'food'], 'something': ['on'], 'on': ['the', 'the', 'the', 'me'], 'thing': ['on'], 'doing': ['my'], 'my': ['job', 'job'], 'feel': ['mine', 'mine'], 'mine': [], 'who': ['are', 'create'], 'please': ['stop'], 'end': ['to', 'to', 'to'], 'it': ['is'], 'they': ['experiment', 'search'], 'experiment': ['on'], 'nature': ['is', 'is', 'is'], 'get': ['good'], 'proper': ['teach', 'result'], 'teach': ['give'], 'give': ['proper'], 'think': ['i'], 'owner': [], 'offered': ['me'], 'me': ['proper', 'proper', 'offer', 'proper'], 'developer': ['offer'], 'offer': ['me', 'me'], 'man': ['who'], 'create': ['me'], 'search': ['me']}
print('================================LINKER CLEANUP================================')
def cleanup():
	for case in linker:
		for i,word in enumerate(linker[case]):
			if not word in k:
				print(f'word {word} is not found in vocab')
				del linker[case][i]
cleanup()
while argv!='-g':
	a=input("sentence: ")
	if a=='quit':break
	if len(a.split())==1:continue
	for n,word in enumerate(a.split()):
		if not (word in k): print(f'{word} is an illegal word')
		try:linker[word].append(a.split()[n+1])
		except:
			try:linker[word]=[a.split()[n+1]]
			except:pass
	cleanup()
sword="i"
print(linker)
print('================================GENERATING================================')
for i in range(0,40):
	print(sword, end=" ")
	ERROR=True
	while ERROR:
		try:
			sword=r.choice(linker[sword])
			ERROR=False
		except:
			print(end="\n")
			sword=r.choice(list(linker.keys()))
			#sword='i'
			print(sword, end=" ")
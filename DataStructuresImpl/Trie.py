class Trie:
	def __init__(self,val=None):
		self.val = val
		self.children = {}
		self.word = False

	def checkWord(self,word,i=0):
		if i == len(word)-1:
			return self.word
		return word[i] in self.children and self.children[word[i]].checkWord(word,i+1)

	def addWord(self,word,i=0):
		if i == len(word)-1:
			self.word = True
		else:
			if word[i] not in self.children:
				self.children[word[i]] = Trie(word[i])
			self.children[word[i]].addWord(word,i+1)

	#Supports ? for any char
	def checkWordWildCard(self,word,i=0):
		if i == len(word)-1:
			return self.word
		elif word[i] == "?":
			for ch in self.children:
				if self.children[ch].checkWordWildCard(word,i+1):
					return True
			return False
		else:	
			return word[i] in self.children and self.children[word[i]].checkWordWildCard(word,i+1)

head = Trie()
head.addWord("Hello")
head.addWord("Hellebores")


assert head.checkWord("Hello"), "Hello should be found inside Trie"

assert head.checkWord("Hellebores"), "Hellebores should be found inside Trie"

assert not head.checkWord("hello"), "hello (lowercase) should not be found inside Trie"

assert not head.checkWord("He"), "He (incomplete word) should not be found inside Trie"

assert not head.checkWord("He"), "HelloThere (Too long word) should not be found inside Trie"


assert head.checkWordWildCard("Hell?"), "Hell? should be found inside Trie"

assert head.checkWordWildCard("He?l?"), "He?l? should be found inside Trie"

assert head.checkWordWildCard("?????"), "????? should be found inside Trie"

assert not head.checkWordWildCard("??????"), "?????? should not be found inside Trie"

assert not head.checkWordWildCard("?"), "?????? should not be found inside Trie"



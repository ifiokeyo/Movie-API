
class Trie:
	def __init__(self):
		"""Construct and object of type Trie."""
		self.trie = [[]]


	def is_trie_bucket(self, x):
		return isinstance(x, tuple) and len(x) == 2 and isinstance(x[0], str) and isinstance(x[1], list) and len(x[1]) == 1

	def is_trie_branch(self, x):
		return isinstance(x, list)

	def get_bucket_key(self, b):
		return b[0]

	def get_bucket_val(self, b):
		return b[1][0]

	### ******************** INSERT_KEY ************************

	def insert_key(self, k, v):
		## do not insert empty keys
		if k == '':
			return None
		## if trie has k or stores it with the same value v,
		## do not insert
		elif self.trie_has_key(k) and self.retrieve_movie_object(k) == v:
			return None
		else:
			trie = self.trie
			## for each character c in k, find a child
			## branch that starts with c
			for c in k:
				branch = self.find_child_branch(trie, c)
				## if there is no branch that starts with c,
				## create it and append it at the end of
				## the current level.
				if branch == None:
					new_branch = [c]
					trie.append(new_branch)
					trie = new_branch
				else:
					trie = branch
			## tr is now bound to the branch, so insert
			## a new bucket.
			trie.append((k, [v]))
			return None

	## a branch is either empty or it is a list whose first
	## element is a character and the rest are buckets or
	## sub-branches.
	def get_child_branches(self, trie):
		if trie == []:
			return []
		else:
			return trie[1:]

	def find_child_branch(self, trie, c):
		for branch in self.get_child_branches(trie):
			if branch[0] == c:
				return branch
		return None

	### ************************ TR_HAS_KEY *************************

	def trie_has_key(self, k):
		br = self.retrieve_branch(k)
		if br == None:
			return False
		else:
			return self.is_trie_bucket(self.get_child_branches(br)[0])

	### ******************** RETRIEVE_VAL ************************

	## find a branch in trie that is indexed under k.
	def retrieve_branch(self, k):
		if k == '':
			return None
		else:
			trie = self.trie
			for c in k:
				br = self.find_child_branch(trie, c)
				if br == None:
					return None
				else:
					trie = br
			return trie

	## find a branch and retrieve its bucket, second element.
	def retrieve_movie_object(self, k):
		if not self.trie_has_key(k):
			return None
		br = self.retrieve_branch(k)
		return self.get_bucket_val(br[1])

	### *************** START_WITH_PREFIX ************************

	def start_with_prefix(self, prefix):
		## 1. find the branch indexed by prefix
		br = self.retrieve_branch(prefix)
		if br == None:
			return []

		key_list = []
		q = self.get_child_branches(br)
		## 2. go through the sub-branches of the
		## branch indexed by the prefix and
		## collect the bucket strings into key_list
		while not q == []:
			curr_br = q.pop(0)
			if self.is_trie_bucket(curr_br):
				key_list.append(self.get_bucket_key(curr_br))
			elif self.is_trie_branch(curr_br):
				q.extend(self.get_child_branches(curr_br))
			else:
				return 'ERROR: bad branch'
		return key_list

	@staticmethod
	def build_movie_trie(trie_instance, movies):
		for movie in movies:
			trie_instance.insert_key(movie['name'].lower(), movie)
		return

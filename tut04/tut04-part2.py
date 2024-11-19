def group_anagrams(strings):
  anagrams={}
  for words in strings:
    sorted_word="".join(sorted(words))
    if sorted_word not in anagrams:
      anagrams[sorted_word]=[]
    anagrams[sorted_word].append(words)

  return list(anagrams.values())


def anagram_count(strings):
  anagram_count={}
  for string in strings:
    sorted_string="".join(sorted(string))
    if sorted_string in anagram_count:
      anagram_count[sorted_string]+=1
    else:
      anagram_count[sorted_string] = 1
  return anagram_count

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(strings))

print(anagram_count(strings))
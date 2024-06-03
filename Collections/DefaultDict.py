def find_occurrences(group_a, group_b):
  result = []
  for word_b in group_b:
    occurrences = []
    for i, word_a in enumerate(group_a):
      if word_a == word_b:
        occurrences.append(i + 1) 
    result.append(occurrences)
  return result


n, m = map(int, input().split())

group_a = []
for _ in range(n):
  group_a.append(input())

group_b = []
for _ in range(m):
  group_b.append(input())

results = find_occurrences(group_a, group_b)
for occurrence_list in results:
  if not occurrence_list:
    print("-1")
  else:
    print(*occurrence_list)  


"""
5 2
a
a
b
a
b
a
b


==============OUTPUT
1 2 4
3 5
"""

import sys
# grid rows: M , grid columns: N
# Time: O(M N)
# Space O(length of word)
def findWord(word, grid):
  # IMPLEMENTATION GOES HERE. Prints to standard output.
  m = len(grid)
  n = len(grid[0])
  directions = [(0, 1), (1, 0)]
  path = []
  res = []
  def backtracking(x, y, cur_word, path):
    nonlocal res
    if len(cur_word) == 1:
      res = path[:]
      res.append((x, y))
      return True
    
    grid[x][y] = '#'
    ans = False
    path.append((x, y))
    for d in directions:
      x0, y0 = x + d[0], y + d[1]
      if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or grid[x0][y0] != cur_word[1]:
        continue
      ans = backtracking(x0, y0, cur_word[1:], path)
      if ans: break
    grid[x][y] = cur_word[0]
    path.pop()
    return ans
  
  for i in range(m):
    for j in range(n):
      if word[0] == grid[i][j]:
        backtracking(i, j, word, path)
  if not res:
    print("None")
  else:
    for x, y in res:
      print(x,y)
        
    
# DO NOT MODIFY BELOW THIS LINE
def main():
  word = []
  grid = []
  first_arg = True
  for line in sys.stdin:
    if len(line.strip()) == 0:
      continue
    line = line.rstrip()
    if first_arg:
      word = line
      first_arg = False
    else:
      grid.append(line.split(" "))
  findWord(word, grid)
main()

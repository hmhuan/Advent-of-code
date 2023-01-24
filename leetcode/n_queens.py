# https://leetcode.com/problems/n-queens/
def solveNQueens(self, n: int) -> List[List[str]]:
  col = set()
  posDiag = set() #(r + c)
  negDiag = set() #(r - c)

  result = []
  board = [["."] * n for i in range(n)]
  
  def dfs(r):
    if r == n:
      result.append(["".join(row) for row in board])
      return
    for c in range(n):
      if c in col or (r+c) in posDiag or (r-c) in negDiag:
        continue
      board[r][c] = 'Q'
      col.add(c)
      posDiag.add(r+c)
      negDiag.add(r-c)
      dfs(r+1)
      negDiag.remove(r-c)
      posDiag.remove(r+c)
      col.remove(c)
      board[r][c] = '.'
   
  dfs(0)
  return result

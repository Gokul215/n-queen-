class queen:
    def __init__(self,n) -> None:
        self.board=[['.']*n for i in range(n)]
        self.colset=set()
        self.pdiagonal=set()
        self.ndiagonal=set()
        
    def solveNQueens(self,r):
        n=len(self.board)
       
        if r==n:
            res=self.board
            print('-----------------------')
            for i in range(len(res)):
                for j in range(len(res)):
                    print(res[i][j],end='  ')
                print()
            return res
        for c in range(n):
            if c in self.colset or r+c in self.pdiagonal or r-c in self.ndiagonal:
                continue
            self.colset.add(c)
            self.pdiagonal.add(r+c)
            self.ndiagonal.add(r-c)
            self.board[r][c]='Q'

            self.solveNQueens(r+1)
            # if self.solveNQueens(r+1):
            #     return
            
            self.colset.remove(c)
            self.pdiagonal.remove(r+c)
            self.ndiagonal.remove(r-c)
            self.board[r][c]='.'



    
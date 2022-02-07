class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        print(word)
        length = len(board)
        for x in range(length):
            for y in range(len(board[0])):
                if  board[x][y] == word[0]:
                    # print("Matches letter",x,y,word[0])
                    if self.dfs(x,y,board,word[1:],set([(x,y)])):
                        return True
        return False



    def dfs(self,x,y,board,word,memo):
        # print("Memor",memo)
        if len(word) == 0:
            return True
        for index in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
            if index not in memo:
                if index[0]>=0 and index[0] < len(board) and index[1]>=0 and index[1] < len(board[0]):
                    newMemo = memo.copy()
                    newMemo.add(index)
                    if board[index[0]][index[1]] == word[0]:
                        # print("Matches letter",index,newMemo)
                        if self.dfs(index[0],index[1],board,word[1:],newMemo):
                            # print("True",index)
                            return True
            #         else:
            #             print("Unmactched",index,word[0])
            #     else:
            #         print("Out of bound",index)
            # else:
            #     print("Already visited",index)
        return False
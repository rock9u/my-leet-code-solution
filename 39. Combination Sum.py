class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # brute: through all number, find number small than target return remainder        
        self.list = []
        memo = []
        self.findComb(candidates,target,memo)

        return self.list

    def findComb(self,cand,targ,memo):
        for i  in range(len(cand)):
            c = cand[i]

            if c < targ:
                self.findComb(cand[i:],targ-c,[*memo, c])
            elif c == targ:
                self.list.append([*memo,c])
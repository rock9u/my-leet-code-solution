class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        for each word
            count letter
            put each item in map
        for each keypair
            print
            
        '''

        bucket = dict()
        for word in strs:
            key = ''.join(sorted(word))

            #these can be simplified with d[key] = d.get(key, []) + [w]
            if not key in bucket.keys():   
                bucket[key] = [word]
            else:
                bucket[key].append(word)

        return bucket.values()
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h=0
        for i, citations_count in enumerate(citations):
            if citations_count >= i+1:
                h=i+1
            else:
                break
        return h

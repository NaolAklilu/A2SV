class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        dic = defaultdict(int)
        elected_person = []
        maxPerson = persons[0]
        maxPersonCount = 1
        for i in range(len(persons)):
            dic[persons[i]] += 1
            if dic[persons[i]] >= maxPersonCount:
                maxPerson = persons[i]
                maxPersonCount = dic[persons[i]]
            
            elected_person.append(maxPerson)
        
        self.persons = elected_person
            

    def q(self, t: int) -> int:
        left = -1
        right = len(self.times)
        
        while left+1 < right:
            mid = left + (right-left)//2
            
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid
                
        return self.persons[left]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
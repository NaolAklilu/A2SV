class ThroneInheritance:

    def __init__(self, kingName: str):
        self.curOrder = defaultdict(list)
        self.deadPeople = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.curOrder[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deadPeople.add(name)

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        
        inheritanceOrder = []
        def getInheritance(person):
            if person not in visited and person not in self.deadPeople:
                inheritanceOrder.append(person)
                visited.add(person)
            
            for child in self.curOrder[person]:
                if child not in visited:
                    getInheritance(child)
            
            return
        
        
        getInheritance(self.king)
        
        return inheritanceOrder

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
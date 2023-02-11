class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        playerPtr, trainerPtr = 0, 0
        count = 0
        while playerPtr<len(players) and trainerPtr<len(trainers):
            if players[playerPtr] <= trainers[trainerPtr]:
                count += 1
                playerPtr += 1
                trainerPtr += 1
                
            else:
                trainerPtr += 1
                
        return count
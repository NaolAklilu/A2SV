class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.news_feed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(tweetId)
        self.news_feed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for user, tweet in reversed(self.news_feed):
            if user == userId or user in self.followers[userId]:
                feed.append(tweet)
            if len(feed) == 10:
                break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
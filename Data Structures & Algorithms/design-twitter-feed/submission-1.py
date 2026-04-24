class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.cnt = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.cnt, tweetId])
        self.cnt -= 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for u in self.users[userId]:
            if u in self.tweets:
                tweets.extend(self.tweets[u])
        if userId in self.tweets:
            tweets.extend(self.tweets[userId])
        heapq.heapify(tweets)
        res = []
        for _ in range(10):
            if not tweets:
                return res
            cnt, tid = heapq.heappop(tweets)
            res.append(tid)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
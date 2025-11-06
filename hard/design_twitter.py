"""
Problem: Design Twitter
Design Twitter with postTweet, follow, unfollow, getNewsFeed.
"""

from collections import defaultdict

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)  # userId → list of (time, tweetId)
        self.following = defaultdict(set)  # userId → set of followees
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Post a tweet
        Time: O(1)
        """
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId):
        """
        Get 10 most recent tweet IDs from user and followees
        Time: O(n log n) - can be optimized with heap to O(k log k)
        """
        followees = self.following[userId] | {userId}
        all_tweets = []

        for user in followees:
            if user in self.tweets:
                all_tweets.extend(self.tweets[user])

        all_tweets.sort(reverse=True, key=lambda x: x[0])
        return [tweet[1] for tweet in all_tweets[:10]]

    def follow(self, followerId, followeeId):
        """
        Follow a user
        Time: O(1)
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Unfollow a user
        Time: O(1)
        """
        self.following[followerId].discard(followeeId)

# Test
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))  # [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))  # [6, 5]
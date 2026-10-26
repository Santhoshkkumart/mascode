"""
Tests for Design Twitter (LeetCode 355)
Heap / Priority Queue / Medium
"""
import sys
from pathlib import Path

# Add repo root to path for lib imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

# Load solution from this directory (avoids module name collision with other test_solution.py files)
import importlib.util
_solution_path = Path(__file__).parent / "solution.py"
_spec = importlib.util.spec_from_file_location("_solution", _solution_path)
_solution_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_solution_mod)
Twitter = _solution_mod.Twitter




def test_twitter_basic():
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]

def test_twitter_multiple_tweets():
    twitter = Twitter()
    twitter.postTweet(1, 1)
    twitter.postTweet(1, 2)
    twitter.postTweet(1, 3)
    assert twitter.getNewsFeed(1) == [3, 2, 1]

def test_twitter_feed_limit():
    twitter = Twitter()
    for i in range(12):
        twitter.postTweet(1, i)
    feed = twitter.getNewsFeed(1)
    assert len(feed) == 10
    assert feed[0] == 11

def test_twitter_follow_self():
    twitter = Twitter()
    twitter.postTweet(1, 10)
    assert twitter.getNewsFeed(1) == [10]


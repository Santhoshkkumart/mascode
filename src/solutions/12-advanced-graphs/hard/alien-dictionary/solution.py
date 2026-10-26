"""
Problem: LeetCode 269 - Alien Dictionary

Key Idea:
The problem can be solved using topological sorting. The given words can be
thought of as directed edges between characters of adjacent words. We build
a graph where each character is a node, and edges represent order. Then we
perform topological sorting (Kahn's algorithm) to find the character order.

Time Complexity: O(N * L + V + E) where N is number of words, L is max word length.

Space Complexity: O(V + E) for the graph and in-degree map.
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        # Initialize in_degree for all unique characters
        all_chars = set()
        for word in words:
            for c in word:
                all_chars.add(c)
        for c in all_chars:
            in_degree[c] = 0

        # Build edges from adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            # Check for invalid case: prefix word is longer
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    in_degree[word2[j]] += 1
                    break

        # Kahn's topological sort
        queue = deque(char for char, indeg in in_degree.items() if indeg == 0)
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) < len(all_chars):
            return ""
        return "".join(result)

"""
1813. Sentence Similarity III [MEDIUM]

You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list
of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase
and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside
one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from
existing words by spaces.

For example,

- s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by inserting "my name is" between "Hello" and
  "Jane" in s1.

- s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although there is a sentence "s are" inserted into
  s1, it is not separated from "Frog" by a space.

Given two sentences, return true if sentence1 and sentence2 are similar. Otherwise, return false.


Example 1:

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true

Explanation:
sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".


Example 2:

Input: sentence1 = "of", sentence2 = "A lot of words"
Output: false

Explanation:
No single sentence can be inserted inside one of the sentences to make it equal to the other.


Example 3:

Input: sentence1 = "Eating right now", sentence2 = "Eating"
Output: true

Explanation:
sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.


Constraints:

    -> 1 <= sentence1.length, sentence2.length <= 100
    -> sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
    -> The words in sentence1 and sentence2 are separated by a single space.


Concepts: Deque
"""
from collections import deque


def areSentencesSimilar(sentence1: str, sentence2: str) -> bool:
    dq1, dq2 = map(deque, (sentence1.split(),
                           sentence2.split()))      # Split sentences into words and store them in deque(s)

    while dq1 and dq2 and dq1[0] == dq2[0]:         # While the first elements of deque(s) match, remove the elements
        dq1.popleft()
        dq2.popleft()

    while dq1 and dq2 and dq1[-1] == dq2[-1]:       # While the end elements of deque(s) match, remove the elements
        dq1.pop()
        dq2.pop()

    return not dq1 or not dq2                       # Check if either of the deque is empty

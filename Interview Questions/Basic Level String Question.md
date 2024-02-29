# Problem Statements

Write a Python function that takes in two arguments: a string `s` and a character `c`. The function should return the index of the first occurrence of the character `c` in the string `s`. If the character `c` is not found in the string `s`, the function should return -1.

For example:

```python
>>> find_first_occurrence("hello", "l")
2
>>> find_first_occurrence("hello", "o")
4
>>> find_first_occurrence("hello", "x")
-1
```

Question:
Implement the `find_first_occurrence` function in Python according to the given problem statement.
___

 You are given a string `s`. Your task is to determine whether it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

```plaintext
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
```

Example 2:

```plaintext
Input: s = "aba"
Output: false
```

Example 3:

```plaintext
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
```

Question:
Implement a Python function named `can_construct_substring` that takes a string `s` as input and returns `True` if it can be constructed by taking a substring of it and appending multiple copies of the substring together, otherwise return `False`.

___

Problem Statement:
You are given two strings `s` and `goal`. Your task is to determine whether `s` can become `goal` after some number of shifts on `s`.

A shift on `s` consists of moving the leftmost character of `s` to the rightmost position.

Example 1:

```plaintext
Input: s = "abcde", goal = "cdeab"
Output: true
Explanation: After shifting "abcde" by two positions, it becomes "cdeab", which matches the goal.
```

Example 2:

```plaintext
Input: s = "abcde", goal = "abced"
Output: false
Explanation: No matter how many shifts you apply on "abcde", it can never become "abced".
```

Question:
Implement a Python function named `can_shift_to_goal` that takes two strings `s` and `goal` as input and returns `True` if and only if `s` can become `goal` after some number of shifts on `s`, otherwise return `False`.

___

Problem Statement:
You are given an array of string `words`. Your task is to return all strings in `words` that are substrings of another word in the array. You can return the answer in any order.

A substring is a contiguous sequence of characters within a string.

Example 1:

```plaintext
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is a substring of "mass" and "hero" is a substring of "superhero".
```

Example 2:

```plaintext
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et" and "code" are substrings of "leetcode".
```

Example 3:

```plaintext
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string in the array is a substring of another string.
```

Question:
Implement a Python function named `find_substring_words` that takes an array of strings `words` as input and returns all strings in `words` that are substrings of another word in the array. You can return the answer in any order.

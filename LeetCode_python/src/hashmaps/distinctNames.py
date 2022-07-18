'''
You are given an array of strings ideas that represents a list of names to be used 
in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB 
(the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.

The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.


Solution:
    - Use a hashmap to store ideas: first_letter:second_to_last_letters
    - Count corresponds to the number of non-common occurences in each group

Created on July 10, 2022
@author: smaiya
'''
from typing import Dict, Any, List
from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        i_deas = defaultdict(set)
        for i in ideas:
            i_deas[i[0]].add(i[1:])
        
        count = 0
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for i, l1 in enumerate(letters):
            if l1 in i_deas:
                for j in range(i+1, len(letters)):
                    l2 = letters[j]
                    if l2 in i_deas:
                        num_l1, num_l2 = len(i_deas[l1]), len(i_deas[l2])
                        num_common = len(i_deas[l1].intersection(i_deas[l2]))
                        # 2* because 2 combinations of ideas: (a, b) and (b, a)
                        count += 2*(num_l1-num_common)*(num_l2-num_common)
        return count


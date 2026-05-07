# CISC121-FinalProject_MergeSort

# Problem - Scholarship Shortlist  Algorithm - Merge Sort
Project overview: The app will assist in sorting students by their grades, gpa, extra-curriculars using Merge sort which can help admission teams decide who shall receive scholarships

# Computational Thinking

Problem Decomposition:
Input - List of students with their names and merit scores
Divide - Breaks list down into halves until all sub-lists have only one student
Compare - Checks score of 2 different students at the front of their designated sub list
Merge - Sorts and orders students from high to low in terms of scores, creating a new list

Pattern Recognition:
Follows the pattern of "split, sort, merge" no matter the total number of students. This method is consistent and breaks the large sorting issue into smaller, more manageable parts

Abstraction:
Focus is on the logic used to sort and the merit scores themselves. App should ignore/hide calls to recursive function and memory management. The user should only see the final result/leaderboard of students

Algorithm Design
Flowchart:
<img width="1432" height="1574" alt="image" src="https://github.com/user-attachments/assets/f4d00705-7c78-4774-8080-5d7bbf206979" />
Explanation:
Main Sort - splits list in half until each student has their own list. When a list is one student exactly, it sorts and returns
Merge - compares top student in left vs right list, student with better scores goes first in the result list to create the rankings, yellow highlights will shows user which scores are being compared, any students left are added once a side is finished

# More Explanation
Why Merge Sort - Merge sort is stable, and helps verify that students with the same score stay in their original order, also the efficiency helps reduce lag for greater applicants (uses O(nlogn))
Preconditions - Inputs must be a certain structure (Name, Score). App should enforce this by checking if each score is a valid number before sorting begins, should also disregard any invalid inputs to avoid crashing
Simulation - the yellow highlight should show 2 specific students being compared against each other

AI Disclosure: Full level 4 ai used (Gemini) to generate solutions, rough drafts, and overall code. Used with minimal modicfication and assisted with various issues.

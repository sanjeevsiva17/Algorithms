# Hiring Assistant Problem Randomized Algorithm
# By Sanjeev
# The goal : devise an strategy that maximizes the probability of hiring the best of the n candidates.
#

import random


def hireAssistant(candidates):
    best = 0
    numberOfHired = 0
    for i in range(len(candidates)):
        if (candidates[i] > best):
            best = candidates[i]
            numberOfHired += 1
            print("the candidate hired", candidates[i])
    return numberOfHired


def randomizedHireAssistant(candidates):
    candidateList = candidates
    randomizeInPlace(candidateList)
    return hireAssistant(candidateList)

# Function to randomize the list
def randomizeInPlace(array):
    n = len(array)
    print(n)
    for i in range(1, n):
        x = random.choice(array)
        for y in range(len(array)):
            if x == array[y]:
                break
        swap(array, i, y)


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


candidateRanks = [1, 2, 4, 6, 3, 9, 5, 12, 56, 7, 8]
candHired = [0 for x in range(len(candidateRanks))]
numberOfHiredCandidates = hireAssistant(candidateRanks)
print("Number of hired candidates: ", numberOfHiredCandidates)

numberOfHiredCandidatesRandom = randomizedHireAssistant(candidateRanks)
print("After randomized algorithms, number of hire candidates: ", numberOfHiredCandidatesRandom)

# Complexity
# E[total cost]= for all n E[(fee to be paid for i-th candidate)]
#        =f. ln n

def avg(scores):
    assert len(scores)!=0,"The list is empty."
    return sum(scores)/len(scores)
scores2 = [2,34,4,2]
print("The average of scores2:",avg(scores2))
scores1 =[]
print("The average of scores1:",avg(scores1))

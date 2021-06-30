import math
def permutate(person, interview): 
    container = list()
    length = len(interview)
    interview_copy = interview.copy()
    interview_copy.insert(length, person)
    container.append(interview_copy)
    for i in range(length):
        interview_copy = interview.copy()
        interview_copy.insert(i, person)
        container.append(interview_copy)
    return container

person_names = ['a','b','c','d','e','f','g','h','i','j'] #does not works with 9 or 10 persons; takes long time; in my machine it did not output the result
person_names = ['a','b','c','d','e','f','g','h']  # works upto 8 persons in this list 
interviews = [[]]
total_posibility = math.factorial(person_names.__len__())
txt = open("interviews.txt", 'w')

for person in person_names:
    for interview in interviews:
        interviews = interviews + permutate(person, interview)
        interviews.remove(interview)
#print(interviews)  uncommnet thes line to see the total 40120 list output on terminl
print(len(interviews))


# below portion is for counting the combination 
count = 0
a, b, c = False, False, False

for interview in interviews:
    for person in interview:
        if person == 'a':
            count = count + 1
print("person 'a' can give interview in", count, "numbers way. The probability is 1 /",  total_posibility / count, "...")

count = 0
for interview in interviews:
    for person in interview:
        if person == 'a':
            a = True
        if person == 'b' and a:
            count = count + 1
    a = False
print("person 'a' before 'b' can give interview in", count, "numbers way. The probability is 1 /", total_posibility / count, "...")

count = 0
num = 1
for interview in interviews:
    txt.write(str(num))
    txt.write('\t')
    txt.write(str(interview))
    for person in interview:
        if person == 'a':
            a = True
        if person == 'b' and a:
            b = True
        if person == 'c' and b:
            count = count + 1
            txt.write('\t')
            txt.write("'a' is before 'b' and 'b' is before 'c'")
    a = False
    b = False
    txt.write('\n')
    num = num + 1
txt.close()
print("person 'a' before 'b' and person 'b' before 'c' can give interview in", count, "numbers way. The probability is 1 /", total_posibility / count, "...")

print('\n ***************Check the "interviews.txt" file for those combinations****************')
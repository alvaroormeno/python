import re

sampleData = '/Users/alvaroormeno/Desktop/python-learning/ExtractingDataWithRegularExpressions/sampleData.txt'
actualData = '/Users/alvaroormeno/Desktop/python-learning/ExtractingDataWithRegularExpressions/actualData.txt'

content = open(actualData)

totalSum = 0
totalValues = 0

for line in content:
    line = line.rstrip()
    # print(line)
    nums = re.findall('[0-9]+', line)
    totalValues = totalValues + len(nums)
    
    for number in nums:
        totalSum = totalSum + int(number)

print(totalValues)
print(totalSum)
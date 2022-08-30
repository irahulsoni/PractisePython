import pandas as pd


#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#
def calcMissing(readings):
    # Write your code here
    myList = []
    missingIndex = []
    for i in range(len(readings)):
        l = readings[i].split('\t')
        if (l[1].startswith("Missing")):
            l[1] = float("NAN")
            missingIndex.append(i)
        myList.append(l)

    df = pd.DataFrame(myList, columns=['Date', 'Values'])
    df['Values'] = pd.to_numeric(df['Values'])
    df['Values'] = df['Values'].interpolate()
    for mi in missingIndex:
        print(df.loc[mi]['Values'])


if __name__ == '__main__':
    readings_count = int(input().strip())
    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)

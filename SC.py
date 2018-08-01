import csv

with open('spam.csv','r') as EmailData:
    OrganisedData = list(csv.reader(EmailData))

def RemoveDuplicate(Message):
    BlankList = []
    for Word in Message:
        if len(Word) > 1:
            SplittedSentence = Word.split()
        else:
            SplittedSentence = Word

        for SingleWord in SplittedSentence:
            if SingleWord not in BlankList:
                BlankList.append(SingleWord)

    return BlankList
#print(OrganisedData)
WordsWithoutRepeat = []
for i in range(1,len(OrganisedData)):
    WordsWithoutRepeat.append(RemoveDuplicate(OrganisedData[i][1:len(OrganisedData[i])]))

WordVector = []

for SplittedMessage in WordsWithoutRepeat:
    for Word in SplittedMessage:
        if Word not in WordVector:
            WordVector.append(Word)

def WordCount(Word):
    Counter = 0
    for SplittedMessage in WordsWithoutRepeat:
        if Word in SplittedMessage:
            Counter += 1

    return Word, Counter

BagOfWords = {}
for Word in WordVector:
    Key, Value = WordCount(Word)
    BagOfWords[Key] = Value

BlanList = []
BlanList = BagOfWords.values()


slist=[]
hlist=[]
for i in range(1,5573):

    if OrganisedData[i][0] == "ham":
        hlist.append(OrganisedData[i])
    else:
        slist.append(OrganisedData[i])

#Trainig Data For Classifer
Trainig_Ham_Data = hlist[0:4775]
Trainig_Spam_Data = slist[0:697]


Len_Trainig_Data = len(Trainig_Ham_Data) + len(Trainig_Spam_Data)

P_Cap = []
for i in range(0,len(BlanList)):
    ans = BlanList[i] / float(Len_Trainig_Data)
    P_Cap.append(ans)

print (P_Cap)

#conditional probablity



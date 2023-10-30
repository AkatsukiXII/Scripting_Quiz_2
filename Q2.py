def score(ID,name,litScore,mathScore,compScore):
    average = round((litScore+mathScore+compScore)/3,2)
    total = round(litScore+mathScore+compScore,2)
    if average >= 60:
        passTmp = "合格"
    elif average < 60:
        passTmp = "不合格"
    print("------------------------------------------------")
    print("{}({})同學您好:\n以下是您的各科成績與分數判定\n".format(name,ID))
    print("\n")
    print("國文 : {} / 數學 : {} / 電腦 : {}".format(litScore,mathScore,compScore))
    print("總分 : {} / 平均 : {}".format(total,average))
    print("------------------------------------------------")
    print("成績判定 : {}".format(passTmp))

if __name__ =='__main__':
    ID = input("請輸入您的學號 : ")
    name = input("請輸入您的姓名 : ")
    litScore = input("請輸入您的國文成績 : ")
    mathScore = input("請輸入您的數學成績 : ")
    compScore = input("請輸入您的電腦成績 : ")
    scoreDict = {}
    scoreDict["sid"] = ID
    scoreDict["sname"] = name
    scoreDict["fchina"] = round(float(litScore),2)
    scoreDict["fmath"] = round(float(mathScore),2)
    scoreDict["finfo"] = round(float(compScore),2)
    print(scoreDict)
    score(scoreDict["sid"],scoreDict["sname"],scoreDict["fchina"],scoreDict["fmath"],scoreDict["finfo"])
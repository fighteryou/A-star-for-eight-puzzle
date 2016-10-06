#coding=utf-8
import copy

def init(target):
    tlist = [0 for a in range(9)]
    for i in range(3):
        for j in range(3):
            tlist[target[i][j]]=[i,j]
    return tlist

def getStep(tlist,current):
    step = 0
    for i in range(3):
        for j in range(3):
            if current[i][j]!=0:
                k = tlist[current[i][j]]
                step = step + abs(k[0]-i) + abs(k[1]-j)
    return step

def inTable(item,table):
    it = item[2]
    for t in table:
        t2 = t[2]
        if t2==it:
            return True
    return False

def roop(tlist,item,target):
    opened = []
    closed = []
    opened.append(item)
    #print "roop----opened: ",opened,"\n","closed",closed
    while len(opened):
        current = opened[0]
        del opened[0]
        closed.append(current)
        if current[2] == target:
            return closed

        cur1 = copy.deepcopy(current)

        for i in range(3):
            for j in range(3):
                if cur1[2][i][j]==0 and i!=0:
                    temp = cur1[2][i-1][j]
                    cur1[2][i-1][j] = cur1[2][i][j]
                    cur1[2][i][j] = temp
                    break
        if cur1 != current:
            son1 = [current[0]+1,getStep(tlist,cur1[2]),cur1[2],len(closed)-1]
            if not inTable(son1,closed):
                if not inTable(son1,opened):
                    if len(opened)==0:
                        opened.append(son1)
                    else:
                        for i in range(len(opened)):
                            if opened[i][1] > son1[1]:
                                opened.insert(i,son1)
                                break
                            elif i == len(opened)-1:
                                opened.append(son1)
                                break
                else:
                    for i in range(len(opened)-1):
                        if opened[i][2]==son1[2]:
                            if opened[i][0] > son1[0]:
                                opened[i] = son1
                                break
        cur2 = copy.deepcopy(current)
        for i in range(3):
            for j in range(3):
                if cur2[2][i][j]==0 and i!=2:
                    temp = cur2[2][i+1][j]
                    cur2[2][i+1][j] = cur2[2][i][j]
                    cur2[2][i][j] = temp
                    break
        if cur2 != current:
            son2 = [current[0]+1,getStep(tlist,cur2[2]),cur2[2],len(closed)-1]
            if not inTable(son2,closed):
                if not inTable(son2,opened):
                    if len(opened)==0:
                        opened.append(son2)
                    else:
                        for i in range(len(opened)):
                            if opened[i][1] > son2[1]:
                                opened.insert(i,son2)
                                break
                            elif i == len(opened)-1:
                                opened.append(son2)
                                break
                else:
                    for i in range(len(opened)-1):
                        if opened[i][2]==son2[2]:
                            if opened[i][0] > son2[0]:
                                opened[i] = son2
                                break
        cur3 =  copy.deepcopy(current)
        for i in range(3):
            for j in range(3):
                if cur3[2][i][j]==0 and j!=0:
                    temp = cur3[2][i][j-1]
                    cur3[2][i][j-1] = cur3[2][i][j]
                    cur3[2][i][j] = temp
                    break
        if cur3 != current:
            son3 = [current[0]+1,getStep(tlist,cur3[2]),cur3[2],len(closed)-1]
            if not inTable(son3,closed):
                if not inTable(son3,opened):
                    if len(opened)==0:
                        opened.append(son3)
                    else:
                        for i in range(len(opened)):
                            if opened[i][1] > son3[1]:
                                opened.insert(i,son3)
                                break
                            elif i == len(opened)-1:
                                opened.append(son3)
                                break
                else:
                    for i in range(len(opened)-1):
                        if opened[i][2]==son3[2]:
                            if opened[i][0] > son3[0]:
                                opened[i] = son3
                                break
        cur4 =  copy.deepcopy(current)
        for i in range(3):
            for j in range(3):
                if cur4[2][i][j]==0 and j!=2:
                    temp = cur4[2][i][j+1]
                    cur4[2][i][j+1] = cur4[2][i][j]
                    cur4[2][i][j] = temp
                    break
        if cur4 != current:
            son4 = [current[0]+1,getStep(tlist,cur4[2]),cur4[2],len(closed)-1]
            if not inTable(son4,closed):
                if not inTable(son4,opened):
                    if len(opened)==0:
                        opened.append(son4)
                    else:
                        for i in range(len(opened)):
                            if opened[i][1] > son4[1]:
                                opened.insert(i,son4)
                                break
                            elif i == len(opened)-1:
                                opened.append(son4)
                                break
                else:
                    for i in range(len(opened)-1):
                        if opened[i][2]==son4[2]:
                            if opened[i][0] > son4[0]:
                                opened[i] = son4
                                break


    
if __name__=="__main__":
    target = [[1,2,3],[8,0,4],[7,6,5]]
    start = [[2,8,3],[4,1,6],[7,0,5]]#[ [0 for a in range(3)] for b in range(3)]
    tlist = init(target)
    #item = [layer:int,step:int,self:[3:3],father:int]
    item = [0,getStep(tlist,start),start,-1]#-1 not father

    closed = roop(tlist,item,target)

    for c in closed:
        print("layer: ",c[0],"step: ",c[1],"father: ",c[3])
        for i in c[2]:
            print (i)
        print ("\n")

    print("done!")
    

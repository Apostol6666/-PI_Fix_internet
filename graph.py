def count_alone(tops):
    help_mass = []
    k=0
    for i in range (1, N+1):
        help_mass.append(0)
    
    for keys in tops:
        for key in keys:
            help_mass[key-1]=1
    
    for el in help_mass:
        if not el:
            k+=1
    return k
        
def topsToTops2(tops):
    tops2 = {}
    for i in range(1, N+1):
        tops2[i] = []
        for edge in tops: 
            if edge[0]==i:
                tops2[i].append(edge[1])
                
    tops2 = getGroups(tops2)
    return tops2

def getNeirbour(t2):
    for key in range (1, N+1):
        for key_value in t2[key]:
            for el in t2[key_value]:
                t2[key].append(el)
                t2[key_value] = []   
    return t2

def getNeirbour2(t2):
    for key in range (1, N+1):
        for key2 in range (key+1, N+1):
            if t2[key]==t2[key2] and t2[key]:
                t2[key].append(key2)
                t2[key2] = []
    t2 = getNeirbour(t2)
    return t2

def getGroups(tops2):
    tops2 = getNeirbour2(tops2) 
    return tops2

def countGroups(t2):
    k=0
    for el in t2:
        if t2[el]:
            k+=1
    return k

N = int(input("Write the number of vertices"))
tops = [1, 2], [2, 8], [4, 10], [5, 9], [6, 10], [7, 9]
tops2 = {}

count = count_alone(tops)
tops2 = topsToTops2(tops)  
tops2 = getGroups(tops2)            

count += countGroups(tops2) - 1

print('The number of vertices = ', N)
print('Set of graph edges = ', tops)
print('RESULT = ', count) 

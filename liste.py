def echange(liste):
  var=liste[0]
  liste[0]=liste[len(liste)-1]
  liste[len(liste)-1]=var

 #print(echange([4,8,9,1]))

def selectMin(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var
    

def triSelect (list):
    result=[]
    while len(list)>0:
        var=selectMin(list)
        """
        A compléter
        """
    return result

#print(selectMin([4,2,7,8]))
#print(triSelect([4,2,7,8]))

def triFusion(list):
        if len(list)>0:
            """
            A compléter
            list0= partie gauche de la liste
            list1= partie droite de la liste
            
            list0Trie = triFusion(list0)
            list1Trie = triFusion(list1)
            return fusion (list0Trie,list1Trie)
            """
        else :
            return list    
    
def fusion(list):
    """
    A compléter
    """
    return list


  

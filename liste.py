def echange(liste):
  var=liste[0]
  liste[0]=liste[len(liste)-1]
  liste[len(liste)-1]=var

  print(echange([4,8,9,1]))

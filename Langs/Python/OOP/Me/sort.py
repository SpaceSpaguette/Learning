class Sorting: # definice třídy Sorting
  
  def __init__(self):
    # inicializace instanční vlastnosti cisla, prázdný list
    self.cisla = []
    # inicializace instanční vlastnosti smer na implicitní hodnotu řazení
    self.smer = "vzestupne" 
    
   # definice metody pro reřazení hodnot listu v zadaném směru
  def serad(self, seznam_cisel, smer = "vzestupne"):
    self.cisla = seznam_cisel
    if (smer == "vzestupne"):
      self.cisla.sort()
    elif (smer == "sestupne"):
      self.cisla.sort(reverse = True)
      
  def __str__(self):
    return str(self.cisla)



x = Sorting()
x.serad([5, 3, 7, 1, 9, 4, 2, 8, 6], "sestupne")
print(x)
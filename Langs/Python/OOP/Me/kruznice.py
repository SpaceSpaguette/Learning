class kruznice:
  def __init__ (self,d):
    self.d = d if d > 0 else print("Nejde")

  def obsah(self):
    return round((3.14 * (self.d ** 2)) / 4, 2)

  def obvod(self):
    return round(3.14 * self.d, 2)

  def __str__ (self):
    return f"Kružnice o průměru {self.d} má obvod {self.obvod()} a obsah {self.obsah()}"


#Test
a = kruznice(10)
print(a.obsah())
print(a.obvod())
print(a)
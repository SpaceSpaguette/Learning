class Tree:
    def __init__(self, decorations=None):
        self.decorations = decorations
        self.tree = [[], [], []]

    def place_decoration(self,kde,pocet, barva, ozdoby):
        existuje = False
        for i in self.tree[kde]:
            if i[1] == barva and i[2] == ozdoby:
                i[0] += pocet
                existuje = True
                print("Existuje. pridam je tam")
                break
        if not existuje:
            self.tree[kde].append([pocet, barva, ozdoby])

    def __str__(self):
        return str(self.tree)


my_tree = Tree()
my_tree.place_decoration(1, 5, "zelena", "hvezda")
my_tree.place_decoration(1, 5, "zelena", "hvezda")
my_tree.place_decoration(0, 2, "modra", "koule")
print(my_tree)


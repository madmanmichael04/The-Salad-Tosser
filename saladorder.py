from breezypythongui import EasyFrame
entries = []
class Ingredients(EasyFrame):
   
    def __init__(self):
        EasyFrame.__init__(self, title = "Customize your order")

        self.addLabel(text = "Veggies", row = 0, column = 0, columnspan = 2)

        self.addLabel(text = "Romaine Lettuce", row = 1, column = 0)
        self.addButton(text = "Add", row = 1, column = 1,
                       command = self.addRomaine)
        self.addButton(text = "Remove", row = 1, column = 2,
                       command = self.removeRomaine)

        self.addLabel(text = "Spinach", row = 2, column = 0)
        self.addButton(text = "Add", row = 2, column = 1,
                       command = self.addSpinach)
        self.addButton(text = "Remove", row = 2, column = 2,
                       command = self.removeSpinach)

        self.addLabel(text = "Celery", row = 3, column = 0)
        self.addButton(text = "Add", row = 3, column = 1,
                       command = self.addCelery)
        self.addButton(text = "Remove", row = 3, column = 2,
                       command = self.removeCelery)

        self.addLabel(text = "Broccoli", row = 4, column = 0)
        self.addButton(text = "Add", row = 4, column = 1,
                       command = self.addBroccoli)
        self.addButton(text = "Remove", row = 4, column = 2,
                       command = self.removeBroccoli)

        self.addLabel(text = "Cucumbers", row = 5, column = 0)
        self.addButton(text = "Add", row = 5, column = 1,
                       command = self.addCucumbers)
        self.addButton(text = "Remove", row = 5, column = 2,
                       command = self.removeCucumbers)

        self.addLabel(text = "Tomatoes", row = 6, column = 0)
        self.addButton(text = "Add", row = 6, column = 1,
                       command = self.addTomatoes)
        self.addButton(text = "Remove", row = 6, column = 2,
                       command = self.removeTomatoes)

        self.addLabel(text = "Protien", row = 8, column = 0, columnspan = 2)

        self.addLabel(text = "Grilled Chicken", row = 9, column = 0)
        self.addButton(text = "Add", row = 9, column = 1,
                       command = self.addChicken)
        self.addButton(text = "Remove", row = 9, column = 2,
                       command = self.removeChicken)

        self.addLabel(text = "Turkey", row = 10, column = 0)
        self.addButton(text = "Add", row = 10, column = 1,
                       command = self.addTurkey)
        self.addButton(text = "Remove", row = 10, column = 2,
                       command = self.removeTurkey)

        self.addLabel(text = "Chickpeas", row = 11, column = 0)
        self.addButton(text = "Add", row = 11, column = 1,
                       command = self.addChickpeas)
        self.addButton(text = "Remove", row = 11, column = 2,
                       command = self.removeChickpeas)

        self.addLabel(text = "Dressing", row = 13, column = 0, columnspan = 2)

        self.addLabel(text = "Ranch", row = 14, column = 0)
        self.addButton(text = "Add", row = 14, column = 1,
                       command = self.addRanch)
        self.addButton(text = "Remove", row = 14, column = 2,
                       command = self.removeRanch)

        self.addLabel(text = "Thousand Island", row = 15, column = 0)
        self.addButton(text = "Add", row = 15, column = 1,
                       command = self.addIsland)
        self.addButton(text = "Remove", row = 15, column = 2,
                       command = self.removeIsland)

        self.addLabel(text = "Balsamic Vinaigrette", row = 16, column = 0)
        self.addButton(text = "Add", row = 16, column = 1,
                       command = self.addBalsamic)
        self.addButton(text = "Remove", row = 16, column = 2,
                       command = self.removeBalsamic)

        self.addLabel(text = "Caesar", row = 17, column = 0)
        self.addButton(text = "Add", row = 17, column = 1,
                       command = self.addCaesar)
        self.addButton(text = "Remove", row = 17, column = 2,
                       command = self.removeCaesar)

        self.addButton(text = "Confirm Order", row = 18, column = 0,
                       columnspan = 2, command = self.confirm)
        
        self.addLabel(text = "Your Order:", row = 19, column = 0)
        self.ingredientList = self.addTextField(text = "", row = 19, column = 1, columnspan = 10)

    def addRomaine(self):
        entries.append("Romaine Lettuce, ")

    def removeRomaine(self):
        entries.remove("Romaine Lettuce, ")

    def addSpinach(self):
        entries.append("Spinach, ")

    def removeSpinach(self):
        entries.remove("Spinach, ")

    def addCelery(self):
        entries.append("Celery, ")

    def removeCelery(self):
        entries.remove("Celery, ")

    def addBroccoli(self):
        entries.append("Broccoli, ")

    def removeBroccoli(self):
        entries.remove("Broccoli, ")

    def addCucumbers(self):
        entries.append("Cucumbers, ")

    def removeCucumbers(self):
        entries.remove("Cucumbers, ")

    def addTomatoes(self):
        entries.append("Tomatoes, ")

    def removeTomatoes(self):
        entries.remove("Tomatoes, ")

    def addChicken(self):
        entries.append("Chicken, ")

    def removeChicken(self):
        entries.remove("Chicken, ")

    def addTurkey(self):
        entries.append("Turkey, ")

    def removeTurkey(self):
        entries.remove("Turkey, ")

    def addChickpeas(self):
        entries.append("Chickpeas, ")

    def removeChickpeas(self):
        entries.remove("Chickpeas, ")

    def addRanch(self):
        entries.append("Ranch Dressing, ")

    def removeRanch(self):
        entries.remove("Ranch Dressing, ")

    def addIsland(self):
        entries.append("Thousand Island Dressing, ")

    def removeIsland(self):
        entries.remove("Thousand Island Dressing, ")

    def addBalsamic(self):
        entries.append("Balsamic Vinaigrette, ")

    def removeBalsamic(self):
        entries.remove("Balsamic Vinaigrette, ")

    def addCaesar(self):
        entries.append("Caesar Dressing, ")

    def removeCaesar(self):
        entries.remove("Caesar Dressing, ")

    def confirm(self):
        self.ingredientList.setText(entries)


Ingredients().mainloop()

        

        

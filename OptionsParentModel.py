class OptionsParentModel:
  def __init__(self, partName, mainValues, currentSelection, allowsFurtherSelection):
    self.partName = partName
    self.mainValues = mainValues
    self.currentSelection = currentSelection
    self.allowsFurtherSelection = allowsFurtherSelection

  def printname(self):
    print(self.firstname, self.lastname)
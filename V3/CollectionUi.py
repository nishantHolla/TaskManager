from PyQt5.uic import loadUi

class CollectionUi:
    def addCollection(self, parent):
        parent.collectionList.addItem(parent.collectionLineEdit.text())

    def deleteCollection(self, parent):
        current_item = parent.collectionList.currentItem()
        if not current_item: return
        parent.collectionList.takeItem(parent.collectionList.row(current_item))

    def viewCollection(self, parent):
        parent.showWindow('task')

    def hide(self, parent):
        parent.showWindow('login')

    def show(self, parent):
        loadUi('./QtCollection.ui', parent)

        parent.collectionAddButton.clicked.connect(lambda : self.addCollection(parent))
        parent.collectionDeleteButton.clicked.connect(lambda : self.deleteCollection(parent))
        parent.collectionViewButton.clicked.connect(lambda : self.viewCollection(parent))
        parent.collectionBackButton.clicked.connect(lambda : self.hide(parent))

collectionUi = CollectionUi()

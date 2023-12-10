from PyQt5.uic import loadUi

class CollectionUi:
    def addCollection(self, parent):
        collectionName = parent.collectionLineEdit.text()
        parent.todoManager.new_collection(collectionName)
        parent.collectionList.addItem(collectionName)

    def deleteCollection(self, parent):
        current_item = parent.collectionList.currentItem()
        if not current_item: return

        item_index = parent.collectionList.row(current_item)
        parent.todoManager.remove_collection(item_index)
        parent.collectionList.takeItem(item_index)

    def viewCollection(self, parent):
        current_item = parent.collectionList.currentItem()
        if not current_item: return

        item_index = parent.collectionList.row(current_item)
        parent.collectionIndex = item_index
        parent.showWindow('task')

    def logout(self, parent):
        parent.sessionManager.end_session()
        parent.user = None
        parent.showWindow('login')

    def show(self, parent):
        loadUi('./QtCollection.ui', parent)

        parent.collectionAddButton.clicked.connect(lambda : self.addCollection(parent))
        parent.collectionDeleteButton.clicked.connect(lambda : self.deleteCollection(parent))
        parent.collectionViewButton.clicked.connect(lambda : self.viewCollection(parent))
        parent.collectionBackButton.clicked.connect(lambda : self.logout(parent))

        collections = parent.todoManager.get_collections()
        for collection in collections:
            parent.collectionList.addItem(collection['name'])

collectionUi = CollectionUi()

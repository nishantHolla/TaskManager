from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

class CollectionUi:
    def addCollection(self, parent):
        collectionName = parent.collectionsLineEdit.text()
        parent.todoManager.new_collection(collectionName)
        parent.collectionsList.addItem(collectionName)
        parent.collectionsLineEdit.setText('')
        parent.setError()

    def deleteCollection(self, parent):
        current_item = parent.collectionsList.currentItem()
        if not current_item:
            parent.setError('Select a collection before deletion.')
            return

        item_index = parent.collectionsList.row(current_item)
        parent.todoManager.remove_collection(item_index)
        parent.collectionsList.takeItem(item_index)
        parent.setError()

    def viewCollection(self, parent):
        current_item = parent.collectionsList.currentItem()
        if not current_item:
            parent.setError('Select the collection to view.')
            return

        item_index = parent.collectionsList.row(current_item)
        parent.collectionIndex = item_index
        parent.showWindow('task')
        parent.setError()

    def logout(self, parent):
        parent.sessionManager.end_session()
        parent.user = None
        parent.showWindow('login')

    def show(self, parent):
        loadUi('./layouts/collections.ui', parent)

        parent.collectionsBackButton.setIcon(QIcon('./resources/back.png'))
        parent.collectionsAccountButton.setIcon(QIcon('./resources/account.png'))
        parent.collectionsAccountButton.setText(parent.user)

        parent.collectionsAccountButton.clicked.connect(lambda : parent.showWindow('account'))
        parent.collectionsBackButton.clicked.connect(lambda : self.logout(parent))
        parent.collectionsAddButton.clicked.connect(lambda : self.addCollection(parent))
        parent.collectionsDeleteButton.clicked.connect(lambda : self.deleteCollection(parent))
        parent.collectionsViewButton.clicked.connect(lambda : self.viewCollection(parent))

        collections = parent.todoManager.get_collections()
        for collection in collections:
            parent.collectionsList.addItem(collection['name'])
        parent.setError()

collectionUi = CollectionUi()

from todoManager import TodoManager
import datetime

tm = TodoManager("./users/user1.json")
tm.debugPrint()

print("Adding a new collection ...")
tm.new_collection("Collection 1")
tm.debugPrint()
tm.write_DB()
print()

print("Adding a new collection ...")
tm.new_collection("Collection 2")
tm.debugPrint()
tm.write_DB()
print()

print("Adding a new collection ...")
tm.new_collection("Collection 3")
tm.debugPrint()
tm.write_DB()
print()

print("Renaming collection ...")
tm.update_collection(0, "Collection 0")
tm.debugPrint()
tm.write_DB()
print()

print("Deleting collection ...")
tm.remove_collection(2)
tm.debugPrint()
tm.write_DB()
print()

print("Adding a new todo ... ")
tm.new_todo(
    0,
    "New todo",
    "New todo message",
    datetime.datetime.now() + datetime.timedelta(1),
    False,
)
tm.debugPrint()
tm.write_DB()
print()

tm.new_todo(
    0,
    "New todo",
    "New todo message",
)

print("Getting todos ... ")
print(tm.get_todos(1))
tm.write_DB()
print()

print("Getting todo ... ")
print(tm.get_todo(0, -1))
tm.write_DB()
print()

print("Updating todo ...")
tm.update_todo(0, -1, "Todo 4", "message 4", True)
tm.debugPrint()
tm.write_DB()
print()

print("Removing todo ...")
tm.remove_todo(0, -1)
tm.debugPrint()
tm.write_DB()
print()

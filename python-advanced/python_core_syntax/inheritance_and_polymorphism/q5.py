class Wax:
    def melt(self):
        print("wax can be used to form a tool")

class Cheese:
    def melt(self):
        print("Cheese can be eaten")

class Wood:
    def fire(self):
        print("A fire has been started")


for element in Wax(), Cheese(), Wood():
    try:
        element.melt()
    except AttributeError:
        print("No melt() method found")
        
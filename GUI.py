from tkinter import *
from mapFunctions import *
def but():
    name = MapQuest('wQ3sH7PEvqUujVMa7ZsvnmUCLyILr77a')
    name.pointOfInterest(LocationEntry.get(), KeywordEntry.get(), values.get())

window = Tk()
window.title('Lab4_57232669 GUI')
window.geometry('900x200')
location = Label(window, text = 'Location:')
keyword = Label(window, text = 'Keyword:')
NumResults = Label(window, text = 'Number of results:')
mylist = [1, 2, 3, 4, 5]
values = StringVar()
values.set('1')
dropdown = OptionMenu(window, values, *mylist)
search = Button(window, text = 'search', command = but)
LocationEntry = Entry(window)
KeywordEntry = Entry(window)
location.pack(side = LEFT)
LocationEntry.pack(side = LEFT)
keyword.pack(side = LEFT)
KeywordEntry.pack(side = LEFT)
NumResults.pack(side = LEFT)
dropdown.pack(side = LEFT)
search.pack(side = LEFT)
mainloop()



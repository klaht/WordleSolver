import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):

        #setting title
        root.title("WordleSolver")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.line = tk.Entry(root)
        self.listIndex = 0
        self.charList = [[""]*5 for i in range(5)]

        self.buttonsList = [[""]*5 for i in range(6)]

        self.currentWord = ""

        variableX = 175
        variableY = 90

        #create 30 buttons and insert them in 2d array
        for i in range(6):
            for a in range(5):
                button = tk.Button(root)
                self.buttonsList[i][a] = button
                button["text"] = ""
                button["command"] = lambda button=button: self.setColor(button)
                button["bg"]='grey'

                button.place(x=variableX+30,y=variableY+30,width=30,height=30)
                variableX += 40
            variableX = 175
            variableY += 40

        self.wordList = tk.Listbox(root)
        self.wordList.place(x=410,y=120,width=150,height=300)

        file1 = open("wordsFile", 'r')
        self.words = file1.readlines()
        file1.close()

        inputButton = tk.Button(root)
        inputButton["text"] = "Add"
        inputButton["command"] = self.getInputWord
        inputButton["bg"] = 'grey'
        inputButton.place(x=365,y=80,width=30,height=30)

        reloadButton = tk.Button(root)
        reloadButton["text"] = "Reload words"
        reloadButton["command"] = self.reloadWords
        reloadButton["bg"] = 'grey'
        reloadButton.place(x=410,y=80,width=150,height=30)

        resetButton = tk.Button(root)
        resetButton["text"] = "Reset game"
        resetButton["command"] = self.reset
        resetButton["bg"] = 'grey'
        resetButton.place(x=410, y=430, width=150, height=30)

        label = tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        label["font"] = ft
        label["justify"] = "center"
        label["text"] = "WORDLE SOLVER"
        label.place(x=235,y=30,width=130,height=33)

        self.line["borderwidth"] = "1px"
        self.line["text"] = "Entry"
        self.line.place(x=245,y=80,width=110,height=30)

    def getInputWord(self):
        inputString = self.line.get()

        i = 0
        if len(inputString) != 5:
            print("invalid word length")
        else:
            for char in inputString:
                if (char.isalpha()):
                    self.buttonsList[self.listIndex][i]["text"] = char
                    i+=1
                else:
                    print("invalid input")
                    return 0
            self.currentWord = inputString
            self.listIndex += 1

    def setColor(self, button):
        color = button["bg"]
        if color == 'grey':
            button["bg"] = 'yellow'
        elif color == 'yellow':
            button["bg"] = 'green'
        else:
            button["bg"] = 'grey'


    def reloadWords(self):

        tempList = self.buttonsList
        currentChar = ""

        correctList = []

        for c in range(len(self.words)):
            self.words[c] = self.words[c].strip()

        for i in range(5):
            currentChar = tempList[self.listIndex-1][i]["text"]

            if tempList[self.listIndex-1][i]["bg"] == 'green':

                for index in range(len(self.words)):
                    word = self.words[index]
                    if (word[i] == currentChar):
                        correctList.append(word)
                self.words.clear()
                self.words = correctList.copy()
                correctList.clear()
            elif tempList[self.listIndex-1][i]["bg"] == 'yellow':
                for index in range(len(self.words)):
                    word = self.words[index]
                    if ((currentChar in word) and (word[i] != currentChar)):
                        correctList.append(word)
                self.words.clear()
                self.words = correctList.copy()
                correctList.clear()
            else:
                for index in range(len(self.words)):
                    word = self.words[index]
                    if currentChar not in word:
                        correctList.append(word)
                self.words.clear()
                self.words = correctList.copy()

                correctList.clear()


        listIndex = 0


        self.wordList.delete(0, 'end')

        for i in self.words:
            self.wordList.insert(listIndex, i)
            listIndex += 1

    def reset(self):
        self.words.clear()
        for i in range(6):
            for a in range(5):
                self.buttonsList[i][a]["bg"]='grey'
                self.buttonsList[i][a]["text"]=""

        self.listIndex = 0

        self.wordList.delete(0, 'end')

        file1 = open("wordsFile", 'r')
        self.words = file1.readlines()
        file1.close()







if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


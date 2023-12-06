import PySimpleGUI as sg
import time

expression = ""

def press(num):
    global expression

    expression = expression + str(num)

    
def equalpress():
    try:
        global expression

        total = str(eval(expression))
        
        expression = total

    except:
        expression = "error"

def clear():
    global expression 
    expression = ""
    

def main():

    global expression

    logwindow = sg.Multiline(size=(10 , 1), key="display")
    layout = [[sg.Text("Calculator")], 
              [logwindow],
              [sg.Button("9"), sg.Button("8"), sg.Button("7"), sg.Button("/")],
              [sg.Button("6"), sg.Button("5"), sg.Button("4"), sg.Button("*")],
              [sg.Button("3"), sg.Button("2"), sg.Button("1"), sg.Button("-")],
              [sg.Button("0"), sg.Button("+"), sg.Button("=")],
              [sg.Button("close"), sg.Button("clear")],
              ]

    #create window

    window = sg.Window("My Calculator", layout)

    #create event loop

    while True: 
        event, values = window.read()
        if event == "close" or event == sg.WIN_CLOSED:
            break
        if event == "9":
            press("9")
        if event == "8":
            press("8")
        if event == "7":
            press("7")
        if event == "6":
            press("6")
        if event == "5":
            press("5")
        if event == "4":
            press("4")
        if event == "3":
            press("3")
        if event == "2":
            press("2")
        if event == "1":
            press("1")
        if event == "0":
            press("0")
        if event == "/":
            press("/")
        if event == "*":
            press("*")
        if event == "-":
            press("-")
        if event == "+":
            press("+")
        if event == "=":
            equalpress()
        if event == "clear":
            clear()
            
        window["display"].Update(expression)
        


    window.close()






    

if __name__ == "__main__":
    main()
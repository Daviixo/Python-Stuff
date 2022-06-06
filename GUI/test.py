import PySimpleGUI as sg

# This is just a test
# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

layout = [[sg.Text("This is just a test")], [sg.Button("OK")]]

# We will now create a window

window = sg.Window("Test", layout)

# Now, lets create our event loop

while True:
    event, values = window.read()
    #Lets end the program if the user closes the window or presses ok
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
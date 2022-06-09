import PySimpleGUI as sg

layout = [[sg.Text("SafeEntry Check In")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Safe Entry", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
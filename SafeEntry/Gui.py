import PySimpleGUI as sg

#Check in out tab
checkin_layout = [[
    sg.Text("SafeEntry Check In")], 
    [sg.Radio('Koufu', 'place', default=True) ,
           sg.Radio('Foodgle', 'place')
           ,sg.Radio('South Canteen', 'place')
           ,sg.Radio('North Canteen', 'place')],
    [sg.Button("Checkin")], 
    [sg.Button("Checkout")]
    ]

#History tab
history_layout = [[sg.Text('History', background_color='tan1')],
               [sg.Input(key='-in2-')]]

#Notification tab
notification_layout = [[sg.Text('Notification', background_color='tan1')],
               [sg.Input(key='-in2-')]]


# tab group
tab_layout = [[sg.TabGroup([[
    sg.Tab('Check In', checkin_layout), 
    sg.Tab('History', history_layout),
    sg.Tab('Notification', notification_layout)]])]]




# Create the window
window = sg.Window("Safe Entry", tab_layout)

# Create an event loop
while True:
    event, values = window.read()
    print(values)

    # End program if user closes window 
    if event == sg.WIN_CLOSED:
        break

    if event == "Checkin":
        print("checkin")
    if event == "Checkout":
        print("checkout")
    
# window.close()
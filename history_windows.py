import PySimpleGUI as sg

def create(histories):

    history_layout = [
        [sg.Text("History")],
                        [sg.Table(values=histories,
                                    headings=['name', 'nric', 'location', 'checkin_dt','checkout_dt'],
                                    auto_size_columns=True,
                                    num_rows=len(histories),
                                    row_height=35,
                                    justification='right',
                                    key='-HISTORY_TABLE-')]
    ]

    window = sg.Window("Safe Entry", history_layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break


    window.close()
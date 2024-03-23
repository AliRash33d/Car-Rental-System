import PySimpleGUI as sg

#Below details of the 1st car is stored in these variables for their use in functions.
car1 = "Kia Sportage"
car1_a = 3
car1_pd = 6000
car1_l = 250
car1_id = 500

#Below details of the 2nd car is stored in these variables for their use in functions.
car2 = "Toyota Grande"
car2_a = 6
car2_pd = 5500
car2_l = 229
car2_id = 448

#Below details of the 3rd car is stored in these variables for their use in functions.
car3 = "Honda Civic"
car3_a = 5
car3_pd = 5500
car3_l = 229
car3_id = 448

g_rentcost = 0
g_insurance_cost = 0
g_total_tax = 0

def car_rent():
    global car1, car2, car3
    global car1_a, car2_a, car3_a
    global car1_pd, car2_pd, car3_pd
    global car1_l, car2_l, car3_l
    global car1_id, car2_id, car3_id
    global g_rentcost, g_insurance_cost, g_total_tax
    layout = [
        [sg.Text("Car Rental", size=(20, 1), font=("Helvetica", 25))],
        [sg.Text("Choose a car to rent:", size=(20, 1), font=("Helvetica", 15))],
        [[sg.Table(values=[
                      ["1",car1, car1_a, car1_pd, car1_l, car1_id],
                      ["2",car2, car2_a, car2_pd, car2_l, car2_id],
                      ["3",car3, car3_a, car3_pd, car3_l, car3_id]],
                      headings=['S.no','Car Model', 'Available', 'Price/Day', 'Liability Insurance/Day', 'Full Insurance/Day'],
                      auto_size_columns=True, justification='center', num_rows=4)]],
        [sg.Text("Enter Car Model:", size= (15,1), font=("Helvetica", 15))],
        [sg.Input(key = "Select_Car", size=(40,1), font=("Helvetica", 15))],
        [sg.Text("Enter Number of Days:", font=("Helvetica", 15))],
        [sg.Input(key = "days", size=(40,1), font=("Helvetica", 15))],
        [sg.Text("Insurance Type:", size= (15,1), font=("Helvetica", 15))],
        [sg.Radio('Liability Insurance', 1, default=True), sg.Radio('Full Insurance', 1)],
        [sg.Button("Rent", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Back", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
    ]

    window = sg.Window("Car Rental", layout , size = (900,500))
    window.LayoutAndShow
    while True:
        event, values = window.read()
        select_car = values["Select_Car"]
        days = values["days"]
        numbers = "1,2,3,4,5,6,7,8,9,10"
        if any(char in numbers for char in days): # it is to ensure no other than numbers are given input in numbers of days, if given then rent button would not work.
            if event == "Rent":
                insurance = values.get(1) # insurance details are stored in this variable as True for Liability and False for Full Insurance.
                if select_car == "1":
                    window.hide()
                    if car1_a>0:
                        if insurance == True:
                            layout1 = [
                                [sg.Text(f"Car Model: {car1}", font=("Helvetica", 15))],
                                [sg.Text(f"Rent Cost: Pkr {car1_pd*int(days)}", font=("Helvetica", 15))],
                                [sg.Text(f"Insurance Cost: Pkr {car1_l}", font=("Helvetica", 15))],
                                [sg.Text(f"Tax 5% on Rent Cost: Pkr {(car1_pd*int(days))*0.05}", font=("Helvetica", 15))],
                                [sg.Text(f"Total Cost: Pkr {(car1_pd*int(days))+(car1_l)+((car1_pd*int(days))*0.05)}",font=("Helvetica", 15))],
                                [sg.Button("Confirm", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                            ]
                            window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                            window1.LayoutAndShow
                            while True:
                                event, values = window1.read()
                                if event == "Confirm":
                                    car1_a = car1_a - 1
                                    g_rentcost = (g_rentcost) + (car1_pd*int(days))
                                    g_insurance_cost = (g_insurance_cost) + (car1_l)
                                    g_total_tax = (g_total_tax) + ((car1_pd*int(days))*0.05)
                                    window1.hide()
                                    layout2 = [
                                        [sg.Text(f"You have rented Kia Sportage for {days} days.", font=("Helvetica", 15))],
                                        [sg.Button("Main Menu", size= (10,1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                                    ]
                                    window2 = sg.Window("TG Enterprises", layout2, size=(900,500))
                                    window2.LayoutAndShow
                                    while True:
                                        event, values = window2.read()
                                        if event == "Main Menu":
                                            window2.hide()
                                            main_menu()
                                        elif event == sg.WIN_CLOSED or event == "Exit":
                                            break
                                    window2.close()
                                elif event == "Back":
                                    window1.hide()
                                    car_rent()
                                elif event == sg.WIN_CLOSED or event == "Exit":
                                    break
                            window1.close()
                        else:
                            layout1 = [
                                [sg.Text(f"Car Model: {car1}", font=("Helvetica", 15))],
                                [sg.Text(f"Rent Cost: Pkr {car1_pd*int(days)}", font=("Helvetica", 15))],
                                [sg.Text(f"Insurance Cost: Pkr {car1_id}", font=("Helvetica", 15))],
                                [sg.Text(f"Tax 5% on Rent Cost: Pkr {(car1_pd*int(days))*0.05}", font=("Helvetica", 15))],
                                [sg.Text(f"Total Cost: Pkr {(car1_pd*int(days))+(car1_id)+((car1_pd*int(days))*0.05)}",font=("Helvetica", 15))],
                                [sg.Button("Confirm", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                            ]
                            window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                            window1.LayoutAndShow
                            while True:
                                event, values = window1.read()
                                if event == "Confirm":
                                    car1_a = car1_a - 1
                                    g_rentcost = (g_rentcost) + (car1_pd*int(days))
                                    g_insurance_cost = (g_insurance_cost) + (car1_id)
                                    g_total_tax = (g_total_tax) + ((car1_pd*int(days))*0.05)
                                    window1.hide()
                                    layout2 = [
                                        [sg.Text(f"You have rented Kia Sportage for {days} days.", font=("Helvetica", 15))],
                                        [sg.Button("Main Menu", size= (10,1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                                    ]
                                    window2 = sg.Window("TG Enterprises", layout2, size=(900,500))
                                    window2.LayoutAndShow
                                    while True:
                                        event, values = window2.read()
                                        if event == "Main Menu":
                                            window2.hide()
                                            main_menu()
                                        elif event == sg.WIN_CLOSED or event == "Exit":
                                            break
                                    window2.close()
                                elif event == "Back":
                                    window1.hide()
                                    car_rent()
                                elif event == sg.WIN_CLOSED or event == "Exit":
                                    break
                            window1.close()
                    else:
                        layout1 = [
                            [sg.Text("The Specific Car is not available", font=("Helvetica", 15))],
                            [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Back":
                                window1.hide()
                                car_rent()
                            elif event == sg.WIN_CLOSED or event == "Exit":
                                break
                        window1.close()
                elif select_car == "2":
                    window.hide()
                    if car2_a>0:
                        if insurance == True:
                            layout1 = [
                                [sg.Text(f"Car Model: {car2}", font=("Helvetica", 15))],
                                [sg.Text(f"Rent Cost: Pkr {car2_pd*int(days)}", font=("Helvetica", 15))],
                                [sg.Text(f"Insurance Cost: Pkr {car2_l}", font=("Helvetica", 15))],
                                [sg.Text(f"Tax 5% on Rent Cost: Pkr {(car2_pd*int(days))*0.05}", font=("Helvetica", 15))],
                                [sg.Text(f"Total Cost: Pkr {(car2_pd*int(days))+(car2_l)+((car2_pd*int(days))*0.05)}",font=("Helvetica", 15))],
                                [sg.Button("Confirm", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                            ]
                            window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                            window1.LayoutAndShow
                            while True:
                                event, values = window1.read()
                                if event == "Confirm":
                                    car2_a = car2_a - 1
                                    g_rentcost = (g_rentcost) + (car2_pd*int(days))
                                    g_insurance_cost = (g_insurance_cost) + (car2_l)
                                    g_total_tax = (g_total_tax) + ((car2_pd*int(days))*0.05)
                                    window1.hide()
                                    layout2 = [
                                        [sg.Text(f"You have rented Toyota Grande for {days} days.", font=("Helvetica", 15))],
                                        [sg.Button("Main Menu", size= (10,1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                                    ]
                                    window2 = sg.Window("TG Enterprises", layout2, size=(900,500))
                                    window2.LayoutAndShow
                                    while True:
                                        event, values = window2.read()
                                        if event == "Main Menu":
                                            window2.hide()
                                            main_menu()
                                        elif event == sg.WIN_CLOSED or event == "Exit":
                                            break
                                    window2.close()
                                elif event == "Back":
                                    window1.hide()
                                    car_rent()
                                elif event == sg.WIN_CLOSED or event == "Exit":
                                    break
                            window1.close()
                        else:
                            layout1 = [
                                [sg.Text(f"Car Model: {car2}", font=("Helvetica", 15))],
                                [sg.Text(f"Rent Cost: Pkr {car2_pd*int(days)}", font=("Helvetica", 15))],
                                [sg.Text(f"Insurance Cost: Pkr {car2_id}", font=("Helvetica", 15))],
                                [sg.Text(f"Tax 5% on Rent Cost: Pkr {(car2_pd*int(days))*0.05}", font=("Helvetica", 15))],
                                [sg.Text(f"Total Cost: Pkr {(car2_pd*int(days))+(car2_id)+((car2_pd*int(days))*0.05)}",font=("Helvetica", 15))],
                                [sg.Button("Confirm", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                            ]
                            window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                            window1.LayoutAndShow
                            while True:
                                event, values = window1.read()
                                if event == "Confirm":
                                    car2_a = car2_a - 1
                                    g_rentcost = (g_rentcost) + (car2_pd*int(days))
                                    g_insurance_cost = (g_insurance_cost) + (car2_id)
                                    g_total_tax = (g_total_tax) + ((car2_pd*int(days))*0.05)
                                    window1.hide()
                                    layout2 = [
                                        [sg.Text(f"You have rented Toyota Grande for {days} days.", font=("Helvetica", 15))],
                                        [sg.Button("Main Menu", size= (10,1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                                    ]
                                    window2 = sg.Window("TG Enterprises", layout2, size=(900,500))
                                    window2.LayoutAndShow
                                    while True:
                                        event, values = window2.read()
                                        if event == "Main Menu":
                                            window2.hide()
                                            main_menu()
                                        elif event == sg.WIN_CLOSED or event == "Exit":
                                            break
                                    window2.close()
                                elif event == "Back":
                                    window1.hide()
                                    car_rent()
                                elif event == sg.WIN_CLOSED or event == "Exit":
                                    break
                            window1.close()
                    else:
                        layout1 = [
                            [sg.Text("The Specific Car is not available", font=("Helvetica", 15))],
                            [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Back":
                                window1.hide()
                                car_rent()
                            elif event == sg.WIN_CLOSED or event == "Exit":
                                break
                        window1.close()
                elif select_car == "3":
                    window.hide()
                    if car3_a>0:
                        if insurance == True:
                            layout1 = [
                                [sg.Text(f"Car Model: {car3}", font=("Helvetica", 15))],
                                [sg.Text(f"Rent Cost: Pkr {car3_pd*int(days)}", font=("Helvetica", 15))],
                                [sg.Text(f"Insurance Cost: Pkr {car3_l}", font=("Helvetica", 15))],
                                [sg.Text(f"Tax 5% on Rent Cost: Pkr {(car3_pd*int(days))*0.05}", font=("Helvetica", 15))],
                                [sg.Text(f"Total Cost: Pkr {(car3_pd*int(days))+(car3_l)+((car3_pd*int(days))*0.05)}",font=("Helvetica", 15))],
                                [sg.Button("Confirm", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                            ]
                            window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                            window1.LayoutAndShow
                            while True:
                                event, values = window1.read()
                                if event == "Confirm":
                                    car3_a = car3_a - 1
                                    g_rentcost = (g_rentcost) + (car3_pd*int(days))
                                    g_insurance_cost = (g_insurance_cost) + (car3_l)
                                    g_total_tax = (g_total_tax) + ((car3_pd*int(days))*0.05)
                                    window1.hide()
                                    layout2 = [
                                        [sg.Text(f"You have rented Honda Civic for {days} days.", font=("Helvetica", 15))],
                                        [sg.Button("Main Menu", size= (10,1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                                    ]
                                    window2 = sg.Window("TG Enterprises", layout2, size=(900,500))
                                    window2.LayoutAndShow
                                    while True:
                                        event, values = window2.read()
                                        if event == "Main Menu":
                                            window2.hide()
                                            main_menu()
                                        elif event == sg.WIN_CLOSED or event == "Exit":
                                            break
                                    window2.close()
                                elif event == "Back":
                                    window1.hide()
                                    car_rent()
                                elif event == sg.WIN_CLOSED or event == "Exit":
                                    break
                            window1.close()
                        else:
                            layout1 = [
                                [sg.Text(f"Car Model: {car3}", font=("Helvetica", 15))],
                                [sg.Text(f"Rent Cost: Pkr {car3_pd*int(days)}", font=("Helvetica", 15))],
                                [sg.Text(f"Insurance Cost: Pkr {car3_id}", font=("Helvetica", 15))],
                                [sg.Text(f"Tax 5% on Rent Cost: Pkr {(car3_pd*int(days))*0.05}", font=("Helvetica", 15))],
                                [sg.Text(f"Total Cost: Pkr {(car3_pd*int(days))+(car3_id)+((car3_pd*int(days))*0.05)}",font=("Helvetica", 15))],
                                [sg.Button("Confirm", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                                [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                            ]
                            window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                            window1.LayoutAndShow
                            while True:
                                event, values = window1.read()
                                if event == "Confirm":
                                    car3_a = car3_a - 1
                                    g_rentcost = (g_rentcost) + (car3_pd*int(days))
                                    g_insurance_cost = (g_insurance_cost) + (car3_id)
                                    g_total_tax = (g_total_tax) + ((car3_pd*int(days))*0.05)
                                    window1.hide()
                                    layout2 = [
                                        [sg.Text(f"You have rented Kia Sportage for {days} days.", font=("Helvetica", 15))],
                                        [sg.Button("Main Menu", size= (10,1), font=("Helvetica", 15))],
                                        [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                                    ]
                                    window2 = sg.Window("TG Enterprises", layout2, size=(900,500))
                                    window2.LayoutAndShow
                                    while True:
                                        event, values = window2.read()
                                        if event == "Main Menu":
                                            window2.hide()
                                            main_menu()
                                        elif event == sg.WIN_CLOSED or event == "Exit":
                                            break
                                    window2.close()
                                elif event == "Back":
                                    window1.hide()
                                    car_rent()
                                elif event == sg.WIN_CLOSED or event == "Exit":
                                    break
                            window1.close()
                    else:
                        layout1 = [
                            [sg.Text("The Specific Car is not available", font=("Helvetica", 15))],
                            [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Back":
                                window1.hide()
                                car_rent()
                            elif event == sg.WIN_CLOSED or event == "Exit":
                                break
                        window1.close()
                else:
                    layout1 = [
                        [sg.Text("Please select from the Car models provided", font=("Helvetica", 15))],
                        [sg.Button("Back", size= (10,1), font=("Helvetica", 15))],
                        [sg.Button("Exit", size= (10,1), font=("Helvetica", 15))]
                    ]
                    window1 = sg.Window("Details of your Rental", layout1, size = (900,500))
                    window1.LayoutAndShow
                    while True:
                        event, values = window1.read()
                        if event == "Back":
                            window1.hide()
                            car_rent()
                        elif event == sg.WIN_CLOSED or event == "Exit":
                            break
                    window1.close()       
        elif event == "Back":
            window.hide()
            main_menu()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def car_return():
    global car1_a, car2_a, car3_a
    layout = [
        [sg.Text("Car Return", size=(20, 1), font=("Helvetica", 25))],
        [sg.Text("Choose a car to return:", size=(20, 1), font=("Helvetica", 15))],
        [sg.Listbox(values=[car1, car2, car3], size=(500, 5), key="car_list")],
        [sg.Button("Return", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Back", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
    ]

    window = sg.Window("Car Return", layout, size=(900,500))
    window.LayoutAndShow
    while True:
        event, values = window.read()
        select_car = values["car_list"]
        select_car = str(select_car) # Input from the listbox is changed into a string so that we can use it in conditions.
        if select_car != "[]":
            if event == "Return":
                select_car = values["car_list"]
                select_car = str(select_car)
                if select_car == "['Kia Sportage']":
                    if car1_a<3:
                        window.hide()
                        car1_a = car1_a + 1
                        layout1 = [
                            [sg.Text("Kia Sportage is returned sucessfully", font=("Helvetica", 25))],
                            [sg.Button("Main Menu", size=(10, 1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("TG Enterprises", layout1, size=(900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Main Menu":
                                window1.hide()
                                main_menu()
                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        window1.close()
                    else:
                        window.hide()
                        layout1 = [
                            [sg.Text("The Specific Car was never rented", font=("Helvetica", 25))],
                            [sg.Button("Back", size=(10, 1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("TG Enterprises", layout1, size=(900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Back":
                                window1.hide()
                                car_return()
                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        window1.close()
                elif select_car == "['Toyota Grande']":
                    if car2_a<3:
                        window.hide()
                        car2_a = car2_a + 1
                        layout1 = [
                            [sg.Text("Toyota Grande is returned sucessfully", font=("Helvetica", 25))],
                            [sg.Button("Main Menu", size=(10, 1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("TG Enterprises", layout1, size=(900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Main Menu":
                                window1.hide()
                                main_menu()
                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        window1.close()
                    else:
                        window.hide()
                        layout1 = [
                            [sg.Text("The Specific Car was never rented", font=("Helvetica", 25))],
                            [sg.Button("Back", size=(10, 1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("TG Enterprises", layout1, size=(900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Back":
                                window1.hide()
                                car_return()
                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        window1.close()
                elif select_car == "['Honda Civic']":
                    if car3_a<3:
                        window.hide()
                        car3_a = car3_a + 1
                        layout1 = [
                            [sg.Text("Honda Civic is returned sucessfully", font=("Helvetica", 25))],
                            [sg.Button("Main Menu", size=(10, 1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("TG Enterprises", layout1, size=(900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Main Menu":
                                window1.hide()
                                main_menu()
                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        window1.close()
                    else:
                        window.hide()
                        layout1 = [
                            [sg.Text("The Specific Car was never rented", font=("Helvetica", 25))],
                            [sg.Button("Back", size=(10, 1), font=("Helvetica", 15))],
                            [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
                        ]
                        window1 = sg.Window("TG Enterprises", layout1, size=(900,500))
                        window1.LayoutAndShow
                        while True:
                            event, values = window1.read()
                            if event == "Back":
                                window1.hide()
                                car_return()
                            elif event == "Exit" or event == sg.WIN_CLOSED:
                                break
                        window1.close()
        elif event == "Back":
            window.hide()
            main_menu()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def print_totals():
    layout = [
        [sg.Text("Details of your Finance: ", font=("Helvetica", 15))],
        [sg.Text(f"Total Rent Cost: Pkr {g_rentcost}", font=("Helvetica", 15))],
        [sg.Text(f"Total Insurance Cost: Pkr {g_insurance_cost}", font=("Helvetica", 15))],
        [sg.Text(f"Total Tax: Pkr {g_total_tax}", font=("Helvetica", 15))],
        [sg.Text(f"Total Bill: Pkr {g_rentcost + g_insurance_cost + g_total_tax}", font=("Helvetica", 15))],
        [sg.Button("Main Menu", size=(10, 1), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(10, 1), font=("Helvetica", 15))]
    ]
    window = sg.Window("TG Enterprises", layout, size= (900,500), element_justification = "center", text_justification = "center")
    window.LayoutAndShow
    while True:
        event, values = window.read()
        if event == "Main Menu":
            window.hide()
            main_menu()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

def main_menu():
    layout = [
        [sg.Text("TG Enterprises", size=(30, 1), font=("Helvetica", 25), )],
        [sg.Button("Car Rent", size=(20, 2), font=("Helvetica", 15))],
        [sg.Button("Car Return", size=(20, 2), font=("Helvetica", 15))],
        [sg.Button("Total Finance Detail", size=(20, 2), font=("Helvetica", 15))],
        [sg.Button("Exit", size=(20, 2), font=("Helvetica", 15))]
    ]

    window = sg.Window("TG Enterprises", layout , size = (900,500), element_justification = "center", text_justification = "center")
    while True:
        event, values = window.read()
        if event == "Car Rent":
            window.hide()
            car_rent()
        elif event == "Car Return":
            window.hide()
            car_return()
        elif event == "Total Finance Detail":
            window.hide()
            print_totals()
        elif event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.close()

if __name__ == "__main__":
    main_menu()


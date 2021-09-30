class PayoffsData:

    receiver = "O011350"
    template_name = "Szablon - automat"
    template_name_change = "Szablon Ptaszkowo - automat"
    template_file = "C:\\Users\\Sara\\PycharmProjects\\TMS_testy\\test_data\\szablon_awizacje.xlsx"

    payoff_receiver = "O000215"
    payoff_name = "Glencore lp"
    payoff_file = "C:\\Users\\Sara\\PycharmProjects\\TMS_testy\\test_data\\glencore-rozliczenie.xlsx"
    payoff_file_2 = "C:\\Users\\Sara\\PycharmProjects\\TMS_testy\\glencore-rozliczenie.xlsx"

    connections_dict = {
        "KS/004380": ["AW/004462", "AW/004464"],
        "KS/004506": ["AW/004263"]
    }

    payoff_diff_receiver = "O041597"
    payoff_diff_name = "Szablon-test"
    payoff_diff_file = "C:\\Users\\Sara\\PycharmProjects\\TMS_testy\\test_data\\gamawind.xlsx"

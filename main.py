import overheads , cash_on_hand, profit_loss
overheads_value = overheads.find_highest_overhead()
cash_on_hand_values = cash_on_hand.cash_on_hand()
profit_loss_values = profit_loss.profit_lost()

with open('summary_report.txt', mode='w') as file:
    # Write final output from the modularized functions to the "summary_report.txt" file
    file.write(str(overheads_value) + "\n")

    for item in cash_on_hand_values[0]:
          file.write(str(item) + "\n")

    for item in cash_on_hand_values[1]:
       file.write(str(item) + "\n")

    for items in profit_loss_values[0]:
        file.write(str(items) + "\n")

    for items in profit_loss_values[1]:
       file.write(str(items) + "\n")




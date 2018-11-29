inputs = input()
list_inputs = inputs.split()
withdraw_amount = int(list_inputs[0])
available_amount = float(list_inputs[1])

if withdraw_amount % 5 == 0:
    if withdraw_amount <= (available_amount - 0.5):
        available_amount -= (withdraw_amount + 0.5)

print('%.2f' % available_amount)

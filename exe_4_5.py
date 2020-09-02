def computepay(hour, rate):
    if hour <= 40:
        return (hour * rate)

    overtime = hour - 40
    return (rate * 40) + (overtime*rate*1.5)

def check_float(input1):
    try:
        val = float(input1)
        return val
    except ValueError:
        print('Error, please enter number')
        quit()



input_hours = input('Enter Hours: ')
hours = check_float(input_hours)

input_rate = input('Enter Rate: ')
rate = check_float(input_rate)

pay = computepay(hours, rate)
print('Pay:', pay)

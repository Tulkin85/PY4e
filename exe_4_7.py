
def computergrade(score):
    if score >0 and score <1:
        if score>= 0.9:
            return('A')
        elif score>=0.8:
            return('B')
        elif score>=0.7:
            return('C')
        elif score>=0.6:
            return('D')
        elif score<0.6:
            return('F')
    else:
        return('Error occured')

def check_float(input1):
    try:
        val = float(input1)
        return val
    except ValueError:
        print('Error, please enter number')
        quit()



input_score = input('Enter score: ')
score = check_float(input_score)

score = computergrade(score)
print(score)

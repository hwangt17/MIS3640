#exercise 1-1
def check_fermat(a,b,c,n):
    """
    Checks if Fermat's theorem was write or wrong in variables a, b, c, n
    """
    a_p = a ** n
    b_p = b ** n
    c_p = c ** n
    if (n > 2) and (a_p + b_p == c_p):
        return print('Holy smokes, Fermat was wrong!')
    else:
        return print('No, that doesn\'t work.')
     

a = int(input('Enter value for a: '))
b = int(input('Enter value for b: '))
c = int(input('Enter value for c: '))
n = int(input('Enter value for n: '))

print(check_fermat(a,b,c,n))

#exercise 1-2
def calculate_bmi(weight, height):
    """
    Calculates BMI w/ given weight in kg and height in m.   
    """
    bmi = weight/(height ** 2)
    if bmi <= 18.5:
        return print('Underweight')
    elif (bmi >= 18.5) and (bmi <= 24.9):
        return print('Normal Weight')
    elif (bmi >= 25) and (bmi <= 29.9):
        return print('Overweight')
    else:
        return print("Obesity")

weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))

print(calculate_bmi(weight,height))
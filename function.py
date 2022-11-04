# This function adds two numbers
import logging
logger = logging.getLogger()
handler = logging.FileHandler('logfile.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
def add(x, y):
    logger.info(f'info: add({x}, {y})={x+y}')
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    logger.info(f'info: subtract({x}, {y})={x-y}')
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    logger.info(f'info: multiply({x}, {y})={x*y}')
    return x * y

#Need to define divide function.
def divide (x,y):
    if y==0:
        logger.error(f'error: divide({x}, {y})=0')
        print("0으로 나눌 수 없습니다.")
        return 0
    else:    
        logger.info(f'info: divide({x}, {y})={x/y}')
        return x/y
#
def invalid(choice):
    logger.error(f'error: invalid input : {choice}') 
    print("잘못된 입력입니다.")
    return 0
def exit():
    while True:
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            return False
        elif next_calculation.lower() == "yes":
            return True
        else:
            logger.error(f'error: invalid input : {next_calculation}')
            print("say yes or no")
            continue
def showlog():
    with open('logfile.log', 'r') as f:
        print(f.read())
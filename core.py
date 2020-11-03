from tqdm import tqdm
from time import sleep


def calc(num_1, num_2):
    """Multiples 2 numbers and subtracts 20"""
    result = num_1 * num_2
    result -= 20
    return result

def iterate(amount =40):
    for number in tqdm(range(0,amount)):
        sleep(.8)
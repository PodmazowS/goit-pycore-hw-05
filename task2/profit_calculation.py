from typing import Callable
import re


def generator_number(text: str):
    #pattern looks for float nums with spaces on left and right sides
    pattern = r"\b\d+\.\d+\b"

    for num in re.finditer(pattern, text):
        yield float(num.group())
    

def sum_profit(text: str, func: Callable) -> int:
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_number)

print(f"Загальний дохід: {total_income}")
"""
浮点数精度问题
演示Python中浮点数的特点和精度问题的解决方案
"""
from decimal import Decimal, getcontext
import sys

def float_basics():
    # Python的float是双精度浮点数（64位）
    print("=== Float Basics ===")

    # 查看float的信息
    print(f"Float info: {sys.float_info}")
    print(f"Float max digits: {sys.float_info.dig}")
    print(f"Float max value: {sys.float_info.max}")

    # 常见浮点数的精度问题
    print("\n=== Precision Issues ===")
    a = 0.1 + 0.2
    print(f"0.1 + 0.2 = {a}") # 0.30000000000000004
    print(f"Is 0.1 + 0.2 == 0.3? {a == 0.3}") # False

def float_precision_solution():
    print("\n=== Precision Solutions ===")

    # 1. 使用round函数
    print("1. Using round function:")
    a  = round(0.1 + 0.2, 1)
    print(f"round(0.1 + 0.2, 1) = {a}") # 0.3

    # 2. 使用格式化字符串
    print("\n2. Using format string:")
    print(f"{0.1 + 0.2:.1f}") # 0.3

    # 3. 使用Decimal类
    print("\3. Using Decimal:")
    getcontext().prec = 5
    d1 = Decimal('0.1')
    d2 = Decimal('0.2')
    result = d1 + d2
    print(f"Decimal(0.1) + Decimal(0.2) = {result}") # 0.3000

    # 精确的金融计算
    price = Decimal('10.99')
    tax_rate = Decimal('0.08')
    quantity = 3
    total = price * quantity * (1 + tax_rate)
    print(f"Total: {total}") # 35.61
    print(f"price value: {price}")

def decimal_advanced_usage():
    """ 演示Decimal的高级用法 """
    print("\n=== Advanced Decimal Usage ===")

    # 设置全局精度
    getcontext().prec = 6

    # 1. 从字符串创建Decimal(recomment)
    d1 = Decimal('1.23456789')
    print(f"Decimal from string: {d1}")

    # 2. 从float创建Decimal(not recommended,精度会丢失)
    d2 = Decimal(1.23456789)
    print(f"Decimal from float: {d2}")

    # 3. 数学运算
    print("\nMathematical operations:")
    x = Decimal('1.5')
    print(f"Square root of {x}: {x.sqrt()}")
    print(f"Exponential of {x}: {x.exp()}")

def calculate_loan_payment(principal, rate, years):
    """ 计算每月贷款还款金额 """
    rate = Decimal(str(rate)) / 100 / 12
    months = years * 12
    payment = principal * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)
    return payment.quantize(Decimal('0.01'))

if __name__ == "__main__":
    float_basics()
    float_precision_solution()
    decimal_advanced_usage()

    # 计算贷款还款金额
    monthly_payment = calculate_loan_payment(526519, 3.3, 30)
    print(f"Monthly payment: {monthly_payment}")

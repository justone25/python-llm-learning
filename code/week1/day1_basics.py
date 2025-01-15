"""
Day 1: Python基础语法复习
重点比对JAVA和Python的区别
"""

# 1.变量和数据类型
def variable_and_data_type():
    # Python动态类型 vs Java静态类型
    x = 10 # 整数类型
    x = "Hello" # 可以直接修改为字符串类型

    # 数据类型
    integer_num = 2 # int
    float_num = 3.14 # float
    complex_num = 1 + 2j # complex
    text = "Python" # str
    is_true = True # bool

    # Python的None vs Java的null
    empty_value = None

    # 类型检查
    print(f"Type of integer_num: {type(integer_num)}")
    print(f"Type of float_num: {type(float_num)}")
    print(f"Type of float_num: {type(complex_num)}")
    print(f"Type of float_num: {type(text)}")
    print(f"Type of float_num: {type(is_true)}")
    print(f"Type of float_num: {type(empty_value)}")

if __name__ == "__main__":
    variable_and_data_type()

# 2.集合类型
# 3.控制流
# 4.列表推导式(Python特有)
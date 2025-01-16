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
    print(f"Type of complex_num: {type(complex_num)}")
    print(f"Type of text: {type(text)}")
    print(f"Type of is_true: {type(is_true)}")
    print(f"Type of empty_value: {type(empty_value)}")

# 2. 集合类型
def collections_demo():
    # 列表(类似Java的ArrayList)
    languages = ["Java", "Python", "C++", "JavaScript"]
    languages.append("Go")

    # 元组(不可变列表)
    coordinates = (10, 20)

    # 集合(类似Java的HashSet)
    unique_numbers = {1, 2, 3, 3} # 自动去重
    unique_numbers.add(4)

    # 字典(类似Java的HashMap)
    developer = {
        "name": "Alice",
        "languages": ["Java", "Python", "C++"],
        "experience": 8
    }
    developer["gender"] = "female"
    print(f"Languages: {languages}")
    print(f"Unique numbers: {unique_numbers}")
    print(f"Developer info: {developer}")
    
    # 查看各集合对应的类型名称
    print(f"Languages type is : {type(languages)}")
    print(f"Coordinages type is : {type(coordinates)}")
    print(f"Unique number type is : {type(unique_numbers)}")
    print(f"Developer type is : {type(developer)}")

# 3. 控制流
def control_flow_demo():
    # if-elif-else(类似于Java的if-else)
    score = 85
    if score >= 90:  
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"

    # for循环(类似于Java的for-each)
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    
    # range()生成数字序列
    for i in range(3):
        print(i)
        
    # while循环
    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1

# 4. 列表推导式(Python特有)
def list_comprehension_demo():
    # Java需要使用stream或循环，Python可以用列表推导式
    numbers = [1, 2, 3, 4, 5]
    
    # 获取偶数
    evens = [x for x in numbers if x % 2 == 0]
    
    # 计算平方
    squares = [x ** 2 for x in numbers]
    
    print(f"Evens: {evens}")
    print(f"Squares: {squares}")
    
if __name__ == "__main__":
    variable_and_data_type()
    collections_demo()
    list_comprehension_demo()
# 2.集合类型
# 3.控制流
# 4.列表推导式(Python特有)
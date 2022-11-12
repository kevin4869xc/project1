def sayHello():
    print("Hello")

def sayHello_withname(name):
    print(f"Hello {name}")

def square_area(side):
    area = side ** 2
    return area

def rectangle_area(width,height):
    area = width * height
    return area

if __name__ == "__main__":
    side = eval(input("輸入方形邊長:"))
    area = square_area(side)
    print(f"方形邊長為{side},面積為{area}")

    width = eval(input("請輸入寬:"))
    height = eval(input("請輸入長:"))
    area = rectangle_area(width,height)
    print(f"長方形的寬為{width},長為{height},面積為{area}")
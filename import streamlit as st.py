

temper = input("输入带有符号的温度值")
if temper[-1] in ['F','f']:
    c = (eval(temper[0:-1])- 32)/1.8
    print("转换后的温度是{:.2f}C".format(c))
elif temper[-1] in ['C','c']:
    F = 1.8*eval(temper[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式有误")



# 给文本加行号并备份
def add_line_numbers(input_file, output_file):
    # 读取原文件
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 加行号写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, line in enumerate(lines, 1):
            f.write(f"[{i:>3}] {line}")  # 右对齐3位行号

# 测试
if __name__ == "__main__":
    # 创建测试文件
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write("第一行内容\n第二行文字\n第三行测试\n第四行数据\n第五行结束")
    
    # 备份并加行号
    add_line_numbers("input.txt", "output.txt")
    print("备份完成！output.txt 内容：")
    
    # 显示结果
    with open("output.txt", 'r', encoding='utf-8') as f:
        print(f.read())





# 给文本加行号并备份
def add_line_numbers(input_file, output_file):
    # 读取原文件
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 加行号写入新文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, line in enumerate(lines, 1):
            f.write(f"[{i:>3}] {line}")  # 右对齐3位行号

# 测试
if __name__ == "__main__":
    # 创建测试文件
    with open("input.txt", 'w', encoding='utf-8') as f:
        f.write("第一行内容\n第二行文字\n第三行测试\n第四行数据\n第五行结束")
    
    # 备份并加行号
    add_line_numbers("input.txt", "output.txt")
    print("备份完成！output.txt 内容：")
    
    # 显示结果
    with open("output.txt", 'r', encoding='utf-8') as f:
        print(f.read())
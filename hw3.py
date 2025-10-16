import os


def create_file():
    """创建文本文件并写入内容（使用异常处理替代os.path.exists检查）"""
    filename = input("请输入要创建的文件名: ")

    try:
        # 直接尝试打开文件，通过异常处理捕获文件操作错误
        with open(filename, 'w', encoding='utf-8') as f:
            print("请输入文件内容（输入空行结束）：")
            while True:
                line = input("[输入内容]> ")  # 自定义提示符，增强可读hw3.pyhw3.py性
                if line == '':  # 空行触发结束输入
                    break
                f.write(line + '\n')
        print(f"文件 '{filename}' 创建成功！")
    except OSError as e:
        print(f"创建失败: {str(e)}")


def read_file():
    """读取文本文件内容（使用os.path.exists替代异常处理）"""
    filename = input("请输入要读取的文件名: ")

    # 使用os.path.exists检查文件是否存在
    if not os.path.exists(filename):
        print(f"错误：文件 '{filename}' 不存在")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f"\n📄 文件 '{filename}' 内容如下：")
            print("-" * 40)
            for line in f:
                # 移除行尾空白字符（含换行符），print自动添加标准换行
                print(line.rstrip())
            print("-" * 40)
    except OSError as e:
        print(f"读取失败: {str(e)}")


def main():
    """主程序：提供用户交互菜单"""
    print("===== 文本文件读写工具 =====")
    while True:
        print("\n请选择操作:")
        print("1. 创建新文本文件")
        print("2. 读取现有文本文件")
        print("3. 退出程序")

        choice = input("请输入选项 (1/2/3): ").strip()
        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            print("程序已退出")
            break
        else:
            print("无效选项，请输入1、2或3")


if __name__ == "__main__":
    main()
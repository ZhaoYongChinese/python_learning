"""
Exception: 捕获异常并处理它们，以防止程序崩溃。
try: 尝试执行可能引发异常的代码块。
except: 捕获异常并执行相应的处理代码。
else: 如果没有发生异常，则执行else块中的代码。
finally: 无论是否发生异常，finally块中的代码都会执行，通常用于清理资源。
"""
try:
    f = open('non_existent_file.txt', 'r')
except Exception as e:
    print(f"Error: {e}")
else:
    print(f.read())
finally:
    print("This block will always execute, regardless of exceptions.")
print("Program continues to run...")
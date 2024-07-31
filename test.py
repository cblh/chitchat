import subprocess

# 启动子进程
process = subprocess.Popen(
    ['.venv/bin/python3.6', 'interact.py', '--no_cuda', '--model_path', 'model_epoch40_50w'],  # 确保路径和参数正确启动的脚本或命令
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# 与子进程进行交互
try:
    while True:
        text = input("user: ")
        if text.lower() == 'exit':
            process.stdin.write(text + '\n')
            process.stdin.flush()
            break
        # 检查子进程是否仍在运行
        if process.poll() is not None:
            print("Subprocess terminated unexpectedly.")
            break
        # 发送输入到子进程
        process.stdin.write(text + '\n')
        process.stdin.flush()

        # 读取子进程的输出
        output = process.stdout.readline()
        print(f"chatbot: {output.strip()}")

except KeyboardInterrupt:
    pass
finally:
    # 终止子进程
    process.terminate()
    process.wait()
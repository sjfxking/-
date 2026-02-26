import sys
import platform
import time


def main():
    print("=" * 50)
    print("🚀 恭喜！NickyWaG，你的 Python 虚拟机环境运行正常！")
    print("=" * 50)

    # 打印基础系统信息
    print(f"[*] 当前 Python 版本: {sys.version.split()[0]}")
    print(f"[*] 当前 操作系统: {platform.system()} {platform.release()}")
    print(f"[*] 当前 Python 路径: {sys.executable}")

    print("\n⏳ 正在执行一个简单的模拟计算任务...")
    total = 0
    for i in range(1, 6):
        total += i
        print(f"   -> 处理进度: {i}/5 (当前累加结果: {total})")
        time.sleep(0.5)  # 模拟耗时任务，暂停0.5秒

    print("\n✅ 测试脚本执行完毕！你已经掌握了跑代码的全套流程！")


if __name__ == "__main__":
    main()

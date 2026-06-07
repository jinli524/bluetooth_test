import subprocess

# 指定MuMu模拟器地址
DEVICE_ID = "127.0.0.1:7555"

def run_adb(command):
    """负责执行 ADB 命令，并返回命令的输出结果"""
    full_cmd = f"adb -s {DEVICE_ID} {command}"
    result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def get_bluetooth_status():
    """获取蓝牙状态：开启返回 True，关闭返回 False"""
    output = run_adb("shell settings get global bluetooth_on")
    if output == "":
        # 备用方案：通过蓝牙服务状态判断
        output = run_adb("shell dumpsys bluetooth_manager | grep 'enabled: true'")
        return "enabled: true" in output
    return output == "1"

def enable_bluetooth():
    """打开蓝牙"""
    run_adb("shell svc bluetooth enable")

def disable_bluetooth():
    """关闭蓝牙"""
    run_adb("shell svc bluetooth disable")

def get_device_model():
    """获取设备型号"""
    return run_adb("shell getprop ro.product.model")


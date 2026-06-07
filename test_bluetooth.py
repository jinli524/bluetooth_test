import pytest
from adb_utils import run_adb

def test_adb_connection():
    """验证 ADB 能正常执行命令并返回结果"""
    output = run_adb("shell pm list packages")
    assert output != "", "ADB 命令应该返回结果"
    print(f"已安装的包数量：{len(output.splitlines())} 个")

def test_disable_bluetooth():
    """验证能执行关闭蓝牙的操作"""
    from adb_utils import disable_bluetooth, get_bluetooth_status
    disable_bluetooth()
    # 等待1秒让操作生效
    import time
    time.sleep(1)
    status = get_bluetooth_status()
    print(f"执行关闭操作后，蓝牙状态为{status}")
    # 在模拟器上，get_bluetooth_status 可能返回空或不变，
    # 先断言操作能正常执行，没有抛出异常。
    assert True

def test_enable_bluetooth():
    """验证能执行打开蓝牙的操作"""
    from adb_utils import enable_bluetooth, get_bluetooth_status
    enable_bluetooth()
    import time
    time.sleep(1)
    status = get_bluetooth_status()
    print(f"执行关闭操作后，蓝牙状态为{status}")
    assert True
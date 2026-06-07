# 蓝牙自动化测试项目

## 项目简介
本项目演示了如何使用 Python + ADB 对 Android 设备进行蓝牙功能的自动化测试。

## 技术栈
- Python 3.14
- Pytest
- ADB (Android Debug Bridge)
- MuMu 模拟器

## 项目结构
项目包含三个文件 bluetooth_tes：
- adb_utils.py：负责封装 ADB 命令
- test_bluetooth.py：存放测试用例
- README.md：项目说明文档

## 功能说明
- 通过 ADB 连接 Android 设备
- 控制设备蓝牙开启/关闭
- Pytest 自动化执行测试并断言结果

## 遇到的问题与解决
1. 多设备环境下 ADB 命令返回空：通过 -s 参数指定目标设备解决
2. Python 拼接命令时参数粘连：在设备 ID 和命令之间补空格解决
3. 模拟器 ADB 断连：通过 adb connect 重新连接

## 如何运行
1. 确保电脑已安装 ADB 并配置环境变量
2. 打开 MuMu 模拟器，执行 `adb connect 127.0.0.1:7555`
3. 在本项目目录下执行 `pytest test_bluetooth.py -v -s`

## 作者
huangyu
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF 工具箱打包脚本
使用 PyInstaller 将应用程序打包为可执行文件
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def check_dependencies():
    """检查必要的依赖是否安装"""
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
    except ImportError:
        print("✗ PyInstaller 未安装，正在安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # 检查其他依赖
    dependencies = ["PySide6", "popdf", "pymupdf", "PyPDF2", "loguru", "pofile", "poprogress"]
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep} 已安装")
        except ImportError:
            print(f"✗ {dep} 未安装，正在安装...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])


def build_executable():
    """构建可执行文件"""
    print("\n开始构建可执行文件...")
    
    # 获取当前目录
    current_dir = Path(__file__).parent
    main_script = current_dir / "main.py"
    
    # PyInstaller 配置
    pyinstaller_args = [
        sys.executable, "-m", "PyInstaller",
        "--name=PDF工具箱",
        "--onefile",
        "--windowed",  # 不显示控制台窗口
        "--icon=NONE",  # 暂时不使用图标
        "--add-data=../popdf;popdf",  # 包含 popdf 模块
        "--hidden-import=popdf.api.pdf",
        "--hidden-import=popdf.core.PDFType",
        "--hidden-import=popdf.core.Batch_PDFType",
        "--hidden-import=popdf.lib",
        "--hidden-import=pofile",
        "--hidden-import=poprogress",
        "--clean",  # 清理临时文件
        str(main_script)
    ]
    
    try:
        print("运行 PyInstaller...")
        subprocess.run(pyinstaller_args, check=True)
        print("✓ 构建完成")
    except subprocess.CalledProcessError as e:
        print(f"✗ 构建失败: {e}")
        return False
    
    return True


def create_distribution():
    """创建发布包"""
    print("\n创建发布包...")
    
    current_dir = Path(__file__).parent
    dist_dir = current_dir / "dist"
    build_dir = current_dir / "build"
    
    # 创建发布文件夹
    release_dir = current_dir / "release"
    release_dir.mkdir(exist_ok=True)
    
    # 复制可执行文件
    exe_file = dist_dir / "PDF工具箱.exe"
    if exe_file.exists():
        shutil.copy2(exe_file, release_dir / "PDF工具箱.exe")
        print("✓ 可执行文件已复制到 release 文件夹")
    
    # 创建说明文件
    readme_content = """PDF 工具箱
==========

基于 popdf 库的 PDF 处理工具

功能特性
--------
- PDF 转 Word 文档
- PDF 转图片
- 文本文件转 PDF
- PDF 分割
- PDF 加密/解密
- 添加文本水印
- PDF 合并
- 删除 PDF 页面
- 支持单个文件和批量处理

使用说明
--------
1. 直接运行 "PDF工具箱.exe"
2. 选择需要的功能标签页
3. 选择输入文件和输出位置
4. 点击开始按钮执行操作

系统要求
--------
- Windows 7/8/10/11
- 无需安装 Python 环境

注意事项
--------
- 首次运行可能需要一些时间初始化
- 确保有足够的磁盘空间用于文件处理
- 批量处理大量文件时请耐心等待
"""
    
    with open(release_dir / "README.txt", "w", encoding="utf-8") as f:
        f.write(readme_content)
    print("✓ 说明文件已创建")
    
    # 清理临时文件
    if build_dir.exists():
        shutil.rmtree(build_dir)
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    
    spec_file = current_dir / "PDF工具箱.spec"
    if spec_file.exists():
        spec_file.unlink()
    
    print("✓ 临时文件已清理")
    print(f"\n🎉 发布包已创建在: {release_dir}")


def main():
    """主函数"""
    print("PDF 工具箱打包程序")
    print("=" * 50)
    
    # 检查依赖
    check_dependencies()
    
    # 构建可执行文件
    if build_executable():
        # 创建发布包
        create_distribution()
    else:
        print("\n❌ 打包失败，请检查错误信息")
        sys.exit(1)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF 工具箱启动脚本
直接运行此文件可以启动 GUI 应用程序
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def main():
    """主函数"""
    try:
        # 检查依赖
        required_packages = ["PySide6", "popdf", "pymupdf", "pypdf", "loguru", "pofile", "poprogress"]
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package)
                print(f"✓ {package} 已安装")
            except ImportError:
                missing_packages.append(package)
                print(f"✗ {package} 未安装")
        
        if missing_packages:
            print(f"\n缺少以下依赖包: {', '.join(missing_packages)}")
            install = input("是否自动安装? (y/n): ").lower().strip()
            if install == 'y':
                import subprocess
                for package in missing_packages:
                    print(f"正在安装 {package}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print("✓ 所有依赖安装完成")
            else:
                print("请手动安装依赖后重新运行")
                sys.exit(1)
        
        # 导入并启动主程序
        from main import main as gui_main
        print("\n启动 PDF 工具箱...")
        gui_main()
        
    except Exception as e:
        print(f"启动失败: {e}")
        input("按回车键退出...")
        sys.exit(1)


if __name__ == "__main__":
    main()
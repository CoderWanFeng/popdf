#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试美化后的 GUI 界面
"""

import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_gui():
    """测试 GUI 界面"""
    try:
        # 检查依赖
        required_packages = ["PySide6", "popdf", "pymupdf", "PyPDF2", "loguru", "pofile", "poprogress"]
        missing_packages = []
        
        print("🔍 检查依赖包...")
        for package in required_packages:
            try:
                __import__(package)
                print(f"✅ {package} 已安装")
            except ImportError:
                missing_packages.append(package)
                print(f"❌ {package} 未安装")
        
        if missing_packages:
            print(f"\n⚠️ 缺少以下依赖包: {', '.join(missing_packages)}")
            install = input("是否自动安装? (y/n): ").lower().strip()
            if install == 'y':
                import subprocess
                for package in missing_packages:
                    print(f"📦 正在安装 {package}...")
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print("✅ 所有依赖安装完成")
            else:
                print("请手动安装依赖后重新运行")
                sys.exit(1)
        
        # 导入并启动主程序
        from main import main as gui_main
        print("\n🚀 启动 PDF 智能处理平台...")
        print("✨ 界面已美化，具有科技感设计")
        print("🎨 包含渐变背景、现代化按钮、图标等")
        print("\n正在加载界面...")
        
        gui_main()
        
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        import traceback
        traceback.print_exc()
        input("按回车键退出...")
        sys.exit(1)


if __name__ == "__main__":
    test_gui()
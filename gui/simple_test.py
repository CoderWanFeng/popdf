#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单测试程序 - 验证基本功能
"""

import sys
import os
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root.parent))

def test_basic_imports():
    """测试基本导入"""
    print("测试基本导入...")
    
    try:
        from PySide6.QtWidgets import QApplication, QLabel, QWidget
        from PySide6.QtCore import Qt
        print("✅ PySide6 导入成功")
        
        import pymupdf
        print("✅ pymupdf 导入成功")
        
        import popdf.api.pdf
        print("✅ popdf 导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 导入失败: {e}")
        return False

def test_simple_gui():
    """测试简单 GUI"""
    print("测试简单 GUI...")
    
    try:
        from PySide6.QtWidgets import QApplication, QLabel, QWidget
        from PySide6.QtCore import Qt
        
        app = QApplication(sys.argv)
        
        window = QWidget()
        window.setWindowTitle("测试窗口")
        window.setGeometry(100, 100, 300, 200)
        
        label = QLabel("✅ GUI 测试成功！", window)
        label.setAlignment(Qt.AlignCenter)
        label.setGeometry(50, 50, 200, 100)
        
        window.show()
        
        # 短暂显示后退出
        from PySide6.QtCore import QTimer
        QTimer.singleShot(1000, app.quit)
        
        return app.exec()
    except Exception as e:
        print(f"❌ GUI 测试失败: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("PDF 工具箱 - 简单测试程序")
    print("=" * 50)
    
    if test_basic_imports():
        print("\n开始 GUI 测试...")
        test_simple_gui()
    else:
        print("\n基本导入测试失败，无法进行 GUI 测试")
    
    input("\n按回车键退出...")

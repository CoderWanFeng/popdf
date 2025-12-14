# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                               QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, 
                               QFileDialog, QMessageBox, QTabWidget, QGroupBox,
                               QCheckBox, QSpinBox, QComboBox, QProgressBar,
                               QFrame, QScrollArea)
from PySide6.QtCore import Qt, QThread, Signal, QPropertyAnimation, QEasingCurve, QRect
from PySide6.QtGui import QFont, QPalette, QColor, QLinearGradient, QPainter, QFontDatabase

# 添加项目根目录到 Python 路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from popdf.api.pdf import (
    pdf2docx, pdf2imgs, txt2pdf, split4pdf, encrypt4pdf, 
    decrypt4pdf, add_text_watermark, merge2pdf, del4pdf
)


class TechButton(QPushButton):
    """科技感按钮"""
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(40)
        self.setFont(QFont("Microsoft YaHei", 10, QFont.Bold))
        
    def enterEvent(self, event):
        self.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00b4ff, stop:0.5 #0099ff, stop:1 #0077ff);
                color: white;
                border: 2px solid #00b4ff;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0099ff, stop:0.5 #0077ff, stop:1 #0055ff);
                border: 2px solid #0099ff;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0077ff, stop:0.5 #0055ff, stop:1 #0033ff);
            }
        """)
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        self.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1e3a8a, stop:0.5 #1d4ed8, stop:1 #3b82f6);
                color: white;
                border: 2px solid #3b82f6;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
            }
        """)
        super().leaveEvent(event)


class TechLineEdit(QLineEdit):
    """科技感输入框"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QLineEdit {
                background: rgba(30, 41, 59, 0.8);
                border: 2px solid #3b82f6;
                border-radius: 6px;
                padding: 8px 12px;
                color: #e2e8f0;
                font-size: 12px;
                selection-background-color: #3b82f6;
            }
            QLineEdit:focus {
                border: 2px solid #00b4ff;
                background: rgba(30, 41, 59, 0.9);
            }
        """)


class TechGroupBox(QGroupBox):
    """科技感分组框"""
    def __init__(self, title="", parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("""
            QGroupBox {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 rgba(15, 23, 42, 0.8), stop:1 rgba(30, 41, 59, 0.8));
                border: 2px solid #1e40af;
                border-radius: 10px;
                margin-top: 10px;
                padding-top: 10px;
                color: #e2e8f0;
                font-weight: bold;
                font-size: 13px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 8px 0 8px;
                color: #60a5fa;
            }
        """)


class TechProgressBar(QProgressBar):
    """科技感进度条"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QProgressBar {
                border: 2px solid #1e40af;
                border-radius: 5px;
                text-align: center;
                background: rgba(15, 23, 42, 0.8);
                color: white;
                font-weight: bold;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00b4ff, stop:0.5 #0099ff, stop:1 #0077ff);
                border-radius: 3px;
            }
        """)


class TechTabWidget(QTabWidget):
    """科技感标签页"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #1e40af;
                border-radius: 8px;
                background: rgba(15, 23, 42, 0.9);
            }
            QTabWidget::tab-bar {
                alignment: center;
            }
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1e3a8a, stop:1 #1d4ed8);
                border: 2px solid #1e40af;
                border-bottom: none;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                min-width: 120px;
                padding: 8px 16px;
                color: white;
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00b4ff, stop:1 #0099ff);
                border-color: #00b4ff;
            }
            QTabBar::tab:hover:!selected {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #60a5fa);
            }
        """)


class HeaderWidget(QWidget):
    """头部标题组件"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(120)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)
        
        # 主标题
        title_label = QLabel("PDF 智能处理平台")
        title_label.setStyleSheet("""
            QLabel {
                color: #00b4ff;
                font-size: 28px;
                font-weight: bold;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 transparent, stop:0.5 rgba(0, 180, 255, 0.1), stop:1 transparent);
                padding: 10px;
                border-radius: 5px;
            }
        """)
        title_label.setAlignment(Qt.AlignCenter)
        
        # 副标题
        subtitle_label = QLabel("基于 AI 技术的多功能 PDF 处理工具")
        subtitle_label.setStyleSheet("""
            QLabel {
                color: #60a5fa;
                font-size: 14px;
                font-weight: normal;
                padding: 5px;
            }
        """)
        subtitle_label.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)


class WorkerThread(QThread):
    """工作线程，用于执行耗时的 PDF 操作"""
    progress_signal = Signal(int)
    message_signal = Signal(str)
    finished_signal = Signal(bool, str)
    
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
    
    def run(self):
        try:
            self.message_signal.emit("🚀 开始处理...")
            self.progress_signal.emit(10)
            
            result = self.func(*self.args, **self.kwargs)
            
            self.progress_signal.emit(100)
            self.message_signal.emit("✅ 处理完成！")
            self.finished_signal.emit(True, "操作成功完成")
        except Exception as e:
            self.finished_signal.emit(False, f"❌ 错误: {str(e)}")


class PDFConverterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_styles()
        self.init_ui()
        self.worker_thread = None
        
    def setup_styles(self):
        """设置全局样式"""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f172a, stop:0.5 #1e293b, stop:1 #334155);
                color: #e2e8f0;
                font-family: "Microsoft YaHei";
            }
            QLabel {
                color: #cbd5e1;
                font-size: 12px;
                padding: 2px;
            }
            QCheckBox {
                color: #cbd5e1;
                font-size: 12px;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #3b82f6;
                border-radius: 3px;
                background: rgba(15, 23, 42, 0.8);
            }
            QCheckBox::indicator:checked {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00b4ff, stop:1 #0099ff);
                border: 2px solid #00b4ff;
            }
            QSpinBox {
                background: rgba(30, 41, 59, 0.8);
                border: 2px solid #3b82f6;
                border-radius: 6px;
                padding: 6px;
                color: #e2e8f0;
                font-size: 12px;
            }
            QTextEdit {
                background: rgba(30, 41, 59, 0.8);
                border: 2px solid #3b82f6;
                border-radius: 6px;
                padding: 8px;
                color: #e2e8f0;
                font-size: 12px;
            }
        """)
        
    def init_ui(self):
        self.setWindowTitle("PDF 智能处理平台 - 基于 popdf")
        self.setGeometry(100, 100, 1000, 700)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 添加头部
        header = HeaderWidget()
        main_layout.addWidget(header)
        
        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        
        # 创建内容部件
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 10, 20, 20)
        
        # 创建标签页
        tab_widget = TechTabWidget()
        content_layout.addWidget(tab_widget)
        
        # 添加各个功能标签页
        tab_widget.addTab(self.create_pdf2docx_tab(), "📄 PDF转Word")
        tab_widget.addTab(self.create_pdf2imgs_tab(), "🖼️ PDF转图片")
        tab_widget.addTab(self.create_txt2pdf_tab(), "📝 文本转PDF")
        tab_widget.addTab(self.create_split_tab(), "✂️ PDF分割")
        tab_widget.addTab(self.create_encrypt_tab(), "🔒 PDF加密")
        tab_widget.addTab(self.create_decrypt_tab(), "🔓 PDF解密")
        tab_widget.addTab(self.create_watermark_tab(), "💧 添加水印")
        tab_widget.addTab(self.create_merge_tab(), "📚 PDF合并")
        tab_widget.addTab(self.create_delete_tab(), "🗑️ 删除页面")
        
        scroll_area.setWidget(content_widget)
        main_layout.addWidget(scroll_area)
        
        # 状态栏
        self.status_label = QLabel("🟢 系统就绪")
        self.status_label.setStyleSheet("QLabel { color: #10b981; font-weight: bold; padding: 8px; }")
        self.statusBar().addWidget(self.status_label)
        
        # 进度条
        self.progress_bar = TechProgressBar()
        self.progress_bar.setFixedWidth(200)
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.progress_bar.setVisible(False)
    
    def create_file_selection_group(self, title, is_input=True, file_types="PDF 文件 (*.pdf)"):
        """创建文件选择组件的通用方法"""
        group = TechGroupBox(title)
        layout = QVBoxLayout(group)
        
        # 单文件选择
        single_layout = QHBoxLayout()
        single_label = QLabel("📄 单个文件:")
        single_file_edit = TechLineEdit()
        single_browse_btn = TechButton("浏览文件")
        
        single_layout.addWidget(single_label)
        single_layout.addWidget(single_file_edit, 1)
        single_layout.addWidget(single_browse_btn)
        layout.addLayout(single_layout)
        
        # 批量文件选择
        batch_layout = QHBoxLayout()
        batch_label = QLabel("📁 批量文件夹:")
        batch_folder_edit = TechLineEdit()
        batch_browse_btn = TechButton("浏览文件夹")
        
        batch_layout.addWidget(batch_label)
        batch_layout.addWidget(batch_folder_edit, 1)
        batch_layout.addWidget(batch_browse_btn)
        layout.addLayout(batch_layout)
        
        # 连接信号
        single_browse_btn.clicked.connect(lambda: self.browse_file(single_file_edit, file_types))
        batch_browse_btn.clicked.connect(lambda: self.browse_folder(batch_folder_edit))
        
        return group, single_file_edit, batch_folder_edit
    
    def create_pdf2docx_tab(self):
        """创建 PDF 转 Word 标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, input_batch = self.create_file_selection_group("选择 PDF 文件", True, "PDF 文件 (*.pdf)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, output_batch = self.create_file_selection_group("选择输出位置", False, "Word 文件 (*.docx)")
        layout.addWidget(output_group)
        
        # 执行按钮
        execute_btn = TechButton("🚀 开始转换")
        execute_btn.setFixedHeight(50)
        execute_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #10b981, stop:0.5 #059669, stop:1 #047857);
                color: white;
                border: 2px solid #10b981;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #059669, stop:0.5 #047857, stop:1 #065f46);
            }
        """)
        execute_btn.clicked.connect(lambda: self.execute_pdf2docx(input_single, input_batch, output_single, output_batch))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_pdf2imgs_tab(self):
        """创建 PDF 转图片标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, input_batch = self.create_file_selection_group("选择 PDF 文件", True, "PDF 文件 (*.pdf)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, output_batch = self.create_file_selection_group("选择输出位置", False, "图片文件夹")
        layout.addWidget(output_group)
        
        # 选项
        options_layout = QHBoxLayout()
        merge_checkbox = QCheckBox("🖼️ 合并为单张图片")
        merge_checkbox.setStyleSheet("QCheckBox { font-weight: bold; }")
        options_layout.addWidget(merge_checkbox)
        options_layout.addStretch()
        layout.addLayout(options_layout)
        
        # 执行按钮
        execute_btn = TechButton("🚀 开始转换")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(lambda: self.execute_pdf2imgs(input_single, input_batch, output_single, output_batch, merge_checkbox.isChecked()))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_txt2pdf_tab(self):
        """创建文本转 PDF 标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, input_batch = self.create_file_selection_group("选择文本文件", True, "文本文件 (*.txt)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, output_batch = self.create_file_selection_group("选择输出位置", False, "PDF 文件 (*.pdf)")
        layout.addWidget(output_group)
        
        # 执行按钮
        execute_btn = TechButton("🚀 开始转换")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(lambda: self.execute_txt2pdf(input_single, input_batch, output_single, output_batch))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_split_tab(self):
        """创建 PDF 分割标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, input_batch = self.create_file_selection_group("选择 PDF 文件", True, "PDF 文件 (*.pdf)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, output_batch = self.create_file_selection_group("选择输出位置", False, "PDF 文件 (*.pdf)")
        layout.addWidget(output_group)
        
        # 页面范围设置
        page_group = TechGroupBox("页面范围设置")
        page_layout = QHBoxLayout(page_group)
        
        page_layout.addWidget(QLabel("📄 起始页码:"))
        from_page = QSpinBox()
        from_page.setMinimum(1)
        from_page.setValue(1)
        from_page.setMaximum(999)
        page_layout.addWidget(from_page)
        
        page_layout.addWidget(QLabel("📄 结束页码:"))
        to_page = QSpinBox()
        to_page.setMinimum(1)
        to_page.setValue(-1)
        to_page.setMaximum(999)
        to_page.setSpecialValueText("末尾")
        page_layout.addWidget(to_page)
        page_layout.addStretch()
        
        layout.addWidget(page_group)
        
        # 执行按钮
        execute_btn = TechButton("✂️ 开始分割")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(lambda: self.execute_split4pdf(input_single, input_batch, output_single, output_batch, from_page.value(), to_page.value()))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_encrypt_tab(self):
        """创建 PDF 加密标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, input_batch = self.create_file_selection_group("选择 PDF 文件", True, "PDF 文件 (*.pdf)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, output_batch = self.create_file_selection_group("选择输出位置", False, "PDF 文件 (*.pdf)")
        layout.addWidget(output_group)
        
        # 密码设置
        password_group = TechGroupBox("密码设置")
        password_layout = QHBoxLayout(password_group)
        password_layout.addWidget(QLabel("🔑 设置密码:"))
        password_edit = TechLineEdit()
        password_edit.setEchoMode(QLineEdit.Password)
        password_edit.setPlaceholderText("请输入加密密码")
        password_layout.addWidget(password_edit, 1)
        layout.addWidget(password_group)
        
        # 执行按钮
        execute_btn = TechButton("🔒 开始加密")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(lambda: self.execute_encrypt4pdf(input_single, input_batch, output_single, output_batch, password_edit.text()))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_decrypt_tab(self):
        """创建 PDF 解密标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, input_batch = self.create_file_selection_group("选择 PDF 文件", True, "PDF 文件 (*.pdf)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, output_batch = self.create_file_selection_group("选择输出位置", False, "PDF 文件 (*.pdf)")
        layout.addWidget(output_group)
        
        # 密码设置
        password_group = TechGroupBox("密码输入")
        password_layout = QHBoxLayout(password_group)
        password_layout.addWidget(QLabel("🔓 输入密码:"))
        password_edit = TechLineEdit()
        password_edit.setPlaceholderText("请输入PDF文件的密码")
        password_layout.addWidget(password_edit, 1)
        layout.addWidget(password_group)
        
        # 执行按钮
        execute_btn = TechButton("🔓 开始解密")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(lambda: self.execute_decrypt4pdf(input_single, input_batch, output_single, output_batch, password_edit.text()))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_watermark_tab(self):
        """创建添加水印标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, _ = self.create_file_selection_group("选择 PDF 文件", True, "PDF 文件 (*.pdf)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, _ = self.create_file_selection_group("选择输出位置", False, "PDF 文件 (*.pdf)")
        layout.addWidget(output_group)
        
        # 水印设置
        watermark_group = TechGroupBox("水印设置")
        watermark_layout = QVBoxLayout(watermark_group)
        
        # 水印文本
        text_layout = QHBoxLayout()
        text_layout.addWidget(QLabel("💧 水印文本:"))
        watermark_text = TechLineEdit()
        watermark_text.setText("python-office")
        text_layout.addWidget(watermark_text, 1)
        watermark_layout.addLayout(text_layout)
        
        # 位置设置
        position_layout = QHBoxLayout()
        position_layout.addWidget(QLabel("📍 位置 X:"))
        pos_x = QSpinBox()
        pos_x.setRange(0, 1000)
        pos_x.setValue(100)
        position_layout.addWidget(pos_x)
        
        position_layout.addWidget(QLabel("📍 位置 Y:"))
        pos_y = QSpinBox()
        pos_y.setRange(0, 1000)
        pos_y.setValue(100)
        position_layout.addWidget(pos_y)
        position_layout.addStretch()
        watermark_layout.addLayout(position_layout)
        
        # 字体设置
        font_layout = QHBoxLayout()
        font_layout.addWidget(QLabel("🔤 字体大小:"))
        font_size = QSpinBox()
        font_size.setRange(8, 72)
        font_size.setValue(12)
        font_layout.addWidget(font_size)
        font_layout.addStretch()
        watermark_layout.addLayout(font_layout)
        
        layout.addWidget(watermark_group)
        
        # 执行按钮
        execute_btn = TechButton("💧 添加水印")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(lambda: self.execute_watermark(input_single, output_single, (pos_x.value(), pos_y.value()), watermark_text.text(), font_size.value()))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_merge_tab(self):
        """创建 PDF 合并标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 文件列表
        file_group = TechGroupBox("选择要合并的 PDF 文件")
        file_layout = QVBoxLayout(file_group)
        
        self.merge_files_list = QTextEdit()
        self.merge_files_list.setPlaceholderText("📚 每行一个文件路径，或点击下方按钮添加文件")
        self.merge_files_list.setMaximumHeight(150)
        file_layout.addWidget(self.merge_files_list)
        
        # 文件选择按钮
        file_buttons_layout = QHBoxLayout()
        add_file_btn = TechButton("➕ 添加文件")
        add_file_btn.clicked.connect(self.add_merge_files)
        clear_files_btn = TechButton("🗑️ 清空列表")
        clear_files_btn.clicked.connect(lambda: self.merge_files_list.clear())
        
        file_buttons_layout.addWidget(add_file_btn)
        file_buttons_layout.addWidget(clear_files_btn)
        file_buttons_layout.addStretch()
        file_layout.addLayout(file_buttons_layout)
        
        layout.addWidget(file_group)
        
        # 输出文件选择
        output_group = TechGroupBox("输出设置")
        output_layout = QHBoxLayout(output_group)
        output_layout.addWidget(QLabel("📄 输出文件:"))
        self.merge_output_edit = TechLineEdit()
        self.merge_output_edit.setPlaceholderText("选择合并后的PDF文件保存位置")
        output_layout.addWidget(self.merge_output_edit, 1)
        output_browse_btn = TechButton("浏览")
        output_browse_btn.clicked.connect(lambda: self.browse_file(self.merge_output_edit, "PDF 文件 (*.pdf)"))
        output_layout.addWidget(output_browse_btn)
        layout.addWidget(output_group)
        
        # 执行按钮
        execute_btn = TechButton("📚 开始合并")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(self.execute_merge2pdf)
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def create_delete_tab(self):
        """创建删除页面标签页"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(15)
        
        # 输入文件选择
        input_group, input_single, input_batch = self.create_file_selection_group("选择 PDF 文件", True, "PDF 文件 (*.pdf)")
        layout.addWidget(input_group)
        
        # 输出文件选择
        output_group, output_single, output_batch = self.create_file_selection_group("选择输出位置", False, "PDF 文件 (*.pdf)")
        layout.addWidget(output_group)
        
        # 页面设置
        page_group = TechGroupBox("删除页面设置")
        page_layout = QHBoxLayout(page_group)
        page_layout.addWidget(QLabel("🗑️ 删除页码:"))
        page_nums_edit = TechLineEdit()
        page_nums_edit.setPlaceholderText("例如: 1,3,5-8 (支持单个页码和范围)")
        page_layout.addWidget(page_nums_edit, 1)
        layout.addWidget(page_group)
        
        # 执行按钮
        execute_btn = TechButton("🗑️ 删除页面")
        execute_btn.setFixedHeight(50)
        execute_btn.clicked.connect(lambda: self.execute_del4pdf(input_single, input_batch, output_single, output_batch, page_nums_edit.text()))
        layout.addWidget(execute_btn)
        
        layout.addStretch()
        return widget
    
    def browse_file(self, line_edit, file_types):
        """浏览文件"""
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", file_types)
        if file_path:
            line_edit.setText(file_path)
    
    def browse_folder(self, line_edit):
        """浏览文件夹"""
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            line_edit.setText(folder_path)
    
    def add_merge_files(self):
        """添加合并文件"""
        files, _ = QFileDialog.getOpenFileNames(self, "选择 PDF 文件", "", "PDF 文件 (*.pdf)")
        if files:
            current_text = self.merge_files_list.toPlainText()
            new_files = "\n".join(files)
            if current_text:
                new_files = current_text + "\n" + new_files
            self.merge_files_list.setText(new_files)
    
    def validate_inputs(self, input_single, input_batch, output_single, output_batch, require_both=False):
        """验证输入参数"""
        has_single = bool(input_single.text().strip()) and bool(output_single.text().strip())
        has_batch = bool(input_batch.text().strip()) and bool(output_batch.text().strip())
        
        if require_both and not (has_single or has_batch):
            QMessageBox.warning(self, "输入错误", "请选择输入文件和输出位置")
            return False
        
        if has_single and has_batch:
            QMessageBox.warning(self, "输入错误", "请选择单个文件处理或批量处理，不要同时填写")
            return False
        
        if not has_single and not has_batch:
            QMessageBox.warning(self, "输入错误", "请填写必要的文件路径")
            return False
        
        return True
    
    def start_worker(self, func, *args, **kwargs):
        """启动工作线程"""
        if self.worker_thread and self.worker_thread.isRunning():
            QMessageBox.warning(self, "操作进行中", "请等待当前操作完成")
            return
        
        self.worker_thread = WorkerThread(func, *args, **kwargs)
        self.worker_thread.progress_signal.connect(self.update_progress)
        self.worker_thread.message_signal.connect(self.update_status)
        self.worker_thread.finished_signal.connect(self.operation_finished)
        
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.worker_thread.start()
    
    def update_progress(self, value):
        """更新进度条"""
        self.progress_bar.setValue(value)
    
    def update_status(self, message):
        """更新状态栏"""
        self.status_label.setText(message)
    
    def operation_finished(self, success, message):
        """操作完成回调"""
        self.progress_bar.setVisible(False)
        if success:
            QMessageBox.information(self, "操作成功", message)
            self.status_label.setText("🟢 系统就绪")
        else:
            QMessageBox.critical(self, "操作失败", message)
            self.status_label.setText("🔴 操作失败")
    
    # 各个功能的执行方法
    def execute_pdf2docx(self, input_single, input_batch, output_single, output_batch):
        if not self.validate_inputs(input_single, input_batch, output_single, output_batch):
            return
        
        if input_single.text() and output_single.text():
            self.start_worker(pdf2docx, input_file=input_single.text(), output_file=output_single.text())
        else:
            self.start_worker(pdf2docx, input_path=input_batch.text(), output_path=output_batch.text())
    
    def execute_pdf2imgs(self, input_single, input_batch, output_single, output_batch, merge):
        if not self.validate_inputs(input_single, input_batch, output_single, output_batch):
            return
        
        if input_single.text() and output_single.text():
            self.start_worker(pdf2imgs, input_file=input_single.text(), output_file=output_single.text(), merge=merge)
        else:
            self.start_worker(pdf2imgs, input_path=input_batch.text(), output_path=output_batch.text(), merge=merge)
    
    def execute_txt2pdf(self, input_single, input_batch, output_single, output_batch):
        if not self.validate_inputs(input_single, input_batch, output_single, output_batch):
            return
        
        if input_single.text() and output_single.text():
            self.start_worker(txt2pdf, input_file=input_single.text(), output_file=output_single.text())
        else:
            self.start_worker(txt2pdf, input_path=input_batch.text(), output_path=output_batch.text())
    
    def execute_split4pdf(self, input_single, input_batch, output_single, output_batch, from_page, to_page):
        if not self.validate_inputs(input_single, input_batch, output_single, output_batch):
            return
        
        if input_single.text() and output_single.text():
            self.start_worker(split4pdf, input_file=input_single.text(), output_file=output_single.text(), 
                            from_page=from_page, to_page=to_page)
        else:
            self.start_worker(split4pdf, input_path=input_batch.text(), output_path=output_batch.text(), 
                            from_page=from_page, to_page=to_page)
    
    def execute_encrypt4pdf(self, input_single, input_batch, output_single, output_batch, password):
        if not password:
            QMessageBox.warning(self, "输入错误", "请输入密码")
            return
        
        if not self.validate_inputs(input_single, input_batch, output_single, output_batch):
            return
        
        if input_single.text() and output_single.text():
            self.start_worker(encrypt4pdf, password=password, input_file=input_single.text(), output_file=output_single.text())
        else:
            self.start_worker(encrypt4pdf, password=password, input_path=input_batch.text(), output_path=output_batch.text())
    
    def execute_decrypt4pdf(self, input_single, input_batch, output_single, output_batch, password):
        if not password:
            QMessageBox.warning(self, "输入错误", "请输入密码")
            return
        
        if not self.validate_inputs(input_single, input_batch, output_single, output_batch):
            return
        
        if input_single.text() and output_single.text():
            self.start_worker(decrypt4pdf, input_file=input_single.text(), password=password, output_file=output_single.text())
        else:
            self.start_worker(decrypt4pdf, input_path=input_batch.text(), output_path=output_batch.text(), password=password)
    
    def execute_watermark(self, input_single, output_single, point, text, fontsize):
        if not input_single.text() or not output_single.text():
            QMessageBox.warning(self, "输入错误", "请选择输入文件和输出位置")
            return
        
        self.start_worker(add_text_watermark, input_file=input_single.text(), point=point, 
                         text=text, output_file=output_single.text(), fontsize=fontsize)
    
    def execute_merge2pdf(self):
        files_text = self.merge_files_list.toPlainText().strip()
        if not files_text:
            QMessageBox.warning(self, "输入错误", "请添加要合并的 PDF 文件")
            return
        
        if not self.merge_output_edit.text():
            QMessageBox.warning(self, "输入错误", "请选择输出文件位置")
            return
        
        file_list = [f.strip() for f in files_text.split('\n') if f.strip()]
        self.start_worker(merge2pdf, input_file_list=file_list, output_file=self.merge_output_edit.text())
    
    def execute_del4pdf(self, input_single, input_batch, output_single, output_batch, page_nums):
        if not page_nums:
            QMessageBox.warning(self, "输入错误", "请输入要删除的页码")
            return
        
        if not self.validate_inputs(input_single, input_batch, output_single, output_batch):
            return
        
        if input_single.text() and output_single.text():
            self.start_worker(del4pdf, page_nums=page_nums, input_file=input_single.text(), output_file=output_single.text())
        else:
            self.start_worker(del4pdf, page_nums=page_nums, input_path=input_batch.text(), output_path=output_batch.text())


def main():
    app = QApplication(sys.argv)
    
    # 设置应用程序信息
    app.setApplicationName("PDF 智能处理平台")
    app.setApplicationVersion("1.0.0")
    
    # 设置应用程序图标和样式
    app.setStyle("Fusion")
    
    window = PDFConverterGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
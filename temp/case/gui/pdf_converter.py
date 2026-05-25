# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QPushButton, QLabel, QLineEdit, QTextEdit,
                               QFileDialog, QMessageBox, QGroupBox, QProgressBar,
                               QFrame, QComboBox, QCheckBox, QSpinBox, QSlider)
from PySide6.QtCore import Qt, QThread, Signal, QTimer
from PySide6.QtGui import QFont, QColor, QPalette

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import popdf


class ConvertThread(QThread):
    progress = Signal(int)
    finished = Signal(bool, str)
    log = Signal(str)

    def __init__(self, files, output_dir, quality=2):
        super().__init__()
        self.files = files
        self.output_dir = output_dir
        self.quality = quality
        self.success_count = 0
        self.fail_count = 0

    def run(self):
        total = len(self.files)
        for i, file_path in enumerate(self.files):
            try:
                self.log.emit(f"正在转换: {os.path.basename(file_path)}")
                file_name = os.path.splitext(os.path.basename(file_path))[0]
                output_file = os.path.join(self.output_dir, f"{file_name}.docx")
                popdf.pdf2docx(input_file=file_path, output_file=output_file)
                self.success_count += 1
                self.log.emit(f"转换成功: {os.path.basename(file_path)}")
            except Exception as e:
                self.fail_count += 1
                self.log.emit(f"转换失败: {os.path.basename(file_path)} - {str(e)}")
            self.progress.emit(int((i + 1) / total * 100))
        self.finished.emit(True, f"完成！成功: {self.success_count}, 失败: {self.fail_count}")


class AboutDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("关于")
        self.setFixedSize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("PDF to Word 转换器")
        title.setFont(QFont("Microsoft YaHei", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        version = QLabel("版本: 1.0.0")
        version.setAlignment(Qt.AlignCenter)

        author = QLabel("作者: PDF转换开发团队")
        author.setAlignment(Qt.AlignCenter)

        desc = QLabel("一个简洁高效的PDF转Word工具\n基于PySide6和popdf开发")
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("color: #94a3b8; padding: 20px;")

        btn = QPushButton("关闭")
        btn.clicked.connect(self.close)
        btn.setFixedHeight(35)

        layout.addWidget(title)
        layout.addWidget(version)
        layout.addWidget(author)
        layout.addWidget(desc)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f172a, stop:1 #1e3a8a);
                color: #e2e8f0;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #1d4ed8);
                border: none;
                border-radius: 8px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #60a5fa, stop:1 #3b82f6);
            }
        """)


class HelpDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("帮助")
        self.setFixedSize(500, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("使用说明")
        title.setFont(QFont("Microsoft YaHei", 14, QFont.Bold))

        help_text = QTextEdit()
        help_text.setReadOnly(True)
        help_text.setHtml("""
        <h3 style="color: #60a5fa;">常见问题</h3>
        <p><b>Q: 如何转换单个PDF文件？</b><br>
        A: 点击"选择文件"按钮，选择一个PDF文件，然后选择输出目录，点击"开始转换"即可。</p>

        <p><b>Q: 如何批量转换PDF文件？</b><br>
        A: 点击"选择文件夹"按钮，选择包含多个PDF文件的文件夹，然后选择输出目录，点击"批量转换"即可。</p>

        <p><b>Q: 转换后的Word文件保存在哪里？</b><br>
        A: 默认保存在您选择的输出目录中，文件名与原PDF文件相同。</p>

        <p><b>Q: 转换失败怎么办？</b><br>
        A: 请确保：<br>
        - PDF文件没有加密<br>
        - PDF文件不是扫描件（图片型PDF需要先OCR处理）<br>
        - 输出目录有写入权限</p>

        <h3 style="color: #60a5fa;">快捷键</h3>
        <p>Ctrl + O: 打开文件<br>
        Ctrl + D: 打开文件夹<br>
        Ctrl + R: 开始转换</p>
        """)
        help_text.setStyleSheet("""
            QTextEdit {
                background: rgba(30, 41, 59, 0.9);
                border: 1px solid #3b82f6;
                border-radius: 8px;
                color: #e2e8f0;
                padding: 10px;
            }
        """)

        btn = QPushButton("关闭")
        btn.clicked.connect(self.close)
        btn.setFixedHeight(35)

        layout.addWidget(title)
        layout.addWidget(help_text)
        layout.addWidget(btn)

        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f172a, stop:1 #1e3a8a);
                color: #e2e8f0;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #1d4ed8);
                border: none;
                border-radius: 8px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #60a5fa, stop:1 #3b82f6);
            }
            QLabel {
                color: #e2e8f0;
            }
        """)


class SettingsDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("设置")
        self.setFixedSize(400, 350)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("转换设置")
        title.setFont(QFont("Microsoft YaHei", 14, QFont.Bold))

        quality_box = QGroupBox("转换质量")
        quality_layout = QVBoxLayout()

        self.quality_combo = QComboBox()
        self.quality_combo.addItems(["快速（低质量）", "平衡（中质量）", "高质量（慢速）"])
        self.quality_combo.setCurrentIndex(1)

        quality_layout.addWidget(QLabel("转换速度与质量平衡:"))
        quality_layout.addWidget(self.quality_combo)
        quality_box.setLayout(quality_layout)

        output_box = QGroupBox("输出设置")
        output_layout = QVBoxLayout()

        self.same_dir_check = QCheckBox("转换到源文件同一目录")
        self.same_dir_check.setChecked(True)

        self.overwrite_check = QCheckBox("覆盖已存在的文件")
        self.overwrite_check.setChecked(False)

        output_layout.addWidget(self.same_dir_check)
        output_layout.addWidget(self.overwrite_check)
        output_box.setLayout(output_layout)

        btn_layout = QHBoxLayout()
        save_btn = QPushButton("保存")
        save_btn.clicked.connect(self.save_settings)
        cancel_btn = QPushButton("取消")
        cancel_btn.clicked.connect(self.close)

        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)

        layout.addWidget(title)
        layout.addWidget(quality_box)
        layout.addWidget(output_box)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f172a, stop:1 #1e3a8a);
                color: #e2e8f0;
            }
            QGroupBox {
                background: rgba(30, 41, 59, 0.8);
                border: 1px solid #3b82f6;
                border-radius: 8px;
                padding: 15px;
                margin-top: 10px;
            }
            QGroupBox::title {
                color: #60a5fa;
                subcontrol-origin: margin;
            }
            QComboBox, QSpinBox {
                background: rgba(30, 41, 59, 0.9);
                border: 1px solid #3b82f6;
                border-radius: 4px;
                padding: 5px;
                color: #e2e8f0;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #1d4ed8);
                border: none;
                border-radius: 8px;
                color: white;
                font-weight: bold;
                padding: 8px 20px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #60a5fa, stop:1 #3b82f6);
            }
        """)

    def save_settings(self):
        self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.files = []
        self.output_dir = ""
        self.convert_thread = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PDF to Word 转换器")
        self.setFixedSize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(30, 30, 30, 30)

        header = QLabel("PDF to Word 转换器")
        header.setFont(QFont("Microsoft YaHei", 20, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)

        desc = QLabel("简单、高效、专业的PDF转Word解决方案")
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet("color: #94a3b8; margin-bottom: 20px;")

        file_box = QGroupBox("文件选择")
        file_layout = QVBoxLayout()

        file_btn_layout = QHBoxLayout()
        self.single_btn = QPushButton("选择文件")
        self.single_btn.clicked.connect(self.select_file)
        self.folder_btn = QPushButton("选择文件夹")
        self.folder_btn.clicked.connect(self.select_folder)

        file_btn_layout.addWidget(self.single_btn)
        file_btn_layout.addWidget(self.folder_btn)

        self.file_label = QLabel("未选择任何文件")
        self.file_label.setStyleSheet("color: #94a3b8; padding: 10px;")

        file_layout.addLayout(file_btn_layout)
        file_layout.addWidget(self.file_label)
        file_box.setLayout(file_layout)

        output_box = QGroupBox("输出设置")
        output_layout = QHBoxLayout()

        self.output_input = QLineEdit()
        self.output_input.setPlaceholderText("选择输出目录...")
        self.output_btn = QPushButton("选择输出目录")
        self.output_btn.clicked.connect(self.select_output)

        output_layout.addWidget(self.output_input)
        output_layout.addWidget(self.output_btn)
        output_box.setLayout(output_layout)

        self.progress = QProgressBar()
        self.progress.setVisible(False)
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #3b82f6;
                border-radius: 8px;
                background: rgba(30, 41, 59, 0.9);
                height: 25px;
                text-align: center;
                color: white;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00b4ff, stop:1 #3b82f6);
                border-radius: 6px;
            }
        """)

        self.log_edit = QTextEdit()
        self.log_edit.setReadOnly(True)
        self.log_edit.setMaximumHeight(150)
        self.log_edit.setPlaceholderText("转换日志...")
        self.log_edit.setStyleSheet("""
            QTextEdit {
                background: rgba(15, 23, 42, 0.9);
                border: 1px solid #3b82f6;
                border-radius: 8px;
                color: #e2e8f0;
                padding: 10px;
            }
        """)

        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("开始转换")
        self.start_btn.clicked.connect(self.start_convert)
        self.open_btn = QPushButton("打开输出目录")
        self.open_btn.clicked.connect(self.open_output_dir)
        self.exit_btn = QPushButton("退出")
        self.exit_btn.clicked.connect(self.close)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.open_btn)
        btn_layout.addWidget(self.exit_btn)

        menu_bar = self.menuBar()
        tool_menu = menu_bar.addMenu("工具")

        about_action = tool_menu.addAction("关于")
        about_action.triggered.connect(self.show_about)

        help_action = tool_menu.addAction("帮助")
        help_action.triggered.connect(self.show_help)

        settings_action = tool_menu.addAction("设置")
        settings_action.triggered.connect(self.show_settings)

        main_layout.addWidget(header)
        main_layout.addWidget(desc)
        main_layout.addWidget(file_box)
        main_layout.addWidget(output_box)
        main_layout.addWidget(self.progress)
        main_layout.addWidget(self.log_edit)
        main_layout.addLayout(btn_layout)

        central_widget.setLayout(main_layout)

        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f172a, stop:0.5 #1e3a8a, stop:1 #0f172a);
            }
            QGroupBox {
                background: rgba(30, 41, 59, 0.8);
                border: 2px solid #3b82f6;
                border-radius: 10px;
                padding: 15px;
                margin-top: 15px;
                font-weight: bold;
            }
            QGroupBox::title {
                color: #60a5fa;
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #1d4ed8);
                border: 2px solid #60a5fa;
                border-radius: 8px;
                color: white;
                font-weight: bold;
                padding: 10px 20px;
                min-width: 100px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #60a5fa, stop:1 #3b82f6);
                border: 2px solid #93c5fd;
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1d4ed8, stop:1 #1e40af);
            }
            QPushButton:disabled {
                background: #475569;
                border: 2px solid #64748b;
                color: #94a3b8;
            }
            QLineEdit {
                background: rgba(30, 41, 59, 0.9);
                border: 2px solid #3b82f6;
                border-radius: 6px;
                padding: 10px;
                color: #e2e8f0;
            }
            QLineEdit:focus {
                border: 2px solid #00b4ff;
            }
            QLabel {
                color: #e2e8f0;
            }
            QMenuBar {
                background: rgba(30, 41, 59, 0.95);
                color: #e2e8f0;
            }
            QMenuBar::item:selected {
                background: #3b82f6;
            }
            QMenu {
                background: rgba(30, 41, 59, 0.98);
                border: 1px solid #3b82f6;
                color: #e2e8f0;
            }
            QMenu::item:selected {
                background: #3b82f6;
            }
        """)

    def select_file(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "选择PDF文件", "", "PDF Files (*.pdf)"
        )
        if files:
            self.files = files
            self.file_label.setText(f"已选择 {len(files)} 个文件:\n" + "\n".join([os.path.basename(f) for f in files[:5]]))
            if len(files) > 5:
                self.file_label.setText(self.file_label.text() + f"\n... 还有 {len(files) - 5} 个文件")

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if folder:
            self.files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.pdf')]
            self.file_label.setText(f"已选择文件夹: {folder}\n包含 {len(self.files)} 个PDF文件")

    def select_output(self):
        folder = QFileDialog.getExistingDirectory(self, "选择输出目录")
        if folder:
            self.output_dir = folder
            self.output_input.setText(folder)

    def start_convert(self):
        if not self.files:
            QMessageBox.warning(self, "提示", "请先选择PDF文件！")
            return
        if not self.output_dir:
            QMessageBox.warning(self, "提示", "请选择输出目录！")
            return

        self.progress.setVisible(True)
        self.progress.setValue(0)
        self.start_btn.setEnabled(False)
        self.log_edit.clear()

        self.convert_thread = ConvertThread(self.files, self.output_dir)
        self.convert_thread.progress.connect(self.progress.setValue)
        self.convert_thread.log.connect(self.log_edit.append)
        self.convert_thread.finished.connect(self.convert_finished)
        self.convert_thread.start()

    def convert_finished(self, success, message):
        self.progress.setValue(100)
        self.start_btn.setEnabled(True)
        self.log_edit.append(message)

        total_size = 0
        for f in self.files:
            try:
                total_size += os.path.getsize(f)
            except:
                pass

        QMessageBox.information(self, "转换完成", f"{message}\n总文件大小: {total_size / 1024 / 1024:.2f} MB")

    def open_output_dir(self):
        if self.output_dir and os.path.exists(self.output_dir):
            os.startfile(self.output_dir) if sys.platform == 'win32' else os.system(f'open "{self.output_dir}"')
        else:
            QMessageBox.warning(self, "提示", "请先设置输出目录！")

    def show_about(self):
        self.about_dialog = AboutDialog()
        self.about_dialog.show()

    def show_help(self):
        self.help_dialog = HelpDialog()
        self.help_dialog.show()

    def show_settings(self):
        self.settings_dialog = SettingsDialog()
        self.settings_dialog.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
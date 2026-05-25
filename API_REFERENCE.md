# popdf API 参考文档

## 概述

`popdf` 是一个用于PDF文件自动化处理的Python库，提供了丰富的PDF操作功能。

## 安装

```bash
pip install popdf
```

## 快速开始

```python
import popdf

# PDF转Word
popdf.pdf2docx(input_file='input.pdf', output_file='output.docx')

# PDF转图片
popdf.pdf2imgs(input_file='document.pdf', output_path='/images/')

# PDF加密
popdf.encrypt4pdf(password='secret', input_file='input.pdf', output_file='encrypted.pdf')
```

## API 接口列表

### 1. pdf2docx - PDF转Word

将PDF文件转换为Microsoft Word文档（.docx格式）。

```python
def pdf2docx(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None
```

**参数说明：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| input_file | str | 否 | 输入的单个PDF文件路径 |
| output_file | str | 否 | 输出的单个Word文件路径（需带.docx后缀） |
| input_path | str | 否 | 批量转换时的输入目录路径 |
| output_path | str | 否 | 批量转换时的输出目录路径 |

**使用示例：**

```python
# 单文件转换
popdf.pdf2docx(input_file='document.pdf', output_file='document.docx')

# 批量转换
popdf.pdf2docx(input_path='/pdfs/', output_path='/docs/')
```

---

### 2. pdf2imgs - PDF转图片

将PDF文件转换为图片格式。

```python
def pdf2imgs(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None,
    merge: bool = False
) -> None
```

**参数说明：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| input_file | str | 否 | 输入的单个PDF文件路径 |
| output_file | str | 否 | 合并模式时的输出图片路径 |
| input_path | str | 否 | 批量转换时的输入目录路径 |
| output_path | str | 否 | 批量转换时的输出目录路径 |
| merge | bool | 否 | 是否合并为单张图片，默认False |

**使用示例：**

```python
# 转换为多张图片
popdf.pdf2imgs(input_file='document.pdf', output_path='/images/')

# 合并为单张图片
popdf.pdf2imgs(input_file='document.pdf', output_file='merged.png', merge=True)
```

---

### 3. txt2pdf - TXT转PDF

将文本文件转换为PDF文件。

```python
def txt2pdf(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None
```

**使用示例：**

```python
popdf.txt2pdf(input_file='readme.txt', output_file='readme.pdf')
```

---

### 4. split4pdf - PDF分割

截取PDF文件的指定页面范围。

```python
def split4pdf(
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None,
    from_page: int = 1,
    to_page: int = -1
) -> bool
```

**参数说明：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| from_page | int | 否 | 起始页码，默认1 |
| to_page | int | 否 | 结束页码，默认-1（最后一页） |

**使用示例：**

```python
popdf.split4pdf(input_file='document.pdf', output_file='pages_1-5.pdf', from_page=1, to_page=5)
```

---

### 5. encrypt4pdf - PDF加密

给PDF文件添加密码保护。

```python
def encrypt4pdf(
    password: str,
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None
```

**使用示例：**

```python
popdf.encrypt4pdf(password='mypassword', input_file='document.pdf', output_file='encrypted.pdf')
```

---

### 6. decrypt4pdf - PDF解密

解密受密码保护的PDF文件。

```python
def decrypt4pdf(
    input_file: Optional[str] = None,
    password: Optional[str] = None,
    output_file: str = 'decrypt.pdf',
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None
```

**使用示例：**

```python
popdf.decrypt4pdf(input_file='encrypted.pdf', password='mypassword', output_file='decrypted.pdf')
```

---

### 7. add_text_watermark - 添加文本水印

在PDF文档中添加文本水印。

```python
def add_text_watermark(
    input_file: str,
    point: Tuple[int, int],
    text: str = 'www.python-office.com',
    output_file: str = './pdf_watermark.pdf',
    fontname: str = "Helvetica",
    fontsize: int = 12,
    color: Tuple[float, float, float] = (1, 0, 0)
) -> None
```

**参数说明：**

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| point | tuple | 是 | 水印位置(x, y) |
| color | tuple | 否 | RGB颜色，范围0-1，默认红色(1,0,0) |

**使用示例：**

```python
popdf.add_text_watermark(
    input_file='document.pdf', 
    point=(100, 100), 
    text='机密', 
    color=(0.5, 0.5, 0.5)
)
```

---

### 8. merge2pdf - PDF合并

合并多个PDF文件为一个PDF文件。

```python
def merge2pdf(
    input_file_list: List[str],
    output_file: str
) -> None
```

**使用示例：**

```python
popdf.merge2pdf(input_file_list=['part1.pdf', 'part2.pdf'], output_file='merged.pdf')
```

---

### 9. del4pdf - 删除PDF页面

删除PDF文件中的指定页码。

```python
def del4pdf(
    page_nums: List[int],
    input_file: Optional[str] = None,
    output_file: Optional[str] = None,
    input_path: Optional[str] = None,
    output_path: Optional[str] = None
) -> None
```

**使用示例：**

```python
popdf.del4pdf(page_nums=[2, 4], input_file='document.pdf', output_file='cleaned.pdf')
```

---

## 批量处理模式

所有API都支持批量处理模式，只需提供`input_path`和`output_path`参数：

```python
# 批量转换PDF到Word
popdf.pdf2docx(input_path='/pdfs/', output_path='/docs/')

# 批量加密PDF
popdf.encrypt4pdf(password='secret', input_path='/pdfs/', output_path='/encrypted/')
```

## 错误处理

所有函数都内置了错误处理机制，当参数填写错误时会抛出`ValueError`并记录日志。

## 版本信息

- **版本**: 1.0.8
- **作者**: 程序员晚枫
- **许可证**: MIT
- **官方文档**: https://www.python-office.com/office/pdf.html
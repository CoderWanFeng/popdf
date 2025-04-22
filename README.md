<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>


<p align="center">
  <a target="_blank" href='https://github.com/CoderWanFeng/popdf'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/popdf.svg?style=social" alt="github star"/>
    </a>
        <a target="_blank" href='https://gitcode.com/python4office/popdf'>
		<img src='https://gitcode.com/python4office/popdf/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>
 <a target="_blank" href='https://github.com/CoderWanFeng/popdf'>
<img src="https://static.pepy.tech/badge/popdf" alt="PyPI Downloads">
</a>
</p>



-------------------------------------------------------------------------------

## 📚简介

popdf 是python自动化办公之Excel操作的第三方库。


-------------------------------------------------------------------------------

## 📦安装

### 🍊pip 自动下载&更新


#### 源码安装

```
git clone https://gitcode.com/python4office/popdf.git

cd popdf

pip install -e .
```


#### 源安装&更新

我使用的是阿里云镜像。如果你的网络环境无法访问阿里云镜像，请自行更换为其他镜像。


```
pip install -i https://mirrors.aliyun.com/pypi/simple/ popdf -U
```

-------------------------------------------------------------------------------

## 📝功能

已有功能的说明如下：


| 序号 | 功能        | 视频                                                  | 文档                                                                                             |
| ---- | ----------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 1    | 下载和安装  | 💻 [播放](https://www.bilibili.com/video/BV1BS9UYGEW7) | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/0-install)             |
| 2    | PDF 转 Word | 💻 [播放](https://www.bilibili.com/video/BV1pB9UYSEoG) | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/)           |
| 3    | PDF 转 图片 | 💻[播放](https://www.bilibili.com/video/BV19WRVYKEEY)  | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/)           |
| 4    | TXT转PDF    | [播放](https://www.bilibili.com/video/BV1aCQ5YhEBm)   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/)            |
| 5    | 按页切割PDF | 💻[播放](https://www.bilibili.com/video/BV1PYQpY3E8z)  | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/)          |
| 6    | PDF加密     | [播放](https://www.bilibili.com/video/BV1n1QPYJE61)   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/)        |
| 7    | PDF解密     | [播放](https://www.bilibili.com/video/BV11FQ6YdEU1)   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf/)        |
| 8    | PDF加水印   | [播放](https://www.bilibili.com/video/BV1x7QtYdEJt)   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_text_watermark/) |
| 9    | 合并PDF     | [播放](https://www.bilibili.com/video/BV1NNQhYaEVG)   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf/)          |
| 10   | 删除PDF     | [播放](https://www.bilibili.com/video/BV1KPQhYAENX)   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf/)            |

## 🏗️添砖加瓦

本项目欢迎任何人参与开发，如果是小白，可以看一下开发教程👉[如何参与开源项目？0基础入门：怎么打开GitHub？什么是issue？什么是PR？](https://www.bilibili.com/video/BV1EP411d7Np/?spm_id_from=333.999.0.0)


#### 目录结构和pr要求如下：

- docs：存放该项目的文档，包括教程、案例等。
- examples：存放该项目的案例，**如果你有新增功能或者接口，请在这里新建一个py文件，并在这里写一个使用案例。**
- popdf：存放该项目的源代码，其中：
    - api：提供外部调用的接口。
    - core：存放该项目的核心代码，包括类、函数等。
    - lib：存放工具类、工具函数等。
- tests：存放该项目的单元测试的代码，其中：
    - test_code：存放测试代码，**每新增/修改任一个函数，提交之前必须写单元测试**！
    - test_files：存放测试文件，包括图片、Excel等。
- README.md、requirement.txt、setup等文件，一般不修改。


### 🐞提供bug反馈或建议

提交问题反馈时，请务必填写和该项目本身有关的问题，不进行有关python学习，甚至是个人练习的知识答疑和讨论。

- [Github issue](https://github.com/CoderWanFeng/popdf/issues)
- [gitee issue](https://gitee.com/CoderWanFeng/popdf/issues)
- [GitCode issue](https://gitcode.com/python4office/popdf/issues)

### 🧬贡献代码的步骤

1. 在Gitee/Github/GitCode上fork项目到自己的repo
2. 把fork过去的项目也就是你的项目clone到你的本地
3. 修改代码
4. commit后push到自己的库
5. 登录Gitee/Github/GitCode在你首页可以看到一个 pull request 按钮，点击它，填写一些说明信息，然后提交到master/main分支即可。
6. 等待程序员晚枫合并，＋微信说一声更好👉[CoderWanFeng](http://python4office.cn/wechat-qrcode/)

-------------------------------------------------------------------------------

## 📕参考文档

- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/index.html)
- [click](https://click.palletsprojects.com/en/stable/options/)
- [python-office](https://www.python-office.com/)

## 📌联系作者

<p align="center" id='开源交流群-banner'>
<a target="_blank" href='https://cos.python-office.com/group%2Ffree-group.jpg'>
<img src="https://cos.python-office.com/group/python-office-qr.jpg" width="100%"/>
</a> 
</p>


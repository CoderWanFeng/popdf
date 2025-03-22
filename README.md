<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>

<p align="center">
 <a target="_blank" href='https://github.com/CoderWanFeng/popdf'>
<img src="https://static.pepy.tech/badge/popdf" alt="PyPI Downloads">
</a>
</p>



-------------------------------------------------------------------------------

## 📚简介

popdf 是python自动化办公之Excel操作的第三方库。

来自于开源项目：python-office，[📘官网：https://www.python-office.com/](https://www.python-office.com/)。

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

| 序号 | 方法名             | 功能         | 视频                                                                    | 文档                                                                                             |
|----| ------------------ | ------------ | ----------------------------------------------------------------------- |------------------------------------------------------------------------------------------------|
| 1  | pdf2docx           | 💻PDF 转 Word | 💻 [播放](https://www.bilibili.com/video/BV1em4y1H7ir)                   | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/1-pdf2docx/)           |
| 2  | pdf2imgs           | PDF 转 图片  | 💻[文档](https://mp.weixin.qq.com/s/Ve5FH6q6ZqNbhUUG9RR8aw)              | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/2-pdf2imgs/)           |
| 3  | txt2pdf            | TXT转PDF     | [文档](https://blog.csdn.net/weixin_42321517/article/details/130612189) | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/3-txt2pdf/)            |
| 4  | split4pdf          | 按页切割PDF  | 💻[文档](https://mp.weixin.qq.com/s/Ve5FH6q6ZqNbhUUG9RR8aw)              | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/4-split4pdf/)          |
| 5  | encrypt4pdf        | PDF加密      | [文档](https://blog.csdn.net/weixin_42321517/article/details/129963432) | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/5-encrypt4pdf/)        |
| 6  | decrypt4pdf        | PDF解密      | [文档](https://mp.weixin.qq.com/s/GiXYB_xZdlsYv5AIeIELkA)               | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/6-decrypt4pdf/)        |
| 7  | add_text_watermark | PDF加水印    | [播放](https://www.bilibili.com/video/BV1Se411T7au)                     | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/7-add_text_watermark/) |
| 8  | merge2pdf          | 合并PDF      | [文档](https://baijiahao.baidu.com/s?id=1733062611567959337)            | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/8-merge2pdf/)          |
| 9  | del4pdf          | 合并PDF      | [文档](https://baijiahao.baidu.com/s?id=1733062611567959337)            | [查看](http://www.python4office.cn/python-office/popdf/%E8%AF%BE%E7%A8%8B/9-del4pdf/)            |

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
    - test)files：存放测试文件，包括图片、Excel等。
- README.md、requirement.txt、setup等文件，一般不修改。


### 🐞提供bug反馈或建议

提交问题反馈时，请务必填写和该项目本身有关的问题，不进行有关python学习，甚至是个人练习的知识答疑和讨论。

- [Github issue](https://github.com/CoderWanFeng/popdf/issues)
- [gitee issue](https://gitee.com/CoderWanFeng/popdf/issues)
- [GitCode issue](https://gitcode.com/python4office/popdf/issues)

### 🧬贡献代码的步骤

1. 在Gitee或者Github上fork项目到自己的repo
2. 把fork过去的项目也就是你的项目clone到你的本地
3. 修改代码
4. commit后push到自己的库
5. 登录Gitee或Github在你首页可以看到一个 pull request 按钮，点击它，填写一些说明信息，然后提交到master分支即可。
6. 等待程序员晚枫合并，＋微信说一声更好👉[CoderWanFeng](http://python4office.cn/wechat-qrcode/)

-------------------------------------------------------------------------------

## 📕参考文档

- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/index.html)
- [python-office](https://www.python-office.com/)

## 📌联系作者

<p align="center" id='开源交流群-banner'>
<a target="_blank" href='https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/python-office.jpg'>
<img src="https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/group/python-office-qr.jpg" width="100%"/>
</a> 
</p>

## 读者福利

几个没有套路的福利，每天都可以领一次~

<p align="center" id='福利合集-banner'>
    <a target="_blank" href='http://python4office.cn/sideline-pro-list/'>
    <img src="https://python-office-1300615378.cos.ap-chongqing.myqcloud.com/ads/fuli/all-1.jpg" width="100%"/>
    </a>   
</p>
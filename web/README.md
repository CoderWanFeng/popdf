# POPDF Web - 在线PDF处理工具

基于React + TypeScript + Tailwind CSS构建的现代化PDF处理Web应用，将桌面GUI软件的功能完整迁移到Web平台。

## 🌟 功能特性

### 📄 PDF查看器
- 高质量PDF文档渲染
- 缩放、旋转、页面导航
- 文本搜索功能
- 缩略图导航

### 🔄 格式转换
- **PDF转Word** - 转换为可编辑的Word文档
- **PDF转图片** - 支持JPG/PNG格式，可设置分辨率
- **文本转PDF** - 将文本文件转换为PDF格式

### ✏️ 编辑工具
- **添加水印** - 自定义文本水印，支持位置、透明度、旋转
- **删除页面** - 按页码或范围删除指定页面

### 🔒 安全工具
- **PDF加密** - 添加密码保护，设置权限控制
- **PDF解密** - 移除PDF文件的密码保护

### 📚 组织工具
- **PDF分割** - 按页面范围分割PDF文件
- **PDF合并** - 将多个PDF文件合并为一个

## 🚀 快速开始

### 环境要求
- Node.js 16.0+
- npm 或 yarn

### 安装依赖
```bash
cd web
npm install
```

### 开发模式
```bash
npm run dev
```
访问 http://localhost:3000

### 构建生产版本
```bash
npm run build
```

### 预览生产版本
```bash
npm run preview
```

## 🛠️ 技术栈

- **前端框架**: React 18 + TypeScript
- **样式框架**: Tailwind CSS
- **PDF处理**: PDF.js + react-pdf
- **构建工具**: Vite
- **图标库**: Lucide React
- **代码质量**: ESLint + TypeScript

## 📁 项目结构

```
web/
├── src/
│   ├── components/          # React组件
│   │   ├── Header.tsx      # 顶部导航
│   │   ├── Sidebar.tsx     # 侧边栏菜单
│   │   ├── MainContent.tsx # 主内容区域
│   │   ├── FileUpload.tsx  # 文件上传
│   │   ├── PDFViewer.tsx   # PDF查看器
│   │   ├── PDFConverter.tsx # 格式转换
│   │   ├── PDFEditor.tsx   # 编辑工具
│   │   ├── PDFSecurity.tsx # 安全工具
│   │   └── PDFOrganizer.tsx # 组织工具
│   ├── contexts/           # React Context
│   │   └── FileContext.tsx # 文件状态管理
│   ├── types.ts            # TypeScript类型定义
│   ├── App.tsx             # 主应用组件
│   ├── main.tsx           # 应用入口
│   └── index.css          # 全局样式
├── public/                 # 静态资源
├── package.json           # 项目配置
├── vite.config.ts         # Vite配置
├── tailwind.config.js     # Tailwind配置
└── tsconfig.json          # TypeScript配置
```

## 🎨 界面特色

- **现代化设计**: 采用毛玻璃效果和渐变色彩
- **响应式布局**: 完美适配桌面和移动设备
- **暗色模式**: 支持亮色/暗色主题切换
- **流畅动画**: 丰富的交互动画效果
- **直观操作**: 拖拽上传、批量处理等便捷功能

## 🔒 数据安全

- **本地处理**: 所有PDF操作都在浏览器本地完成
- **无服务器上传**: 文件不会上传到任何服务器
- **隐私保护**: 确保用户数据完全私密

## 🌐 浏览器兼容性

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📈 性能优化

- **代码分割**: 按需加载组件
- **懒加载**: PDF页面按需渲染
- **缓存策略**: 优化重复操作性能
- **压缩优化**: 构建产物优化

## 🚀 部署

### Vercel部署
```bash
npm run build
# 将dist目录部署到Vercel
```

### Netlify部署
```bash
npm run build
# 将dist目录部署到Netlify
```

### 静态服务器部署
```bash
npm run build
# 将dist目录部署到任何静态文件服务器
```

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 📄 许可证

本项目基于MIT许可证开源。

## 🙏 致谢

- [PDF.js](https://mozilla.github.io/pdf.js/) - Mozilla的PDF渲染库
- [React-PDF](https://react-pdf.org/) - React PDF组件
- [Tailwind CSS](https://tailwindcss.com/) - 实用优先的CSS框架
- [Lucide](https://lucide.dev/) - 精美图标库

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- 提交Issue
- 发送邮件

---

**POPDF Web** - 让PDF处理更简单、更安全！
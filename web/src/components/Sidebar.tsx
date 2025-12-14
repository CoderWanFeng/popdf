import React from 'react'
import { 
  Upload, 
  FileText, 
  Image, 
  FileInput, 
  Lock, 
  Unlock, 
  Split, 
  Merge, 
  Trash2,
  Type,
  Download
} from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'

const operations = [
  {
    id: 'viewer',
    name: 'PDF查看器',
    icon: FileText,
    category: 'viewer'
  },
  {
    id: 'upload',
    name: '上传PDF',
    icon: Upload,
    category: 'upload'
  },
  {
    id: 'pdf2docx',
    name: 'PDF转Word',
    icon: FileInput,
    category: 'conversion',
    description: '将PDF转换为可编辑的Word文档'
  },
  {
    id: 'pdf2imgs',
    name: 'PDF转图片',
    icon: Image,
    category: 'conversion',
    description: '将PDF页面转换为图片格式'
  },
  {
    id: 'txt2pdf',
    name: '文本转PDF',
    icon: Type,
    category: 'conversion',
    description: '将文本文件转换为PDF格式'
  },
  {
    id: 'split4pdf',
    name: 'PDF分割',
    icon: Split,
    category: 'organize',
    description: '按页面范围分割PDF文件'
  },
  {
    id: 'encrypt4pdf',
    name: 'PDF加密',
    icon: Lock,
    category: 'security',
    description: '为PDF文件添加密码保护'
  },
  {
    id: 'decrypt4pdf',
    name: 'PDF解密',
    icon: Unlock,
    category: 'security',
    description: '移除PDF文件的密码保护'
  },
  {
    id: 'addWatermark',
    name: '添加水印',
    icon: Type,
    category: 'edit',
    description: '在PDF中添加自定义文本水印'
  },
  {
    id: 'merge2pdf',
    name: 'PDF合并',
    icon: Merge,
    category: 'organize',
    description: '将多个PDF文件合并为一个'
  },
  {
    id: 'del4pdf',
    name: '删除页面',
    icon: Trash2,
    category: 'edit',
    description: '删除PDF中的指定页面'
  }
]

const Sidebar: React.FC = () => {
  const { activeTab, setActiveTab, currentFile } = useFileContext()

  const categories = {
    viewer: operations.filter(op => op.category === 'viewer'),
    upload: operations.filter(op => op.category === 'upload'),
    conversion: operations.filter(op => op.category === 'conversion'),
    edit: operations.filter(op => op.category === 'edit'),
    security: operations.filter(op => op.category === 'security'),
    organize: operations.filter(op => op.category === 'organize')
  }

  return (
    <aside className="w-80 bg-white/30 dark:bg-slate-800/30 border-r border-white/20 dark:border-slate-700/50 overflow-y-auto">
      <div className="p-6">
        {/* 文件上传区域 */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold text-slate-700 dark:text-slate-300 mb-4">
            文件操作
          </h3>
          {categories.upload.map(operation => (
            <button
              key={operation.id}
              onClick={() => setActiveTab(operation.id)}
              className={`w-full flex items-center space-x-3 p-3 rounded-lg mb-2 transition-all duration-200 ${
                activeTab === operation.id
                  ? 'bg-primary-500 text-white shadow-lg'
                  : 'bg-white/50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-white/80 dark:hover:bg-slate-600/80'
              }`}
            >
              <operation.icon className="h-5 w-5" />
              <span className="font-medium">{operation.name}</span>
            </button>
          ))}
        </div>

        {/* 查看器 */}
        {currentFile && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-slate-700 dark:text-slate-300 mb-4">
              查看工具
            </h3>
            {categories.viewer.map(operation => (
              <button
                key={operation.id}
                onClick={() => setActiveTab(operation.id)}
                className={`w-full flex items-center space-x-3 p-3 rounded-lg mb-2 transition-all duration-200 ${
                  activeTab === operation.id
                    ? 'bg-primary-500 text-white shadow-lg'
                    : 'bg-white/50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-white/80 dark:hover:bg-slate-600/80'
                }`}
              >
                <operation.icon className="h-5 w-5" />
                <span className="font-medium">{operation.name}</span>
              </button>
            ))}
          </div>
        )}

        {/* 转换工具 */}
        {currentFile && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-slate-700 dark:text-slate-300 mb-4">
              转换工具
            </h3>
            {categories.conversion.map(operation => (
              <button
                key={operation.id}
                onClick={() => setActiveTab(operation.id)}
                className={`w-full flex items-center space-x-3 p-3 rounded-lg mb-2 transition-all duration-200 ${
                  activeTab === operation.id
                    ? 'bg-primary-500 text-white shadow-lg'
                    : 'bg-white/50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-white/80 dark:hover:bg-slate-600/80'
                }`}
              >
                <operation.icon className="h-5 w-5" />
                <span className="font-medium">{operation.name}</span>
              </button>
            ))}
          </div>
        )}

        {/* 编辑工具 */}
        {currentFile && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-slate-700 dark:text-slate-300 mb-4">
              编辑工具
            </h3>
            {categories.edit.map(operation => (
              <button
                key={operation.id}
                onClick={() => setActiveTab(operation.id)}
                className={`w-full flex items-center space-x-3 p-3 rounded-lg mb-2 transition-all duration-200 ${
                  activeTab === operation.id
                    ? 'bg-primary-500 text-white shadow-lg'
                    : 'bg-white/50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-white/80 dark:hover:bg-slate-600/80'
                }`}
              >
                <operation.icon className="h-5 w-5" />
                <span className="font-medium">{operation.name}</span>
              </button>
            ))}
          </div>
        )}

        {/* 安全工具 */}
        {currentFile && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-slate-700 dark:text-slate-300 mb-4">
              安全工具
            </h3>
            {categories.security.map(operation => (
              <button
                key={operation.id}
                onClick={() => setActiveTab(operation.id)}
                className={`w-full flex items-center space-x-3 p-3 rounded-lg mb-2 transition-all duration-200 ${
                  activeTab === operation.id
                    ? 'bg-primary-500 text-white shadow-lg'
                    : 'bg-white/50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-white/80 dark:hover:bg-slate-600/80'
                }`}
              >
                <operation.icon className="h-5 w-5" />
                <span className="font-medium">{operation.name}</span>
              </button>
            ))}
          </div>
        )}

        {/* 组织工具 */}
        {currentFile && (
          <div className="mb-8">
            <h3 className="text-lg font-semibold text-slate-700 dark:text-slate-300 mb-4">
              组织工具
            </h3>
            {categories.organize.map(operation => (
              <button
                key={operation.id}
                onClick={() => setActiveTab(operation.id)}
                className={`w-full flex items-center space-x-3 p-3 rounded-lg mb-2 transition-all duration-200 ${
                  activeTab === operation.id
                    ? 'bg-primary-500 text-white shadow-lg'
                    : 'bg-white/50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-white/80 dark:hover:bg-slate-600/80'
                }`}
              >
                <operation.icon className="h-5 w-5" />
                <span className="font-medium">{operation.name}</span>
              </button>
            ))}
          </div>
        )}
      </div>
    </aside>
  )
}

export default Sidebar
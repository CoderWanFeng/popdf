import React, { useState } from 'react'
import { FileText, Type, Trash2, Download } from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'

const PDFEditor: React.FC = () => {
  const { currentFile, activeTab } = useFileContext()
  const [processing, setProcessing] = useState(false)
  const [options, setOptions] = useState({
    // 添加水印选项
    addWatermark: {
      text: '保密文件',
      fontSize: 24,
      opacity: 0.3,
      position: 'center' as 'center' | 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right',
      rotation: 45
    },
    // 删除页面选项
    del4pdf: {
      pages: '1'
    }
  })

  const editorTypes = {
    addWatermark: {
      icon: Type,
      title: '添加水印',
      description: '在PDF中添加自定义文本水印'
    },
    del4pdf: {
      icon: Trash2,
      title: '删除页面',
      description: '删除PDF中的指定页面'
    }
  }

  const currentType = editorTypes[activeTab as keyof typeof editorTypes]

  const handleProcess = async () => {
    if (!currentFile) return
    
    setProcessing(true)
    
    try {
      // 模拟处理过程
      await new Promise(resolve => setTimeout(resolve, 2000))
      
      console.log('开始处理:', currentFile.name, '选项:', options)
      
      // 模拟下载链接
      const downloadUrl = URL.createObjectURL(new Blob(['模拟处理结果'], { type: 'application/octet-stream' }))
      
      const link = document.createElement('a')
      link.href = downloadUrl
      link.download = `${currentFile.name.replace('.pdf', '')}_processed.pdf`
      link.click()
      
      URL.revokeObjectURL(downloadUrl)
    } catch (error) {
      console.error('处理失败:', error)
    } finally {
      setProcessing(false)
    }
  }

  const renderOptions = () => {
    switch (activeTab) {
      case 'addWatermark':
        return (
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                水印文本
              </label>
              <input
                type="text"
                value={options.addWatermark.text}
                onChange={(e) => setOptions({
                  ...options,
                  addWatermark: { ...options.addWatermark, text: e.target.value }
                })}
                className="input-field"
                placeholder="输入水印文本"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                字体大小
              </label>
              <input
                type="number"
                value={options.addWatermark.fontSize}
                onChange={(e) => setOptions({
                  ...options,
                  addWatermark: { ...options.addWatermark, fontSize: parseInt(e.target.value) }
                })}
                min="12"
                max="72"
                className="input-field"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                透明度
              </label>
              <input
                type="range"
                min="0.1"
                max="1"
                step="0.1"
                value={options.addWatermark.opacity}
                onChange={(e) => setOptions({
                  ...options,
                  addWatermark: { ...options.addWatermark, opacity: parseFloat(e.target.value) }
                })}
                className="w-full"
              />
              <div className="flex justify-between text-sm text-slate-600 dark:text-slate-400">
                <span>10%</span>
                <span>{Math.round(options.addWatermark.opacity * 100)}%</span>
                <span>100%</span>
              </div>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                位置
              </label>
              <select
                value={options.addWatermark.position}
                onChange={(e) => setOptions({
                  ...options,
                  addWatermark: { ...options.addWatermark, position: e.target.value as any }
                })}
                className="input-field"
              >
                <option value="center">居中</option>
                <option value="top-left">左上角</option>
                <option value="top-right">右上角</option>
                <option value="bottom-left">左下角</option>
                <option value="bottom-right">右下角</option>
              </select>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                旋转角度
              </label>
              <input
                type="number"
                value={options.addWatermark.rotation}
                onChange={(e) => setOptions({
                  ...options,
                  addWatermark: { ...options.addWatermark, rotation: parseInt(e.target.value) }
                })}
                min="0"
                max="360"
                className="input-field"
              />
            </div>
          </div>
        )
      
      case 'del4pdf':
        return (
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                要删除的页面
              </label>
              <input
                type="text"
                value={options.del4pdf.pages}
                onChange={(e) => setOptions({
                  ...options,
                  del4pdf: { ...options.del4pdf, pages: e.target.value }
                })}
                className="input-field"
                placeholder="例如: 1,3,5-8"
              />
              <p className="text-sm text-slate-500 dark:text-slate-400 mt-1">
                支持单个页码(1,3,5)或页码范围(1-5)，用逗号分隔
              </p>
            </div>
            
            <div className="bg-yellow-50 dark:bg-yellow-900/20 p-3 rounded-lg">
              <p className="text-sm text-yellow-700 dark:text-yellow-300">
                ⚠️ 删除页面操作不可逆，请谨慎操作
              </p>
            </div>
          </div>
        )
      
      default:
        return null
    }
  }

  if (!currentFile) {
    return (
      <div className="text-center py-12">
        <FileText className="h-16 w-16 text-slate-400 mx-auto mb-4" />
        <p className="text-slate-500 dark:text-slate-400">请先上传PDF文件</p>
      </div>
    )
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="card p-8">
        {/* 标题区域 */}
        <div className="text-center mb-8">
          <div className="bg-gradient-to-r from-primary-500 to-primary-600 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <currentType.icon className="h-8 w-8 text-white" />
          </div>
          <h2 className="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-2">
            {currentType.title}
          </h2>
          <p className="text-slate-600 dark:text-slate-400">
            {currentType.description}
          </p>
        </div>

        {/* 文件信息 */}
        <div className="bg-slate-50 dark:bg-slate-800/50 rounded-lg p-4 mb-6">
          <div className="flex items-center space-x-3">
            <FileText className="h-6 w-6 text-primary-500" />
            <div>
              <p className="font-medium text-slate-800 dark:text-slate-200">
                {currentFile.name}
              </p>
              <p className="text-sm text-slate-600 dark:text-slate-400">
                {currentFile.pages} 页 • {(currentFile.size / 1024 / 1024).toFixed(2)} MB
              </p>
            </div>
          </div>
        </div>

        {/* 编辑选项 */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold text-slate-800 dark:text-slate-200 mb-4">
            编辑选项
          </h3>
          {renderOptions()}
        </div>

        {/* 预览区域（水印预览） */}
        {activeTab === 'addWatermark' && (
          <div className="mb-6 p-4 border border-slate-200 dark:border-slate-600 rounded-lg">
            <h4 className="font-medium text-slate-700 dark:text-slate-300 mb-3">水印预览</h4>
            <div className="relative h-32 bg-gradient-to-br from-slate-100 to-slate-200 dark:from-slate-700 dark:to-slate-800 rounded flex items-center justify-center">
              <div 
                className="absolute"
                style={{
                  opacity: options.addWatermark.opacity,
                  fontSize: `${options.addWatermark.fontSize}px`,
                  transform: `rotate(${options.addWatermark.rotation}deg)`,
                  ...getPositionStyle(options.addWatermark.position)
                }}
              >
                <span className="text-slate-600 dark:text-slate-400 font-semibold">
                  {options.addWatermark.text}
                </span>
              </div>
            </div>
          </div>
        )}

        {/* 处理按钮 */}
        <button
          onClick={handleProcess}
          disabled={processing}
          className="w-full btn-primary py-3 text-lg disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {processing ? (
            <>
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
              处理中...
            </>
          ) : (
            <>
              <Download className="h-5 w-5 mr-2" />
              开始处理
            </>
          )}
        </button>
      </div>
    </div>
  )
}

// 获取水印位置样式
const getPositionStyle = (position: string) => {
  switch (position) {
    case 'top-left':
      return { top: '20%', left: '20%' }
    case 'top-right':
      return { top: '20%', right: '20%' }
    case 'bottom-left':
      return { bottom: '20%', left: '20%' }
    case 'bottom-right':
      return { bottom: '20%', right: '20%' }
    default: // center
      return { top: '50%', left: '50%', transform: 'translate(-50%, -50%)' }
  }
}

export default PDFEditor
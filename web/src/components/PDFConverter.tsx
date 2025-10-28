import React, { useState } from 'react'
import { FileText, Image, FileInput, Download, Upload } from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'

const PDFConverter: React.FC = () => {
  const { currentFile, activeTab } = useFileContext()
  const [processing, setProcessing] = useState(false)
  const [options, setOptions] = useState({
    // PDF转Word选项
    pdf2docx: {
      quality: 'standard' as 'standard' | 'high'
    },
    // PDF转图片选项
    pdf2imgs: {
      format: 'jpg' as 'jpg' | 'png',
      dpi: 150,
      merge: false
    },
    // 文本转PDF选项
    txt2pdf: {
      fontSize: 12,
      margin: 20
    }
  })

  const conversionTypes = {
    pdf2docx: {
      icon: FileInput,
      title: 'PDF转Word',
      description: '将PDF转换为可编辑的Word文档',
      outputFormat: '.docx'
    },
    pdf2imgs: {
      icon: Image,
      title: 'PDF转图片',
      description: '将PDF页面转换为图片格式',
      outputFormat: '.jpg/.png'
    },
    txt2pdf: {
      icon: FileText,
      title: '文本转PDF',
      description: '将文本文件转换为PDF格式',
      outputFormat: '.pdf'
    }
  }

  const currentType = conversionTypes[activeTab as keyof typeof conversionTypes]

  const handleConvert = async () => {
    if (!currentFile) return
    
    setProcessing(true)
    
    try {
      // 模拟转换过程
      await new Promise(resolve => setTimeout(resolve, 2000))
      
      // 这里应该调用实际的转换API
      console.log('开始转换:', currentFile.name, '选项:', options)
      
      // 模拟下载链接
      const downloadUrl = URL.createObjectURL(new Blob(['模拟转换结果'], { type: 'application/octet-stream' }))
      
      const link = document.createElement('a')
      link.href = downloadUrl
      link.download = `${currentFile.name.replace('.pdf', '')}${currentType.outputFormat}`
      link.click()
      
      URL.revokeObjectURL(downloadUrl)
    } catch (error) {
      console.error('转换失败:', error)
    } finally {
      setProcessing(false)
    }
  }

  const renderOptions = () => {
    switch (activeTab) {
      case 'pdf2docx':
        return (
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                转换质量
              </label>
              <select
                value={options.pdf2docx.quality}
                onChange={(e) => setOptions({
                  ...options,
                  pdf2docx: { ...options.pdf2docx, quality: e.target.value as 'standard' | 'high' }
                })}
                className="input-field"
              >
                <option value="standard">标准质量</option>
                <option value="high">高质量</option>
              </select>
            </div>
          </div>
        )
      
      case 'pdf2imgs':
        return (
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                图片格式
              </label>
              <select
                value={options.pdf2imgs.format}
                onChange={(e) => setOptions({
                  ...options,
                  pdf2imgs: { ...options.pdf2imgs, format: e.target.value as 'jpg' | 'png' }
                })}
                className="input-field"
              >
                <option value="jpg">JPG</option>
                <option value="png">PNG</option>
              </select>
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                分辨率 (DPI)
              </label>
              <input
                type="number"
                value={options.pdf2imgs.dpi}
                onChange={(e) => setOptions({
                  ...options,
                  pdf2imgs: { ...options.pdf2imgs, dpi: parseInt(e.target.value) }
                })}
                min="72"
                max="300"
                className="input-field"
              />
            </div>
            
            <div className="flex items-center space-x-2">
              <input
                type="checkbox"
                id="merge"
                checked={options.pdf2imgs.merge}
                onChange={(e) => setOptions({
                  ...options,
                  pdf2imgs: { ...options.pdf2imgs, merge: e.target.checked }
                })}
                className="rounded border-slate-300 text-primary-600 focus:ring-primary-500"
              />
              <label htmlFor="merge" className="text-sm text-slate-700 dark:text-slate-300">
                合并为单张图片
              </label>
            </div>
          </div>
        )
      
      case 'txt2pdf':
        return (
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                字体大小
              </label>
              <input
                type="number"
                value={options.txt2pdf.fontSize}
                onChange={(e) => setOptions({
                  ...options,
                  txt2pdf: { ...options.txt2pdf, fontSize: parseInt(e.target.value) }
                })}
                min="8"
                max="24"
                className="input-field"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                页边距 (mm)
              </label>
              <input
                type="number"
                value={options.txt2pdf.margin}
                onChange={(e) => setOptions({
                  ...options,
                  txt2pdf: { ...options.txt2pdf, margin: parseInt(e.target.value) }
                })}
                min="10"
                max="50"
                className="input-field"
              />
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
        <Upload className="h-16 w-16 text-slate-400 mx-auto mb-4" />
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
          <div className="flex items-center justify-between">
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
            <span className="text-sm text-slate-500 dark:text-slate-500">
              输出格式: {currentType.outputFormat}
            </span>
          </div>
        </div>

        {/* 转换选项 */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold text-slate-800 dark:text-slate-200 mb-4">
            转换选项
          </h3>
          {renderOptions()}
        </div>

        {/* 转换按钮 */}
        <button
          onClick={handleConvert}
          disabled={processing}
          className="w-full btn-primary py-3 text-lg disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {processing ? (
            <>
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-2"></div>
              转换中...
            </>
          ) : (
            <>
              <Download className="h-5 w-5 mr-2" />
              开始转换
            </>
          )}
        </button>

        {/* 转换说明 */}
        <div className="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
          <p className="text-sm text-blue-700 dark:text-blue-300">
            💡 转换过程将在浏览器中完成，文件不会上传到服务器，确保您的数据安全。
          </p>
        </div>
      </div>
    </div>
  )
}

export default PDFConverter
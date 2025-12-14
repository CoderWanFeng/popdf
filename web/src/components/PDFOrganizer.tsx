import React, { useState } from 'react'
import { FileText, Split, Merge, Download, Plus, X } from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'

const PDFOrganizer: React.FC = () => {
  const { currentFile, activeTab, files } = useFileContext()
  const [processing, setProcessing] = useState(false)
  const [options, setOptions] = useState({
    // PDF分割选项
    split4pdf: {
      startPage: 1,
      endPage: 1
    },
    // PDF合并选项
    merge2pdf: {
      selectedFiles: [] as string[],
      order: [] as string[]
    }
  })

  const organizerTypes = {
    split4pdf: {
      icon: Split,
      title: 'PDF分割',
      description: '按页面范围分割PDF文件'
    },
    merge2pdf: {
      icon: Merge,
      title: 'PDF合并',
      description: '将多个PDF文件合并为一个'
    }
  }

  const currentType = organizerTypes[activeTab as keyof typeof organizerTypes]

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
      link.download = `${currentFile.name.replace('.pdf', '')}_${activeTab === 'split4pdf' ? 'split' : 'merged'}.pdf`
      link.click()
      
      URL.revokeObjectURL(downloadUrl)
    } catch (error) {
      console.error('处理失败:', error)
    } finally {
      setProcessing(false)
    }
  }

  const toggleMergeFile = (fileId: string) => {
    setOptions(prev => {
      const isSelected = prev.merge2pdf.selectedFiles.includes(fileId)
      const selectedFiles = isSelected
        ? prev.merge2pdf.selectedFiles.filter(id => id !== fileId)
        : [...prev.merge2pdf.selectedFiles, fileId]
      
      return {
        ...prev,
        merge2pdf: {
          ...prev.merge2pdf,
          selectedFiles,
          order: selectedFiles
        }
      }
    })
  }

  const moveFileInOrder = (fileId: string, direction: 'up' | 'down') => {
    setOptions(prev => {
      const order = [...prev.merge2pdf.order]
      const index = order.indexOf(fileId)
      
      if (direction === 'up' && index > 0) {
        [order[index - 1], order[index]] = [order[index], order[index - 1]]
      } else if (direction === 'down' && index < order.length - 1) {
        [order[index], order[index + 1]] = [order[index + 1], order[index]]
      }
      
      return {
        ...prev,
        merge2pdf: {
          ...prev.merge2pdf,
          order
        }
      }
    })
  }

  const renderOptions = () => {
    switch (activeTab) {
      case 'split4pdf':
        return (
          <div className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                  起始页码
                </label>
                <input
                  type="number"
                  value={options.split4pdf.startPage}
                  onChange={(e) => setOptions({
                    ...options,
                    split4pdf: { 
                      ...options.split4pdf, 
                      startPage: Math.max(1, parseInt(e.target.value) || 1),
                      endPage: Math.max(options.split4pdf.startPage, parseInt(e.target.value) || 1)
                    }
                  })}
                  min="1"
                  max={currentFile?.pages || 1}
                  className="input-field"
                />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                  结束页码
                </label>
                <input
                  type="number"
                  value={options.split4pdf.endPage}
                  onChange={(e) => setOptions({
                    ...options,
                    split4pdf: { 
                      ...options.split4pdf, 
                      endPage: Math.min(currentFile?.pages || 1, Math.max(options.split4pdf.startPage, parseInt(e.target.value) || 1))
                    }
                  })}
                  min={options.split4pdf.startPage}
                  max={currentFile?.pages || 1}
                  className="input-field"
                />
              </div>
            </div>
            
            <div className="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-lg">
              <p className="text-sm text-blue-700 dark:text-blue-300">
                📄 将分割出第 {options.split4pdf.startPage} 页到第 {options.split4pdf.endPage} 页的内容
              </p>
            </div>
          </div>
        )
      
      case 'merge2pdf':
        return (
          <div className="space-y-4">
            <div>
              <h4 className="font-medium text-slate-700 dark:text-slate-300 mb-3">
                选择要合并的文件 ({options.merge2pdf.selectedFiles.length} 个文件)
              </h4>
              <div className="space-y-2 max-h-40 overflow-y-auto">
                {files.map(file => (
                  <div key={file.id} className="flex items-center justify-between p-3 bg-slate-50 dark:bg-slate-800/30 rounded-lg">
                    <div className="flex items-center space-x-3">
                      <input
                        type="checkbox"
                        checked={options.merge2pdf.selectedFiles.includes(file.id)}
                        onChange={() => toggleMergeFile(file.id)}
                        className="rounded border-slate-300 text-primary-600 focus:ring-primary-500"
                      />
                      <FileText className="h-5 w-5 text-primary-500" />
                      <span className="text-sm font-medium text-slate-700 dark:text-slate-300">
                        {file.name}
                      </span>
                    </div>
                    <span className="text-xs text-slate-500 dark:text-slate-500">
                      {file.pages}页
                    </span>
                  </div>
                ))}
              </div>
            </div>
            
            {options.merge2pdf.selectedFiles.length > 0 && (
              <div>
                <h4 className="font-medium text-slate-700 dark:text-slate-300 mb-3">
                  合并顺序
                </h4>
                <div className="space-y-2">
                  {options.merge2pdf.order.map((fileId, index) => {
                    const file = files.find(f => f.id === fileId)
                    if (!file) return null
                    
                    return (
                      <div key={fileId} className="flex items-center justify-between p-3 bg-slate-50 dark:bg-slate-800/30 rounded-lg">
                        <div className="flex items-center space-x-3">
                          <span className="text-sm font-medium text-slate-500 dark:text-slate-500 w-6">
                            {index + 1}
                          </span>
                          <FileText className="h-4 w-4 text-primary-500" />
                          <span className="text-sm text-slate-700 dark:text-slate-300">
                            {file.name}
                          </span>
                        </div>
                        <div className="flex space-x-1">
                          <button
                            onClick={() => moveFileInOrder(fileId, 'up')}
                            disabled={index === 0}
                            className="p-1 rounded disabled:opacity-30"
                            title="上移"
                          >
                            <Plus className="h-3 w-3 text-slate-500" />
                          </button>
                          <button
                            onClick={() => moveFileInOrder(fileId, 'down')}
                            disabled={index === options.merge2pdf.order.length - 1}
                            className="p-1 rounded disabled:opacity-30"
                            title="下移"
                          >
                            <X className="h-3 w-3 text-slate-500" />
                          </button>
                        </div>
                      </div>
                    )
                  })}
                </div>
              </div>
            )}
            
            <div className="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-lg">
              <p className="text-sm text-blue-700 dark:text-blue-300">
                🔄 合并后的文件将按照您设置的顺序排列
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

        {/* 组织选项 */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold text-slate-800 dark:text-slate-200 mb-4">
            {activeTab === 'split4pdf' ? '分割设置' : '合并设置'}
          </h3>
          {renderOptions()}
        </div>

        {/* 处理按钮 */}
        <button
          onClick={handleProcess}
          disabled={processing || (activeTab === 'merge2pdf' && options.merge2pdf.selectedFiles.length < 2)}
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
              开始{activeTab === 'split4pdf' ? '分割' : '合并'}
            </>
          )}
        </button>
      </div>
    </div>
  )
}

export default PDFOrganizer
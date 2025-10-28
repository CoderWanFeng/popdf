import React, { useState } from 'react'
import { FileText, Lock, Unlock, Download } from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'

const PDFSecurity: React.FC = () => {
  const { currentFile, activeTab } = useFileContext()
  const [processing, setProcessing] = useState(false)
  const [options, setOptions] = useState({
    // PDF加密选项
    encrypt4pdf: {
      password: '',
      ownerPassword: '',
      permissions: {
        printing: true,
        modifying: false,
        copying: true,
        annotating: true
      }
    },
    // PDF解密选项
    decrypt4pdf: {
      password: ''
    }
  })

  const securityTypes = {
    encrypt4pdf: {
      icon: Lock,
      title: 'PDF加密',
      description: '为PDF文件添加密码保护'
    },
    decrypt4pdf: {
      icon: Unlock,
      title: 'PDF解密',
      description: '移除PDF文件的密码保护'
    }
  }

  const currentType = securityTypes[activeTab as keyof typeof securityTypes]

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
      link.download = `${currentFile.name.replace('.pdf', '')}_${activeTab === 'encrypt4pdf' ? 'encrypted' : 'decrypted'}.pdf`
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
      case 'encrypt4pdf':
        return (
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                用户密码
              </label>
              <input
                type="password"
                value={options.encrypt4pdf.password}
                onChange={(e) => setOptions({
                  ...options,
                  encrypt4pdf: { ...options.encrypt4pdf, password: e.target.value }
                })}
                className="input-field"
                placeholder="输入打开PDF所需的密码"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                所有者密码（可选）
              </label>
              <input
                type="password"
                value={options.encrypt4pdf.ownerPassword}
                onChange={(e) => setOptions({
                  ...options,
                  encrypt4pdf: { ...options.encrypt4pdf, ownerPassword: e.target.value }
                })}
                className="input-field"
                placeholder="输入权限管理密码"
              />
            </div>
            
            <div>
              <h4 className="font-medium text-slate-700 dark:text-slate-300 mb-3">权限设置</h4>
              <div className="grid grid-cols-2 gap-4">
                {Object.entries(options.encrypt4pdf.permissions).map(([key, value]) => (
                  <div key={key} className="flex items-center space-x-2">
                    <input
                      type="checkbox"
                      id={key}
                      checked={value}
                      onChange={(e) => setOptions({
                        ...options,
                        encrypt4pdf: {
                          ...options.encrypt4pdf,
                          permissions: {
                            ...options.encrypt4pdf.permissions,
                            [key]: e.target.checked
                          }
                        }
                      })}
                      className="rounded border-slate-300 text-primary-600 focus:ring-primary-500"
                    />
                    <label htmlFor={key} className="text-sm text-slate-700 dark:text-slate-300">
                      {getPermissionLabel(key)}
                    </label>
                  </div>
                ))}
              </div>
            </div>
            
            <div className="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-lg">
              <p className="text-sm text-blue-700 dark:text-blue-300">
                💡 用户密码用于打开文件，所有者密码用于设置权限。如果只设置用户密码，则所有权限默认允许。
              </p>
            </div>
          </div>
        )
      
      case 'decrypt4pdf':
        return (
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
                当前密码
              </label>
              <input
                type="password"
                value={options.decrypt4pdf.password}
                onChange={(e) => setOptions({
                  ...options,
                  decrypt4pdf: { ...options.decrypt4pdf, password: e.target.value }
                })}
                className="input-field"
                placeholder="输入PDF文件的当前密码"
              />
            </div>
            
            <div className="bg-yellow-50 dark:bg-yellow-900/20 p-3 rounded-lg">
              <p className="text-sm text-yellow-700 dark:text-yellow-300">
                ⚠️ 请确保您有合法的权限来解密此PDF文件。
              </p>
            </div>
          </div>
        )
      
      default:
        return null
    }
  }

  const getPermissionLabel = (key: string) => {
    const labels = {
      printing: '允许打印',
      modifying: '允许修改',
      copying: '允许复制',
      annotating: '允许注释'
    }
    return labels[key as keyof typeof labels] || key
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

        {/* 安全选项 */}
        <div className="mb-8">
          <h3 className="text-lg font-semibold text-slate-800 dark:text-slate-200 mb-4">
            {activeTab === 'encrypt4pdf' ? '加密设置' : '解密设置'}
          </h3>
          {renderOptions()}
        </div>

        {/* 处理按钮 */}
        <button
          onClick={handleProcess}
          disabled={processing || (activeTab === 'encrypt4pdf' && !options.encrypt4pdf.password)}
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
              开始{activeTab === 'encrypt4pdf' ? '加密' : '解密'}
            </>
          )}
        </button>

        {/* 安全说明 */}
        <div className="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
          <p className="text-sm text-green-700 dark:text-green-300">
            🔒 所有操作都在本地浏览器中完成，您的文件不会上传到任何服务器，确保数据安全。
          </p>
        </div>
      </div>
    </div>
  )
}

export default PDFSecurity
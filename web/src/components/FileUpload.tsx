import React, { useRef } from 'react'
import { Upload, FileText, FolderOpen } from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'
import type { PDFFile } from '../types'

const FileUpload: React.FC = () => {
  const { addFile } = useFileContext()
  const fileInputRef = useRef<HTMLInputElement>(null)
  const folderInputRef = useRef<HTMLInputElement>(null)

  const handleFileSelect = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files
    if (!files) return

    for (const file of Array.from(files)) {
      if (file.type === 'application/pdf') {
        const fileUrl = URL.createObjectURL(file)
        
        // 获取PDF页数（简化实现，实际应用中可能需要更复杂的PDF解析）
        const pageCount = await getPDFPageCount(file)
        
        const pdfFile: PDFFile = {
          id: Math.random().toString(36).substr(2, 9),
          name: file.name,
          size: file.size,
          url: fileUrl,
          pages: pageCount,
          uploadTime: new Date()
        }
        
        addFile(pdfFile)
      }
    }
  }

  const getPDFPageCount = async (file: File): Promise<number> => {
    // 简化实现，实际应用中应该使用PDF.js来解析页数
    return 1 // 默认返回1页
  }

  const handleDragOver = (event: React.DragEvent) => {
    event.preventDefault()
    event.dataTransfer.dropEffect = 'copy'
  }

  const handleDrop = async (event: React.DragEvent) => {
    event.preventDefault()
    const files = event.dataTransfer.files
    
    for (const file of Array.from(files)) {
      if (file.type === 'application/pdf') {
        const fileUrl = URL.createObjectURL(file)
        const pdfFile: PDFFile = {
          id: Math.random().toString(36).substr(2, 9),
          name: file.name,
          size: file.size,
          url: fileUrl,
          pages: 1, // 简化处理
          uploadTime: new Date()
        }
        
        addFile(pdfFile)
      }
    }
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-slate-800 dark:text-slate-200 mb-4">
          上传PDF文件
        </h2>
        <p className="text-lg text-slate-600 dark:text-slate-400">
          选择单个PDF文件或批量上传多个PDF文件进行处理
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-8">
        {/* 单个文件上传 */}
        <div 
          className="card p-8 text-center cursor-pointer hover:scale-105 transition-transform duration-200"
          onClick={() => fileInputRef.current?.click()}
          onDragOver={handleDragOver}
          onDrop={handleDrop}
        >
          <div className="bg-gradient-to-r from-green-500 to-green-600 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <FileText className="h-8 w-8 text-white" />
          </div>
          <h3 className="text-xl font-semibold text-slate-800 dark:text-slate-200 mb-2">
            上传单个PDF
          </h3>
          <p className="text-slate-600 dark:text-slate-400 mb-4">
            选择单个PDF文件进行查看和处理
          </p>
          <button className="btn-primary">
            <Upload className="h-4 w-4 mr-2" />
            选择文件
          </button>
          <input
            ref={fileInputRef}
            type="file"
            accept=".pdf"
            onChange={handleFileSelect}
            className="hidden"
          />
        </div>

        {/* 批量上传 */}
        <div 
          className="card p-8 text-center cursor-pointer hover:scale-105 transition-transform duration-200"
          onClick={() => folderInputRef.current?.click()}
          onDragOver={handleDragOver}
          onDrop={handleDrop}
        >
          <div className="bg-gradient-to-r from-blue-500 to-blue-600 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
            <FolderOpen className="h-8 w-8 text-white" />
          </div>
          <h3 className="text-xl font-semibold text-slate-800 dark:text-slate-200 mb-2">
            批量上传PDF
          </h3>
          <p className="text-slate-600 dark:text-slate-400 mb-4">
            选择包含多个PDF文件的文件夹
          </p>
          <button className="btn-primary">
            <Upload className="h-4 w-4 mr-2" />
            选择文件夹
          </button>
          <input
            ref={folderInputRef}
            type="file"
            accept=".pdf"
            multiple
            onChange={handleFileSelect}
            className="hidden"
          />
        </div>
      </div>

      {/* 拖拽区域 */}
      <div 
        className="card p-12 text-center border-2 border-dashed border-slate-300 dark:border-slate-600 mt-8"
        onDragOver={handleDragOver}
        onDrop={handleDrop}
      >
        <Upload className="h-16 w-16 text-slate-400 dark:text-slate-500 mx-auto mb-4" />
        <h3 className="text-xl font-semibold text-slate-800 dark:text-slate-200 mb-2">
          拖拽PDF文件到这里
        </h3>
        <p className="text-slate-600 dark:text-slate-400">
          支持单个或多个PDF文件拖拽上传
        </p>
      </div>

      {/* 功能特性 */}
      <div className="mt-12">
        <h3 className="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 text-center">
          支持的功能
        </h3>
        <div className="grid md:grid-cols-3 gap-6">
          {[
            { icon: FileText, title: 'PDF查看', desc: '高质量PDF文档查看器' },
            { icon: FileText, title: '格式转换', desc: 'PDF转Word、图片等格式' },
            { icon: FileText, title: '编辑处理', desc: '分割、合并、加密等操作' }
          ].map((feature, index) => (
            <div key={index} className="card p-6 text-center">
              <feature.icon className="h-8 w-8 text-primary-500 mx-auto mb-3" />
              <h4 className="font-semibold text-slate-800 dark:text-slate-200 mb-2">
                {feature.title}
              </h4>
              <p className="text-sm text-slate-600 dark:text-slate-400">
                {feature.desc}
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default FileUpload
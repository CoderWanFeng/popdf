import React, { useState } from 'react'
import { Document, Page, pdfjs } from 'react-pdf'
import { 
  ZoomIn, 
  ZoomOut, 
  ChevronLeft, 
  ChevronRight, 
  Download,
  RotateCw,
  Search
} from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'

// 配置PDF.js worker
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`

const PDFViewer: React.FC = () => {
  const { currentFile } = useFileContext()
  const [numPages, setNumPages] = useState<number>(0)
  const [pageNumber, setPageNumber] = useState<number>(1)
  const [scale, setScale] = useState<number>(1.0)
  const [rotation, setRotation] = useState<number>(0)
  const [searchText, setSearchText] = useState<string>('')

  const onDocumentLoadSuccess = ({ numPages }: { numPages: number }) => {
    setNumPages(numPages)
    setPageNumber(1)
  }

  const goToPreviousPage = () => {
    setPageNumber(prevPageNumber => Math.max(prevPageNumber - 1, 1))
  }

  const goToNextPage = () => {
    setPageNumber(prevPageNumber => Math.min(prevPageNumber + 1, numPages))
  }

  const zoomIn = () => {
    setScale(prevScale => Math.min(prevScale + 0.25, 3.0))
  }

  const zoomOut = () => {
    setScale(prevScale => Math.max(prevScale - 0.25, 0.5))
  }

  const rotate = () => {
    setRotation(prevRotation => (prevRotation + 90) % 360)
  }

  const handlePageInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    const page = parseInt(e.target.value)
    if (page >= 1 && page <= numPages) {
      setPageNumber(page)
    }
  }

  const downloadPDF = () => {
    if (currentFile) {
      const link = document.createElement('a')
      link.href = currentFile.url
      link.download = currentFile.name
      link.click()
    }
  }

  if (!currentFile) {
    return (
      <div className="text-center py-12">
        <p className="text-slate-500 dark:text-slate-400">请先上传PDF文件</p>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto">
      {/* 工具栏 */}
      <div className="card p-4 mb-6">
        <div className="flex flex-wrap items-center justify-between gap-4">
          {/* 文件信息 */}
          <div className="flex items-center space-x-4">
            <div className="bg-primary-100 dark:bg-primary-900 p-2 rounded-lg">
              <Download className="h-5 w-5 text-primary-600 dark:text-primary-400" />
            </div>
            <div>
              <h3 className="font-semibold text-slate-800 dark:text-slate-200">
                {currentFile.name}
              </h3>
              <p className="text-sm text-slate-600 dark:text-slate-400">
                {numPages} 页 • {(currentFile.size / 1024 / 1024).toFixed(2)} MB
              </p>
            </div>
          </div>

          {/* 搜索框 */}
          <div className="relative">
            <Search className="h-4 w-4 text-slate-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
            <input
              type="text"
              placeholder="搜索文本..."
              value={searchText}
              onChange={(e) => setSearchText(e.target.value)}
              className="input-field pl-10 pr-4 py-2 w-64"
            />
          </div>

          {/* 控制按钮 */}
          <div className="flex items-center space-x-2">
            <button
              onClick={zoomOut}
              disabled={scale <= 0.5}
              className="p-2 rounded-lg bg-white/50 dark:bg-slate-700/50 hover:bg-white/80 dark:hover:bg-slate-600/80 disabled:opacity-50"
              title="缩小"
            >
              <ZoomOut className="h-5 w-5 text-slate-600 dark:text-slate-400" />
            </button>
            
            <span className="text-sm font-medium text-slate-600 dark:text-slate-400 min-w-[60px] text-center">
              {Math.round(scale * 100)}%
            </span>
            
            <button
              onClick={zoomIn}
              disabled={scale >= 3.0}
              className="p-2 rounded-lg bg-white/50 dark:bg-slate-700/50 hover:bg-white/80 dark:hover:bg-slate-600/80 disabled:opacity-50"
              title="放大"
            >
              <ZoomIn className="h-5 w-5 text-slate-600 dark:text-slate-400" />
            </button>
            
            <button
              onClick={rotate}
              className="p-2 rounded-lg bg-white/50 dark:bg-slate-700/50 hover:bg-white/80 dark:hover:bg-slate-600/80"
              title="旋转"
            >
              <RotateCw className="h-5 w-5 text-slate-600 dark:text-slate-400" />
            </button>
            
            <button
              onClick={downloadPDF}
              className="btn-primary"
              title="下载PDF"
            >
              <Download className="h-4 w-4 mr-2" />
              下载
            </button>
          </div>
        </div>

        {/* 页面导航 */}
        <div className="flex items-center justify-center space-x-4 mt-4">
          <button
            onClick={goToPreviousPage}
            disabled={pageNumber <= 1}
            className="p-2 rounded-lg bg-white/50 dark:bg-slate-700/50 hover:bg-white/80 dark:hover:bg-slate-600/80 disabled:opacity-50"
          >
            <ChevronLeft className="h-5 w-5 text-slate-600 dark:text-slate-400" />
          </button>
          
          <div className="flex items-center space-x-2">
            <input
              type="number"
              value={pageNumber}
              onChange={handlePageInput}
              min={1}
              max={numPages}
              className="input-field w-20 text-center"
            />
            <span className="text-slate-600 dark:text-slate-400">/ {numPages}</span>
          </div>
          
          <button
            onClick={goToNextPage}
            disabled={pageNumber >= numPages}
            className="p-2 rounded-lg bg-white/50 dark:bg-slate-700/50 hover:bg-white/80 dark:hover:bg-slate-600/80 disabled:opacity-50"
          >
            <ChevronRight className="h-5 w-5 text-slate-600 dark:text-slate-400" />
          </button>
        </div>
      </div>

      {/* PDF显示区域 */}
      <div className="card p-6">
        <div className="flex justify-center">
          <Document
            file={currentFile.url}
            onLoadSuccess={onDocumentLoadSuccess}
            loading={
              <div className="flex items-center justify-center h-96">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
              </div>
            }
            error={
              <div className="text-center py-12">
                <p className="text-red-500">加载PDF文件失败</p>
              </div>
            }
          >
            <Page 
              pageNumber={pageNumber} 
              scale={scale}
              rotate={rotation}
              loading={
                <div className="flex items-center justify-center h-96">
                  <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500"></div>
                </div>
              }
            />
          </Document>
        </div>
      </div>

      {/* 缩略图导航 */}
      {numPages > 1 && (
        <div className="card p-4 mt-6">
          <h4 className="font-semibold text-slate-800 dark:text-slate-200 mb-3">页面导航</h4>
          <div className="grid grid-cols-8 gap-2 max-h-40 overflow-y-auto">
            {Array.from({ length: numPages }, (_, i) => i + 1).map((page) => (
              <button
                key={page}
                onClick={() => setPageNumber(page)}
                className={`p-2 rounded-lg text-sm transition-all ${
                  page === pageNumber
                    ? 'bg-primary-500 text-white'
                    : 'bg-white/50 dark:bg-slate-700/50 text-slate-700 dark:text-slate-300 hover:bg-white/80 dark:hover:bg-slate-600/80'
                }`}
              >
                {page}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

export default PDFViewer
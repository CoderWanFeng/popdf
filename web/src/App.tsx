import React, { useState } from 'react'
import Header from './components/Header'
import Sidebar from './components/Sidebar'
import MainContent from './components/MainContent'
import { FileContext } from './contexts/FileContext'
import type { PDFFile } from './types'

function App() {
  const [currentFile, setCurrentFile] = useState<PDFFile | null>(null)
  const [files, setFiles] = useState<PDFFile[]>([])
  const [activeTab, setActiveTab] = useState<string>('viewer')

  const addFile = (file: PDFFile) => {
    setFiles(prev => [...prev, file])
    setCurrentFile(file)
  }

  const removeFile = (fileId: string) => {
    setFiles(prev => prev.filter(f => f.id !== fileId))
    if (currentFile?.id === fileId) {
      setCurrentFile(files.length > 1 ? files[0] : null)
    }
  }

  return (
    <FileContext.Provider value={{
      currentFile,
      files,
      activeTab,
      setCurrentFile,
      setFiles,
      setActiveTab,
      addFile,
      removeFile
    }}>
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 dark:from-slate-900 dark:to-blue-900">
        <Header />
        <div className="flex h-[calc(100vh-64px)]">
          <Sidebar />
          <MainContent />
        </div>
      </div>
    </FileContext.Provider>
  )
}

export default App
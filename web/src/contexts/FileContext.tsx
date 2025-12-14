import React, { createContext, useContext } from 'react'
import type { PDFFile } from '../types'

interface FileContextType {
  currentFile: PDFFile | null
  files: PDFFile[]
  activeTab: string
  setCurrentFile: (file: PDFFile | null) => void
  setFiles: (files: PDFFile[]) => void
  setActiveTab: (tab: string) => void
  addFile: (file: PDFFile) => void
  removeFile: (fileId: string) => void
}

export const FileContext = createContext<FileContextType | undefined>(undefined)

export const useFileContext = () => {
  const context = useContext(FileContext)
  if (context === undefined) {
    throw new Error('useFileContext must be used within a FileProvider')
  }
  return context
}
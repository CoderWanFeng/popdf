import React from 'react'
import { useFileContext } from '../contexts/FileContext'
import FileUpload from './FileUpload'
import PDFViewer from './PDFViewer'
import PDFConverter from './PDFConverter'
import PDFEditor from './PDFEditor'
import PDFSecurity from './PDFSecurity'
import PDFOrganizer from './PDFOrganizer'

const MainContent: React.FC = () => {
  const { activeTab, currentFile } = useFileContext()

  const renderContent = () => {
    switch (activeTab) {
      case 'upload':
        return <FileUpload />
      case 'viewer':
        return currentFile ? <PDFViewer /> : <FileUpload />
      case 'pdf2docx':
      case 'pdf2imgs':
      case 'txt2pdf':
        return currentFile ? <PDFConverter /> : <FileUpload />
      case 'split4pdf':
      case 'merge2pdf':
        return currentFile ? <PDFOrganizer /> : <FileUpload />
      case 'encrypt4pdf':
      case 'decrypt4pdf':
        return currentFile ? <PDFSecurity /> : <FileUpload />
      case 'addWatermark':
      case 'del4pdf':
        return currentFile ? <PDFEditor /> : <FileUpload />
      default:
        return currentFile ? <PDFViewer /> : <FileUpload />
    }
  }

  return (
    <main className="flex-1 overflow-auto">
      <div className="p-6">
        {renderContent()}
      </div>
    </main>
  )
}

export default MainContent
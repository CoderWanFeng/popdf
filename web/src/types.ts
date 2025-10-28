export interface PDFFile {
  id: string
  name: string
  size: number
  url: string
  pages: number
  uploadTime: Date
}

export interface PDFOperation {
  id: string
  name: string
  description: string
  icon: string
  category: 'conversion' | 'edit' | 'security' | 'organize'
}

export interface ProcessingOptions {
  // PDF转Word选项
  pdf2docx?: {
    quality?: 'standard' | 'high'
  }
  
  // PDF转图片选项
  pdf2imgs?: {
    format: 'jpg' | 'png'
    dpi: number
    merge: boolean
  }
  
  // PDF分割选项
  split4pdf?: {
    startPage: number
    endPage: number
  }
  
  // PDF加密选项
  encrypt4pdf?: {
    password: string
    ownerPassword?: string
    permissions?: {
      printing?: boolean
      modifying?: boolean
      copying?: boolean
      annotating?: boolean
    }
  }
  
  // 添加水印选项
  addWatermark?: {
    text: string
    fontSize: number
    opacity: number
    position: 'center' | 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right'
    rotation: number
  }
  
  // PDF合并选项
  merge2pdf?: {
    files: PDFFile[]
    order: string[]
  }
  
  // 删除页面选项
  del4pdf?: {
    pages: string // 如 "1,3,5-8"
  }
}

export interface ProcessingResult {
  success: boolean
  message: string
  downloadUrl?: string
  file?: PDFFile
  error?: string
}
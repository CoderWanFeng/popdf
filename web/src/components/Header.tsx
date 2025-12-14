import React from 'react'
import { FileText, Settings, Moon, Sun } from 'lucide-react'
import { useFileContext } from '../contexts/FileContext'

const Header: React.FC = () => {
  const { currentFile } = useFileContext()
  const [darkMode, setDarkMode] = React.useState(false)

  React.useEffect(() => {
    const isDark = document.documentElement.classList.contains('dark')
    setDarkMode(isDark)
  }, [])

  const toggleDarkMode = () => {
    document.documentElement.classList.toggle('dark')
    setDarkMode(!darkMode)
  }

  return (
    <header className="glass-effect border-b border-white/20 dark:border-slate-700/50 px-6 py-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="bg-gradient-to-r from-primary-500 to-primary-600 p-2 rounded-lg">
            <FileText className="h-6 w-6 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold bg-gradient-to-r from-primary-600 to-primary-700 bg-clip-text text-transparent">
              POPDF
            </h1>
            <p className="text-sm text-slate-600 dark:text-slate-400">
              在线PDF处理工具
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-4">
          {currentFile && (
            <div className="text-right">
              <p className="font-medium text-slate-700 dark:text-slate-300">
                {currentFile.name}
              </p>
              <p className="text-sm text-slate-500 dark:text-slate-500">
                {currentFile.pages} 页 • {(currentFile.size / 1024 / 1024).toFixed(2)} MB
              </p>
            </div>
          )}
          
          <button
            onClick={toggleDarkMode}
            className="p-2 rounded-lg bg-white/50 dark:bg-slate-700/50 hover:bg-white/80 dark:hover:bg-slate-600/80 transition-colors"
            title={darkMode ? '切换到亮色模式' : '切换到暗色模式'}
          >
            {darkMode ? (
              <Sun className="h-5 w-5 text-yellow-500" />
            ) : (
              <Moon className="h-5 w-5 text-slate-600" />
            )}
          </button>
          
          <button className="p-2 rounded-lg bg-white/50 dark:bg-slate-700/50 hover:bg-white/80 dark:hover:bg-slate-600/80 transition-colors">
            <Settings className="h-5 w-5 text-slate-600 dark:text-slate-400" />
          </button>
        </div>
      </div>
    </header>
  )
}

export default Header
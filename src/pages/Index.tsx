import { useState } from 'react'
import { Header } from '@/components/Header'
import { InputPanel, FormData } from '@/components/InputPanel'
import { OutputPanel } from '@/components/OutputPanel'
import { generateReport } from '@/services/api'
import { useToast } from '@/hooks/use-toast'

const Index = () => {
  const [reportContent, setReportContent] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const { toast } = useToast()

  const handleSubmit = async (data: FormData) => {
    setIsLoading(true)
    setReportContent('')

    try {
      // Validate JSON input
      JSON.parse(data.jsonInput)
      
      const response = await generateReport(data)
      
      if (response.success) {
        setReportContent(response.report)
        toast({
          title: "Report Generated Successfully! 🎉",
          description: "Your empathetic code review is ready.",
        })
      } else {
        throw new Error(response.error || 'Failed to generate report')
      }
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Invalid JSON format'
      toast({
        title: "Generation Failed",
        description: errorMessage,
        variant: "destructive",
      })
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-background">
      <Header />
      
      <main className="container mx-auto px-4 py-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 h-[calc(100vh-7rem)]">
          <div className="animate-fade-in">
            <InputPanel onSubmit={handleSubmit} isLoading={isLoading} />
          </div>
          
          <div className="animate-fade-in" style={{ animationDelay: '150ms' }}>
            <OutputPanel content={reportContent} isLoading={isLoading} />
          </div>
        </div>
      </main>
    </div>
  )
};

export default Index;

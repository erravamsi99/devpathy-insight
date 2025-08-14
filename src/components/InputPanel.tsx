import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { Checkbox } from '@/components/ui/checkbox'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Upload, Play, Loader2 } from 'lucide-react'

export interface FormData {
  jsonInput: string
  style: string
  includeResourceLinks: boolean
}

interface InputPanelProps {
  onSubmit: (data: FormData) => void
  isLoading: boolean
}

const examplePayload = `{
  "project": "devpathy-frontend",
  "files": [
    {
      "path": "src/components/Button.tsx",
      "content": "import React from 'react';\\n\\nexport const Button = ({ children, onClick }) => {\\n  return (\\n    <button onClick={onClick} style={{ padding: '10px' }}>\\n      {children}\\n    </button>\\n  );\\n};",
      "issues": [
        {
          "line": 3,
          "type": "TypeScript",
          "severity": "warning",
          "message": "Missing prop types for onClick and children"
        },
        {
          "line": 5,
          "type": "Accessibility",
          "severity": "error",
          "message": "Button lacks proper ARIA attributes"
        }
      ]
    }
  ],
  "context": {
    "reviewer": "Senior Frontend Developer",
    "focus_areas": ["TypeScript", "Accessibility", "Performance"],
    "project_guidelines": "Follow React best practices and ensure full accessibility compliance"
  }
}`

export function InputPanel({ onSubmit, isLoading }: InputPanelProps) {
  const [jsonInput, setJsonInput] = useState(examplePayload)
  const [style, setStyle] = useState('friendly')
  const [includeResourceLinks, setIncludeResourceLinks] = useState(true)

  const handleSubmit = () => {
    onSubmit({
      jsonInput,
      style,
      includeResourceLinks,
    })
  }

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file && file.type === 'application/json') {
      const reader = new FileReader()
      reader.onload = (e) => {
        const content = e.target?.result as string
        try {
          // Validate JSON
          JSON.parse(content)
          setJsonInput(content)
        } catch (error) {
          alert('Invalid JSON file')
        }
      }
      reader.readAsText(file)
    }
  }

  return (
    <Card className="h-full flex flex-col">
      <CardHeader className="pb-4">
        <CardTitle className="text-xl font-semibold flex items-center gap-2">
          <Play className="h-5 w-5 text-primary" />
          Code Review Input
        </CardTitle>
      </CardHeader>
      
      <CardContent className="flex-1 flex flex-col space-y-6">
        {/* JSON Input */}
        <div className="flex-1 flex flex-col space-y-3">
          <div className="flex items-center justify-between">
            <Label htmlFor="json-input" className="text-sm font-medium">
              JSON Payload
            </Label>
            <div className="flex items-center gap-2">
              <input
                type="file"
                accept=".json"
                onChange={handleFileUpload}
                className="hidden"
                id="file-upload"
              />
              <Button
                variant="outline"
                size="sm"
                onClick={() => document.getElementById('file-upload')?.click()}
                className="h-8 px-3"
              >
                <Upload className="h-3 w-3 mr-1" />
                Upload JSON
              </Button>
            </div>
          </div>
          
          <Textarea
            id="json-input"
            value={jsonInput}
            onChange={(e) => setJsonInput(e.target.value)}
            className="flex-1 min-h-[300px] font-mono text-sm code-block resize-none"
            placeholder="Paste your JSON payload here..."
          />
        </div>

        {/* Style Selector */}
        <div className="space-y-2">
          <Label className="text-sm font-medium">Review Style</Label>
          <Select value={style} onValueChange={setStyle}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Select review style" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="friendly">
                <div className="flex flex-col items-start">
                  <span className="font-medium">Friendly</span>
                  <span className="text-xs text-muted-foreground">Encouraging and supportive tone</span>
                </div>
              </SelectItem>
              <SelectItem value="neutral">
                <div className="flex flex-col items-start">
                  <span className="font-medium">Neutral</span>
                  <span className="text-xs text-muted-foreground">Professional and balanced</span>
                </div>
              </SelectItem>
              <SelectItem value="direct">
                <div className="flex flex-col items-start">
                  <span className="font-medium">Direct</span>
                  <span className="text-xs text-muted-foreground">Straight to the point</span>
                </div>
              </SelectItem>
            </SelectContent>
          </Select>
        </div>

        {/* Include Resource Links */}
        <div className="flex items-center space-x-3">
          <Checkbox
            id="resource-links"
            checked={includeResourceLinks}
            onCheckedChange={(checked) => setIncludeResourceLinks(checked as boolean)}
          />
          <Label htmlFor="resource-links" className="text-sm font-medium cursor-pointer">
            Include helpful resource links
          </Label>
        </div>

        {/* Submit Button */}
        <Button
          onClick={handleSubmit}
          disabled={isLoading || !jsonInput.trim()}
          variant="generate"
          size="lg"
          className="w-full h-12 text-base font-semibold"
        >
          {isLoading ? (
            <>
              <Loader2 className="h-4 w-4 mr-2 animate-spin" />
              Generating Report...
            </>
          ) : (
            <>
              <Play className="h-4 w-4 mr-2" />
              Generate Report
            </>
          )}
        </Button>
      </CardContent>
    </Card>
  )
}
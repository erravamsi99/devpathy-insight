import { FormData } from '@/components/InputPanel'

export interface ApiResponse {
  report: string
  success: boolean
  error?: string
}

// Mock API service for local testing
export const generateReport = async (data: FormData): Promise<ApiResponse> => {
  // Simulate API delay
  await new Promise(resolve => setTimeout(resolve, 2000))

  // Mock response based on the input style
  const mockResponse = generateMockReport(data.style, data.includeResourceLinks)

  return {
    report: mockResponse,
    success: true
  }
}

// Production API call (uncomment when backend is ready)
export const generateReportFromAPI = async (data: FormData): Promise<ApiResponse> => {
  try {
    const response = await fetch('/api/generate', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        payload: JSON.parse(data.jsonInput),
        style: data.style,
        includeResourceLinks: data.includeResourceLinks,
      }),
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const result = await response.json()
    return {
      report: result.report,
      success: true
    }
  } catch (error) {
    return {
      report: '',
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error occurred'
    }
  }
}

function generateMockReport(style: string, includeLinks: boolean): string {
  const friendlyTone = style === 'friendly'
  const directTone = style === 'direct'
  
  const greeting = friendlyTone 
    ? `Hi there! 👋 I've reviewed your code and I'm excited to share some insights with you.` 
    : directTone 
    ? `Code review complete. Here are the identified issues and recommendations.`
    : `Thank you for submitting your code for review. Below are my findings and suggestions.`

  const encouragement = friendlyTone 
    ? `

Remember, every piece of feedback is an opportunity to grow as a developer! 🌱`
    : ""

  const resourceLinks = includeLinks ? `

## 📚 Helpful Resources

- [TypeScript Handbook - Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
- [Web Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)` : ""

  return `# 🔍 Code Review Report

${greeting}

## 📋 Summary

I've analyzed your \`Button.tsx\` component and found a few areas where we can enhance the code quality, accessibility, and type safety. Overall, you're on the right track with a clean, functional component!

## 🚨 Issues Found

### 1. TypeScript Type Safety (Warning)
**File:** \`src/components/Button.tsx\` - Line 3  
**Issue:** Missing prop types for \`onClick\` and \`children\`

${friendlyTone ? "This is a great opportunity to strengthen your TypeScript skills! 💪" : "This reduces type safety and IDE support."}

**Current code:**
\`\`\`typescript
export const Button = ({ children, onClick }) => {
\`\`\`

**Suggested improvement:**
\`\`\`typescript
interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  variant?: 'primary' | 'secondary' | 'outline';
}

export const Button = ({ children, onClick, disabled, variant = 'primary' }: ButtonProps) => {
\`\`\`

### 2. Accessibility Enhancement (Error)
**File:** \`src/components/Button.tsx\` - Line 5  
**Issue:** Button lacks proper ARIA attributes

${friendlyTone ? "Accessibility is so important - you're making the web better for everyone! ♿️" : "This impacts users with assistive technologies."}

**Current code:**
\`\`\`typescript
<button onClick={onClick} style={{ padding: '10px' }}>
\`\`\`

**Suggested improvement:**
\`\`\`typescript
<button 
  onClick={onClick}
  disabled={disabled}
  className={cn("btn", \`btn-\${variant}\`)}
  aria-label={ariaLabel}
  type={type || "button"}
>
\`\`\`

## ✨ Additional Recommendations

### 1. Styling Improvements
Consider moving away from inline styles to a more maintainable approach:

\`\`\`typescript
// Use CSS modules or styled-components
const buttonStyles = {
  primary: "bg-blue-600 hover:bg-blue-700 text-white",
  secondary: "bg-gray-200 hover:bg-gray-300 text-gray-900",
  outline: "border border-gray-300 hover:bg-gray-50"
};
\`\`\`

### 2. Event Handler Type Safety
${friendlyTone ? "Let's make those event handlers even more robust! 🛡️" : "Improve type safety for event handlers:"}

\`\`\`typescript
onClick?: (event: React.MouseEvent<HTMLButtonElement>) => void;
\`\`\`

### 3. Loading State Support
Consider adding loading state support for better UX:

\`\`\`typescript
interface ButtonProps {
  // ... other props
  isLoading?: boolean;
}

// In the component
{isLoading ? <Spinner /> : children}
\`\`\`

## 🎯 Priority Action Items

1. **High Priority:** Add proper TypeScript interfaces
2. **High Priority:** Implement ARIA attributes for accessibility
3. **Medium Priority:** Replace inline styles with CSS classes
4. **Low Priority:** Add loading state and additional variants

${encouragement}

## 📊 Code Quality Score

- **Type Safety:** 6/10 → Target: 9/10
- **Accessibility:** 4/10 → Target: 10/10  
- **Maintainability:** 7/10 → Target: 9/10
- **Performance:** 8/10 → Target: 8/10

${resourceLinks}

---
*Generated with ❤️ by Devpathy - Your empathetic AI code reviewer*`
}

export interface VendorSkillMeta {
  official?: boolean
  source: string
  skills: Record<string, string> // sourceSkillName -> outputSkillName
}

/**
 * Hand-written skills with custom preferences/tastes/recommendations
 */
export const manual = [
  'deepwiki',
  'docs-simplify',
  'vitepress-migration',
]

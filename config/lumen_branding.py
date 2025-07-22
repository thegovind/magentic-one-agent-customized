class LumenBrandConfig:
    """Lumen brand configuration and theming for the Magentic-One Agent."""
    
    def __init__(self):
        self.primary_color = "#3b82f6"
        self.secondary_color = "#1e40af"
        self.accent_color = "#60a5fa"
        self.text_color = "#1f2937"
        self.background_color = "#ffffff"
        
        self.company_name = "Lumen Technologies"
        self.industry = "Technology"
        self.brand_voice = "Professional, innovative, customer-focused"
        
        self.logo_text = "LUMEN"
        self.tagline = "Enabling amazing things"
        
    def get_color_scheme(self):
        """Get the complete Lumen color scheme."""
        return {
            "primary": self.primary_color,
            "secondary": self.secondary_color,
            "accent": self.accent_color,
            "text": self.text_color,
            "background": self.background_color
        }
    
    def get_brand_identity(self):
        """Get Lumen brand identity information."""
        return {
            "company": self.company_name,
            "industry": self.industry,
            "voice": self.brand_voice,
            "logo": self.logo_text,
            "tagline": self.tagline
        }
    
    def get_header(self):
        """Get branded header for agent responses."""
        return f"""
╔══════════════════════════════════════════════════════════════╗
║  {self.logo_text} - {self.tagline}                                    ║
║  Technology Solutions & Channel Partner Support             ║
╚══════════════════════════════════════════════════════════════╝
        """.strip()
    
    def get_footer(self):
        """Get branded footer for agent responses."""
        return f"""
────────────────────────────────────────────────────────────────
{self.company_name} | Empowering Digital Transformation
For additional support: Contact your dedicated partner manager
        """.strip()
    
    def get_css_variables(self):
        """Get CSS variables for web interfaces."""
        return f"""
:root {{
    --lumen-primary: {self.primary_color};
    --lumen-secondary: {self.secondary_color};
    --lumen-accent: {self.accent_color};
    --lumen-text: {self.text_color};
    --lumen-background: {self.background_color};
}}
        """.strip()
    
    def get_styled_message(self, message: str, message_type: str = "info"):
        """Get a styled message with Lumen branding."""
        colors = {
            "info": self.primary_color,
            "success": "#10b981",
            "warning": "#f59e0b",
            "error": "#ef4444"
        }
        
        color = colors.get(message_type, self.primary_color)
        
        return f"""
┌─ {self.company_name} {message_type.upper()} ─────────────────────────────────
│ {message}
└─────────────────────────────────────────────────────────────
        """.strip()

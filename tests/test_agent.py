"""
Basic tests for the Lumen Magentic-One Agent functionality.
"""

import unittest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.lumen_branding import LumenBrandConfig
from templates.support_templates import CustomerSupportTemplates

class TestLumenBrandConfig(unittest.TestCase):
    """Test the Lumen brand configuration."""
    
    def setUp(self):
        self.brand_config = LumenBrandConfig()
    
    def test_primary_color(self):
        """Test that the primary color is set correctly."""
        self.assertEqual(self.brand_config.primary_color, "#3b82f6")
    
    def test_company_name(self):
        """Test that the company name is set correctly."""
        self.assertEqual(self.brand_config.company_name, "Lumen Technologies")
    
    def test_industry(self):
        """Test that the industry is set correctly."""
        self.assertEqual(self.brand_config.industry, "Technology")
    
    def test_color_scheme(self):
        """Test that the color scheme is returned correctly."""
        colors = self.brand_config.get_color_scheme()
        self.assertIn("primary", colors)
        self.assertEqual(colors["primary"], "#3b82f6")
    
    def test_brand_identity(self):
        """Test that the brand identity is returned correctly."""
        identity = self.brand_config.get_brand_identity()
        self.assertIn("company", identity)
        self.assertEqual(identity["company"], "Lumen Technologies")
    
    def test_header_contains_lumen(self):
        """Test that the header contains Lumen branding."""
        header = self.brand_config.get_header()
        self.assertIn("LUMEN", header)
        self.assertIn("Technology Solutions", header)
    
    def test_footer_contains_company(self):
        """Test that the footer contains company information."""
        footer = self.brand_config.get_footer()
        self.assertIn("Lumen Technologies", footer)
    
    def test_css_variables(self):
        """Test that CSS variables are generated correctly."""
        css = self.brand_config.get_css_variables()
        self.assertIn("--lumen-primary: #3b82f6", css)
    
    def test_styled_message(self):
        """Test that styled messages are formatted correctly."""
        message = self.brand_config.get_styled_message("Test message", "info")
        self.assertIn("Test message", message)
        self.assertIn("LUMEN", message)

class TestCustomerSupportTemplates(unittest.TestCase):
    """Test the customer support templates."""
    
    def setUp(self):
        self.templates = CustomerSupportTemplates()
    
    def test_scaling_template_generation(self):
        """Test that scaling templates are generated correctly."""
        partner_profile = {
            "partner_name": "Test Partner",
            "partner_tier": "Gold",
            "focus_area": "Cloud Services",
            "region": "North America"
        }
        
        template = self.templates.get_scaling_template(partner_profile)
        self.assertIn("Test Partner", template)
        self.assertIn("Gold", template)
        self.assertIn("Cloud Services", template)
        self.assertIn("GROWTH OPPORTUNITIES", template)
        self.assertIn("OPERATIONAL SCALING", template)
    
    def test_technical_template_generation(self):
        """Test that technical templates are generated correctly."""
        issue = "Network connectivity problem"
        template = self.templates.get_technical_template(issue, "high")
        
        self.assertIn("Network connectivity problem", template)
        self.assertIn("HIGH", template)
        self.assertIn("IMMEDIATE ASSESSMENT", template)
        self.assertIn("TECHNICAL SOLUTION", template)
    
    def test_product_inquiry_template(self):
        """Test that product inquiry templates are generated correctly."""
        template = self.templates.get_product_inquiry_template("Cloud", "Data backup")
        
        self.assertIn("Cloud", template)
        self.assertIn("Data backup", template)
        self.assertIn("SOLUTION OVERVIEW", template)
        self.assertIn("USE CASE ALIGNMENT", template)
    
    def test_onboarding_template(self):
        """Test that onboarding templates are generated correctly."""
        template = self.templates.get_onboarding_template("MSP", "Managed Services")
        
        self.assertIn("MSP", template)
        self.assertIn("Managed Services", template)
        self.assertIn("PARTNERSHIP OVERVIEW", template)
        self.assertIn("BUSINESS ENABLEMENT", template)

class TestAgentConfiguration(unittest.TestCase):
    """Test agent configuration and setup."""
    
    def test_oneshot_mode_config(self):
        """Test that oneshot mode is properly configured."""
        self.assertTrue(True)  # Placeholder for actual configuration test
    
    def test_lumen_customization(self):
        """Test that Lumen customizations are applied."""
        brand_config = LumenBrandConfig()
        
        self.assertEqual(brand_config.primary_color, "#3b82f6")
        self.assertEqual(brand_config.company_name, "Lumen Technologies")
        self.assertEqual(brand_config.industry, "Technology")
    
    def test_customer_support_focus(self):
        """Test that customer support features are configured."""
        templates = CustomerSupportTemplates()
        
        self.assertIsNotNone(templates.scaling_templates)
        self.assertIsNotNone(templates.technical_templates)
        self.assertIn("cloud_infrastructure", templates.scaling_templates)

if __name__ == "__main__":
    print("🧪 Running Lumen Magentic-One Agent Tests")
    print("=" * 50)
    
    unittest.main(verbosity=2)

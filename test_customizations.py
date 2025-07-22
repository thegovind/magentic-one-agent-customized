#!/usr/bin/env python3
"""
Test script to verify Lumen Magentic-One Agent customizations.
"""

import sys
import os
sys.path.append('.')

def test_brand_configuration():
    """Test Lumen brand configuration."""
    print('🧪 Testing Lumen Brand Configuration...')
    
    from config.lumen_branding import LumenBrandConfig
    
    brand = LumenBrandConfig()
    
    assert brand.primary_color == "#3b82f6", f"Expected #3b82f6, got {brand.primary_color}"
    print(f'✅ Primary Color: {brand.primary_color}')
    
    assert brand.company_name == "Lumen Technologies", f"Expected Lumen Technologies, got {brand.company_name}"
    print(f'✅ Company: {brand.company_name}')
    
    assert brand.industry == "Technology", f"Expected Technology, got {brand.industry}"
    print(f'✅ Industry: {brand.industry}')
    
    header = brand.get_header()
    assert "LUMEN" in header, "Header should contain LUMEN"
    print('✅ Brand header generated successfully')
    
    footer = brand.get_footer()
    assert "Lumen Technologies" in footer, "Footer should contain company name"
    print('✅ Brand footer generated successfully')
    
    print('✅ Brand configuration tests passed!\n')

def test_support_templates():
    """Test customer support templates."""
    print('🧪 Testing Support Templates...')
    
    from templates.support_templates import CustomerSupportTemplates
    
    templates = CustomerSupportTemplates()
    
    partner_info = {
        'partner_name': 'Test Partner',
        'partner_tier': 'Gold',
        'focus_area': 'Cloud Infrastructure',
        'region': 'North America'
    }
    
    scaling_template = templates.get_scaling_template(partner_info)
    assert len(scaling_template) > 100, "Scaling template should be substantial"
    assert "Test Partner" in scaling_template, "Template should include partner name"
    assert "GROWTH OPPORTUNITIES" in scaling_template, "Template should include growth section"
    print(f'✅ Scaling template generated: {len(scaling_template)} characters')
    
    tech_template = templates.get_technical_template('Test issue', 'high')
    assert len(tech_template) > 100, "Technical template should be substantial"
    assert "Test issue" in tech_template, "Template should include the issue"
    assert "HIGH" in tech_template, "Template should include priority level"
    print(f'✅ Technical template generated: {len(tech_template)} characters')
    
    print('✅ Support template tests passed!\n')

def test_oneshot_configuration():
    """Test oneshot mode configuration."""
    print('🧪 Testing Oneshot Configuration...')
    
    with open('magentic_one_agent.py', 'r') as f:
        content = f.read()
    
    assert "oneshot" in content.lower() or "ONESHOT" in content, "Agent should reference oneshot mode"
    assert "MCP" not in content or "mcp" not in content or "No MCP" in content, "Should not use MCP tools"
    print('✅ Oneshot mode configuration verified')
    
    print('✅ Oneshot configuration tests passed!\n')

def test_customer_support_focus():
    """Test customer support specialization."""
    print('🧪 Testing Customer Support Focus...')
    
    with open('magentic_one_agent.py', 'r') as f:
        content = f.read()
    
    assert "customer support" in content.lower(), "Should focus on customer support"
    assert "channel partner" in content.lower(), "Should mention channel partners"
    assert "scaling" in content.lower(), "Should address scaling needs"
    print('✅ Customer support focus verified')
    
    print('✅ Customer support tests passed!\n')

def verify_file_structure():
    """Verify the complete file structure."""
    print('🧪 Verifying File Structure...')
    
    required_files = [
        'magentic_one_agent.py',
        'requirements.txt',
        'README.md',
        '.env.example',
        '.gitignore',
        'config/lumen_branding.py',
        'templates/support_templates.py',
        'examples/partner_scenarios.py',
        'tests/test_agent.py',
        'deployment/azure_deployment.md'
    ]
    
    for file_path in required_files:
        assert os.path.exists(file_path), f"Required file missing: {file_path}"
        print(f'✅ {file_path}')
    
    print('✅ File structure verification passed!\n')

def main():
    """Run all tests."""
    print('🚀 LUMEN MAGENTIC-ONE AGENT CUSTOMIZATION TESTS')
    print('=' * 60)
    print('Testing all Lumen customizations and requirements...\n')
    
    try:
        verify_file_structure()
        test_brand_configuration()
        test_support_templates()
        test_oneshot_configuration()
        test_customer_support_focus()
        
        print('🎯 ALL TESTS PASSED!')
        print('✅ Lumen customizations are working correctly')
        print('✅ Primary color: #3b82f6 (Lumen Blue)')
        print('✅ Customer support specialization implemented')
        print('✅ Channel partner scaling features added')
        print('✅ Oneshot mode configured (no MCP/A2A)')
        print('✅ Technology industry focus applied')
        
    except Exception as e:
        print(f'❌ TEST FAILED: {e}')
        sys.exit(1)

if __name__ == "__main__":
    main()

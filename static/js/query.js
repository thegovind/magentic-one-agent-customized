// Query page specific JavaScript functionality
document.addEventListener('DOMContentLoaded', function() {
    console.log('🔍 Query page JavaScript loaded');
    
    // Initialize tab functionality
    initializeTabs();
    
    // Initialize form handling
    initializeFormHandling();
    
    // Initialize response functionality
    initializeResponseHandling();
});

function initializeTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            const tabName = this.getAttribute('data-tab');
            
            // Remove active class from all tabs and buttons
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and corresponding content
            this.classList.add('active');
            const targetContent = document.getElementById(tabName + '-tab');
            if (targetContent) {
                targetContent.classList.add('active');
            }
            
            // Clear form data when switching tabs
            clearFormData();
        });
    });
}

function initializeFormHandling() {
    const queryForm = document.getElementById('queryForm');
    if (queryForm) {
        queryForm.addEventListener('submit', handleFormSubmit);
    }
    
    // Auto-save form data to localStorage
    const formInputs = queryForm.querySelectorAll('input, select, textarea');
    formInputs.forEach(input => {
        // Load saved data on page load
        const savedValue = localStorage.getItem(`lumen_form_${input.name}`);
        if (savedValue && input.type !== 'submit') {
            input.value = savedValue;
        }
        
        // Save data on change
        input.addEventListener('change', function() {
            localStorage.setItem(`lumen_form_${input.name}`, this.value);
        });
    });
}

function handleFormSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const submitButton = form.querySelector('button[type="submit"]');
    const buttonText = submitButton.querySelector('.btn-text');
    const loadingSpinner = submitButton.querySelector('.loading');
    
    // Get active tab
    const activeTab = document.querySelector('.tab-btn.active').getAttribute('data-tab');
    
    // Collect form data
    const formData = collectFormData(form, activeTab);
    
    if (!formData.query.trim()) {
        LumenUtils.showNotification('Please enter your question or query.', 'warning');
        return;
    }
    
    // Show loading state
    setLoadingState(true, submitButton, buttonText, loadingSpinner);
    
    // Submit query to backend
    submitQuery(formData)
        .then(response => {
            displayResponse(response);
            // Clear form after successful submission
            if (!response.demo_mode) {
                clearFormData();
            }
        })
        .catch(error => {
            console.error('Query submission error:', error);
            LumenUtils.showNotification('Failed to process your query. Please try again.', 'error');
        })
        .finally(() => {
            setLoadingState(false, submitButton, buttonText, loadingSpinner);
        });
}

function collectFormData(form, queryType) {
    const formData = new FormData(form);
    const data = {
        query_type: queryType,
        query: '',
        partner_info: {},
        urgency: 'medium'
    };
    
    // Get the query text from the active tab
    const activeTabContent = document.querySelector(`#${queryType}-tab`);
    const queryTextarea = activeTabContent.querySelector('textarea[name="query"]');
    data.query = queryTextarea ? queryTextarea.value : '';
    
    // Collect partner information
    const partnerFields = ['partner_name', 'partner_tier', 'focus_area', 'region'];
    partnerFields.forEach(field => {
        const value = formData.get(field);
        if (value) {
            data.partner_info[field] = value;
        }
    });
    
    // Add query-specific data
    if (queryType === 'technical') {
        data.urgency = formData.get('urgency') || 'medium';
    }
    
    if (queryType === 'scaling') {
        if (formData.get('current_revenue')) {
            data.partner_info.current_revenue = formData.get('current_revenue');
        }
        if (formData.get('target_growth')) {
            data.partner_info.target_growth = formData.get('target_growth');
        }
    }
    
    if (queryType === 'onboarding') {
        if (formData.get('partner_type')) {
            data.partner_info.partner_type = formData.get('partner_type');
        }
        if (formData.get('business_focus')) {
            data.partner_info.business_focus = formData.get('business_focus');
        }
    }
    
    return data;
}

async function submitQuery(data) {
    const response = await fetch('/api/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });
    
    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Network error');
    }
    
    return await response.json();
}

function displayResponse(response) {
    const responseContainer = document.getElementById('responseContainer');
    const responseContent = document.getElementById('responseContent');
    const demoBadge = responseContainer.querySelector('.demo-badge');
    
    // Show/hide demo badge
    if (response.demo_mode) {
        demoBadge.style.display = 'inline-block';
    } else {
        demoBadge.style.display = 'none';
    }
    
    // Display response content
    responseContent.textContent = response.response;
    responseContainer.style.display = 'block';
    
    // Smooth scroll to response
    responseContainer.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
    
    // Show success notification
    const mode = response.demo_mode ? 'demo' : 'live';
    LumenUtils.showNotification(`Query processed successfully in ${mode} mode!`, 'success');
}

function setLoadingState(isLoading, button, buttonText, spinner) {
    if (isLoading) {
        button.disabled = true;
        buttonText.textContent = 'Processing...';
        spinner.classList.add('active');
        button.classList.add('btn-loading');
    } else {
        button.disabled = false;
        buttonText.textContent = 'Submit Query';
        spinner.classList.remove('active');
        button.classList.remove('btn-loading');
    }
}

function clearFormData() {
    const form = document.getElementById('queryForm');
    if (form) {
        const textareas = form.querySelectorAll('textarea');
        textareas.forEach(textarea => {
            if (textarea.name === 'query') {
                textarea.value = '';
            }
        });
        
        // Clear localStorage for query fields
        textareas.forEach(textarea => {
            if (textarea.name === 'query') {
                localStorage.removeItem(`lumen_form_${textarea.name}`);
            }
        });
    }
}

function initializeResponseHandling() {
    // Add global functions for response actions
    window.clearResponse = function() {
        const responseContainer = document.getElementById('responseContainer');
        responseContainer.style.display = 'none';
        
        // Clear the query field in the active tab
        const activeTab = document.querySelector('.tab-btn.active').getAttribute('data-tab');
        const activeTabContent = document.querySelector(`#${activeTab}-tab`);
        const queryTextarea = activeTabContent.querySelector('textarea[name="query"]');
        if (queryTextarea) {
            queryTextarea.value = '';
            queryTextarea.focus();
        }
    };
    
    window.copyResponse = function() {
        const responseContent = document.getElementById('responseContent');
        const text = responseContent.textContent;
        
        LumenUtils.copyToClipboard(text)
            .then(() => {
                LumenUtils.showNotification('Response copied to clipboard!', 'success');
            })
            .catch(() => {
                LumenUtils.showNotification('Failed to copy response.', 'error');
            });
    };
}

// Sample queries for quick testing
const sampleQueries = {
    general: "What Lumen solutions are best for small business cloud services?",
    scaling: "We're looking to expand our cloud services offering to small businesses. What strategies would help us scale our operations efficiently?",
    technical: "We're experiencing intermittent connectivity issues with our SD-WAN deployment. Need guidance on troubleshooting.",
    onboarding: "We're a new partner specializing in managed services. What should we prioritize to get started quickly?"
};

// Add sample query functionality
function loadSampleQuery() {
    const activeTab = document.querySelector('.tab-btn.active').getAttribute('data-tab');
    const activeTabContent = document.querySelector(`#${activeTab}-tab`);
    const queryTextarea = activeTabContent.querySelector('textarea[name="query"]');
    
    if (queryTextarea && sampleQueries[activeTab]) {
        queryTextarea.value = sampleQueries[activeTab];
        LumenUtils.showNotification('Sample query loaded!', 'info');
    }
}

// Expose sample query function globally
window.loadSampleQuery = loadSampleQuery;
import re

def extract_emails(text):
    # Regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the text
    emails = re.findall(email_pattern, text)
    
    return emails

# Test the function
input_text = 'Contact us at support@example.com and sales@example.org.'
emails = extract_emails(input_text)
print(f"Extracted emails: {emails}")
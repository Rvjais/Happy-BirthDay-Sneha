import os
import glob

# Replace September 16 with September 17 in all HTML files
html_files = glob.glob("**/*.html", recursive=True)

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "September 16" in content or "16th September" in content or "16 Sept" in content:
        content = content.replace("September 16", "September 17")
        content = content.replace("16th September", "17th September")
        content = content.replace("16 Sept", "17 Sept")
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Updated birthday date")

import os
import re

# Append CSS for pagination
css_path = '/Users/devit/Desktop/sdfds/style.css'
with open(css_path, 'a', encoding='utf-8') as f:
    f.write("""
/* Pagination Navigation */
.page-navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 3rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
}
.page-nav-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.8rem 1.5rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: var(--text-primary);
    border-radius: 4px;
    font-weight: 600;
    transition: all 0.3s ease;
}
.page-nav-btn:hover {
    background: var(--accent-gold);
    color: #000;
    border-color: var(--accent-gold);
}
.page-nav-btn.next {
    margin-left: auto;
}
.page-nav-btn span {
    color: var(--accent-silver);
}
.page-nav-btn:hover span {
    color: #333;
}
""")

pages = [
    ('index.html', 'หน้าแรก'),
    ('history.html', 'ประวัติศาสตร์'),
    ('hardware.html', 'ฮาร์ดแวร์'),
    ('coding.html', 'การเขียนโค้ด'),
    ('setup.html', 'การตั้งค่าระบบ'),
    ('hosting.html', 'โฮสติ้ง'),
    ('seo.html', 'การปรับแต่ง SEO')
]

for i in range(1, len(pages)): # Skip index.html
    current_file = pages[i][0]
    prev_file = pages[i-1][0]
    prev_name = pages[i-1][1]
    
    next_file = pages[i+1][0] if i+1 < len(pages) else None
    next_name = pages[i+1][1] if next_file else None

    nav_html = '<div class="page-navigation">'
    nav_html += f'<a href="{prev_file}" class="page-nav-btn prev">&larr; ย้อนกลับ: <span>{prev_name}</span></a>'
    
    if next_file:
        nav_html += f'<a href="{next_file}" class="page-nav-btn next">หน้าถัดไป: <span>{next_name}</span> &rarr;</a>'
    else:
        # Last page goes to home
        nav_html += f'<a href="index.html" class="page-nav-btn next">กลับสู่: <span>หน้าแรก</span> &rarr;</a>'
        
    nav_html += '</div>'

    file_path = f'/Users/devit/Desktop/sdfds/{current_file}'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert before the Footer
    if '<div class="page-navigation">' not in content:
        content = content.replace('<!-- Footer -->', nav_html + '\n<!-- Footer -->')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Pagination navigation added to all pages.")

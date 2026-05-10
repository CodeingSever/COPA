import re

with open('/Users/devit/Desktop/sdfds/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace nav links in the content first
new_nav = """<div class="nav-links">
                <a href="index.html">หน้าแรก</a>
                <a href="history.html">ประวัติศาสตร์</a>
                <a href="hardware.html">ฮาร์ดแวร์</a>
                <a href="coding.html">การเขียนโค้ด</a>
                <a href="setup.html">การตั้งค่าระบบ</a>
                <a href="hosting.html">โฮสติ้ง</a>
                <a href="seo.html">การปรับแต่ง SEO</a>
            </div>"""
content = re.sub(r'<div class="nav-links">.*?</div>', new_nav, content, flags=re.DOTALL)

# Update logo link to point to index.html
content = re.sub(r'<a href="#" class="logo">', '<a href="index.html" class="logo">', content)

# Extract template parts
head_match = re.search(r'(.*?<!-- Navigation -->.*?</nav>)', content, re.DOTALL)
template_top = head_match.group(1)

footer_match = re.search(r'(<!-- Footer -->.*)', content, re.DOTALL)
template_bottom = footer_match.group(1)

# Extract sections safely
def extract_section(regex_str):
    match = re.search(regex_str, content, re.DOTALL)
    return match.group(1) if match else ""

hero = extract_section(r'(<!-- Hero Section -->.*?</header>)')
history = extract_section(r'(<!-- Section: Computer History -->.*?</section>)')
hardware = extract_section(r'(<!-- Section: Hardware -->.*?</section>)')
coding = extract_section(r'(<!-- Section: Coding Basics -->.*?</section>)')
setup = extract_section(r'(<!-- Section: Environment Setup -->.*?</section>)')
hosting = extract_section(r'(<!-- Section: Website Hosting -->.*?</section>)')
seo = extract_section(r'(<!-- Section: Search Engine Deployment -->.*?</section>)')

def write_page(filename, body_content):
    with open(f'/Users/devit/Desktop/sdfds/{filename}', 'w', encoding='utf-8') as f:
        f.write(template_top + "\n" + body_content + "\n" + template_bottom)

write_page('index.html', hero)
write_page('history.html', history)
write_page('hardware.html', hardware)
write_page('coding.html', coding)
write_page('setup.html', setup)
write_page('hosting.html', hosting)
write_page('seo.html', seo)

print("Split completed successfully")

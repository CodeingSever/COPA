import re
import base64
import os

images = {
    'abacus': '/Users/devit/.gemini/antigravity/brain/63e23425-7e2b-4355-9937-5210a6897f6d/history_abacus_1778446500959.png',
    'analytical': '/Users/devit/.gemini/antigravity/brain/63e23425-7e2b-4355-9937-5210a6897f6d/history_analytical_1778446517228.png',
    'eniac': '/Users/devit/.gemini/antigravity/brain/63e23425-7e2b-4355-9937-5210a6897f6d/history_eniac_1778446530660.png',
    'microprocessor': '/Users/devit/.gemini/antigravity/brain/63e23425-7e2b-4355-9937-5210a6897f6d/history_microprocessor_1778446545917.png',
    'quantum': '/Users/devit/.gemini/antigravity/brain/63e23425-7e2b-4355-9937-5210a6897f6d/history_quantum_1778446559916.png'
}

b64_images = {}
for key, path in images.items():
    with open(path, 'rb') as f:
        b64_images[key] = f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

history_html = f"""
            <div class="split-layout" style="margin-bottom: 6rem;">
                <div class="split-content reveal">
                    <div class="timeline-date" style="color: var(--accent-gold); font-weight: bold; margin-bottom: 0.5rem;">ยุคโบราณ (2700 ปีก่อนคริสตกาล)</div>
                    <h3 class="timeline-title" style="font-size: 2rem; margin-bottom: 1rem;">จุดเริ่มต้น: ลูกคิด (Abacus)</h3>
                    <p>อุปกรณ์ช่วยคำนวณชิ้นแรกๆ ของมนุษยชาติ ถือกำเนิดขึ้นในเมโสโปเตเมียและจีนโบราณ เป็นรากฐานสำคัญที่จุดประกายแนวคิดในการใช้เครื่องมือเพื่อช่วยประมวลผลข้อมูลและตัวเลขที่ซับซ้อน</p>
                </div>
                <div class="split-image reveal">
                    <img src="{b64_images['abacus']}" alt="ลูกคิดโบราณ">
                </div>
            </div>

            <div class="split-layout reverse" style="margin-bottom: 6rem;">
                <div class="split-content reveal">
                    <div class="timeline-date" style="color: var(--accent-gold); font-weight: bold; margin-bottom: 0.5rem;">ค.ศ. 1837</div>
                    <h3 class="timeline-title" style="font-size: 2rem; margin-bottom: 1rem;">เครื่องจักรเชิงวิเคราะห์ (Analytical Engine)</h3>
                    <p>ออกแบบโดย Charles Babbage บิดาแห่งคอมพิวเตอร์ นี่คือแบบร่างของเครื่องจักรกลที่ขับเคลื่อนด้วยฟันเฟืองและไอน้ำ ซึ่งมีโครงสร้างเทียบเท่ากับคอมพิวเตอร์ยุคใหม่ (มีหน่วยความจำและหน่วยประมวลผล) แม้จะสร้างไม่เสร็จในยุคนั้นก็ตาม</p>
                </div>
                <div class="split-image reveal">
                    <img src="{b64_images['analytical']}" alt="เครื่องจักรกลของ Charles Babbage">
                </div>
            </div>

            <div class="split-layout" style="margin-bottom: 6rem;">
                <div class="split-content reveal">
                    <div class="timeline-date" style="color: var(--accent-gold); font-weight: bold; margin-bottom: 0.5rem;">ค.ศ. 1945</div>
                    <h3 class="timeline-title" style="font-size: 2rem; margin-bottom: 1rem;">ENIAC & หลอดสุญญากาศ</h3>
                    <p>จุดเริ่มต้นของคอมพิวเตอร์อิเล็กทรอนิกส์อเนกประสงค์เครื่องแรก ENIAC มีขนาดใหญ่เท่าห้อง ใช้หลอดสุญญากาศกว่า 18,000 หลอดในการคำนวณวิถีกระสุนด้วยความเร็วที่ไม่เคยมีมาก่อนในประวัติศาสตร์</p>
                </div>
                <div class="split-image reveal">
                    <img src="{b64_images['eniac']}" alt="คอมพิวเตอร์ ENIAC ขนาดเท่าห้อง">
                </div>
            </div>

            <div class="split-layout reverse" style="margin-bottom: 6rem;">
                <div class="split-content reveal">
                    <div class="timeline-date" style="color: var(--accent-gold); font-weight: bold; margin-bottom: 0.5rem;">ค.ศ. 1971</div>
                    <h3 class="timeline-title" style="font-size: 2rem; margin-bottom: 1rem;">การปฏิวัติชิปซิลิคอน (Microprocessor)</h3>
                    <p>Intel เปิดตัว 4004 ซึ่งย่อพลังการประมวลผลของเครื่องเมนเฟรมขนาดยักษ์ลงในชิปซิลิคอนขนาดเล็กเพียงชิ้นเดียว นำไปสู่การถือกำเนิดของยุคคอมพิวเตอร์ส่วนบุคคล (PC) และอุปกรณ์พกพาในปัจจุบัน</p>
                </div>
                <div class="split-image reveal">
                    <img src="{b64_images['microprocessor']}" alt="ชิปไมโครโปรเซสเซอร์รุ่นแรก">
                </div>
            </div>

            <div class="split-layout" style="margin-bottom: 6rem;">
                <div class="split-content reveal">
                    <div class="timeline-date" style="color: var(--accent-gold); font-weight: bold; margin-bottom: 0.5rem;">อนาคต</div>
                    <h3 class="timeline-title" style="font-size: 2rem; margin-bottom: 1rem;">ควอนตัมคอมพิวเตอร์ (Quantum Leap)</h3>
                    <p>สถาปัตยกรรมระดับอะตอมที่ใช้ "คิวบิต (Qubits)" ในการคำนวณสถานะที่ทับซ้อนกัน นำมาซึ่งพลังประมวลผลแบบก้าวกระโดดที่จะทำลายขีดจำกัดเดิม และแก้ปัญหาที่ซูเปอร์คอมพิวเตอร์ปัจจุบันต้องใช้เวลาหลายล้านปีในเวลาเพียงไม่กี่วินาที</p>
                </div>
                <div class="split-image reveal">
                    <img src="{b64_images['quantum']}" alt="ควอนตัมคอมพิวเตอร์ล้ำสมัย">
                </div>
            </div>
"""

file_path = '/Users/devit/Desktop/sdfds/history.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the existing timeline div with the new split-layout blocks
new_content = re.sub(r'<div class="timeline">.*?</div>', history_html, content, flags=re.DOTALL)

# Add padding to history section so it's not hidden under navbar
new_content = new_content.replace('<section id="history" class="section history-section dark-bg">', '<section id="history" class="section history-section dark-bg" style="padding-top: 150px;">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated history.html with comprehensive history and base64 images.")

import re

# 파일 읽기
with open('week_4_ko_el_5_2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# <!DOCTYPE html>부터 시작하는 올바른 HTML 찾기
html_start = content.find('<!DOCTYPE html>')
if html_start == -1:
    print("올바른 HTML 시작점을 찾을 수 없습니다.")
else:
    # 첫 번째 올바른 HTML 부분만 추출
    content = content[html_start:]
    
    # </html>로 끝나는 부분 찾기
    html_end = content.find('</html>') + len('</html>')
    if html_end > len('</html>'):
        content = content[:html_end]
    
    # 분수 스타일 CSS 추가
    fraction_css = """
        /* 분수 표시 스타일 */
        .fraction {
            display: inline-block;
            vertical-align: middle;
            text-align: center;
            margin: 0 3px;
            font-size: inherit;
            font-weight: inherit;
        }
        
        .fraction .num {
            display: block;
            border-bottom: 2px solid currentColor;
            padding: 0 5px 2px 5px;
            line-height: 1.2;
        }
        
        .fraction .denom {
            display: block;
            padding: 2px 5px 0 5px;
            line-height: 1.2;
        }
        
        .mixed-number {
            display: inline-flex;
            align-items: center;
            gap: 3px;
        }
        
        .mixed-number .whole {
            font-size: 1em;
        }
"""
    
    # CSS를 body 스타일 앞에 삽입
    body_pos = content.find('        body {')
    if body_pos > 0:
        content = content[:body_pos] + fraction_css + '\n' + content[body_pos:]
    
    # 분수 표현을 HTML 형식으로 변경
    replacements = [
        ('12/4', '<span class="fraction"><span class="num">12</span><span class="denom">4</span></span>'),
        ('7/4', '<span class="fraction"><span class="num">7</span><span class="denom">4</span></span>'),
        ('2/7', '<span class="fraction"><span class="num">2</span><span class="denom">7</span></span>'),
        ('10/7', '<span class="fraction"><span class="num">10</span><span class="denom">7</span></span>'),
        ('2/5', '<span class="fraction"><span class="num">2</span><span class="denom">5</span></span>'),
        ('6/5', '<span class="fraction"><span class="num">6</span><span class="denom">5</span></span>'),
        ('1/5', '<span class="fraction"><span class="num">1</span><span class="denom">5</span></span>'),
        ('3/4', '<span class="fraction"><span class="num">3</span><span class="denom">4</span></span>'),
        ('1/3', '<span class="fraction"><span class="num">1</span><span class="denom">3</span></span>'),
        ('4/3', '<span class="fraction"><span class="num">4</span><span class="denom">3</span></span>'),
        ('8/3', '<span class="fraction"><span class="num">8</span><span class="denom">3</span></span>'),
        ('2/3', '<span class="fraction"><span class="num">2</span><span class="denom">3</span></span>'),
        ('1/4', '<span class="fraction"><span class="num">1</span><span class="denom">4</span></span>'),
        ('9/4', '<span class="fraction"><span class="num">9</span><span class="denom">4</span></span>'),
        ('27/4', '<span class="fraction"><span class="num">27</span><span class="denom">4</span></span>'),
        ('1/2', '<span class="fraction"><span class="num">1</span><span class="denom">2</span></span>'),
        ('3/5', '<span class="fraction"><span class="num">3</span><span class="denom">5</span></span>'),
        ('5/6', '<span class="fraction"><span class="num">5</span><span class="denom">6</span></span>'),
        ('3/8', '<span class="fraction"><span class="num">3</span><span class="denom">8</span></span>'),
        ('3/2', '<span class="fraction"><span class="num">3</span><span class="denom">2</span></span>'),
        ('1/6', '<span class="fraction"><span class="num">1</span><span class="denom">6</span></span>'),
        ('12/3', '<span class="fraction"><span class="num">12</span><span class="denom">3</span></span>'),
        ('13/2', '<span class="fraction"><span class="num">13</span><span class="denom">2</span></span>'),
    ]
    
    # 대분수 형식 변경
    mixed_replacements = [
        ('1과 1/5', '<span class="mixed-number"><span class="whole">1</span>과 <span class="fraction"><span class="num">1</span><span class="denom">5</span></span></span>'),
        ('1과 1/3', '<span class="mixed-number"><span class="whole">1</span>과 <span class="fraction"><span class="num">1</span><span class="denom">3</span></span></span>'),
        ('2와 2/3', '<span class="mixed-number"><span class="whole">2</span>와 <span class="fraction"><span class="num">2</span><span class="denom">3</span></span></span>'),
        ('2와 1/4', '<span class="mixed-number"><span class="whole">2</span>와 <span class="fraction"><span class="num">1</span><span class="denom">4</span></span></span>'),
        ('6과 1/4', '<span class="mixed-number"><span class="whole">6</span>과 <span class="fraction"><span class="num">1</span><span class="denom">4</span></span></span>'),
        ('6과 3/4', '<span class="mixed-number"><span class="whole">6</span>과 <span class="fraction"><span class="num">3</span><span class="denom">4</span></span></span>'),
        ('7과 1/4', '<span class="mixed-number"><span class="whole">7</span>과 <span class="fraction"><span class="num">1</span><span class="denom">4</span></span></span>'),
        ('1과 3/4', '<span class="mixed-number"><span class="whole">1</span>과 <span class="fraction"><span class="num">3</span><span class="denom">4</span></span></span>'),
        ('1과 3/7', '<span class="mixed-number"><span class="whole">1</span>과 <span class="fraction"><span class="num">3</span><span class="denom">7</span></span></span>'),
        ('2와1/6', '<span class="mixed-number"><span class="whole">2</span>와<span class="fraction"><span class="num">1</span><span class="denom">6</span></span></span>'),
        ('6과1/2', '<span class="mixed-number"><span class="whole">6</span>과<span class="fraction"><span class="num">1</span><span class="denom">2</span></span></span>'),
        ('1과1/2', '<span class="mixed-number"><span class="whole">1</span>과<span class="fraction"><span class="num">1</span><span class="denom">2</span></span></span>'),
    ]
    
    # 먼저 대분수를 변경
    for old, new in mixed_replacements:
        content = content.replace(old, new)
    
    # 그 다음 일반 분수를 변경
    for old, new in replacements:
        # 이미 HTML로 변경된 부분은 건너뛰기
        if 'class="fraction"' not in content[:content.find(old) if old in content else len(content)]:
            # 단어 경계를 확인하여 정확한 매칭
            pattern = r'\b' + re.escape(old) + r'\b'
            content = re.sub(pattern, new, content)
    
    # MathJax 관련 스크립트 제거
    content = re.sub(r'<script src="[^"]*mathjax[^"]*"></script>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<script>\s*MathJax\s*=\s*\{[^}]*\}[^<]*</script>', '', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 새 파일로 저장
    with open('week_4_ko_el_5_2_fixed.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("파일이 수정되어 week_4_ko_el_5_2_fixed.html로 저장되었습니다.")
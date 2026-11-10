import os
from html import escape
from v1_script import LAYERS, STYLES
from render_utils import render_split_keyboard

OUT_DIR = "/Users/yong/Documents/UseVia/wallpapers"

# Version 4: Cheatsheet Hybrid Edition
# Left: Large L0 Base & L1 Nav/Num Keyboards
# Right: 4 Structured Action Cheat Sheet Cards
W, H = 1920, 1080

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
svg.append('<defs>')
svg.append('<linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
svg.append('  <stop offset="0%" stop-color="#090d16"/>')
svg.append('  <stop offset="50%" stop-color="#0f172a"/>')
svg.append('  <stop offset="100%" stop-color="#020617"/>')
svg.append('</linearGradient>')
svg.append('<filter id="cardGlow" x="-10%" y="-10%" width="120%" height="120%">')
svg.append('  <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000000" flood-opacity="0.4"/>')
svg.append('</filter>')
svg.append('</defs>')

# Background
svg.append(f'<rect width="{W}" height="{H}" fill="url(#bgGrad)"/>')

# Safe zone guide line
svg.append('<rect x="160" y="15" width="1600" height="1050" fill="none" stroke="#1e293b" stroke-dasharray="4 4" stroke-width="0.8"/>')

# Header
svg.append('<g transform="translate(960, 48)">')
svg.append('  <text fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="24" font-weight="800" text-anchor="middle" letter-spacing="1.5">X.TIPS X7 — CHEATSHEET HYBRID EDITION (Ver. 4)</text>')
svg.append('  <text y="24" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="13" font-weight="500" text-anchor="middle">왼쪽: 메인 키보드 하드웨어 그래픽 (L0 / L1)  |  오른쪽: 실전 단축키 &amp; 상황별 치트시트 요약표</text>')
svg.append('</g>')

# Left Section: 2 Keyboards (L0 Base, L1 Nav/Num)
# bx: 175, Width: 770
# Top KB: by = 95, Height = 450
# Bot KB: by = 565, Height = 480
left_kbs = [
    (175, 95, 450, LAYERS[0]),  # Layer 0 Base
    (175, 565, 480, LAYERS[1]), # Layer 1 Nav/Num
]

for bx, by, bh, layer_data in left_kbs:
    svg.append(f'<rect x="{bx}" y="{by}" width="770" height="{bh}" rx="14" fill="#0f172a" fill-opacity="0.85" stroke="#334155" stroke-width="1.5" filter="url(#cardGlow)"/>')
    kb_x = bx + 22
    kb_y = by + 62
    svg.append(render_split_keyboard(layer_data, kb_x, kb_y, kw=66, kh=47, col_gap=6, row_gap=6, split_gap=52, title_mode="full"))

# Right Section: 4 Cheatsheet Cards (2 rows x 2 cols inside 770px width)
# rx_base = 975, width = 770
# Row 1: y = 95, height = 450
# Card 1 (IDE): x = 975, w = 375
# Card 2 (Window): x = 1370, w = 375
# Row 2: y = 565, height = 480
# Card 3 (Browser): x = 975, w = 375
# Card 4 (Thumb & Quick): x = 1370, w = 375

def render_cheat_card(x, y, w, h, title, icon, color, shortcuts):
    res = []
    res.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#0f172a" fill-opacity="0.9" stroke="{color}" stroke-opacity="0.4" stroke-width="1.5" filter="url(#cardGlow)"/>')
    # Card Header
    res.append(f'<rect x="{x}" y="{y}" width="{w}" height="42" rx="14" fill="{color}" fill-opacity="0.12"/>')
    res.append(f'<line x1="{x}" y1="{y+42}" x2="{x+w}" y2="{y+42}" stroke="{color}" stroke-opacity="0.3" stroke-width="1"/>')
    res.append(f'<text x="{x + 16}" y="{y + 26}" fill="{color}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="14" font-weight="700">{icon} {escape(title)}</text>')
    
    # Shortcut rows
    start_y = y + 62
    line_h = 32
    for i, (key_label, desc_label) in enumerate(shortcuts):
        cur_y = start_y + i * line_h
        # Key Badge
        res.append(f'<rect x="{x + 14}" y="{cur_y - 14}" width="105" height="22" rx="5" fill="#1e293b" stroke="#475569" stroke-width="1"/>')
        res.append(f'<text x="{x + 66}" y="{cur_y}" fill="#f8fafc" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="11" font-weight="700" text-anchor="middle" dominant-baseline="central">{escape(key_label)}</text>')
        # Description
        res.append(f'<text x="{x + 128}" y="{cur_y}" fill="#cbd5e1" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="12" font-weight="500" dominant-baseline="central">{escape(desc_label)}</text>')
    
    return "\n".join(res)

# Card 1: IDE / VS Code (Layer 5)
ide_shortcuts = [
    ("X + F5", "디버깅 시작 / 계속"),
    ("X + ⇧F5", "디버깅 중지"),
    ("X + ⇧⌘F5", "디버깅 재시작"),
    ("X + F9", "중단점(Breakpoint) 토글"),
    ("X + F10", "Step Over (한줄 건너뜀)"),
    ("X + F11 / ⇧F11", "Step Into / Step Out"),
    ("X + ⌥↑ / ⌥↓", "현재 줄 위/아래 이동"),
    ("X + ⌥⇧↓", "현재 줄 아래 복사"),
    ("X + ⌘/", "한 줄 주석 토글"),
    ("X + ⌥F12", "함수 정의 미리보기 (Peek)"),
    ("X + ⇧⌘F", "전체 파일 내용 검색"),
    ("X + ⇧⌘P", "명령 팔레트 열기"),
]

# Card 2: Window Management (Layer 6)
window_shortcuts = [
    ("C + H / L", "창 좌반 / 우반 분할 (Rectangle)"),
    ("C + J / K", "창 하반 / 상반 분할"),
    ("C + U / I", "좌상 / 우상 코너 분할"),
    ("C + J / K(엄)", "좌하 / 우하 코너 분할"),
    ("C + Enter", "전체 화면 최대화"),
    ("C + Backspace", "창 원래 크기로 복원"),
    ("C + ` (백틱)", "동일 앱 내 창 전환 (⌘`)"),
    ("C + ⌃← / ⌃→", "가상 데스크톱 이전/다음"),
    ("C + M", "창 최소화 (⌘M)"),
    ("C + W", "현재 창/탭 닫기 (⌘W)"),
    ("C + ⌥⌘E", "화면 중앙 정렬 (Almost Max)"),
    ("C + ⌥⌘C", "화면 정중앙 배치"),
]

# Card 3: Browser & Text Edit (Layer 4)
browser_shortcuts = [
    ("Z + T", "새 탭 열기 (⌘T)"),
    ("Z + W", "현재 탭 닫기 (⌘W)"),
    ("Z + ⇧T", "닫았던 마지막 탭 복구"),
    ("Z + R", "현재 페이지 새로고침 (⌘R)"),
    ("Z + L", "URL 주소창 즉시 포커스"),
    ("Z + [ / ]", "뒤로 가기 / 앞으로 가기"),
    ("Z + ⌥← / ⌥→", "단어 단위 커서 이동"),
    ("Z + ⌥Backspace", "단어 단위 삭제"),
    ("Z + ⌘← / ⌘→", "줄 맨앞 / 줄 맨끝 이동"),
    ("Z + ⌘A / ⌘S", "전체 선택 / 파일 저장"),
    ("Z + ⌘Z / ⇧⌘Z", "실행 취소 / 다시 실행"),
    ("Z + ⌥⌘I", "개발자 도구 (Inspector)"),
]

# Card 4: Thumb Clusters & System Quick (Layer 2, 3, 7, 8)
thumb_shortcuts = [
    ("Space Hold", "Layer 1 활성화 (숫자/방향키)"),
    ("Enter Hold", "Layer 2 활성화 (Shift 특수기호)"),
    ("L-Thumb MO(3)", "Layer 3 (마우스/휠/볼륨)"),
    ("V Hold", "Layer 7 (오른손 3x3 넘패드)"),
    ("B Hold", "Layer 8 (화면캡처/화면잠금)"),
    ("B + ⌃⌘Q", "화면 즉시 잠금 (Lock Screen)"),
    ("B + ⌘⇧4", "영역 캡처 (선택 영역 스크린샷)"),
    ("B + ⌘⇧5", "화면 녹화 / 캡처 바 열기"),
    ("B + ⌃⌘Space", "맥 이모지 &amp; 특수문자 입력창"),
    ("Caps Tap", "한/영 전환 (단독 탭)"),
    ("SftEnt Tap", "단독 탭: Enter / 홀드: Shift"),
    ("L1 Right 3키", "← / ↓ / ↑ / → 풀 화살표"),
]

svg.append(render_cheat_card(975, 95, 375, 450, "IDE 코딩 &amp; 디버깅 (X Hold)", "💻", "#10b981", ide_shortcuts))
svg.append(render_cheat_card(1370, 95, 375, 450, "창 분할 &amp; 멀티태스킹 (C Hold)", "🪟", "#a855f7", window_shortcuts))
svg.append(render_cheat_card(975, 565, 375, 480, "브라우징 &amp; 텍스트편집 (Z Hold)", "🌐", "#0ea5e9", browser_shortcuts))
svg.append(render_cheat_card(1370, 565, 375, 480, "엄지 레이어 &amp; 시스템 핫키", "⚡", "#f59e0b", thumb_shortcuts))

# Footer
svg.append('<g transform="translate(960, 1065)">')
svg.append('  <text fill="#64748b" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="11" font-weight="500" text-anchor="middle">X.Tips X7 36-Key Split Keyboard Cheat Sheet Wallpaper — All shortcuts tailored for macOS &amp; VS Code</text>')
svg.append('</g>')

svg.append('</svg>')

out_path = f"{OUT_DIR}/version4_cheatsheet_hybrid.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print(f"Saved {out_path}")

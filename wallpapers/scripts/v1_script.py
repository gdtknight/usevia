import os
import json
from html import escape

OUT_DIR = "/Users/yong/Documents/UseVia/wallpapers"
os.makedirs(OUT_DIR, exist_ok=True)

STYLES = {
    "normal":  {"bg": "#1e293b", "border": "#475569", "main": "#f8fafc", "sub": "#94a3b8"},
    "hold":    {"bg": "#78350f", "border": "#f59e0b", "main": "#fef08a", "sub": "#fde68a"},
    "layer":   {"bg": "#3b0764", "border": "#a855f7", "main": "#f3e8ff", "sub": "#d8b4fe"},
    "mod":     {"bg": "#172554", "border": "#3b82f6", "main": "#dbeafe", "sub": "#93c5fd"},
    "accent1": {"bg": "#083344", "border": "#06b6d4", "main": "#ecfeff", "sub": "#67e8f9"},
    "accent2": {"bg": "#064e3b", "border": "#10b981", "main": "#ecfdf5", "sub": "#6ee7b7"},
    "warn":    {"bg": "#4c0519", "border": "#f43f5e", "main": "#ffe4e6", "sub": "#fda4af"},
    "muted":   {"bg": "#0f172a", "border": "#1e293b", "main": "#475569", "sub": "#334155"},
}

LAYERS = [
    {
        "num": 0,
        "title": "Layer 0: Base (QWERTY & 한/영)",
        "trigger": "기본 상태 (Base)",
        "left": [
            [("Q", "ㅂ", "normal"), ("W", "ㅈ", "normal"), ("E", "ㄷ", "normal"), ("R", "ㄱ", "normal"), ("T", "ㅅ", "normal")],
            [("A", "ㅁ", "normal"), ("S", "ㄴ", "normal"), ("D", "ㅇ", "normal"), ("F", "ㄹ", "normal"), ("G", "ㅎ", "normal")],
            [("Z", "L4", "layer"), ("X", "L5", "layer"), ("C", "L6", "layer"), ("V", "L7", "layer"), ("B", "L8", "layer")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("Y", "ㅛ", "normal"), ("U", "ㅕ", "normal"), ("I", "ㅑ", "normal"), ("O", "ㅐ", "normal"), ("P", "ㅔ", "normal")],
            [("H", "ㅗ", "normal"), ("J", "ㅓ", "normal"), ("K", "ㅏ", "normal"), ("L", "ㅣ", "normal"), ("Bksp", "⌫", "warn")],
            [("N", "ㅜ", "normal"), ("M", "ㅡ", "normal"), ("Tab", "⇥", "mod"), ("Caps", "한/영", "accent1"), ("SftEnt", "⇧/⏎", "mod")],
        ],
        "right_thumb": [("Space", "L1", "layer"), ("Enter", "L2", "layer"), ("MO(3)", "L3", "layer")],
    },
    {
        "num": 1,
        "title": "Layer 1: 숫자 · 방향키 · 기본기호",
        "trigger": "오른손 엄지 Spc Hold",
        "left": [
            [("1", "숫자1", "accent1"), ("2", "숫자2", "accent1"), ("3", "숫자3", "accent1"), ("4", "숫자4", "accent1"), ("5", "숫자5", "accent1")],
            [("Esc", "취소", "warn"), ("Tab", "⇥", "mod"), ("`", "백틱", "accent2"), ("-", "마이너스", "accent2"), ("=", "이퀄", "accent2")],
            [("Shift", "선택", "mod"), ("←", "Left", "accent2"), ("↓", "Down", "accent2"), ("↑", "Up", "accent2"), ("→", "Right", "accent2")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("6", "숫자6", "accent1"), ("7", "숫자7", "accent1"), ("8", "숫자8", "accent1"), ("9", "숫자9", "accent1"), ("0", "숫자0", "accent1")],
            [(";", "세미콜론", "accent2"), ("[", "대괄호열", "accent1"), ("]", "대괄호닫", "accent1"), ("\\", "백슬래시", "accent2"), ("Del", "⌦", "warn")],
            [("'", "따옴표", "accent2"), (",", "쉼표", "accent2"), (".", "마침표", "accent2"), ("/", "슬래시", "accent2"), ("SftEnt", "⇧/⏎", "mod")],
        ],
        "right_thumb": [("★ L1", "Space", "hold"), ("MO(3)", "L3", "layer"), ("TO(3)", "고정", "layer")],
    },
    {
        "num": 2,
        "title": "Layer 2: 코딩 · Shift 기호",
        "trigger": "오른손 엄지 Ent Hold",
        "left": [
            [("!", "S-1", "accent1"), ("@", "S-2", "accent1"), ("#", "S-3", "accent1"), ("$", "S-4", "accent1"), ("%", "S-5", "accent1")],
            [("Esc", "취소", "warn"), ("Tab", "⇥", "mod"), ("~", "물결", "accent2"), ("_", "언더바", "accent2"), ("+", "플러스", "accent2")],
            [("Shift", "선택", "mod"), ("Home", "⌘←", "accent2"), ("PgDn", "Page↓", "accent2"), ("PgUp", "Page↑", "accent2"), ("End", "⌘→", "accent2")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("^", "S-6", "accent1"), ("&", "S-7", "accent1"), ("*", "S-8", "accent1"), ("(", "소괄호열", "accent1"), (")", "소괄호닫", "accent1")],
            [(":", "콜론", "accent2"), ("{", "중괄호열", "accent1"), ("}", "중괄호닫", "accent1"), ("|", "파이프", "accent2"), ("Bksp", "⌫", "warn")],
            [("\"", "큰따옴", "accent2"), ("<", "꺾쇠열", "accent2"), (">", "꺾쇠닫", "accent2"), ("?", "물음표", "accent2"), ("Enter", "줄바꿈", "mod")],
        ],
        "right_thumb": [("MO(3)", "L3", "layer"), ("★ L2", "Enter", "hold"), ("TO(3)", "고정", "layer")],
    },
    {
        "num": 3,
        "title": "Layer 3: 마우스 · 미디어 · 창관리",
        "trigger": "오른손 바깥 엄지 / TO(3)",
        "left": [
            [("F1", "기능키", "normal"), ("F2", "기능키", "normal"), ("F3", "기능키", "normal"), ("F4", "기능키", "normal"), ("F5", "기능키", "normal")],
            [("공간←", "⌃←", "accent1"), ("앱윈도우", "⌃↓", "accent1"), ("미션컨트롤", "⌃↑", "accent1"), ("공간→", "⌃→", "accent1"), ("캡처", "⌘⇧4", "accent2")],
            [("F6", "기능키", "normal"), ("F7", "기능키", "normal"), ("F8", "기능키", "normal"), ("F9", "기능키", "normal"), ("F10", "기능키", "normal")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("⏪", "MRWD", "accent2"), ("⏯", "MPLY", "accent2"), ("⏩", "MFFD", "accent2"), ("Vol-", "볼륨↓", "accent2"), ("Vol+", "볼륨↑", "accent2")],
            [("마우스←", "MS-Left", "accent1"), ("마우스↓", "MS-Down", "accent1"), ("마우스↑", "MS-Up", "accent1"), ("마우스→", "MS-Rght", "accent1"), ("감속", "ACCEL0", "mod")],
            [("휠←", "WH-Left", "normal"), ("휠↓", "WH-Down", "normal"), ("휠↑", "WH-Up", "normal"), ("휠→", "WH-Rght", "normal"), ("음소거", "Mute", "warn")],
        ],
        "right_thumb": [("좌클릭", "BTN1", "accent1"), ("우클릭", "BTN2", "accent1"), ("★ L3/복귀", "TO(0)", "hold")],
    },
    {
        "num": 4,
        "title": "Layer 4: 브라우저 & 고속 텍스트 편집",
        "trigger": "왼손 하단 Z Hold",
        "left": [
            [("탭닫기", "⌘W", "warn"), ("탭복구", "⌘⇧T", "accent1"), ("새탭", "⌘T", "accent1"), ("새로고침", "⌘R", "accent1"), ("주소창", "⌘L", "accent1")],
            [("—", "비어있음", "muted"), ("뒤로", "⌘[", "accent1"), ("이전탭", "⌘⇧[", "accent1"), ("다음탭", "⌘⇧]", "accent1"), ("앞으로", "⌘]", "accent1")],
            [("★ L4", "Z Hold", "hold"), ("잘라내기", "⌘X", "normal"), ("복사", "⌘C", "normal"), ("붙여넣기", "⌘V", "normal"), ("실행취소", "⌘Z", "normal")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("페이지찾기", "⌘F", "accent1"), ("이전찾기", "⌘⇧G", "accent1"), ("화면축소", "⌘-", "normal"), ("화면확대", "⌘+", "normal"), ("원본배율", "⌘0", "normal")],
            [("줄처음", "⌘←", "accent2"), ("단어←", "⌥←", "accent2"), ("단어→", "⌥→", "accent2"), ("줄끝", "⌘→", "accent2"), ("단어삭제", "⌥⌫", "warn")],
            [("전체선택", "⌘A", "normal"), ("다시실행", "⌘⇧Z", "normal"), ("저장", "⌘S", "accent2"), ("개발도구", "⌘⌥I", "normal"), ("전송실행", "⌘Enter", "accent2")],
        ],
        "right_thumb": [("Space", "공백", "normal"), ("Enter", "엔터", "normal"), ("TO(0)", "복귀", "layer")],
    },
    {
        "num": 5,
        "title": "Layer 5: IDE 코드 탐색 & 디버깅",
        "trigger": "왼손 하단 X Hold",
        "left": [
            [("디버그중지", "⇧F5", "warn"), ("재시작", "⌘⇧F5", "accent1"), ("디버그창", "⌘⇧D", "accent1"), ("콘솔", "⌘⇧Y", "accent1"), ("터미널", "⌃`", "normal")],
            [("중단점", "F9", "warn"), ("실행▶", "F5", "accent2"), ("StepOver", "F10", "accent1"), ("StepInto", "F11", "accent1"), ("StepOut", "⇧F11", "accent1")],
            [("에러창", "⌘⇧M", "normal"), ("★ L5", "X Hold", "hold"), ("전체검색", "⌘⇧F", "normal"), ("명령팔레트", "⌘⇧P", "normal"), ("줄삭제", "⌘⇧K", "warn")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("정의미리", "⌥F12", "accent1"), ("정의이동", "F12", "accent2"), ("구현체이동", "⌘F12", "accent1"), ("참조찾기", "⇧F12", "accent1"), ("이름변경", "F2", "warn")],
            [("뒤로◀", "⌃-", "accent2"), ("앞으로▶", "⌃⇧-", "accent2"), ("심볼목록", "⌘⇧O", "accent1"), ("다음에러", "F8", "warn"), ("짝괄호", "⌘⇧\\", "accent1")],
            [("주석", "⌘/", "normal"), ("줄아래", "⌥↓", "normal"), ("줄위로", "⌥↑", "normal"), ("줄복제", "⇧⌥↓", "normal"), ("코드포맷", "⇧⌥F", "accent2")],
        ],
        "right_thumb": [("QuickFix", "⌘.", "accent2"), ("이전에러", "⇧F8", "warn"), ("TO(0)", "복귀", "layer")],
    },
    {
        "num": 6,
        "title": "Layer 6: Rectangle 창분할 & 창제어",
        "trigger": "왼손 하단 C Hold",
        "left": [
            [("창전환", "⌘`", "accent2"), ("창닫기", "⌘W", "warn"), ("좌측 2/3", "⌃⌥E", "accent1"), ("정중앙", "⌃⌥C", "accent2"), ("우측 2/3", "⌃⌥T", "accent1")],
            [("전체화면", "⌃⌘F", "accent2"), ("창최소화", "⌘M", "normal"), ("좌측 1/3", "⌃⌥D", "accent1"), ("중앙 1/3", "⌃⌥F", "accent1"), ("우측 1/3", "⌃⌥G", "accent1")],
            [("앱숨김", "⌘H", "normal"), ("타앱숨김", "⌥⌘H", "normal"), ("★ L6", "C Hold", "hold"), ("공간←", "⌃←", "accent2"), ("공간→", "⌃→", "accent2")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("세로최대", "⌃⌥⇧↑", "accent2"), ("좌상 1/4", "⌃⌥U", "accent1"), ("우상 1/4", "⌃⌥I", "accent1"), ("좌하 1/4", "⌃⌥J", "accent1"), ("우하 1/4", "⌃⌥K", "accent1")],
            [("좌측절반", "⌃⌥←", "accent2"), ("하단절반", "⌃⌥↓", "accent2"), ("상단절반", "⌃⌥↑", "accent2"), ("우측절반", "⌃⌥→", "accent2"), ("최대화", "⌃⌥⏎", "warn")],
            [("이전모니터", "⌃⌥⌘←", "accent1"), ("다음모니터", "⌃⌥⌘→", "accent1"), ("축소 -", "⌃⌥-", "normal"), ("확대 +", "⌃⌥=", "normal"), ("최대화", "⌃⌥⏎", "warn")],
        ],
        "right_thumb": [("정중앙", "⌃⌥C", "accent2"), ("복원", "⌃⌥⌫", "warn"), ("TO(0)", "복귀", "layer")],
    },
    {
        "num": 7,
        "title": "Layer 7: 오른손 3×3 넘패드 & 시트",
        "trigger": "왼손 하단 V Hold",
        "left": [
            [("Esc", "취소", "warn"), ("이전셀", "⇧Tab", "accent2"), ("위로", "↑", "accent2"), ("다음셀", "Tab", "accent2"), ("Bksp", "⌫", "warn")],
            [("Shift", "범위", "mod"), ("왼쪽", "←", "accent2"), ("아래", "↓", "accent2"), ("오른쪽", "→", "accent2"), ("Enter", "입력", "mod")],
            [("실행취소", "⌘Z", "normal"), ("잘라내기", "⌘X", "normal"), ("복사", "⌘C", "normal"), ("★ L7", "V Hold", "hold"), ("붙여넣기", "⌘V", "normal")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("÷", "/", "accent2"), ("7", "Num7", "accent1"), ("8", "Num8", "accent1"), ("9", "Num9", "accent1"), ("-", "빼기", "accent2")],
            [("×", "*", "accent2"), ("4", "Num4", "accent1"), ("5", "Num5", "accent1"), ("6", "Num6", "accent1"), ("+", "더하기", "accent2")],
            [("=", "수식", "accent2"), ("1", "Num1", "accent1"), ("2", "Num2", "accent1"), ("3", "Num3", "accent1"), ("Enter", "완료", "mod")],
        ],
        "right_thumb": [("0", "Num0", "accent1"), (".", "소수점", "accent2"), ("TO(0)", "복귀", "layer")],
    },
    {
        "num": 8,
        "title": "Layer 8: macOS 시스템 · 캡처 · 회의",
        "trigger": "왼손 하단 B Hold",
        "left": [
            [("화면잠금", "⌃⌘Q", "warn"), ("전체캡처", "⌘⇧3", "accent1"), ("영역캡처", "⌘⇧4", "accent1"), ("캡처도구", "⌘⇧5", "accent1"), ("이모지", "⌃⌘Space", "accent2")],
            [("창최소화", "⌘M", "normal"), ("앱숨기기", "⌘H", "normal"), ("미션컨트롤", "⌃↑", "accent2"), ("전체화면", "⌃⌘F", "accent2"), ("Spotlight", "⌘Space", "accent1")],
            [("마이크", "⌘⇧A", "accent1"), ("카메라", "⌘⇧V", "accent1"), ("복사", "⌘C", "normal"), ("붙여넣기", "⌘V", "normal"), ("★ L8", "B Hold", "hold")],
        ],
        "left_thumb": [("Ctrl", "⌃", "mod"), ("Opt", "⌥", "mod"), ("Cmd", "⌘", "mod")],
        "right": [
            [("음소거", "Mute", "warn"), ("Vol-", "볼륨↓", "accent2"), ("Vol+", "볼륨↑", "accent2"), ("밝기-", "어둡게", "accent1"), ("밝기+", "밝게", "accent1")],
            [("←", "Left", "normal"), ("↓", "Down", "normal"), ("↑", "Up", "normal"), ("→", "Right", "normal"), ("Bksp", "⌫", "warn")],
            [("Space", "공백", "normal"), ("강제종료", "⌘⌥Esc", "warn"), ("—", "비어있음", "muted"), ("TO(0)", "복귀", "layer"), ("Enter", "엔터", "normal")],
        ],
        "right_thumb": [("Space", "공백", "normal"), ("Enter", "엔터", "normal"), ("TO(0)", "복귀", "layer")],
    },
]

TOTAL_W = 1920
TOTAL_H = 1080
SAFE_W = 1600
SAFE_H = 1050
SAFE_X = (TOTAL_W - SAFE_W) / 2 # 160
SAFE_Y = (TOTAL_H - SAFE_H) / 2 # 15

def draw_key_custom(x, y, w, h, main_t, sub_t, st_name, f_main=11, f_sub=8):
    st = STYLES[st_name]
    stroke_w = "2" if st_name == "hold" else "1"
    parts = [
        f'<g transform="translate({x:.1f},{y:.1f})">',
        f'  <rect width="{w:.1f}" height="{h:.1f}" rx="5.5" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="{stroke_w}"/>',
        f'  <text x="{w/2:.1f}" y="{h/2 - 2:.1f}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{f_main}" font-weight="700" text-anchor="middle" dominant-baseline="middle">{escape(main_t)}</text>'
    ]
    if sub_t:
        parts.append(f'  <text x="{w/2:.1f}" y="{h - 6:.1f}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{f_sub}" font-weight="500" text-anchor="middle">{escape(sub_t)}</text>')
    parts.append('</g>')
    return "\n".join(parts)

def render_board(layer, cx, cy, cw, ch, is_hero=False):
    parts = []
    # Card bg
    bg_color = "#0f172a" if not is_hero else "#131d38"
    border_color = "#1e293b" if not is_hero else "#38bdf8"
    border_w = "1.5" if not is_hero else "2"
    parts.append(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{cw:.1f}" height="{ch:.1f}" rx="12" fill="{bg_color}" stroke="{border_color}" stroke-width="{border_w}"/>')
    
    # Title
    t_size = 14 if is_hero else 12
    badge_bg = "#1e293b" if not is_hero else "#0369a1"
    parts.append(f'<text x="{cx + 14:.1f}" y="{cy + 22:.1f}" fill="#f8fafc" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{t_size}" font-weight="800">{escape(layer["title"])}</text>')
    badge_w = 140 if is_hero else 115
    parts.append(f'<rect x="{cx + cw - 14 - badge_w:.1f}" y="{cy + 10:.1f}" width="{badge_w}" height="19" rx="9.5" fill="{badge_bg}" stroke="#334155" stroke-width="1"/>')
    parts.append(f'<text x="{cx + cw - 14 - badge_w/2:.1f}" y="{cy + 23:.1f}" fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="9.5" font-weight="700" text-anchor="middle">{escape(layer["trigger"])}</text>')

    # Determine key sizing
    if is_hero:
        KW = 58.0
        KH = 62.0
        GAP = 5.0
        f_main = 14.5
        f_sub = 10.5
        KY0 = cy + 42.0
        LX0 = cx + 22.0
        RX0 = cx + cw - 22.0 - (5 * KW + 4 * GAP)
    else:
        KW = 35.0
        KH = 39.0
        GAP = 3.5
        f_main = 9.5
        f_sub = 7.0
        KY0 = cy + 34.0
        LX0 = cx + 12.0
        RX0 = cx + cw - 12.0 - (5 * KW + 4 * GAP)

    L_STAGGER = [s * (1.2 if is_hero else 0.8) for s in [6.0, 3.0, 0.0, 2.5, 5.0]]
    R_STAGGER = [s * (1.2 if is_hero else 0.8) for s in [5.0, 2.5, 0.0, 3.0, 6.0]]

    # Left 3x5
    for r in range(3):
        for c in range(5):
            x = LX0 + c * (KW + GAP)
            y = KY0 + r * (KH + GAP) + L_STAGGER[c]
            main_t, sub_t, st_name = layer["left"][r][c]
            parts.append(draw_key_custom(x, y, KW, KH, main_t, sub_t, st_name, f_main, f_sub))

    # Right 3x5
    for r in range(3):
        for c in range(5):
            x = RX0 + c * (KW + GAP)
            y = KY0 + r * (KH + GAP) + R_STAGGER[c]
            main_t, sub_t, st_name = layer["right"][r][c]
            parts.append(draw_key_custom(x, y, KW, KH, main_t, sub_t, st_name, f_main, f_sub))

    # Thumbs row
    TY = KY0 + 3 * (KH + GAP) + (10.0 if is_hero else 7.0)
    for i in range(3):
        x = LX0 + (i + 2.15) * (KW + GAP)
        main_t, sub_t, st_name = layer["left_thumb"][i]
        parts.append(draw_key_custom(x, TY, KW, KH, main_t, sub_t, st_name, f_main, f_sub))

    for i in range(3):
        x = RX0 + (i - 0.15) * (KW + GAP)
        main_t, sub_t, st_name = layer["right_thumb"][i]
        parts.append(draw_key_custom(x, TY, KW, KH, main_t, sub_t, st_name, f_main, f_sub))

    return "\n".join(parts)

# ==========================================
# 1. VERSION 1: Hero + Satellite Layout
# ==========================================
svg1 = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TOTAL_W} {TOTAL_H}" width="{TOTAL_W}" height="{TOTAL_H}">',
    f'  <rect width="{TOTAL_W}" height="{TOTAL_H}" fill="#030712"/>',
    f'  <text x="{TOTAL_W/2}" y="{SAFE_Y + 28}" fill="#f8fafc" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="22" font-weight="900" text-anchor="middle">⌨️ X.Tips X7 — Version 1: Hero &amp; Satellite (핵심 레이어 특대 확대)</text>',
    f'  <text x="{TOTAL_W/2}" y="{SAFE_Y + 48}" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">중앙 L0·L1·L2를 초대형 배치하여 가독성을 극대화하고, 보조 L3~L8은 좌우 위성 배치</text>',
]

# Layout:
# Left column: L3, L4, L5 (satellites)
# Center column: L0, L1, L2 (HEROES, large!)
# Right column: L6, L7, L8 (satellites)
C_SAT_W = 430
C_HERO_W = 700
C_GAP = 15
TOTAL_GRID_W = 2 * C_SAT_W + C_HERO_W + 2 * C_GAP # 1590 <= 1600!
V1_X0 = SAFE_X + (SAFE_W - TOTAL_GRID_W) / 2 # 165
V1_Y0 = SAFE_Y + 62

# 3 rows
SAT_H = 300
HERO_H = 300
ROW_GAP = 12

# Left satellites
svg1.append(render_board(LAYERS[3], V1_X0, V1_Y0, C_SAT_W, SAT_H, is_hero=False))
svg1.append(render_board(LAYERS[4], V1_X0, V1_Y0 + SAT_H + ROW_GAP, C_SAT_W, SAT_H, is_hero=False))
svg1.append(render_board(LAYERS[5], V1_X0, V1_Y0 + 2 * (SAT_H + ROW_GAP), C_SAT_W, SAT_H, is_hero=False))

# Center Heroes
CX = V1_X0 + C_SAT_W + C_GAP
svg1.append(render_board(LAYERS[0], CX, V1_Y0, C_HERO_W, HERO_H, is_hero=True))
svg1.append(render_board(LAYERS[1], CX, V1_Y0 + HERO_H + ROW_GAP, C_HERO_W, HERO_H, is_hero=True))
svg1.append(render_board(LAYERS[2], CX, V1_Y0 + 2 * (HERO_H + ROW_GAP), C_HERO_W, HERO_H, is_hero=True))

# Right satellites
RX = CX + C_HERO_W + C_GAP
svg1.append(render_board(LAYERS[6], RX, V1_Y0, C_SAT_W, SAT_H, is_hero=False))
svg1.append(render_board(LAYERS[7], RX, V1_Y0 + SAT_H + ROW_GAP, C_SAT_W, SAT_H, is_hero=False))
svg1.append(render_board(LAYERS[8], RX, V1_Y0 + 2 * (SAT_H + ROW_GAP), C_SAT_W, SAT_H, is_hero=False))

svg1.append('</svg>')

with open(f"{OUT_DIR}/version1_hero_satellite.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg1))
print("Saved version 1 SVG")
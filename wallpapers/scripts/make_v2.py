import os
import json
from html import escape

OUT_DIR = "/Users/yong/Documents/UseVia/wallpapers"
os.makedirs(OUT_DIR, exist_ok=True)

# 1920 x 1080 Fullscreen (No safe margin, maximum key dimensions)
TOTAL_W = 1920
TOTAL_H = 1080

with open("/Users/yong/Documents/UseVia/x_tips_x7_keyboard.layout.json") as f:
    layout_data = json.load(f)

layers = layout_data["layers"] # 9 layers (0 to 8)

# Clean character extractor for L0, L1, L2
def get_clean_char(k, l_idx):
    if k in ("KC_TRNS", "KC_NO", ""):
        return "·"
    
    clean_map = {
        "KC_Q": "Q", "KC_W": "W", "KC_E": "E", "KC_R": "R", "KC_T": "T",
        "KC_Y": "Y", "KC_U": "U", "KC_I": "I", "KC_O": "O", "KC_P": "P",
        "KC_A": "A", "KC_S": "S", "KC_D": "D", "KC_F": "F", "KC_G": "G",
        "KC_H": "H", "KC_J": "J", "KC_K": "K", "KC_L": "L",
        "KC_Z": "Z", "KC_X": "X", "KC_C": "C", "KC_V": "V", "KC_B": "B",
        "KC_N": "N", "KC_M": "M",
        "KC_1": "1", "KC_2": "2", "KC_3": "3", "KC_4": "4", "KC_5": "5",
        "KC_6": "6", "KC_7": "7", "KC_8": "8", "KC_9": "9", "KC_0": "0",
        "KC_ESC": "Esc", "KC_TAB": "Tab", "KC_GRV": "`",
        "KC_MINS": "-", "KC_EQL": "=",
        "KC_SCLN": ";", "KC_LBRC": "[", "KC_RBRC": "]",
        "KC_BSLS": "\\", "KC_DEL": "Del", "KC_BSPC": "⌫",
        "KC_QUOT": "'", "KC_COMM": ",", "KC_DOT": ".",
        "KC_SLSH": "/", "KC_ENT": "⏎", "KC_SPC": "Space",
        "KC_LSFT": "Shift", "KC_LCTL": "Ctrl", "KC_LALT": "Opt", "KC_LGUI": "Cmd",
        "KC_LEFT": "←", "KC_DOWN": "↓", "KC_UP": "↑", "KC_RGHT": "→",
        "KC_PGDN": "PgDn", "KC_PGUP": "PgUp", "KC_CAPS": "Caps",
        "KC_SFTENT": "⇧/⏎",
    }
    if k in clean_map:
        return clean_map[k]

    if k.startswith("S("):
        inner = k[2:-1]
        shift_clean = {
            "KC_1": "!", "KC_2": "@", "KC_3": "#", "KC_4": "$", "KC_5": "%",
            "KC_6": "^", "KC_7": "&", "KC_8": "*", "KC_9": "(", "KC_0": ")",
            "KC_GRV": "~", "KC_MINS": "_", "KC_EQL": "+",
            "KC_SCLN": ":", "KC_LBRC": "{", "KC_RBRC": "}",
            "KC_BSLS": "|", "KC_QUOT": '"', "KC_COMM": "<",
            "KC_DOT": ">", "KC_SLSH": "?",
            "KC_TAB": "⇧Tab",
        }
        if inner in shift_clean:
            return shift_clean[inner]

    if k.startswith("G("):
        inner = k[2:-1]
        if inner == "KC_LEFT": return "⌘←"
        if inner == "KC_RGHT": return "⌘→"

    if k.startswith("LT("):
        parts = k[3:-1].split(",")
        return get_clean_char(parts[1], l_idx)

    if k.startswith("TO("):
        return f"TO({k[3:-1]})"
    if k.startswith("MO("):
        return f"MO({k[3:-1]})"

    return k

# Action text translator for L3 ~ L8
def get_human_label(k, l_idx):
    if k in ("KC_TRNS", "KC_NO", ""):
        return ""
    
    # Layer switch / Tap-hold
    if k.startswith("TO("):
        return f"TO({k[3:-1]}) 고정"
    if k.startswith("MO("):
        return f"MO({k[3:-1]})" if l_idx == 0 else f"L{k[3:-1]} 유지"
    if k.startswith("LT("):
        parts = k[3:-1].split(",")
        l_num, base = parts[0], parts[1]
        base_str = get_human_label(base, l_idx)
        return f"{base_str} (L{l_num})"

    d = {
        "KC_Q": "Q", "KC_W": "W", "KC_E": "E", "KC_R": "R", "KC_T": "T",
        "KC_Y": "Y", "KC_U": "U", "KC_I": "I", "KC_O": "O", "KC_P": "P",
        "KC_A": "A", "KC_S": "S", "KC_D": "D", "KC_F": "F", "KC_G": "G",
        "KC_H": "H", "KC_J": "J", "KC_K": "K", "KC_L": "L",
        "KC_Z": "Z", "KC_X": "X", "KC_C": "C", "KC_V": "V", "KC_B": "B",
        "KC_N": "N", "KC_M": "M",
        "KC_1": "1", "KC_2": "2", "KC_3": "3", "KC_4": "4", "KC_5": "5",
        "KC_6": "6", "KC_7": "7", "KC_8": "8", "KC_9": "9", "KC_0": "0",
        "KC_ESC": "Esc", "KC_TAB": "Tab ⇥", "KC_GRV": "` 백틱",
        "KC_MINS": "- 빼기", "KC_EQL": "= 이퀄",
        "KC_SCLN": "; 세미", "KC_LBRC": "[ 대열", "KC_RBRC": "] 대닫",
        "KC_BSLS": "\\ 백슬", "KC_DEL": "Del ⌦", "KC_BSPC": "Bksp ⌫",
        "KC_QUOT": "' 따옴", "KC_COMM": ", 쉼표", "KC_DOT": ". 마침",
        "KC_SLSH": "/ 슬래", "KC_ENT": "Enter ⏎", "KC_SPC": "Space",
        "KC_LSFT": "Shift ⇧", "KC_LCTL": "Ctrl ⌃", "KC_LALT": "Opt ⌥", "KC_LGUI": "Cmd ⌘",
        "KC_LEFT": "← Left", "KC_DOWN": "↓ Down", "KC_UP": "↑ Up", "KC_RGHT": "→ Right",
        "KC_PGDN": "PgDn", "KC_PGUP": "PgUp", "KC_CAPS": "한/영",
        "KC_SFTENT": "⇧/⏎",
        "KC_F1": "F1", "KC_F2": "F2 심볼", "KC_F3": "F3", "KC_F4": "F4", "KC_F5": "F5 실행▶",
        "KC_F6": "F6", "KC_F7": "F7", "KC_F8": "F8 다음", "KC_F9": "F9 중단점", "KC_F10": "F10 StepO",
        "KC_F11": "F11 StepI", "KC_F12": "F12 정의",
        "KC_MRWD": "⏪ 되감", "KC_MPLY": "⏯ 재생", "KC_MFFD": "⏩ 빨리",
        "KC_VOLD": "🔉 볼륨-", "KC_VOLU": "🔊 볼륨+", "KC_MUTE": "🔇 음소거",
        "KC_BRID": "🔅 밝기-", "KC_BRIU": "🔆 밝기+",
        "KC_MS_LEFT": "마우스←", "KC_MS_DOWN": "마우스↓", "KC_MS_UP": "마우스↑", "KC_MS_RIGHT": "마우스→",
        "KC_MS_WH_LEFT": "휠←", "KC_MS_WH_DOWN": "휠↓", "KC_MS_WH_UP": "휠↑", "KC_MS_WH_RIGHT": "휠→",
        "KC_MS_BTN1": "좌클릭", "KC_MS_BTN2": "우클릭", "KC_MS_ACCEL0": "정밀모드",
    }
    if k in d:
        return d[k]

    # Shift combinations S(KC_...)
    if k.startswith("S("):
        inner = k[2:-1]
        shift_map = {
            "KC_1": "!", "KC_2": "@", "KC_3": "#", "KC_4": "$", "KC_5": "%",
            "KC_6": "^", "KC_7": "&", "KC_8": "*", "KC_9": "(", "KC_0": ")",
            "KC_GRV": "~", "KC_MINS": "_", "KC_EQL": "+",
            "KC_SCLN": ":", "KC_LBRC": "{", "KC_RBRC": "}",
            "KC_BSLS": "|", "KC_QUOT": '"', "KC_COMM": "<",
            "KC_DOT": ">", "KC_SLSH": "?",
            "KC_F5": "⇧F5 중지", "KC_F8": "⇧F8 이전", "KC_F11": "⇧F11 StepOut", "KC_F12": "⇧F12 참조",
            "KC_TAB": "⇧Tab 역탭", "KC_8": "* 곱하기", "KC_EQL": "+ 더하기",
        }
        return shift_map.get(inner, f"⇧{get_human_label(inner, l_idx)}")

    # Cmd combinations G(KC_...)
    if k.startswith("G("):
        inner = k[2:-1]
        cmd_map = {
            "KC_W": "⌘W 창닫", "KC_T": "⌘T 새탭", "KC_R": "⌘R 새로고", "KC_L": "⌘L 주소창",
            "KC_F": "⌘F 찾기", "KC_MINS": "⌘- 축소", "KC_EQL": "⌘= 확대", "KC_0": "⌘0 원본",
            "KC_LEFT": "⌘← 줄앞", "KC_RGHT": "⌘→ 줄끝",
            "KC_X": "⌘X 잘라", "KC_C": "⌘C 복사", "KC_V": "⌘V 붙여", "KC_Z": "⌘Z 실행취",
            "KC_A": "⌘A 전선", "KC_S": "⌘S 저장", "KC_M": "⌘M 최소화", "KC_H": "⌘H 앱숨김",
            "KC_SPC": "⌘Space", "KC_ENT": "⌘⏎ 실행", "KC_SLSH": "⌘/ 주석", "KC_DOT": "⌘. Quick",
            "KC_GRV": "⌘` 창전환", "KC_F12": "⌘F12 구현",
        }
        return cmd_map.get(inner, f"⌘{get_human_label(inner, l_idx)}")

    # Alt combinations A(KC_...)
    if k.startswith("A("):
        inner = k[2:-1]
        alt_map = {
            "KC_LEFT": "⌥← 단어", "KC_RGHT": "⌥→ 단어", "KC_BSPC": "⌥⌫ 단삭",
            "KC_UP": "⌥↑ 줄위", "KC_DOWN": "⌥↓ 줄아", "KC_F12": "⌥F12 정의",
        }
        return alt_map.get(inner, f"⌥{get_human_label(inner, l_idx)}")

    # Ctrl combinations C(KC_...)
    if k.startswith("C("):
        inner = k[2:-1]
        ctrl_map = {
            "KC_LEFT": "⌃← 공간", "KC_DOWN": "⌃↓ 앱윈", "KC_UP": "⌃↑ 미션", "KC_RGHT": "⌃→ 공간",
            "KC_GRV": "⌃` 터미널", "KC_MINS": "⌃- 뒤로▶",
        }
        if inner.startswith("G("):
            cg_inner = inner[2:-1]
            cg_map = {"KC_F": "⌃⌘F 전체화", "KC_Q": "⌃⌘Q 잠금", "KC_SPC": "⌃⌘Space 이모지"}
            return cg_map.get(cg_inner, f"⌃⌘{cg_inner}")
        return ctrl_map.get(inner, f"⌃{get_human_label(inner, l_idx)}")

    # Cmd+Shift LSG(KC_...)
    if k.startswith("LSG("):
        inner = k[4:-1]
        lsg_map = {
            "KC_T": "⌘⇧T 복구", "KC_LBRC": "⌘⇧[ 이탭", "KC_RBRC": "⌘⇧] 다탭",
            "KC_G": "⌘⇧G 이찾", "KC_Z": "⌘⇧Z 다시",
            "KC_F5": "⌘⇧F5 재시", "KC_D": "⌘⇧D 디버그", "KC_Y": "⌘⇧Y 콘솔",
            "KC_M": "⌘⇧M 에러", "KC_F": "⌘⇧F 전검색", "KC_P": "⌘⇧P 팔레트", "KC_K": "⌘⇧K 줄삭",
            "KC_O": "⌘⇧O 심볼", "KC_BSLS": "⌘⇧\\ 괄호",
            "KC_3": "⌘⇧3 전캡처", "KC_4": "⌘⇧4 영캡처", "KC_5": "⌘⇧5 캡처바",
            "KC_A": "⌘⇧A 활동", "KC_V": "⌘⇧V 클립",
        }
        return lsg_map.get(inner, f"⌘⇧{inner}")

    # Ctrl+Alt LCA(KC_...) (Rectangle window tiling)
    if k.startswith("LCA("):
        inner = k[4:-1]
        lca_map = {
            "KC_E": "⌃⌥E 좌2/3", "KC_C": "⌃⌥C 정중앙", "KC_T": "⌃⌥T 우2/3",
            "KC_D": "⌃⌥D 좌1/3", "KC_F": "⌃⌥F 중1/3", "KC_G": "⌃⌥G 우1/3",
            "KC_U": "⌃⌥U 좌상1/4", "KC_I": "⌃⌥I 우상1/4", "KC_J": "⌃⌥J 좌하1/4", "KC_K": "⌃⌥K 우하1/4",
            "KC_LEFT": "⌃⌥← 좌1/2", "KC_DOWN": "⌃⌥↓ 하1/2", "KC_UP": "⌃⌥↑ 상1/2", "KC_RGHT": "⌃⌥→ 우1/2",
            "KC_ENT": "⌃⌥⏎ 최대화", "KC_MINS": "⌃⌥- 축소", "KC_EQL": "⌃⌥= 확대", "KC_BSPC": "⌃⌥⌫ 복원",
        }
        return lca_map.get(inner, f"⌃⌥{inner}")

    # Ctrl+Alt+Cmd LCAG(KC_...)
    if k.startswith("LCAG("):
        inner = k[5:-1]
        lcag_map = {"KC_LEFT": "⌃⌥⌘← 모◀", "KC_RGHT": "⌃⌥⌘→ 모▶"}
        return lcag_map.get(inner, f"⌃⌥⌘{inner}")

    # Alt+Cmd LAG(KC_...)
    if k.startswith("LAG("):
        inner = k[4:-1]
        lag_map = {"KC_H": "⌥⌘H 타숨김", "KC_I": "⌥⌘I 개발자", "KC_ESC": "⌥⌘Esc 강제종료"}
        return lag_map.get(inner, f"⌥⌘{inner}")

    # Alt+Shift LSA(KC_...)
    if k.startswith("LSA("):
        inner = k[4:-1]
        lsa_map = {"KC_DOWN": "⌥⇧↓ 복제", "KC_F": "⌥⇧F 포맷"}
        return lsa_map.get(inner, f"⌥⇧{inner}")

    return k

# Left Alpha Indices:
# Row 0: 0, 1, 2, 3, 4
# Row 1: 5, 6, 7, 8, 9
# Row 2: 10, 11, 12, 13, 14
# Left Thumb Indices: 17, 18, 19

# Right Alpha Indices (visual order: left -> right, descending JSON indices):
# Row 0: 24, 23, 22, 21, 20
# Row 1: 29, 28, 27, 26, 25
# Row 2: 34, 33, 32, 31, 30
# Right Thumb Indices: 39, 38, 37 (Space, Enter, MO(3))

LEFT_KEY_INDICES = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
]
LEFT_THUMB_INDICES = [17, 18, 19]

RIGHT_KEY_INDICES = [
    [24, 23, 22, 21, 20],
    [29, 28, 27, 26, 25],
    [34, 33, 32, 31, 30],
]
RIGHT_THUMB_INDICES = [39, 38, 37]

# Special hold badges on Layer 0
L0_HOLD_BADGES = {
    10: "▶L4", 11: "▶L5", 12: "▶L6", 13: "▶L7", 14: "▶L8",
    39: "▶L1", 38: "▶L2", 37: "▶L3"
}

# Layer Theme Colors for L3 ~ L8
LAYER_COLORS = {
    3: ("#c084fc", "L3 Mouse"),
    4: ("#fbbf24", "L4 Browser"),
    5: ("#f43f5e", "L5 Coding"),
    6: ("#a3e635", "L6 Window"),
    7: ("#fb923c", "L7 Numpad"),
    8: ("#e879f9", "L8 System"),
}

# Grid Geometry
KW = 174.0
KH = 237.0
COL_GAP = 10.0
ROW_GAP = 10.0

LX0 = 25.0
RX0 = 985.0
KY0 = 56.0

L_STAGGER = [12, 6, 0, 5, 10]
R_STAGGER = [10, 5, 0, 6, 12]

HEADER_H = 46.0
COL_W = KW / 3.0 # 58.0px per cell

def render_key_all_layers(x, y, key_idx):
    parts = []
    parts.append(f'<g transform="translate({x:.1f},{y:.1f})">')
    # Card Border & Background
    parts.append(f'  <rect width="{KW:.1f}" height="{KH:.1f}" rx="11" fill="#0b1120" stroke="#334155" stroke-width="1.6"/>')
    
    # --- Top Header: 3 Cells for L0, L1, L2 ---
    # Header Banner Background
    parts.append(f'  <path d="M 0,11 A 11,11 0 0 1 11,0 L {KW-11:.1f},0 A 11,11 0 0 1 {KW:.1f},11 L {KW:.1f},{HEADER_H:.1f} L 0,{HEADER_H:.1f} Z" fill="#1e293b"/>')
    # Header Bottom Border
    parts.append(f'  <line x1="0" y1="{HEADER_H:.1f}" x2="{KW:.1f}" y2="{HEADER_H:.1f}" stroke="#475569" stroke-width="1.2"/>')
    # 2 Vertical Dividers inside Header
    parts.append(f'  <line x1="{COL_W:.1f}" y1="0" x2="{COL_W:.1f}" y2="{HEADER_H:.1f}" stroke="#334155" stroke-width="1"/>')
    parts.append(f'  <line x1="{COL_W*2:.1f}" y1="0" x2="{COL_W*2:.1f}" y2="{HEADER_H:.1f}" stroke="#334155" stroke-width="1"/>')

    # Cell 1: Layer 0 (BASE)
    c0 = get_clean_char(layers[0][key_idx], 0)
    if key_idx in L0_HOLD_BADGES:
        b_txt = L0_HOLD_BADGES[key_idx]
        parts.append(f'  <text x="{COL_W*0.5:.1f}" y="12" fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="8" font-weight="800" text-anchor="middle">L0 ({b_txt})</text>')
    else:
        parts.append(f'  <text x="{COL_W*0.5:.1f}" y="12" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="8" font-weight="700" text-anchor="middle">L0 BASE</text>')
    font_s0 = 19 if len(c0) <= 2 else (14 if len(c0) <= 4 else 11)
    parts.append(f'  <text x="{COL_W*0.5:.1f}" y="33" fill="#f8fafc" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_s0}" font-weight="900" text-anchor="middle">{escape(c0)}</text>')

    # Cell 2: Layer 1 (SPC)
    c1 = get_clean_char(layers[1][key_idx], 1)
    parts.append(f'  <text x="{COL_W*1.5:.1f}" y="12" fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="8" font-weight="700" text-anchor="middle">L1 SPC</text>')
    font_s1 = 18 if len(c1) <= 2 else (13 if len(c1) <= 4 else 10)
    parts.append(f'  <text x="{COL_W*1.5:.1f}" y="33" fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_s1}" font-weight="900" text-anchor="middle">{escape(c1)}</text>')

    # Cell 3: Layer 2 (ENT)
    c2 = get_clean_char(layers[2][key_idx], 2)
    parts.append(f'  <text x="{COL_W*2.5:.1f}" y="12" fill="#34d399" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="8" font-weight="700" text-anchor="middle">L2 ENT</text>')
    font_s2 = 18 if len(c2) <= 2 else (13 if len(c2) <= 4 else 10)
    parts.append(f'  <text x="{COL_W*2.5:.1f}" y="33" fill="#34d399" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_s2}" font-weight="900" text-anchor="middle">{escape(c2)}</text>')

    # --- Body: 6 Rows for Layer 3 through Layer 8 ---
    # Start ry at 66.0, step is 30.5px
    ry = 68.0
    for l_idx in [3, 4, 5, 6, 7, 8]:
        color, l_title = LAYER_COLORS[l_idx]
        raw_key = layers[l_idx][key_idx]
        act_text = get_human_label(raw_key, l_idx)

        # Tag on the left
        tag = f"L{l_idx}"
        parts.append(f'  <text x="12" y="{ry:.1f}" fill="#64748b" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11.5" font-weight="700">{tag}</text>')

        # Check if this key is the hold trigger for this layer
        is_hold_key = (
            (l_idx == 3 and key_idx == 37) or # MO(3)
            (l_idx == 4 and key_idx == 10) or # Z
            (l_idx == 5 and key_idx == 11) or # X
            (l_idx == 6 and key_idx == 12) or # C
            (l_idx == 7 and key_idx == 13) or # V
            (l_idx == 8 and key_idx == 14)    # B
        )
        if is_hold_key:
            act_text = f"★ L{l_idx} 유지"
            color = "#fbbf24" # Gold

        # Action text on the right
        if act_text and act_text != "—":
            font_act = 13.5 if len(act_text) <= 6 else 12.0
            parts.append(f'  <text x="{KW - 12:.1f}" y="{ry:.1f}" fill="{color}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_act}" font-weight="700" text-anchor="end">{escape(act_text)}</text>')
        else:
            parts.append(f'  <text x="{KW - 12:.1f}" y="{ry:.1f}" fill="#1e293b" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11" font-weight="600" text-anchor="end">·</text>')

        ry += 30.5

    parts.append('</g>')
    return "\n".join(parts)

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TOTAL_W} {TOTAL_H}" width="{TOTAL_W}" height="{TOTAL_H}">')
svg.append('<defs>')
svg.append('<linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
svg.append('  <stop offset="0%" stop-color="#030712"/>')
svg.append('  <stop offset="50%" stop-color="#0a0f1d"/>')
svg.append('  <stop offset="100%" stop-color="#020617"/>')
svg.append('</linearGradient>')
svg.append('</defs>')

# Canvas Background
svg.append(f'<rect width="{TOTAL_W}" height="{TOTAL_H}" fill="url(#bgGrad)"/>')

# Sleek Header
svg.append(f'<text x="{TOTAL_W/2}" y="28" fill="#f8fafc" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="20" font-weight="900" text-anchor="middle" letter-spacing="1">⌨️ X.TIPS X7 — 9-LAYER FULLSCREEN OVERLAY MATRIX (1920×1080)</text>')
svg.append(f'<text x="{TOTAL_W/2}" y="47" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">상단 3분할: [L0 기본] │ [L1 숫자/기호] │ [L2 Shift기호]  |  키 본문: L3~L8 기능 대형화 렌더링</text>')

# Render Left Hand (3 rows x 5 cols)
for r in range(3):
    for c in range(5):
        k_idx = LEFT_KEY_INDICES[r][c]
        x = LX0 + c * (KW + COL_GAP)
        y = KY0 + r * (KH + ROW_GAP) + L_STAGGER[c]
        svg.append(render_key_all_layers(x, y, k_idx))

# Render Right Hand (3 rows x 5 cols)
for r in range(3):
    for c in range(5):
        k_idx = RIGHT_KEY_INDICES[r][c]
        x = RX0 + c * (KW + COL_GAP)
        y = KY0 + r * (KH + ROW_GAP) + R_STAGGER[c]
        svg.append(render_key_all_layers(x, y, k_idx))

# Left Thumbs
TY = KY0 + 3 * (KH + ROW_GAP) + 14
for i, k_idx in enumerate(LEFT_THUMB_INDICES):
    x = LX0 + (i + 2.0) * (KW + COL_GAP)
    y = TY + i * 4
    svg.append(render_key_all_layers(x, y, k_idx))

# Right Thumbs
for i, k_idx in enumerate(RIGHT_THUMB_INDICES):
    x = RX0 + i * (KW + COL_GAP)
    y = TY + (2 - i) * 4
    svg.append(render_key_all_layers(x, y, k_idx))

# Bottom Legend with Layer Colors
legend_items = [
    ("#f8fafc", "상단: [L0] [L1 Spc] [L2 Ent]"),
    ("#c084fc", "L3 엄지(마우스)"),
    ("#fbbf24", "L4 Z(브라우저)"),
    ("#f43f5e", "L5 X(VSCode)"),
    ("#a3e635", "L6 C(창분할)"),
    ("#fb923c", "L7 V(텐키)"),
    ("#e879f9", "L8 B(macOS제어)"),
]

lx = 140
svg.append('<g transform="translate(0, 1066)">')
for color, name in legend_items:
    svg.append(f'  <circle cx="{lx}" cy="0" r="4" fill="{color}"/>')
    svg.append(f'  <text x="{lx + 8}" y="3.5" fill="{color}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11" font-weight="700">{escape(name)}</text>')
    lx += 235
svg.append('</g>')

svg.append('</svg>')

out_path = f"{OUT_DIR}/version2_overlay_board.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print(f"Saved {out_path}")

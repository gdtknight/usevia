import os
from html import escape
from v1_script import LAYERS, STYLES
from render_utils import render_split_keyboard

OUT_DIR = "/Users/yong/Documents/UseVia/wallpapers"

# 3B: System & Navigation Edition (L3, L4, L6, L7, L8)
W, H = 1920, 1080

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
svg.append('<defs>')
svg.append('<linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
svg.append('  <stop offset="0%" stop-color="#0b0f19"/>')
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
svg.append('  <text fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="24" font-weight="800" text-anchor="middle" letter-spacing="1.5">X.TIPS X7 — SYSTEM &amp; NAVIGATION EDITION (Ver. 3B)</text>')
svg.append('  <text y="24" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="13" font-weight="500" text-anchor="middle">시스템 제어 5대 레이어 (마우스/미디어 · 브라우징 · 창분할/하이퍼 · 텐키 · macOS제어)</text>')
svg.append('</g>')

# Top Row: 2 Big Keyboards (L3, L4)
# Y: 95, Height: 445
# Col 1: X = 175, Col 2: X = 975
top_positions = [
    (175, 95, LAYERS[3]), # L3: Mouse & Media
    (975, 95, LAYERS[4]), # L4: Browser & Edit
]

for bx, by, layer_data in top_positions:
    svg.append(f'<rect x="{bx}" y="{by}" width="770" height="445" rx="14" fill="#0f172a" fill-opacity="0.85" stroke="#334155" stroke-width="1.5" filter="url(#cardGlow)"/>')
    kb_x = bx + 22
    kb_y = by + 60
    svg.append(render_split_keyboard(layer_data, kb_x, kb_y, kw=66, kh=46, col_gap=6, row_gap=6, split_gap=52, title_mode="full"))

# Bottom Row: 3 Keyboards (L6, L7, L8)
# Y: 565, Height: 480
# Width: 505 each, gaps: 22
# Col 1: 175, Col 2: 175 + 505 + 22 = 702, Col 3: 702 + 505 + 22 = 1229
bot_positions = [
    (175, 565, LAYERS[6]),  # L6: Window & Hyper
    (710, 565, LAYERS[7]),  # L7: Numpad & Calc
    (1245, 565, LAYERS[8]), # L8: macOS System
]

for bx, by, layer_data in bot_positions:
    svg.append(f'<rect x="{bx}" y="{by}" width="500" height="480" rx="14" fill="#0f172a" fill-opacity="0.85" stroke="#334155" stroke-width="1.5" filter="url(#cardGlow)"/>')
    kb_x = bx + 16
    kb_y = by + 65
    svg.append(render_split_keyboard(layer_data, kb_x, kb_y, kw=42, kh=38, col_gap=4, row_gap=5, split_gap=24, title_mode="compact"))

# Footer Quick Tips
svg.append('<g transform="translate(960, 1065)">')
svg.append('  <text fill="#64748b" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="11" font-weight="500" text-anchor="middle">Tip: 엄지 MO(3) ➜ 마우스/볼륨 | Z Hold ➜ 브라우저 탭제어 | C Hold ➜ 창분할타일링 | V Hold ➜ 텐키계산기 | B Hold ➜ 시스템화면캡처</text>')
svg.append('</g>')

svg.append('</svg>')

out_path = f"{OUT_DIR}/version3_dual_b_system.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print(f"Saved {out_path}")

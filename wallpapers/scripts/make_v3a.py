import os
from html import escape
from v1_script import LAYERS, STYLES
from render_utils import render_split_keyboard

OUT_DIR = "/Users/yong/Documents/UseVia/wallpapers"

# 3A: Coding & Writing Edition (L0, L1, L2, L5)
# 4 large keyboards in 2x2 grid
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

# Safe zone guide line (very subtle)
svg.append('<rect x="160" y="15" width="1600" height="1050" fill="none" stroke="#1e293b" stroke-dasharray="4 4" stroke-width="0.8"/>')

# Header
svg.append('<g transform="translate(960, 48)">')
svg.append('  <text fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="24" font-weight="800" text-anchor="middle" letter-spacing="1.5">X.TIPS X7 — CODING &amp; TYPING EDITION (Ver. 3A)</text>')
svg.append('  <text y="24" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="13" font-weight="500" text-anchor="middle">핵심 4개 레이어 (기본입력 · 숫자방향키 · 특수문자기호 · IDE개발코딩) 집중 대형 레이아웃</text>')
svg.append('</g>')

# 2x2 Grid Positions
# Block width: 770, height: 460
# Col 1: X = 175, Col 2: X = 975
# Row 1: Y = 100, Row 2: Y = 575
positions = [
    (175, 100, LAYERS[0]), # Top Left: Layer 0 Base
    (975, 100, LAYERS[1]), # Top Right: Layer 1 Nav/Num
    (175, 575, LAYERS[2]), # Bottom Left: Layer 2 Shift Sym
    (975, 575, LAYERS[5]), # Bottom Right: Layer 5 IDE Coding
]

# Render 4 Card backgrounds + Keyboards
for bx, by, layer_data in positions:
    svg.append(f'<rect x="{bx}" y="{by}" width="770" height="465" rx="14" fill="#0f172a" fill-opacity="0.85" stroke="#334155" stroke-width="1.5" filter="url(#cardGlow)"/>')
    # Render keyboard inside card
    kb_x = bx + 22
    kb_y = by + 65
    svg.append(render_split_keyboard(layer_data, kb_x, kb_y, kw=66, kh=48, col_gap=6, row_gap=6, split_gap=52, title_mode="full"))

# Footer Quick Tips
svg.append('<g transform="translate(960, 1060)">')
svg.append('  <text fill="#64748b" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="11" font-weight="500" text-anchor="middle">Tip: Space Hold ➜ L1(숫자/방향키) | Enter Hold ➜ L2(특수기호) | X Hold ➜ L5(VS Code 코딩) | Z Hold ➜ L4(브라우저) | C Hold ➜ L6(창관리)</text>')
svg.append('</g>')

svg.append('</svg>')

out_path = f"{OUT_DIR}/version3_dual_a_coding.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print(f"Saved {out_path}")

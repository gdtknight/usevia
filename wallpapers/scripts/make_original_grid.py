import os
import json
from html import escape
import subprocess

from v1_script import LAYERS, STYLES

OUT_DIR = "/Users/yong/Documents/UseVia/wallpapers"
WIKI_ASSET_DIR = "/Users/yong/Documents/UseVia/wiki/assets"
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

TOTAL_W = 1920
TOTAL_H = 1080
SAFE_W = 1600
SAFE_H = 1050
SAFE_X = (TOTAL_W - SAFE_W) / 2 # 160
SAFE_Y = (TOTAL_H - SAFE_H) / 2 # 15

GRID_X = SAFE_X + 10
GRID_Y = SAFE_Y + 70
CARD_W = 515.0
CARD_H = 300.0
CARD_GAP_X = 17.5
CARD_GAP_Y = 16.0

KW = 43.0
KH = 51.0
GAP_X = 4.0
GAP_Y = 5.0
SPLIT_GAP = 20.0

L_STAGGER = [10, 5, 0, 4, 8]
R_STAGGER = [8, 4, 0, 5, 10]

def render_layer_card(layer_data, cx, cy, cw, ch):
    svg = []
    svg.append(f'  <g transform="translate({cx:.1f},{cy:.1f})">')
    svg.append(f'    <rect width="{cw:.1f}" height="{ch:.1f}" rx="12" fill="#0f172a" fill-opacity="0.9" stroke="#334155" stroke-width="1.5" filter="url(#cardGlow)"/>')
    svg.append(f'    <rect width="{cw:.1f}" height="32" rx="12" fill="#1e293b"/>')
    svg.append(f'    <line x1="0" y1="32" x2="{cw:.1f}" y2="32" stroke="#334155" stroke-width="1"/>')
    svg.append(f'    <text x="14" y="21" fill="#f8fafc" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="13" font-weight="800">{escape(layer_data["title"])}</text>')
    svg.append(f'    <text x="{cw - 14:.1f}" y="21" fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11" font-weight="600" text-anchor="end">⚡ {escape(layer_data["trigger"])}</text>')

    kx0 = 12.0
    ky0 = 42.0

    # Left Hand Matrix (3x5)
    for r in range(3):
        for c in range(5):
            main_t, sub_t, st_key = layer_data["left"][r][c]
            st = STYLES.get(st_key, STYLES["normal"])
            kx = kx0 + c * (KW + GAP_X)
            ky = ky0 + r * (KH + GAP_Y) + L_STAGGER[c]
            svg.append(f'    <rect x="{kx:.1f}" y="{ky:.1f}" width="{KW:.1f}" height="{KH:.1f}" rx="5" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
            font_main = 12 if len(main_t) <= 2 else (9.5 if len(main_t) <= 4 else 8)
            if sub_t:
                svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.42:.1f}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_main}" font-weight="800" text-anchor="middle" dominant-baseline="central">{escape(main_t)}</text>')
                font_sub = 8 if len(sub_t) <= 3 else 7
                svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.75:.1f}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_sub}" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_t)}</text>')
            else:
                svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH/2:.1f}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_main}" font-weight="800" text-anchor="middle" dominant-baseline="central">{escape(main_t)}</text>')

    # Left Thumbs
    th_x0 = kx0 + 2 * (KW + GAP_X)
    th_y0 = ky0 + 3 * (KH + GAP_Y) + 8
    for i, (main_t, sub_t, st_key) in enumerate(layer_data["left_thumb"]):
        st = STYLES.get(st_key, STYLES["mod"])
        kx = th_x0 + i * (KW + GAP_X)
        ky = th_y0 + i * 3
        svg.append(f'    <rect x="{kx:.1f}" y="{ky:.1f}" width="{KW:.1f}" height="{KH:.1f}" rx="5" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
        svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.42:.1f}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="10.5" font-weight="800" text-anchor="middle" dominant-baseline="central">{escape(main_t)}</text>')
        if sub_t:
            svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.75:.1f}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="7.5" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_t)}</text>')

    # Right Hand Matrix (3x5)
    rx0 = kx0 + 5 * (KW + GAP_X) + SPLIT_GAP
    for r in range(3):
        for c in range(5):
            main_t, sub_t, st_key = layer_data["right"][r][c]
            st = STYLES.get(st_key, STYLES["normal"])
            kx = rx0 + c * (KW + GAP_X)
            ky = ky0 + r * (KH + GAP_Y) + R_STAGGER[c]
            svg.append(f'    <rect x="{kx:.1f}" y="{ky:.1f}" width="{KW:.1f}" height="{KH:.1f}" rx="5" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
            font_main = 12 if len(main_t) <= 2 else (9.5 if len(main_t) <= 4 else 8)
            if sub_t:
                svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.42:.1f}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_main}" font-weight="800" text-anchor="middle" dominant-baseline="central">{escape(main_t)}</text>')
                font_sub = 8 if len(sub_t) <= 3 else 7
                svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.75:.1f}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_sub}" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_t)}</text>')
            else:
                svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH/2:.1f}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="{font_main}" font-weight="800" text-anchor="middle" dominant-baseline="central">{escape(main_t)}</text>')

    # Right Thumbs
    rth_x0 = rx0
    rth_y0 = ky0 + 3 * (KH + GAP_Y) + 14
    for i, (main_t, sub_t, st_key) in enumerate(layer_data["right_thumb"]):
        st = STYLES.get(st_key, STYLES["layer"])
        kx = rth_x0 + i * (KW + GAP_X)
        ky = rth_y0 - i * 3
        svg.append(f'    <rect x="{kx:.1f}" y="{ky:.1f}" width="{KW:.1f}" height="{KH:.1f}" rx="5" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
        svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.42:.1f}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="10.5" font-weight="800" text-anchor="middle" dominant-baseline="central">{escape(main_t)}</text>')
        if sub_t:
            svg.append(f'    <text x="{kx + KW/2:.1f}" y="{ky + KH*0.75:.1f}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="7.5" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_t)}</text>')

    svg.append('  </g>')
    return "\n".join(svg)

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TOTAL_W} {TOTAL_H}" width="{TOTAL_W}" height="{TOTAL_H}">',
    '<defs>',
    '  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">',
    '    <stop offset="0%" stop-color="#050811"/>',
    '    <stop offset="50%" stop-color="#0f172a"/>',
    '    <stop offset="100%" stop-color="#020617"/>',
    '  </linearGradient>',
    '  <filter id="cardGlow" x="-10%" y="-10%" width="120%" height="120%">',
    '    <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.4"/>',
    '  </filter>',
    '</defs>',
    f'  <rect width="{TOTAL_W}" height="{TOTAL_H}" fill="url(#bgGrad)"/>',
    f'  <text x="{TOTAL_W/2}" y="{SAFE_Y + 28}" fill="#f8fafc" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="23" font-weight="900" text-anchor="middle" letter-spacing="-0.5">⌨️ X.Tips X7 (36-Key Split) Complete Keymap Cheatsheet</text>',
    f'  <text x="{TOTAL_W/2}" y="{SAFE_Y + 48}" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11.5" font-weight="500" text-anchor="middle">macOS Ergonomic Split Workflow | 9 Layers (Layer 0 ~ Layer 8) Quick Reference Wallpaper</text>',
]

for idx, layer in enumerate(LAYERS):
    row = idx // 3
    col = idx % 3
    cx = GRID_X + col * (CARD_W + CARD_GAP_X)
    cy = GRID_Y + row * (CARD_H + CARD_GAP_Y)
    svg.append(render_layer_card(layer, cx, cy, CARD_W, CARD_H))

# Bottom Legend
leg_y = SAFE_Y + SAFE_H - 12
LEG_ITEMS = [
    ("#78350f", "#f59e0b", "주황: 현재 홀드(유지) 키"),
    ("#3b0764", "#a855f7", "보라: 레이어 전환"),
    ("#172554", "#3b82f6", "파랑: 수식키 (Mod)"),
    ("#083344", "#06b6d4", "청록: 주요 기능·숫자"),
    ("#064e3b", "#10b981", "초록: 방향·기호·실행"),
    ("#4c0519", "#f43f5e", "빨강: 삭제·닫기·주의"),
]

leg_svg = ['  <g transform="translate(360, ' + str(leg_y) + ')">']
lx = 0
for bg, border, label in LEG_ITEMS:
    leg_svg.append(f'    <rect x="{lx}" y="-10" width="12" height="12" rx="3" fill="{bg}" stroke="{border}" stroke-width="1.5"/>')
    leg_svg.append(f'    <text x="{lx + 18}" y="0" fill="#94a3b8" font-family="-apple-system,BlinkMacSystemFont,Pretendard,sans-serif" font-size="11" font-weight="600">{label}</text>')
    lx += 18 + len(label) * 9.5 + 24
leg_svg.append('  </g>')

svg.append("\n".join(leg_svg))
svg.append('</svg>')

# Save SVG to both locations
out_svg_wp = f"{OUT_DIR}/version0_original_grid.svg"
out_svg_wiki = f"{WIKI_ASSET_DIR}/x7_keymap_wallpaper_1920x1080.svg"
with open(out_svg_wp, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))
with open(out_svg_wiki, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

# Render PNG
out_png_wp = f"{OUT_DIR}/version0_original_grid.png"
subprocess.run([CHROME_PATH, "--headless=new", "--window-size=1920,1080", f"--screenshot={out_png_wp}", f"file://{out_svg_wp}"], capture_output=True)
print("Saved version 0 original grid SVG & PNG")

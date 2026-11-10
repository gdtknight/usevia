import os
import json
from html import escape
import subprocess

OUT_DIR = "/Users/yong/Documents/UseVia/wallpapers"
os.makedirs(OUT_DIR, exist_ok=True)

from v1_script import LAYERS, STYLES

# Column staggering offsets for X.Tips X7 36-key split
COL_OFFSETS_LEFT = [6, 3, 0, 2.5, 5]
COL_OFFSETS_RIGHT = [5, 2.5, 0, 3, 6]

def render_split_keyboard(layer_data, origin_x, origin_y, kw=58, kh=40, col_gap=5, row_gap=5, split_gap=48, title_mode="full"):
    """
    Renders an ergonomic 36-key split keyboard for a given layer.
    Returns SVG string elements.
    """
    svg = []
    
    # Title / Trigger
    if title_mode == "full":
        svg.append(f'<text x="{origin_x}" y="{origin_y - 14}" fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="14" font-weight="700">{escape(layer_data["title"])}</text>')
        svg.append(f'<rect x="{origin_x + 320}" y="{origin_y - 28}" width="180" height="20" rx="10" fill="#1e293b" stroke="#334155" stroke-width="1"/>')
        svg.append(f'<text x="{origin_x + 410}" y="{origin_y - 14}" fill="#fbbf24" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="11" font-weight="600" text-anchor="middle">⚡ {escape(layer_data["trigger"])}</text>')
    elif title_mode == "compact":
        svg.append(f'<text x="{origin_x}" y="{origin_y - 12}" fill="#38bdf8" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="13" font-weight="700">{escape(layer_data["title"])}</text>')
        svg.append(f'<text x="{origin_x + 360}" y="{origin_y - 12}" fill="#fbbf24" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="10" font-weight="600">⚡ {escape(layer_data["trigger"])}</text>')

    # Left Hand Matrix (3 rows x 5 cols)
    for r in range(3):
        for c in range(5):
            main_txt, sub_txt, style_key = layer_data["left"][r][c]
            st = STYLES.get(style_key, STYLES["normal"])
            kx = origin_x + c * (kw + col_gap)
            ky = origin_y + r * (kh + row_gap) + COL_OFFSETS_LEFT[c]
            
            svg.append(f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="6" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
            
            font_main = 14 if len(main_txt) <= 2 else (11 if len(main_txt) <= 4 else 9)
            if sub_txt:
                svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.48}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="{font_main}" font-weight="700" text-anchor="middle" dominant-baseline="central">{escape(main_txt)}</text>')
                font_sub = 9 if len(sub_txt) <= 3 else 8
                svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.78}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="{font_sub}" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_txt)}</text>')
            else:
                svg.append(f'<text x="{kx + kw/2}" y="{ky + kh/2}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="{font_main}" font-weight="700" text-anchor="middle" dominant-baseline="central">{escape(main_txt)}</text>')

    # Left Hand Thumbs (3 keys)
    thumb_base_x = origin_x + 2 * (kw + col_gap)
    thumb_base_y = origin_y + 3 * (kh + row_gap) + 10
    for i, (main_txt, sub_txt, style_key) in enumerate(layer_data["left_thumb"]):
        st = STYLES.get(style_key, STYLES["mod"])
        kx = thumb_base_x + i * (kw + col_gap)
        ky = thumb_base_y + i * 4
        svg.append(f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="6" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
        svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.46}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="12" font-weight="700" text-anchor="middle" dominant-baseline="central">{escape(main_txt)}</text>')
        if sub_txt:
            svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.78}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="9" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_txt)}</text>')

    # Right Hand Matrix (3 rows x 5 cols)
    right_start_x = origin_x + 5 * (kw + col_gap) + split_gap
    for r in range(3):
        for c in range(5):
            main_txt, sub_txt, style_key = layer_data["right"][r][c]
            st = STYLES.get(style_key, STYLES["normal"])
            kx = right_start_x + c * (kw + col_gap)
            ky = origin_y + r * (kh + row_gap) + COL_OFFSETS_RIGHT[c]
            
            svg.append(f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="6" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
            
            font_main = 14 if len(main_txt) <= 2 else (11 if len(main_txt) <= 4 else 9)
            if sub_txt:
                svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.48}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="{font_main}" font-weight="700" text-anchor="middle" dominant-baseline="central">{escape(main_txt)}</text>')
                font_sub = 9 if len(sub_txt) <= 3 else 8
                svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.78}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="{font_sub}" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_txt)}</text>')
            else:
                svg.append(f'<text x="{kx + kw/2}" y="{ky + kh/2}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="{font_main}" font-weight="700" text-anchor="middle" dominant-baseline="central">{escape(main_txt)}</text>')

    # Right Hand Thumbs (3 keys)
    r_thumb_base_x = right_start_x
    r_thumb_base_y = origin_y + 3 * (kh + row_gap) + 18
    for i, (main_txt, sub_txt, style_key) in enumerate(layer_data["right_thumb"]):
        st = STYLES.get(style_key, STYLES["layer"])
        kx = r_thumb_base_x + i * (kw + col_gap)
        ky = r_thumb_base_y - i * 4
        svg.append(f'<rect x="{kx}" y="{ky}" width="{kw}" height="{kh}" rx="6" fill="{st["bg"]}" stroke="{st["border"]}" stroke-width="1.2"/>')
        svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.46}" fill="{st["main"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="12" font-weight="700" text-anchor="middle" dominant-baseline="central">{escape(main_txt)}</text>')
        if sub_txt:
            svg.append(f'<text x="{kx + kw/2}" y="{ky + kh*0.78}" fill="{st["sub"]}" font-family="-apple-system,BlinkMacSystemFont,sans-serif" font-size="9" font-weight="500" text-anchor="middle" dominant-baseline="central">{escape(sub_txt)}</text>')

    return "\n".join(svg)

print("render_split_keyboard loaded")

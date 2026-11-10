#!/usr/bin/env python3
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.dirname(BASE_DIR)
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SCRIPTS = [
    ("Version 0 (Original 3x3 Grid)", os.path.join(BASE_DIR, "make_original_grid.py"), os.path.join(OUT_DIR, "version0_original_grid.svg"), os.path.join(OUT_DIR, "version0_original_grid.png")),
    ("Version 1 (Hero + Satellite)", os.path.join(BASE_DIR, "v1_script.py"), os.path.join(OUT_DIR, "version1_hero_satellite.svg"), os.path.join(OUT_DIR, "version1_hero_satellite.png")),
    ("Version 2 (Single Giant Overlay Board)", os.path.join(BASE_DIR, "make_v2.py"), os.path.join(OUT_DIR, "version2_overlay_board.svg"), os.path.join(OUT_DIR, "version2_overlay_board.png")),
    ("Version 3A (Coding & Typing)", os.path.join(BASE_DIR, "make_v3a.py"), os.path.join(OUT_DIR, "version3_dual_a_coding.svg"), os.path.join(OUT_DIR, "version3_dual_a_coding.png")),
    ("Version 3B (System & Navigation)", os.path.join(BASE_DIR, "make_v3b.py"), os.path.join(OUT_DIR, "version3_dual_b_system.svg"), os.path.join(OUT_DIR, "version3_dual_b_system.png")),
    ("Version 4 (Cheatsheet Hybrid)", os.path.join(BASE_DIR, "make_v4.py"), os.path.join(OUT_DIR, "version4_cheatsheet_hybrid.svg"), os.path.join(OUT_DIR, "version4_cheatsheet_hybrid.png")),
]

print("=== Starting Wallpaper Build Pipeline ===")

for name, py_script, svg_path, png_path in SCRIPTS:
    print(f"\n[Building] {name}...")
    # 1. Run Python generator
    res = subprocess.run([sys.executable, py_script], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error running {py_script}:\n{res.stderr}")
        continue
    print(f"  ✓ SVG generated: {os.path.basename(svg_path)}")
    
    # 2. Render PNG via Headless Chrome
    chrome_cmd = [
        CHROME_PATH,
        "--headless=new",
        "--window-size=1920,1080",
        f"--screenshot={png_path}",
        f"file://{svg_path}"
    ]
    res_chrome = subprocess.run(chrome_cmd, capture_output=True, text=True)
    if os.path.exists(png_path):
        size_kb = os.path.getsize(png_path) / 1024
        print(f"  ✓ PNG rendered: {os.path.basename(png_path)} ({size_kb:.1f} KB)")
    else:
        print(f"  ✗ Failed to render PNG: {os.path.basename(png_path)}")

print("\n=== All Wallpapers Built Successfully! ===")

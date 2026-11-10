---
title: "X.Tips X7 (36키) LLM Wiki 카탈로그 (Index)"
category: meta
updated: 2026-11-03
tags: [via, x7, index, catalog]
---

# 📚 X.Tips X7 (36키) 키맵 & 워크플로우 위키 카탈로그

이 파일은 위키의 모든 문서를 카테고리별로 정리한 **중앙 색인(Content Index)**입니다.

---

## 🧭 1. 핵심 아키텍처 & 스키마 (Core & Schema)

- [CLAUDE.md](file:///Users/yong/Documents/UseVia/CLAUDE.md) — LLM Wiki 운영 스키마, 오른손 역순 매트릭스 인덱스 규칙, Ingest/Query/Lint 프로토콜 정의
- [[overview|X.Tips X7 (36키) 키맵 아키텍처 총괄]] ([overview.md](file:///Users/yong/Documents/UseVia/wiki/overview.md)) — 4대 설계 철학 및 9개 레이어(`L0~L8`) 전체 진입 구조도
- [x7_keymap_manual.md](file:///Users/yong/Documents/UseVia/x7_keymap_manual.md) — 실사용자를 위한 1페이지 통합 치트시트 및 3일 적응 가이드
- [[log|변경 및 작업 로그 (Chronological Log)]] ([log.md](file:///Users/yong/Documents/UseVia/wiki/log.md)) — 시간순 키맵 변경·실험·Lint 기록

---

## 🗂️ 2. 레이어별 상세 명세 (`wiki/layers/`)

| 레이어 | 위키 문서 | 진입 트리거 | 한 줄 요약 |
| :---: | :--- | :--- | :--- |
| **L0** | [[layer-0-base\|Layer 0: 기본 레이어 (Base)]] | 기본 상태 (`TO(0)`) | QWERTY, `Bksp` 홈 로우, `Caps(한/영)`, `SftEnt`, 왼손 엄지 `⌃⌥⌘` 고정 |
| **L1** | [[layer-1-nav-num-sym\|Layer 1: 숫자 · 방향키 · 기본기호]] | 오른손 엄지 `Spc` 홀드 | 상단 `1~0`, 오른손 기본 기호(`[];'\,./`), 왼손 방향키(`←↓↑→`) + `Del` |
| **L2** | [[layer-2-shift-sym\|Layer 2: 코딩 · Shift 기호]] | 오른손 엄지 `Ent` 홀드 | L1과 1:1 대칭되는 Shift 기호(`!~)`, `{}`, `~_+`, `:"<>?`) 및 `Home/End` |
| **L3** | [[layer-3-mouse-media\|Layer 3: 마우스 · 미디어 · F키]] | 오른손 바깥 엄지 홀드 / `TO(3)` | 오른손 마우스 이동·클릭·휠·미디어, 왼손 `F1~F10` 및 macOS Spaces 전환 |
| **L4** | [[layer-4-browser-edit\|Layer 4: 브라우저 & 고속 편집]] | 왼손 하단 `Z` 홀드 | 왼손 브라우저 탭(`⌘W/T/R/L`) 제어, 오른손 단어·줄 단위 고속 커서 이동 |
| **L5** | [[layer-5-ide-coding\|Layer 5: IDE · 코딩 · 디버깅]] | 왼손 하단 `X` 홀드 | VS Code 명령 팔레트(`⌘⇧P`), 정의 이동(`F12`), 줄 이동·복제·주석, `F5~F11` 디버그 |
| **L6** | [[layer-6-hyper-meh\|Layer 6: Rectangle 창 분할 & Hyper]] | 왼손 하단 `C` 홀드 | Rectangle 기본 단축키 내장(2/3/4분할·최대화·모니터이동 무설정 즉시 작동) + `Hyper` |
| **L7** | [[layer-7-numpad\|Layer 7: 오른손 3×3 넘패드]] | 왼손 하단 `V` 홀드 | 오른손 정통 3×3 계산기 배열 + 사칙연산, 왼손 스프레드시트 셀 이동 |
| **L8** | [[layer-8-macos-system\|Layer 8: macOS 시스템 · 회의]] | 오른손 하단 `M` 홀드 | 화면 잠금(`⌃⌘Q`), 캡처(`⌘⇧3/4/5`), Zoom 마이크/카메라 토글, 밝기·볼륨 |

---

## ⚡ 3. 도메인별 워크플로우 (`wiki/workflows/`)

- [[coding-and-ide|코딩 및 IDE 워크플로우]] ([coding-and-ide.md](file:///Users/yong/Documents/UseVia/wiki/workflows/coding-and-ide.md)) — `L1 + L2` 괄호 근육 기억과 `L5` VS Code/Cursor 단축키 연계
- [[browsing-and-text-editing|브라우징 및 고속 텍스트 편집 워크플로우]] ([browsing-and-text-editing.md](file:///Users/yong/Documents/UseVia/wiki/workflows/browsing-and-text-editing.md)) — 왼손 원핸드 브라우징(`L4`) 및 단어·줄 단위 커서 점프
- [[macos-window-and-raycast|macOS 창 관리 · Raycast · 시스템 제어 워크플로우]] ([macos-window-and-raycast.md](file:///Users/yong/Documents/UseVia/wiki/workflows/macos-window-and-raycast.md)) — `L6` Hyper/Meh 창 분할 및 `L8` 캡처·화상회의 제어

---

## 🧠 4. 핵심 개념 및 하드웨어 명세 (`wiki/concepts/`)

- [[hardware-matrix-x7|X.Tips X7 하드웨어 매트릭스 및 VIA 제약사항]] ([hardware-matrix-x7.md](file:///Users/yong/Documents/UseVia/wiki/concepts/hardware-matrix-x7.md)) — 40슬롯 JSON 배열 인덱스 매핑표(오른손 역순 주의) 및 QMK `LT()` 8비트 제약
- [[layer-trigger-strategy|레이어 트리거 전략 (Thumb + Bottom-Row LT)]] ([layer-trigger-strategy.md](file:///Users/yong/Documents/UseVia/wiki/concepts/layer-trigger-strategy.md)) — Home Row Mods 대신 하단 열(`Z,X,C,V,M`) + 엄지 트리거를 채택한 이유와 양손 분담 원칙

---

## 📦 5. 원본 자료 보관소 (`raw/`)

- [2026-11-03-v1-baseline.layout.json](file:///Users/yong/Documents/UseVia/raw/layouts/2026-11-03-v1-baseline.layout.json) — 9-Layer 초기 베이스라인 레이아웃 스냅샷
- [2026-11-03-llm-wiki-pattern.md](file:///Users/yong/Documents/UseVia/raw/notes/2026-11-03-llm-wiki-pattern.md) — LLM Wiki 아키텍처 원본 아이디어 노트

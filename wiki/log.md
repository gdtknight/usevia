---
title: "X.Tips X7 키맵 위키 작업 로그 (Chronological Log)"
category: meta
updated: 2026-11-03
tags: [via, x7, log, changelog]
---

# 📜 X.Tips X7 키맵 위키 작업 로그

이 문서는 시간순으로 추가되는 변경 기록(Append-only Log)입니다.
최근 5개 항목 조회 명령어: `grep "^## \[" wiki/log.md | tail -5`

---

## [2026-11-06] refactor | Layer 8 왼손 B키 이동(L4~L8 왼손 일렬 정렬), 4종 배경화면 개편 및 디렉토리 구조 정리

- **키맵 변경 (대안 A 채택)**:
  - Layer 0 왼손 `B`(Index 14)를 `LT(8, KC_B)`로 변경하여 **왼손 하단 5키(`Z, X, C, V, B`)가 Layer 4~8로 완벽히 일렬 정렬**.
  - Layer 0 오른손 `M`(Index 33)을 `KC_M` 일반 영문 키로 환원하여 양손 교차 인체공학 유지.
  - `x_tips_x7_keyboard.layout.json`, `x7_keymap_manual.md`, `wiki/layers/`, `wiki/concepts/` 전체 동기화.
- **월페이퍼 시스템 개편**:
  - `wallpapers/` 디렉토리에 4개 버전(Ver 1~4)의 1920x1080 고화질 배경화면 구축.
  - Version 2(Single Giant Overlay Board): 1920x1080 풀스크린 기준으로 키 크기 극대화(174x237px) 및 Layer 0~8 전체 집약 렌더링.
- **디렉토리 클린업**:
  - 구버전 배경화면(`x7_keymap_wallpaper_1920x1080.png`)을 `wallpapers/archive/`로 이동.
  - 백업 레이아웃(`x_tips_x7_keyboard_(wheel).layout.json`)을 `raw/layouts/`로 이동.
  - `__pycache__` 및 `.DS_Store` 임시/캐시 파일 일괄 정리.

---

## [2026-11-05] update | 배경화면 개별 키 세로 높이 약 38% 확대(37px->51px) 및 가독성 개선

- **수행 내용**:
  - 각 레이어 카드 내부의 하단 빈 공간을 모두 키 영역으로 전환.
  - 개별 키캡 세로 높이를 기존 37px에서 **51px로 약 38% 대폭 확대**.
  - 키캡 내 메인 텍스트 및 서브 단축키 폰트 크기와 가독성 개선.
  - [x7_keymap_wallpaper_1920x1080.png](file:///Users/yong/Documents/UseVia/x7_keymap_wallpaper_1920x1080.png) 및 [x7_keymap_wallpaper_1920x1080.svg](file:///Users/yong/Documents/UseVia/wiki/assets/x7_keymap_wallpaper_1920x1080.svg) 재렌더링 완료.

---

## [2026-11-05] feat | 1920x1080 통합 키맵 배경화면 (Layer 0~8 전체 일괄 표시) 생성

- **배경**: 36키 스플릿 X7의 9개 레이어(L0~L8) 전체를 한 화면에서 보면서 작업할 수 있는 고해상도 데스크탑 배경화면 제작 요청.
- **안전 마진 기준**: 1920x1080 해상도를 기본으로 하되, 1600x1050 해상도 화면(약 16:10 비율)에서도 잘리지 않도록 안전 구역(Safe Zone) 마진(좌우 160px, 상하 15px)을 확보하여 3x3 격자 배치.
- **산출물**:
  - SVG 원본: [x7_keymap_wallpaper_1920x1080.svg](file:///Users/yong/Documents/UseVia/wiki/assets/x7_keymap_wallpaper_1920x1080.svg)
  - PNG 배경화면 이미지: [x7_keymap_wallpaper_1920x1080.png](file:///Users/yong/Documents/UseVia/x7_keymap_wallpaper_1920x1080.png)

---

## [2026-11-04] fix | Layer 3 마우스 휠 정식 키코드(`KC_MS_WH_*`) 업데이트 및 VIA Export 레이아웃 동기화

- **원인 분석**:
  - `usevia.app`에서 `KC_WH_U`, `KC_WH_D`, `KC_WH_L`, `KC_WH_R` 약어를 인식하지 못해 해당 자리가 미할당(빈 키)으로 풀려 있었음.
  - 사용자가 VIA UI에서 직접 할당 후 내보낸 `x_tips_x7_keyboard_(wheel).layout.json` 분석 결과 정식 키코드는 **`KC_MS_WH_UP`**, **`KC_MS_WH_DOWN`**, **`KC_MS_WH_LEFT`**, **`KC_MS_WH_RIGHT`**임이 확인됨.
- **수행 작업**:
  - `x_tips_x7_keyboard.layout.json`을 사용자가 검증하고 export한 최신 파일로 전면 교체 완료 (이전 버전은 `raw/layouts/2026-11-04-pre-wheel-fix.layout.json`에 보관).
  - [hardware-matrix-x7.md](file:///Users/yong/Documents/UseVia/wiki/concepts/hardware-matrix-x7.md)에 정식 키코드 및 VIA export 정규화 규칙 반영.

---

## [2026-11-04] update | Layer 8 F자리 전체화면(⌃⌘F) 추가 및 문서/SVG 동기화

- **작업 내용**:
  - [x_tips_x7_keyboard.layout.json](file:///Users/yong/Documents/UseVia/x_tips_x7_keyboard.layout.json): Layer 8의 중복된 `C(KC_DOWN)`(앱 윈도우)을 **`C(G(KC_F))`(`⌃⌘F`, macOS 전체화면 전환)**으로 교체.
  - [x7_keymap_manual.md](file:///Users/yong/Documents/UseVia/x7_keymap_manual.md), [layer-8-macos-system.md](file:///Users/yong/Documents/UseVia/wiki/layers/layer-8-macos-system.md), [layer-8.svg](file:///Users/yong/Documents/UseVia/wiki/assets/layer-8.svg)에 반영 완료.
  - 이제 `오른손 M 홀드 + 왼손 F`로 `Fn + F`와 완벽히 동일한 전체화면 토글 가능.

---

## [2026-11-03] fix | Layer 6 VIA 수식키 파서 호환성 수정(`C(A(...))`, `C(LAG(...))`) 및 macOS 창 제어(`⌃⌘F` 등) 통합

- **원인 분석 (`N, M` 모니터 이동 미동작 원인)**:
  - VIA의 JSON 파서는 `SGUI`, `LAG`, `LSA`, `MEH`, `HYPR`만 내장 키워드로 인식하며 `LCA(...)`와 `LCAG(...)`는 파싱하지 못함을 확인.
  - 이를 VIA 표준 중첩 문법인 **`C(A(KC_...))`**(`⌃⌥`)와 **`C(LAG(KC_...))`**(`⌃⌥⌘`)로 전수 교체하여 해결하고, 해당 규칙을 [hardware-matrix-x7.md](file:///Users/yong/Documents/UseVia/wiki/concepts/hardware-matrix-x7.md)에 영구 기록.
- **왼손 `Hyper` 여유 슬롯 8개를 macOS 기본 창 제어 단축키로 교체**:
  - `Q`(`` ⌘` `` 같은 앱 창 전환), `W`(`⌘W` 창 닫기), `A`(`⌃⌘F` 전체 화면 전환 — `Fn+F` 대체), `S`(`⌘M` 창 최소화), `Z`(`⌘H` 앱 숨기기), `X`(`⌥⌘H` 다른 앱 모두 숨기기), `V/B`(`⌃←/→` 데스크탑 전환).

---

## [2026-11-03] query | macOS 멀티 모니터 포커스 확인 및 Spaces(⌃←/→) 전환 기준 정리

- **질문**: macOS에서 현재 어떤 모니터에 포커싱되어 있는지 확인하는 방법과 `⌃→` 실행 시 어느 모니터의 데스크탑이 전환되는지 구분하는 방법.
- **정리 및 파일링**: [macos-window-and-raycast.md](file:///Users/yong/Documents/UseVia/wiki/workflows/macos-window-and-raycast.md)에 ① macOS 상단 메뉴 막대(Menu Bar) 선명도 차이, ② `⌃←/→`는 키보드 포커스가 아닌 **마우스 포인터가 위치한 모니터**를 전환한다는 핵심 원리, ③ Rectangle의 `moveCursorAcrossDisplays` 옵션 연동 방법을 문서화.

---

## [2026-11-03] update | Layer 5 코드 탐색(오른손) & 디버깅 풀패드(왼손) 완전 분리형으로 고도화

- **배경**: Layer 0에서 `Cmd + 알파벳`으로 쉽게 입력 가능한 단순 단축키(`⌘Q, ⌘W, ⌘P, ⌘Z, ⌘B, ⌘D, ⌘C, ⌘V`)를 Layer 5에서 모두 제거하고, 36키에서 누르기 까다로운 **코드 탐색 및 디버깅 단축키**를 양손 완전 분리형으로 재배치.
- **수행 작업**:
  1. [x_tips_x7_keyboard.layout.json](file:///Users/yong/Documents/UseVia/x_tips_x7_keyboard.layout.json) `layers[5]` 업데이트:
     - **왼손(디버깅 풀패드)**: 상단 `⇧F5`(중지)·`⌘⇧F5`(재시작)·`⌘⇧D`(디버그창)·`⌘⇧Y`(콘솔)·`` ⌃` ``(터미널), 중단 `F9`(중단점)·`F5`(실행)·`F10`(StepOver)·`F11`(StepInto)·`⇧F11`(StepOut), 하단 `⌘⇧M`(에러목록)·`⌘⇧F`(전체검색)·`⌘⇧P`(명령팔레트)·`⌘⇧K`(줄삭제)
     - **오른손(코드 탐색 & 편집)**: 상단 `⌥F12`(Peek)·`F12`(정의)·`⌘F12`(구현체)·`⇧F12`(참조)·`F2`(이름변경), 중단 `⌃-`(뒤로)·`⌃⇧-`(앞으로)·`⌘⇧O`(심볼목록)·`F8`(다음에러)·`⌘⇧\`(짝괄호점프), 하단 `⌘/`(주석)·`⌥↓/↑`(줄이동)·`⇧⌥↓`(줄복제)·`⇧⌥F`(포맷), 엄지 `⌘.`(Quick Fix)·`⇧F8`(이전에러)
  2. [x7_keymap_manual.md](file:///Users/yong/Documents/UseVia/x7_keymap_manual.md), [layer-5.svg](file:///Users/yong/Documents/UseVia/wiki/assets/layer-5.svg), [layer-5-ide-coding.md](file:///Users/yong/Documents/UseVia/wiki/layers/layer-5-ide-coding.md), [coding-and-ide.md](file:///Users/yong/Documents/UseVia/wiki/workflows/coding-and-ide.md) 동기화 완료.

---

## [2026-11-03] update | Layer 6을 Rectangle 무설정(Zero-Config) 창 분할 레이어로 재설계

- **배경**: 가볍고 심플한 오픈소스 창 분할 앱인 **Rectangle**을 별도 단축키 설정 없이 설치 즉시 사용할 수 있도록 Layer 6(`C` Hold) 커스텀 요청.
- **수행 작업**:
  1. [x_tips_x7_keyboard.layout.json](file:///Users/yong/Documents/UseVia/x_tips_x7_keyboard.layout.json)의 `layers[6]` 키코드를 Rectangle 표준 단축키(`LCA`, `LCAG`, `MEH`)에 맞게 업데이트:
     - 오른손 중단(`H,J,K,L,Bksp`): 좌/하/상/우 1/2 분할(`⌃⌥ + ←/↓/↑/→`) 및 최대화(`⌃⌥Enter`)
     - 오른손 엄지(`Spc,Ent`): 정중앙 배치(`⌃⌥C`), 이전 크기 복원(`⌃⌥⌫`)
     - 오른손 상단(`Y,U,I,O,P`): 세로 최대화(`⌃⌥⇧↑`) 및 좌상/우상/좌하/우하 1/4 모서리 분할(`⌃⌥ + U/I/J/K`)
     - 오른손 하단(`N,M,Tab,Caps,SftEnt`): 이전/다음 모니터 이동(`⌃⌥⌘ + ←/→`), 창 축소/확대(`⌃⌥ + -/=`), 최대화
     - 왼손 안쪽(`D,F,G` / `E,R,T`): 좌/중/우 1/3 분할(`⌃⌥ + D/F/G`) 및 좌/우 2/3 분할(`⌃⌥ + E/T`)
  2. [x7_keymap_manual.md](file:///Users/yong/Documents/UseVia/x7_keymap_manual.md), [layer-6.svg](file:///Users/yong/Documents/UseVia/wiki/assets/layer-6.svg), [layer-6-hyper-meh.md](file:///Users/yong/Documents/UseVia/wiki/layers/layer-6-hyper-meh.md), [macos-window-and-raycast.md](file:///Users/yong/Documents/UseVia/wiki/workflows/macos-window-and-raycast.md), [overview.md](file:///Users/yong/Documents/UseVia/wiki/overview.md), [index.md](file:///Users/yong/Documents/UseVia/wiki/index.md) 일괄 동기화 완료.

---

## [2026-11-03] query | Layer 6 (Hyper & Meh) 실전 활용법 및 동선 가이드 정리

- **질문**: Layer 6은 어떻게 활용해야 하는가?
- **정리 및 파일링**: [layer-6-hyper-meh.md](file:///Users/yong/Documents/UseVia/wiki/layers/layer-6-hyper-meh.md)에 `Hyper`/`Meh`의 동작 원리(충돌 없는 빈 호출벨 31개)와 손가락 동선이 가장 편한 3대 활용법(① 오른손 홈 로우 창 분할, ② 오른손 엄지 클립보드/AI 호출, ③ 오른손 상단·왼손 검지 1초 앱 스위처)을 구체화하여 문서화.

---

## [2026-11-03] update | 레이어별 위키 페이지(L0~L8) 시각적 키맵 다이어그램(SVG + ASCII Box) 추가

- **배경**: 레이어별 위키 페이지에서 물리적 36키 스플릿 배치를 한눈에 직관적으로 파악할 수 있도록 시각화 강화 요청.
- **수행 작업**:
  1. `wiki/assets/layer-0.svg` ~ `layer-8.svg` 고해상도 컬러 코딩 키맵 이미지 9종 생성 (현재 홀드 중인 진입키 주황색 강조, 역할별 색상 구분, 스플릿 컬럼 스태거 반영)
  2. `wiki/layers/layer-0-base.md` ~ `layer-8-macos-system.md` 9개 문서 상단에 SVG 다이어그램 임베드 및 한글 전각 폭이 보정된 36키 스플릿 ASCII 박스 다이어그램 병기

---

## [2026-11-03] ingest | X.Tips X7 36키 9-Layer 베이스라인 LLM Wiki 초기 구축

- **배경**: 36키 스플릿 키보드(`X.Tips X7`)의 VIA 키맵과 macOS 워크플로우를 지속적으로 실험·발전시키기 위해 LLM Wiki 아키텍처 도입.
- **수행 작업**:
  1. 최상위 스키마 [CLAUDE.md](file:///Users/yong/Documents/UseVia/CLAUDE.md) 작성 (오른손 역순 JSON 매트릭스 매핑 규칙 및 Ingest/Query/Lint 절차 명문화)
  2. 원본 스냅샷 [2026-11-03-v1-baseline.layout.json](file:///Users/yong/Documents/UseVia/raw/layouts/2026-11-03-v1-baseline.layout.json) 및 [2026-11-03-llm-wiki-pattern.md](file:///Users/yong/Documents/UseVia/raw/notes/2026-11-03-llm-wiki-pattern.md) 보관
  3. 아키텍처 총괄([[overview]]) 및 9개 레이어 상세 문서([[layer-0-base]] ~ [[layer-8-macos-system]]) 생성
  4. 핵심 개념 문서 2종([[hardware-matrix-x7]], [[layer-trigger-strategy]]) 및 실전 워크플로우 문서 3종([[coding-and-ide]], [[browsing-and-text-editing]], [[macos-window-and-raycast]]) 구축
  5. [x_tips_x7_keyboard.layout.json](file:///Users/yong/Documents/UseVia/x_tips_x7_keyboard.layout.json) ↔ [x7_keymap_manual.md](file:///Users/yong/Documents/UseVia/x7_keymap_manual.md) ↔ `wiki/layers/*.md` 간 40개 슬롯×9개 레이어 키코드 정합성 검증 완료

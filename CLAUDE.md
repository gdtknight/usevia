# CLAUDE.md (AGENTS.md) — X.Tips X7 (36-Key) VIA Keymap & LLM Wiki Schema

이 문서는 **X.Tips X7 (36키 스플릿 키보드)** VIA 키맵과 macOS 워크플로우 지식 베이스(**LLM Wiki**)를 구축·유지보수하기 위한 **최상위 스키마(Schema)**입니다.
`AGENTS.md`는 `CLAUDE.md`를 가리키는 심볼릭 링크(`AGENTS.md -> CLAUDE.md`)로, Claude Code, OpenAI Codex, Antigravity 등 모든 에이전트가 동일한 규칙과 워크플로우를 공유합니다.

---

## 0. 핵심 철학 (Core Philosophy — Persistent, Compounding Wiki)

일반적인 RAG가 질의 시점마다 원문 조각을 매번 처음부터 다시 찾아 조합하는 것과 달리, 이 프로젝트는 **에이전트가 지속적으로 컴파일하고 최신 상태로 유지하는 영속적·복리형 위키(Persistent, Compounding Artifact)**를 지향합니다.

- **역할 분담 (Human vs. LLM)**:
  - **사용자 (Human — Architect & Curator)**: 소스 큐레이션, 실사용 피드백 제공, 탐색 방향 지시, 핵심 질문 제기 및 최종 의사결정. Obsidian을 IDE처럼 열어 실시간으로 그래프 뷰(Graph View)와 문서를 탐색합니다.
  - **에이전트 (LLM — Programmer & Maintainer)**: 요약, 교차 참조(Cross-referencing), 파일링(Filing), 이전 설정과의 모순 검출, JSON 키맵·매뉴얼·월페이퍼 동기화 등 지식 베이스의 모든 유지보수(Bookkeeping)를 전담합니다.
  - *"Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."*

---

## 1. 3계층 아키텍처 (3-Layer Architecture)

```
/Users/yong/Documents/UseVia/
├── CLAUDE.md                        # [Schema] 위키 구조, 하드웨어 매핑 규칙, 운영 워크플로우 정의
├── AGENTS.md -> CLAUDE.md           # [Schema] 멀티 에이전트 호환용 심볼릭 링크
├── via-x7.json                      # [Active] VIA 하드웨어 레이아웃 정의 (Rows: 8, Cols: 5)
├── x_tips_x7_keyboard.layout.json   # [Active] 실제 VIA에 로드하여 사용하는 최신 키맵 JSON
├── x7_keymap_manual.md              # [Active] 사용자용 통합 치트시트 (위키 변경 시 항상 동기화)
├── wallpapers/                      # [Active] 고화질 배경화면(1920x1080) 및 빌드 파이프라인
│   ├── version*.png / version*.svg  # 버전별 월페이퍼 산출물 (Ver 0, 1, 2, 3A, 3B, 4)
│   ├── archive/                     # 구버전 배경화면 보관
│   └── scripts/                     # 자동 렌더링 파이썬 스크립트 모음 (`build_all.py` 등)
├── raw/                             # [Layer 1: Raw Sources] 불변(Immutable) 원본 자료 (읽기 전용)
│   ├── layouts/                     # 의미 있는 버전별 레이아웃 JSON 스냅샷 및 외부 레퍼런스
│   ├── notes/                       # 실사용 피드백 메모, 아이디어 원본(`2026-11-03-llm-wiki-pattern.md` 등)
│   └── assets/                      # 클리핑된 외부 이미지 및 원본 첨부파일
└── wiki/                            # [Layer 2: The Wiki] LLM이 전적으로 소유·유지보수하는 지식 베이스
    ├── index.md                     # 콘텐츠 중심 카탈로그 (모든 위키 페이지의 한 줄 요약 및 링크, 탐색 시작점)
    ├── log.md                       # 시간순 작업 기록 (Append-only, unix 도구로 파싱 가능한 고정 프리픽스)
    ├── overview.md                  # 전체 키맵 설계 철학 및 9개 레이어 아키텍처 총괄 요약
    ├── layers/                      # Layer 0 ~ Layer 8 개별 상세 문서 및 키 배치표
    ├── workflows/                   # 도메인·앱별 실전 워크플로우 (IDE 코딩, 브라우저, 창 관리 등)
    ├── concepts/                    # 하드웨어 매트릭스 명세, 트리거 전략, 인체공학 분석, 단축키 충돌 해결
    └── assets/                      # 위키 내장 다이어그램 및 레이어별 SVG 에셋
```

1. **Raw Sources (`raw/`) — 불변의 진실 공급원 (Immutable Source of Truth)**:
   - 레이아웃 스냅샷, 사용자 노트, 외부 레퍼런스 등 원본 자료입니다. 에이전트는 이를 읽고 지식을 추출할 뿐, 기존 원본을 임의로 훼손하지 않습니다.
2. **The Wiki (`wiki/`) — 에이전트 소유 지식 계층**:
   - 에이전트가 생성·갱신하며, 페이지 간 양방향 링크(`[[위키링크]]`)와 일관성을 유지합니다.
3. **The Schema (`CLAUDE.md` / `AGENTS.md`) & Active Artifacts**:
   - 에이전트를 규율 있는 위키 관리자로 동작하게 하는 설정 파일이며, 위키의 지식이 실제 하드웨어 설정(`x_tips_x7_keyboard.layout.json`) 및 시각물(`wallpapers/`)과 1:1로 일치하도록 보장합니다.

---

## 2. 하드웨어 및 JSON 매트릭스 핵심 규칙 (CRITICAL)

`via-x7.json`과 `x_tips_x7_keyboard.layout.json`을 읽거나 수정할 때 **오른손 행렬 인덱스가 좌우 반전(역순)**되어 있음을 반드시 주의해야 합니다.

- **총 행렬 크기**: `8 rows × 5 cols = 레이어당 40개 원소 (Index 0 ~ 39)`
- **왼손 (Rows 0~3)**: 물리적 **왼쪽 → 오른쪽** 순서가 JSON 배열 인덱스 **오름차순(`col 0 → 4`)**과 일치합니다.
- **오른손 (Rows 4~7)**: 물리적 **왼쪽 → 오른쪽** 순서가 JSON 배열 인덱스 **내림차순(`col 4 → 0`)**입니다.

| 물리적 위치 (왼쪽 → 오른쪽 순서) | 행(Row) | 물리적 열 순서 (L → R) | JSON 배열 인덱스 순서 (L → R) | 비고 |
| :--- | :---: | :---: | :---: | :--- |
| **왼손 상단 (5키)** | Row 0 | `0,0` `0,1` `0,2` `0,3` `0,4` | **`0, 1, 2, 3, 4`** | Q W E R T |
| **왼손 중단 (5키)** | Row 1 | `1,0` `1,1` `1,2` `1,3` `1,4` | **`5, 6, 7, 8, 9`** | A S D F G |
| **왼손 하단 (5키)** | Row 2 | `2,0` `2,1` `2,2` `2,3` `2,4` | **`10, 11, 12, 13, 14`** | Z(L4) X(L5) C(L6) V(L7) B(L8) |
| **왼손 엄지 (3키)** | Row 3 | `3,2` `3,3` `3,4` | **`17, 18, 19`** | `15, 16`은 `KC_NO` |
| **오른손 상단 (5키)** | Row 4 | `4,4` `4,3` `4,2` `4,1` `4,0` | **`24, 23, 22, 21, 20`** | ⚠️ 역순 (Y U I O P) |
| **오른손 중단 (5키)** | Row 5 | `5,4` `5,3` `5,2` `5,1` `5,0` | **`29, 28, 27, 26, 25`** | ⚠️ 역순 (H J K L Bksp) |
| **오른손 하단 (5키)** | Row 6 | `6,4` `6,3` `6,2` `6,1` `6,0` | **`34, 33, 32, 31, 30`** | ⚠️ 역순 (N M Tab Caps SftEnt) |
| **오른손 엄지 (3키)** | Row 7 | `7,4` `7,3` `7,2` | **`39, 38, 37`** | ⚠️ 역순 (Space Enter MO3 / `35, 36`=`KC_NO`) |

---

## 3. 인덱싱, 로깅 및 Obsidian 문서 작성 컨벤션

### A. 두 개의 핵심 네비게이션 파일 (`index.md` & `log.md`)
1. **`wiki/index.md` (Content-oriented Catalog)**:
   - 위키 내 모든 문서를 카테고리(`overview`, `layers`, `workflows`, `concepts`)별로 분류하고, 링크·한 줄 요약·최종 수정일을 기록합니다.
   - 에이전트는 질의(Query) 처리 시 임베딩 검색 없이도 **`wiki/index.md`를 가장 먼저 읽고** 관련 문서를 선별해 깊이 들어갑니다(Drill-down).
   - 새로운 페이지가 추가되거나 핵심 요약이 바뀔 때마다 즉시 갱신합니다.
2. **`wiki/log.md` (Chronological Append-only Record)**:
   - 위키의 진화 과정을 시간순(최신 항목 최상단 또는 일관된 Append)으로 기록합니다.
   - 모든 로그는 반드시 파싱 가능한 고정 헤더 형식을 따릅니다:
     `## [YYYY-MM-DD] <type> | <요약 제목>` (`type`: `ingest`, `update`, `refactor`, `query`, `lint`, `feat`, `fix`)
   - 최근 5개 기록 조회 명령어: `grep "^## \[" wiki/log.md | head -5` (또는 `tail -5`)

### B. Obsidian 호환 마크다운 규칙
1. **YAML 프론트매터 필수 포함 (Dataview 호환)**:
   모든 `wiki/` 마크다운 문서 최상단에 YAML 프론트매터를 작성하여 Obsidian Dataview 쿼리를 지원합니다.
   ```yaml
   ---
   title: "문서 제목"
   category: layer | workflow | concept | meta
   layer: 0 # (해당 시 레이어 번호)
   updated: 2026-11-06
   tags: [via, x7, 36key, ...]
   ---
   ```
2. **상호 참조 링크 (Graph View & Agent Navigation)**:
   - Obsidian 그래프 뷰에서 허브(Hub)와 연결망이 선명하게 드러나도록 문서 간 참조 시 `[[문서파일명|표시텍스트]]` 위키링크를 적극 사용합니다.
   - 에이전트 및 IDE에서 즉시 열 수 있도록 중요 파일은 `[파일명](file:///Users/yong/Documents/UseVia/...)` 링크를 병기합니다.
3. **시각적 키 배치 표기**:
   - 모든 레이어 및 워크플로우 표는 JSON 인덱스가 아닌 **실제 사용자의 눈에 보이는 물리적 순서(왼쪽 → 오른쪽)**로 작성합니다.
4. **이미지 및 멀티모달 처리**:
   - 외부 아티클이나 이미지를 참조할 때는 URL 깨짐 방지를 위해 로컬 디렉터리(`raw/assets/` 또는 `wiki/assets/`)에 저장하며, 에이전트는 마크다운 본문을 먼저 읽은 뒤 참조된 이미지 파일을 별도 툴(`read_file`)로 열람하여 컨텍스트를 파악합니다.

---

## 4. 3대 운영 워크플로우 (Operations)

### A. Ingest (피드백·새 아이디어·외부 자료 반영)
사용자가 실사용 피드백을 주거나 `raw/`에 새 자료를 추가했을 때의 처리 절차:
1. **원인 분석 및 설계 합의**: 불편 사항(오타, 동선 꼬임, 단축키 누락 등)이나 새 소스의 핵심 내용을 분석하고 수정 계획을 요약 제시합니다.
2. **Active 파일 업데이트**:
   - `x_tips_x7_keyboard.layout.json` 수정 (오른손 역순 인덱스 `24→20`, `29→25`, `34→30`, `39→37` 엄수)
   - `x7_keymap_manual.md` 통합 치트시트 동기화
   - 주요 마일스톤 변경 시 `raw/layouts/YYYY-MM-DD-설명.layout.json`으로 불변 백업 스냅샷 저장
3. **Wiki 연쇄 업데이트 (10~15개 관련 파일 동시 유지보수)**:
   - 해당 레이어 문서(`wiki/layers/layer-N-*.md`)의 키 배치표 및 변경 배경(Rationale) 업데이트
   - 연관된 워크플로우(`wiki/workflows/*.md`) 및 개념(`wiki/concepts/*.md`) 문서에서 기존 내용과 충돌/모순되는 설명을 찾아 수정하고 교차 참조 갱신
   - `wiki/index.md` 카탈로그 갱신 및 `wiki/log.md`에 작업 이력 기록
4. **월페이퍼(배경화면) 자동 빌드 및 동기화 (MANDATORY)**:
   - **레이아웃 변경 시 항상 배경화면 그림도 함께 업데이트**: `python3 wallpapers/scripts/build_all.py`를 실행하여 6개 버전의 1920×1080 배경화면 이미지(Ver 0, 1, 2, 3A, 3B, 4) 및 `wiki/assets/` 다이어그램을 재생성합니다.
   - 사용자의 현재 macOS 데스크탑 배경화면도 최신 렌더링 결과물로 자동 동기화합니다.

### B. Query (질의응답 및 지식의 위키 파일링 — Filing Back)
사용자가 키맵 구조, 단축키 조합, 인체공학적 대안 설계 등을 질문했을 때의 절차:
1. **`index.md` 우선 탐색**: `wiki/index.md`를 먼저 읽고 관련 위키 페이지들을 찾아 읽습니다.
2. **교차 검증 기반 답변**: 위키의 내용과 `x_tips_x7_keyboard.layout.json` 원본을 대조 검증하여 정확한 근거와 함께 답변합니다.
3. **가치 있는 답변의 위키 자산화 (Filing Back to Wiki)**:
   - 질문 과정에서 도출된 **유의미한 비교 분석, 인체공학 연구(예: 왼손 vs 오른손 레이어 배치 분석), 새로운 워크플로우, 설계 인사이트는 채팅 히스토리에 흘려보내지 않고 `wiki/concepts/` 또는 `wiki/workflows/`에 새 페이지로 파일링( 또는 기존 페이지에 보강)**합니다.
   - 파일링 후 `wiki/index.md`와 `wiki/log.md`에도 반영하여 탐색 결과가 복리로 축적되게 합니다.

### C. Lint (위키 및 키맵 건강 검진)
주기적으로 또는 사용자 요청 시 아래 항목을 전수 점검하고 `wiki/log.md`에 `## [YYYY-MM-DD] lint | 점검 요약`으로 기록합니다:
1. **JSON ↔ 위키 ↔ 월페이퍼 3자 정합성**:
   - `x_tips_x7_keyboard.layout.json`의 실제 40개 키코드와 `x7_keymap_manual.md`, `wiki/layers/*.md`, `wallpapers/scripts/*.py` 표기가 100% 일치하는지 검증하고 구버전 설명(Stale claims)을 교정합니다.
2. **인체공학 및 QMK 기술 제약 점검**:
   - 레이어 진입 키(`Hold`)와 해당 레이어의 주력 액션 키가 **같은 손(One-Hand Chording)**이나 **같은 손가락**에 몰려 손목 비틀림을 유발하는지 점검합니다.
   - 레이어 진입 키(`Hold`)의 해당 레이어 자기 자신 위치가 `KC_TRNS`로 올바르게 비워져 있는지 확인합니다.
   - `LT()`(Layer-Tap) 키에 복합 수정자 키코드(`G(...)`, `SGUI(...)` 등)가 들어가 동작하지 않는 QMK 8비트 키코드 제약 위반 여부를 확인합니다.
3. **위키 그래프 및 링크 무결성**:
   - 인바운드 링크가 없는 고아 페이지(Orphan page), 끊어진 `[[위키링크]]`, 자주 언급되지만 독립 문서가 없는 핵심 개념, `wiki/index.md` 누락 항목을 찾아 연결합니다.

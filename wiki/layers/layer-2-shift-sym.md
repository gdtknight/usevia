---
title: "Layer 2: 코딩 · Shift 기호 전용"
category: layer
layer: 2
updated: 2026-11-03
tags: [via, x7, layer2, symbols, coding, brackets]
---

# 💻 Layer 2: 코딩 · Shift 기호 전용

**진입 방법**: 오른손 중간 엄지(`Enter`, Index `38`) 홀드

[[layer-1-nav-num-sym|Layer 1]]의 모든 숫자와 기본 기호 자리에 **Shift가 적용된 짝꿍 기호**를 1:1로 매핑한 레이어입니다. Shift 키를 별도로 조합할 필요 없이 엄지 하나로 모든 코딩 기호(`!@#$%^&*()`, `{}`, `~_+`, `:"<>?|`)를 입력합니다.

---

## 1. 시각적 키맵 다이어그램 (Visual Keymap)

![Layer 2 Visual Keymap](../assets/layer-2.svg)

### 🤚 왼손 키 배치표 (Left Hand — 1칸 = 1키)

| 행 \ 손가락 | 새끼 (`Col 0`) | 약지 (`Col 1`) | 중지 (`Col 2`) | 검지 (`Col 3`) | 안쪽 검지 (`Col 4`) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **상단 (`Q~T`)** | **!**<br><small>`Shift + 1`</small> | **@**<br><small>`Shift + 2`</small> | **#**<br><small>`Shift + 3`</small> | **$**<br><small>`Shift + 4`</small> | **%**<br><small>`Shift + 5`</small> |
| **중단 (`A~G`)** | **Esc**<br><small>`취소/나가기`</small> | **Tab ⇥**<br><small>`들여쓰기`</small> | **~**<br><small>`물결 (Tilde)`</small> | **_**<br><small>`언더스코어`</small> | **+**<br><small>`플러스`</small> |
| **하단 (`Z~B`)** | **Shift ⇧**<br><small>`범위선택 조합`</small> | **Home**<br><small>`⌘← 줄 처음`</small> | **PgDn**<br><small>`페이지 아래`</small> | **PgUp**<br><small>`페이지 위`</small> | **End**<br><small>`⌘→ 줄 끝`</small> |
| **엄지 (3키)** | *(없음)* | *(없음)* | **Ctrl ⌃**<br><small>`수식키`</small> | **Opt ⌥**<br><small>`수식키`</small> | **Cmd ⌘**<br><small>`수식키`</small> |

### ✋ 오른손 키 배치표 (Right Hand — 1칸 = 1키)

| 행 \ 손가락 | 안쪽 검지 (`Col 4`) | 검지 (`Col 3`) | 중지 (`Col 2`) | 약지 (`Col 1`) | 새끼 (`Col 0`) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **상단 (`Y~P`)** | **^**<br><small>`Shift + 6`</small> | **&**<br><small>`Shift + 7`</small> | *****<br><small>`Shift + 8`</small> | **(**<br><small>`소괄호 열기`</small> | **)**<br><small>`소괄호 닫기`</small> |
| **중단 (`H~⌫`)** | **:**<br><small>`콜론`</small> | **{**<br><small>`중괄호 열기`</small> | **}**<br><small>`중괄호 닫기`</small> | **\|**<br><small>`파이프 (OR)`</small> | **Bksp ⌫**<br><small>`글자 지우기`</small> |
| **하단 (`N~⏎`)** | **"**<br><small>`큰따옴표`</small> | **<**<br><small>`꺾쇠 열기`</small> | **>**<br><small>`꺾쇠 닫기`</small> | **?**<br><small>`물음표`</small> | **Enter ⏎**<br><small>`줄바꿈`</small> |
| **엄지 (3키)** | **MO(3)**<br><small>`Hold ▶ L3`</small> | 🟧 **★ L2 유지중**<br><small>Enter Hold</small> | **TO(3)**<br><small>`마우스 고정`</small> | *(없음)* | *(없음)* |

---

## 2. Layer 1 ↔ Layer 2 1:1 대칭 매핑표

| 위치 | Layer 1 (`Spc` 홀드) | Layer 2 (`Ent` 홀드) | 코딩 활용 예시 |
| :--- | :---: | :---: | :--- |
| **상단 1~10열** | `1 2 3 4 5` / `6 7 8 9 0` | `! @ # $ %` / `^ & * ( )` | 함수 호출 `()` (오른손 약지·새끼 상단) |
| **왼손 중단 3~5열** | `` ` - = `` | `~ _ +` | 스네이크 케이스 `_`, 대입/증감 `= / +` |
| **오른손 중단 6~9열** | `; [ ] \` | `: { } \|` | 코드 블록 `{}` (오른손 검지·중지 홈 로우) |
| **오른손 하단 6~9열** | `' , . /` | `" < > ?` | 문자열 `'` / `"`, 제네릭·화살표 `< >` |
| **왼손 하단 2~5열** | `← ↓ ↑ →` | `⌘← PgDn PgUp ⌘→` | 방향키 자리 그대로 줄 처음/끝·페이지 이동 |

> [!TIP]
> 상세한 코딩 단축키 연쇄 활용법은 [[coding-and-ide|코딩 및 IDE 워크플로우]] 문서를 참고하세요.

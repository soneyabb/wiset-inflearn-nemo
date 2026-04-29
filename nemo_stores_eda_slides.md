---
marp: true
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
style: |
  section {
    background-color: #F5F500;
    color: #000;
    font-family: 'Arial Black', sans-serif;
    border: 4px solid #000;
  }
  h1, h2 {
    font-family: 'Arial Black', sans-serif;
    text-transform: uppercase;
    background-color: #fff;
    border: 4px solid #000;
    box-shadow: 10px 10px 0px #000;
    padding: 20px;
    display: inline-block;
  }
  h3 {
    background-color: #CCFF00;
    border: 3px solid #000;
    box-shadow: 6px 6px 0px #000;
    padding: 10px;
  }
  img {
    border: 4px solid #000;
    box-shadow: 10px 10px 0px #000;
  }
  table {
    border-collapse: separate;
    border-spacing: 10px;
  }
  th, td {
    background-color: #fff;
    border: 3px solid #000 !important;
    box-shadow: 5px 5px 0px #000;
    padding: 10px !important;
  }
  blockquote {
    background-color: #FF2D55;
    color: #fff;
    border: 4px solid #000;
    box-shadow: 8px 8px 0px #000;
  }
  li {
    background-color: #fff;
    border: 2px solid #000;
    box-shadow: 4px 4px 0px #000;
    margin-bottom: 10px;
    padding: 5px 15px;
    list-style-type: none;
  }
  li::before {
    content: "▶ ";
    font-weight: bold;
  }
  header, footer {
    font-weight: bold;
    color: #000;
    text-shadow: 1px 1px 0px #fff;
  }
header: 'Nemo Store Insight - EDA Report'
footer: '© 2026 Nemo Store Project | soneyabb'
---

# **네모 상가 데이터 EDA 리포트**
### 심층 분석 및 비즈니스 전략 제언

2026년 4월 29일
시니어 데이터 분석가

---

## **1. 데이터 개요**

- **전체 데이터 수**: 473행
- **변수 개수**: 40개
- **주요 변수**: 보증금, 월세, 권리금, 업종 등
- **데이터 특징**: 서울 주요 핵심 상권의 매물 데이터

---

## **2. 수치형 데이터 분석 요약**

- **임대료 구조**: 보증금과 월세의 **초양극화** 현상
- **권리금**: **'무권리'** 매물이 25% 이상 차지
- **물리적 특성**: 1층 매물이 압도적 다수
- **시장 심리**: 매우 **보수적으로 탐색** 중

---

## **3. [시각화] 업종 대분류 빈도 분포**

![w:700](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_1.png)

- **음식점업 중심**: 일반/휴게음식점이 중심축 형성
- **인사이트**: 치열한 경쟁(Red Ocean) 예고

---

## **4. [시각화] 거래 형태 및 보증금 분포**

| 거래 형태 | 보증금 구간 분포 |
| :---: | :---: |
| ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_2.png) | ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_3.png) |

- **임대 위주**: 98.7%가 임대차 계약
- **경제적 문턱**: 2,000만~5,000만 원 구간 밀집

---

## **5. [시각화] 보증금-월세 상관관계**

![w:650](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_4.png)

- **상관계수 0.81**: 입지 가치가 가격에 정직하게 반영됨
- **전략**: 이상치(Outlier) 매물 발굴 필요

---

## **6. [시각화] 업종별 임대료(월세) 순위**

![w:700](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_5.png)

- **고비용 업종**: 이동통신점, 스크린골프장, 병원 등
- **생활 밀착형**: 카페, 음식점은 상대적으로 낮은 임대료

---

## **7. [시각화] 층수별 공급 및 면적-권리금**

| 건물 층수별 현황 | 면적 vs 권리금 |
| :---: | :---: |
| ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_6.png) | ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_7.png) |

- **1층 절대우위**: 접근성이 가치를 결정
- **권리금 특징**: 시설 투자 및 단골 확보가 핵심

---

## **8. [시각화] 역세권 관심도 및 매물 규모**

| 주요 역세권별 조회수 | 거래 유형별 면적 비교 |
| :---: | :---: |
| ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_8.png) | ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_9.png) |

- **골든 라인**: 양재, 역삼, 도곡역 인근 관심 집중
- **자산 규모**: 매매 매물이 임대 대비 대형 평수 위주

---

## **9. [시각화] 업종별 진입 장벽 및 키워드**

| 보증금/월세 평균 | 매물 제목 키워드 분석 |
| :---: | :---: |
| ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/graph_10.png) | ![w:350](https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/feat/marp-slides/images/text_analysis.png) |

- **진입 비용**: 판매업 및 기타업종이 높은 장벽 형성
- **3대 키워드**: **#무권리 #인테리어 #역세권**

---

## **10. 종합 비즈니스 전략 제언**

- **입지 전략**: 역세권 안전 자산 집중
- **업종 틈새**: 서비스업(미용, 교육) 기회 포착
- **권리금 활용**: '무권리' 매물 교차 검증 필수
- **마케팅 차별화**: 감성 키워드를 활용한 브랜딩

---

# **감사합니다!**
**Q&A**

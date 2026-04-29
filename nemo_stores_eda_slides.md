---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #F5F500
style: |
  /* Extreme Neo-Brutalism Style */
  section {
    background-color: #F5F500;
    color: #000;
    font-family: 'Arial Black', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 40px;
    border: 8px solid #000;
  }
  
  h1 {
    font-size: 55px;
    color: #000;
    background-color: #fff;
    border: 6px solid #000;
    box-shadow: 15px 15px 0px #000;
    padding: 20px;
    margin-bottom: 20px;
    text-transform: uppercase;
    line-height: 1.2;
  }
  
  h2 {
    font-size: 42px;
    display: inline-block;
    background-color: #CCFF00;
    border: 5px solid #000;
    box-shadow: 10px 10px 0px #000;
    padding: 10px 20px;
    margin-bottom: 20px;
    text-transform: uppercase;
  }

  h3 {
    font-size: 28px;
    background-color: #FF2D55;
    color: #fff;
    border: 4px solid #000;
    box-shadow: 8px 8px 0px #000;
    padding: 10px;
    margin-top: 0;
  }

  p, li {
    font-size: 24px;
    font-weight: 900;
    line-height: 1.3;
  }

  ul {
    list-style: none;
    padding: 0;
  }

  li {
    background-color: #fff;
    border: 4px solid #000;
    box-shadow: 6px 6px 0px #000;
    margin-bottom: 10px;
    padding: 8px 20px;
  }

  li::before {
    content: "▶ ";
    color: #FF2D55;
  }

  img {
    border: 6px solid #000;
    box-shadow: 12px 12px 0px #000;
    background-color: #fff;
    max-height: 320px;
    object-fit: contain;
  }

  table {
    border-collapse: separate;
    border-spacing: 5px;
    width: 100%;
  }

  td {
    background-color: #fff;
    border: 3px solid #000 !important;
    box-shadow: 4px 4px 0px #000;
    padding: 8px;
    font-size: 20px;
  }

  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 25px;
    align-items: center;
  }

  footer {
    font-size: 16px;
    font-weight: bold;
    color: #000;
    bottom: 15px;
  }

header: 'NEMO INSIGHT'
footer: '© 2026 soneyabb | Nemo EDA Project'
---

# **네모 상가 데이터 EDA 리포트**
### 심층 분석 및 비즈니스 전략 제언

2026. 04. 29
SENIOR ANALYST

<!-- 
[발표자 노트]
안녕하십니까. 오늘은 '네모' 플랫폼의 데이터를 통해 강남권 상가 시장의 핵심을 짚어보는 리포트를 발표하겠습니다. 
단순한 데이터 나열을 넘어, 실제 비즈니스 전략에 즉시 적용 가능한 통찰을 공유하는 데 초점을 맞추었습니다. 
-->

---

## **1. DATA OVERVIEW**

- 473개 매물 전수 분석
- 40개 핵심 경제/입지 지표
- 강남/역삼/도곡 골든라인 집중
- 사용자 반응(조회수) 데이터 결합

<!-- 
[발표자 노트]
저희는 강남 핵심 상권의 473개 매물을 전수 조사했습니다. 
보증금, 월세와 같은 가격 지표뿐만 아니라 층수, 면적, 그리고 실제 사용자의 관심도까지 결합하여 입체적인 분석을 진행했습니다. 
-->

---

## **2. PRICE INSIGHT**

- **보증금**: 평균 4,059만 (극심한 양극화)
- **월세**: 평균 296만 (우측 꼬리 분포)
- **권리금**: **무권리 매물 25%** 포착
- **결론**: 입지 가치에 따른 초양극화 뚜렷

<!-- 
[발표자 노트]
가격 지표에서 주목할 점은 '양극화'입니다. 평균치는 존재하지만, 이면 도로와 메인 대로변의 격차가 매우 큽니다. 
특히 권리금이 0원인 '무권리' 매물이 25%나 된다는 사실은 창업자들에게 기회이자 신중한 검증이 필요한 대목입니다. 
-->

---

## **3. BUSINESS DISTRIBUTION**

<div class="grid">
<div>

- **음식점(70%)** 중심 상권
- 치열한 **RED OCEAN** 상황
- **틈새 기회**: 서비스업군
- 업종 다변화 전략 필요

</div>
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_1.png" width="500"/>
</div>

<!-- 
[발표자 노트]
강남 상권은 여전히 '먹고 마시는 장사'인 음식점업이 70%를 차지합니다. 
이미 레드오션인 외식업보다는, 배후 주거 수요를 겨냥한 미용, 교육 등 서비스업이 안정적인 수익을 낼 수 있는 틈새 기회가 될 수 있습니다. 
-->

---

## **4. CONTRACT & DEPOSIT**

<div class="grid">
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_2.png" width="450"/>
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_3.png" width="450"/>
</div>

- **임대(98.7%)** 중심 유통 구조
- **현실적 진입장벽**: 2,000~5,000만
- 매매 매물은 극도로 희소

<!-- 
[발표자 노트]
현재 시장은 99%가 임대입니다. 상가 건물은 자산 가치가 높아 매매가 거의 일어나지 않습니다. 
보증금 분포를 보면 2천만 원에서 5천만 원 사이가 가장 많은데, 이것이 강남 상권 진입의 표준적인 경제적 문턱이라 볼 수 있습니다. 
-->

---

## **5. DEPOSIT VS RENT**

<div class="grid">
<div>

- **상관계수 0.81** (강한 정비례)
- 가격 구조의 높은 투명성
- **전략**: 상관관계에서 벗어난
  '이상치(Outlier)' 매물 공략

</div>
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_4.png" width="550"/>
</div>

<!-- 
[발표자 노트]
보증금과 월세는 0.81이라는 매우 높은 상관관계를 보입니다. 
입지 가치가 가격에 정직하게 반영되어 있다는 뜻입니다. 
우리는 여기서 '가격 거품'이 아닌, 입지 대비 저평가된 '이상치' 매물을 찾는 데 집중해야 합니다. 
-->

---

## **6. RENT RANKING**

<div class="grid">
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_5.png" width="550"/>
<div>

- **고임대료**: 통신점/스크린골프
- 단위 면적당 매출 극대화 필수
- **카페/일반음식점**: 
  이면도로 진출로 고정비 절감

</div>
</div>

<!-- 
[발표자 노트]
가장 비싼 월세를 내는 업종은 가시성이 중요한 통신점과 넓은 면적을 쓰는 스크린골프장입니다. 
반면 카페나 일반 식당은 임대료 부담을 줄이기 위해 메인 로드에서 한 블록 안쪽으로 들어가는 실용적 전략을 취하고 있습니다. 
-->

---

## **7. FLOOR & SIZE**

<div class="grid">
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_6.png" width="450"/>
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_7.png" width="450"/>
</div>

- **1층(50%)** 접근성 절대 우위
- **권리금**: 면적과 비례하지 않음
- 시설 투자 및 단골 확보가 핵심

<!-- 
[발표자 노트]
역시 1층 매물이 절반 이상입니다. 워킹 손님이 매출의 핵심이기 때문입니다. 
특이한 점은 면적이 크다고 권리금이 비싸지 않다는 것입니다. 
권리금은 공간의 크기가 아니라 '얼마나 돈을 벌 수 있는 시설과 고객이 있느냐'에 달려 있습니다. 
-->

---

## **8. HOT STATION**

<div class="grid">
<div>

- **양재/역삼/도곡** 조회수 집중
- **1분 거리**가 조회수 지수적 차이
- 검증된 유동인구 확보가 생존키

</div>
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/graph_8.png" width="550"/>
</div>

<!-- 
[발표자 노트]
사용자들의 관심은 지하철역 인근 도보 5분 내 매물에 폭발적으로 집중됩니다. 
조회수는 잠재적 고객의 유입 가능성을 보여주는 선행 지표입니다. 
조금 더 비싸더라도 역세권을 잡아야 하는 이유를 데이터가 증명합니다. 
-->

---

## **9. KEYWORD ANALYSIS**

<div class="grid">
<img src="https://raw.githubusercontent.com/soneyabb/wiset-inflearn-nemo/main/images/text_analysis.png" width="550"/>
<div>

- 핵심: **#무권리 #역세권 #시설**
- 마케팅: **#감성 #브랜딩** 강조
- 단순 가격보다 '공간 경험' 
  제시가 클릭률 유도

</div>
</div>

<!-- 
[발표자 노트]
매물 제목 키워드 분석 결과, 예비 창업자들은 비용 절감만큼이나 '공간의 퀄리티'에 민감합니다. 
'무권리'라는 경제적 혜택과 '화이트톤, 채광' 같은 감성 키워드를 적절히 조합한 마케팅이 실제 계약 성사율을 높입니다. 
-->

---

## **10. FINAL STRATEGY**

- **입지**: 역세권 안전 자산 집중
- **업종**: 레드오션보다 틈새 서비스업
- **비용**: 무권리 매물의 정교한 검증
- **브랜딩**: 데이터 기반의 타겟 마케팅

<!-- 
[발표자 노트]
결론입니다. 강남 상권은 높은 비용에도 불구하고 회복 탄력성이 가장 좋습니다. 
역세권이라는 안전 자산을 기반으로 하되, 틈새 업종을 공략하고 데이터로 검증된 마케팅을 펼치는 것이 성공의 핵심 전략입니다. 
-->

---

# **THANK YOU!**
**DATA-DRIVEN SUCCESS**

<!-- 
[발표자 노트]
데이터는 거짓말을 하지 않습니다. 보증금, 월세, 권리금의 최적 균형점을 찾아 성공적인 비즈니스를 이루시길 바랍니다. 
이상 발표를 마치겠습니다. 질문 있으시면 부탁드립니다. 감사합니다. 
-->

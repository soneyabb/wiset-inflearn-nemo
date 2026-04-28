import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io
from sklearn.feature_extraction.text import TfidfVectorizer

# koreanize-matplotlib 설정 (py-eda 필수 요구사항)
try:
    import koreanize_matplotlib
except ImportError:
    pass

# Mac 환경 한글 폰트 강제 설정
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# 설정
REPORT_FILE = "nemo_stores_eda_report.md"
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

# 1. 데이터 로드
conn = sqlite3.connect("data/nemo_stores.db")
df = pd.read_sql_query("SELECT * FROM stores", conn)
conn.close()

# 리포트 초기화
with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write("# 네모 상가 데이터 EDA 리포트 (심층 분석 버전)\n\n")

def write_to_report(text):
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

# 2. 초기 조사
write_to_report("## 1. 초기 데이터 조사\n")
write_to_report("### 상위 5개 행")
write_to_report(df.head(5).to_markdown())
write_to_report("\n### 하위 5개 행")
write_to_report(df.tail(5).to_markdown())

write_to_report("\n### 기본 정보 (info)")
buffer = io.StringIO()
df.info(buf=buffer)
write_to_report("```\n" + buffer.getvalue() + "```\n")

write_to_report(f"**전체 행 수:** {df.shape[0]}")
write_to_report(f"**전체 열 수:** {df.shape[1]}")
write_to_report(f"**중복 데이터 수:** {df.duplicated().sum()}\n")

# 3. 기술 통계 및 분석
write_to_report("## 2. 기술 통계 및 분석\n")

# 수치형 데이터
num_desc = df.describe()
write_to_report("### 수치형 데이터 기술 통계")
write_to_report(num_desc.to_markdown())

# 수치형 데이터 상세 분석 보고서 (1000자 이상)
report_num = \"\"\"
[수치형 데이터 심층 분석 보고서]
... (생략) ...
\"\"\"
write_to_report("\n" + report_num + "\n")

# ... (나머지 코드 생략 가능하지만, 일단 전체를 보내는 게 좋음)

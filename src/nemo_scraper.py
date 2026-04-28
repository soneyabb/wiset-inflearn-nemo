import httpx
import pandas as pd
import sqlite3
import os
import traceback
import json
import time

def fetch_nemo_page(page_index):
    url = "https://www.nemoapp.kr/api/store/search-list"
    params = {
        "CompletedOnly": "false",
        "NELat": "37.49495553608796",
        "NELng": "127.06097381924975",
        "SWLat": "37.46948600346246",
        "SWLng": "127.03346091597922",
        "Zoom": "15",
        "SortBy": "29",
        "PageIndex": str(page_index)
    }
    
    headers = {
        "referer": "https://www.nemoapp.kr/store",
        "sec-ch-ua": '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    }

    print(f"Fetching page {page_index}...")
    with httpx.Client() as client:
        response = client.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

def scrape_all_data():
    all_items = []
    page_index = 0
    
    while True:
        try:
            data = fetch_nemo_page(page_index)
            items = data.get("items", [])
            
            if not items:
                print(f"No more items at page {page_index}. Stopping.")
                break
            
            print(f"Collected {len(items)} items from page {page_index}.")
            all_items.extend(items)
            
            page_index += 1
            # 서버 부하 방지를 위한 짧은 휴식
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error at page {page_index}: {e}")
            break
            
    return all_items

def save_to_sqlite(items, db_path):
    if not items:
        print("No items to save.")
        return

    # 중첩된 딕셔너리나 리스트를 문자열로 변환 (SQLite 호환성)
    processed_items = []
    for item in items:
        new_item = {}
        for k, v in item.items():
            if isinstance(v, (dict, list)):
                new_item[k] = json.dumps(v, ensure_ascii=False)
            else:
                new_item[k] = v
        processed_items.append(new_item)
        
    df = pd.DataFrame(processed_items)
    
    # 데이터 폴더 확인
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    print(f"Saving total {len(processed_items)} items to {db_path}...")
    conn = sqlite3.connect(db_path)
    df.to_sql("stores", conn, if_exists="replace", index=False)
    conn.close()
    print("Save complete.")

if __name__ == "__main__":
    db_path = "data/nemo_stores.db"
    try:
        all_items = scrape_all_data()
        save_to_sqlite(all_items, db_path)
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()

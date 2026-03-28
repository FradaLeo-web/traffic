import os
import shutil
import re

KB_BASE = r"D:\AILaw\法律Agents\lawyer-office-assistant\knowledge-base"
CASES_DIR = os.path.join(KB_BASE, "cases")

CASE_CATEGORIES = {
    "职务侵占": ["职务侵占"],
    "挪用资金": ["挪用资金"],
    "贪污受贿": ["贪污", "受贿", "行贿"],
    "非法集资": ["非法吸收", "集资诈骗", "P2P", "非法集资"],
    "其他刑事": ["诈骗", "盗窃", "抢劫", "杀人", "黑社会", "组织、领导", "走私", "毒品", "卖淫", "赌博", "虚报注册资本", "假冒注册商标", "洗钱", "掩饰、隐瞒", "诬告陷害", "妨碍公务", "非法拘禁", "敲诈勒索"],
    "国家赔偿": ["国家赔偿"],
    "破产清算": ["破产", "清算"],
    "知识产权": ["知识产权", "专利", "商标", "商业秘密"],
    "行政诉讼": ["行政判决", "行政赔偿", "行政复议", "行政协议"],
    "证券期货": ["证券", "期货", "操纵市场"],
}

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_category(filename):
    for cat_name, keywords in CASE_CATEGORIES.items():
        for keyword in keywords:
            if keyword in filename:
                return cat_name
    return None

def main():
    files = [f for f in os.listdir(CASES_DIR) if f.endswith('.md')]
    
    print(f"Found {len(files)} files to categorize")
    
    categorized = {}
    uncategorized = []
    
    for filename in files:
        cat = get_category(filename)
        if cat:
            if cat not in categorized:
                categorized[cat] = []
            categorized[cat].append(filename)
        else:
            uncategorized.append(filename)
    
    total_moved = 0
    
    for cat_name, files_list in categorized.items():
        target_dir = os.path.join(CASES_DIR, "刑事案例", cat_name)
        ensure_dir(target_dir)
        
        print(f"\n=== {cat_name}: {len(files_list)} files ===")
        
        for filename in files_list:
            src_path = os.path.join(CASES_DIR, filename)
            dest_path = os.path.join(target_dir, filename)
            
            if os.path.exists(dest_path):
                print(f"  Skip (exists): {filename}")
                continue
            
            shutil.move(src_path, dest_path)
            print(f"  Moved: {filename}")
            total_moved += 1
    
    print(f"\n=== Uncategorized: {len(uncategorized)} files ===")
    for f in uncategorized[:10]:
        print(f"  {f}")
    if len(uncategorized) > 10:
        print(f"  ... and {len(uncategorized) - 10} more")
    
    print(f"\n=== Total: {total_moved} files moved ===")

if __name__ == "__main__":
    main()

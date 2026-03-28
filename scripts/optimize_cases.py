import os
import shutil

KB_BASE = r"D:\AILaw\法律Agents\lawyer-office-assistant\knowledge-base"

MOVE_MAP = {
    os.path.join(KB_BASE, "cases", "职务侵占"): os.path.join(KB_BASE, "cases", "刑事案例", "职务侵占"),
    os.path.join(KB_BASE, "cases", "挪用资金"): os.path.join(KB_BASE, "cases", "刑事案例", "挪用资金"),
    os.path.join(KB_BASE, "cases", "贪污受贿"): os.path.join(KB_BASE, "cases", "刑事案例", "贪污受贿"),
    os.path.join(KB_BASE, "cases", "非法集资"): os.path.join(KB_BASE, "cases", "刑事案例", "非法集资"),
    os.path.join(KB_BASE, "cases", "其他刑事"): os.path.join(KB_BASE, "cases", "刑事案例", "其他刑事"),
}

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_files(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"Source directory does not exist: {src_dir}")
        return 0
    
    ensure_dir(dest_dir)
    
    files = [f for f in os.listdir(src_dir) if f.endswith('.md')]
    count = 0
    
    for filename in files:
        src_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        
        if os.path.exists(dest_path):
            print(f"Skip (exists): {filename}")
            continue
        
        shutil.move(src_path, dest_path)
        print(f"Moved: {filename}")
        count += 1
    
    return count

def main():
    total_moved = 0
    
    for src_dir, dest_dir in MOVE_MAP.items():
        print(f"\n=== Moving from {os.path.basename(src_dir)} to {os.path.basename(dest_dir)} ===")
        count = move_files(src_dir, dest_dir)
        total_moved += count
        print(f"Moved {count} files")
    
    print(f"\n=== Total: {total_moved} files moved ===")

if __name__ == "__main__":
    main()

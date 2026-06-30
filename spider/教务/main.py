import json
import sys
import time
import random
import urllib3
urllib3.disable_warnings()

from login import JWGLSpider
from scrape_courses import scrape_courses
from scrape_grades import scrape_grades, scrape_all_semesters
from utils import DATA_DIR


def load_config():
    """从 config.json 加载配置"""
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def main():
    config = load_config()

    print("=" * 60)
    print(" 教务系统数据爬虫 v1.0")
    print(" QZDatasoft / ZFSoft 教务系统")
    print("=" * 60)
    print()

    # === 登录 (config 由 login 模块内部加载) ===
    spider = JWGLSpider()

    if not spider.login():
        print("[FAIL] Login failed. Exiting.")
        return

    print("\n" + "=" * 60)
    print("  STEP 1: 爬取课程信息")
    print("=" * 60)

    courses = scrape_courses(spider)

    print("\n" + "=" * 60)
    print("  STEP 2: 爬取成绩信息")
    print("=" * 60)

    semesters = config.get("semesters", ["2025-2026-1"])
    all_grades = []

    if "--all-semesters" in sys.argv:
        all_grades = scrape_all_semesters(spider)
    else:
        for sem in semesters:
            grades = scrape_grades(spider, semester=sem)
            all_grades.extend(grades)
            if sem != semesters[-1]:
                time.sleep(random.uniform(1, 2))

    # === 汇总 ===
    print("\n" + "=" * 60)
    print("  爬取完成！")
    print("=" * 60)
    print(f"  课程数量: {len(courses)}")
    print(f"  成绩数量: {len(all_grades)}")
    print(f"  数据目录: {DATA_DIR}")
    print()

    # 列出生成的文件
    import os
    for f in sorted(os.listdir(DATA_DIR)):
        fpath = DATA_DIR / f
        size_kb = fpath.stat().st_size / 1024
        print(f"    {f} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()

from python_graphql_client import GraphqlClient
import feedparser
import httpx
import json
import pathlib
import re
import os
import datetime
import logging
import pendulum

root = pathlib.Path(__file__).parent.resolve()
client = GraphqlClient(endpoint="https://api.github.com/graphql")

TOKEN = os.environ.get("GH_TOKEN", "")

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

def formatGMTime(timestamp):
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    dateStr = datetime.datetime.strptime(timestamp, GMT_FORMAT) + datetime.timedelta(hours=8)
    return dateStr.date()
    
def fetch_code_time():
    return httpx.get(
        "https://gist.github.com/donniesky/f1cb72d6b3792a01b11ad06820022053/raw/"
    )

def get_year_progress(dt):
    year_days = 366 if dt.is_leap_year() else 365
    passed_days = dt.timetuple().tm_yday
    percent = round(((passed_days / year_days) * 100), 2)
    return percent

def get_month_progress(dt):
    days_since_start_of_month = dt.day - 1
    percent = round(((days_since_start_of_month / dt.days_in_month) * 100), 2)
    return percent

def get_day_progress(dt):
    percent = round(((dt.hour / 24) * 100), 2)
    return percent

def make_progress_string(percent):
    blocks = 16
    percent = percent * blocks / 100
    return ''.join(["█" if i < percent else "▁" for i in range(blocks)])

if __name__ == "__main__":
    readme = root / "README.md"
    
    readme_contents = readme.open().read()
    
    dt = pendulum.now()

    year_percents = get_year_progress(dt)
    year_progress = make_progress_string(year_percents)
    
    year_progress_text = "\n```text\n⏳ Year progress "+year_progress+" "+year_percents.text+"%\n```\n"
    logging.info(code_time_text)

    rewritten = replace_chunk(readme_contents, "year_progress", year_progress_text)
    
    code_time_text = "\n```text\n"+fetch_code_time().text+"\n```\n"
    logging.info(code_time_text)

    rewritten = replace_chunk(rewritten, "code_time", code_time_text)
    logging.info(rewritten)

    readme.open("w").write(rewritten)

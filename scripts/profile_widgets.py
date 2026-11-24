"""Render repository-hosted profile cards from GitHub API measurements."""
from datetime import date
from pathlib import Path
import json
import subprocess

from PIL import Image, ImageDraw, ImageFont

OWNER = "toeeshchaudhary"
OUT = Path("assets/profile")
BG, FG, MUTED = "#121922", "#f1f5f9", "#a5b6c7"
ACCENTS = ["#71dbc1", "#86b9ff", "#f8bf78", "#bfabfb", "#ff99ab"]


def api(*args):
    return json.loads(subprocess.check_output(["gh", "api", *args]))


def font(size):
    for face in ("DejaVuSans.ttf", "segoeui.ttf"):
        try:
            return ImageFont.truetype(face, size)
        except OSError:
            continue
    raise RuntimeError("Install DejaVu Sans or Segoe UI")


def card(height):
    image = Image.new("RGB", (864, height), BG)
    return image, ImageDraw.Draw(image)


def label(draw, x, y, value, size=20, color=FG):
    draw.text((x, y), str(value), font=font(size), fill=color)


query = """query {user(login:"toeeshchaudhary"){
 contributionsCollection{contributionCalendar{weeks{contributionDays{
 date weekday contributionCount}}}}}}"""
weeks = api("graphql", "-f", "query=" + query)["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"][-26:]
days = [day for week in weeks for day in week["contributionDays"]]
image, d = card(290)
label(d, 26, 15, "Contribution activity", 32)
label(d, 27, 61, f"{sum(day['contributionCount'] for day in days):,} contributions   /   {sum(day['contributionCount'] > 0 for day in days)} active days", 22, ACCENTS[0])
month = None
for x, week in enumerate(weeks):
    first = date.fromisoformat(week["contributionDays"][0]["date"])
    if first.month != month and x < 25:
        label(d, 76 + x*29, 101, first.strftime("%b"), 16, MUTED)
    month = first.month
    for day in week["contributionDays"]:
        col = sum(day["contributionCount"] >= n for n in (1, 3, 6, 12))
        a, b = 76 + x*29, 130 + day["weekday"]*18
        d.rounded_rectangle((a,b,a+24,b+14), 3, fill=["#2b3541","#205b50","#318772","#47b797",ACCENTS[0]][col])
for row, name in [(1,"Mon"),(3,"Wed"),(5,"Fri")]:
    label(d, 26, 126+row*18, name, 15, MUTED)
label(d, 27, 261, days[0]["date"]+"   —   "+days[-1]["date"], 15, MUTED)
image.save(OUT/"github-contribution-activity.png")

repos = api("users/"+OWNER+"/repos?type=owner&per_page=100&sort=pushed")
recent = [r for r in repos if not r["fork"] and not r["archived"] and r["name"] != OWNER][:4]
image, d = card(110 + len(recent)*54)
label(d, 26, 16, "Recently pushed", 32)
label(d, 27, 65, "Public repositories", 18, MUTED)
for i, repo in enumerate(recent):
    y = 105 + i*54
    d.line((26,y,838,y), fill="#354150")
    d.ellipse((29,y+23,39,y+33),fill=ACCENTS[i])
    label(d, 56, y+10, repo["name"], 24)
    label(d, 472, y+12, repo["language"] or "—", 20, ACCENTS[i])
    label(d, 681, y+12, repo["pushed_at"][:10], 20, MUTED)
image.save(OUT/"recent-projects.png")

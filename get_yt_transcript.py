import urllib.request
import json
import re
import html as html_module

url = "https://www.youtube.com/watch?v=SBLDc4R1d_E"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"})

try:
    html_text = urllib.request.urlopen(req).read().decode("utf-8")
    tt_urls = re.findall(r'https://www\.youtube\.com/api/timedtext\?[^\s"\'<>]+', html_text)
    if tt_urls:
        u = tt_urls[0].replace('\\u0026', '&')
        sub_xml = urllib.request.urlopen(u).read().decode("utf-8")
        text_lines = re.findall(r'<text[^>]*>(.*?)</text>', sub_xml)
        clean_text = " ".join([html_module.unescape(t) for t in text_lines])
        print("Transcript Length:", len(clean_text))
        with open("transcript_graph_eng.txt", "w", encoding="utf-8") as f:
            f.write(clean_text)
        print("Saved to transcript_graph_eng.txt")
        print("--- FIRST 1500 CHARS ---")
        print(clean_text[:1500])
    else:
        print("No timedtext URL found in HTML")
except Exception as e:
    print("Error:", e)

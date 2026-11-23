import asyncio, json, os
import edge_tts

LIST = r"C:\Users\ASuS\Downloads\tts_list.json"
OUT  = r"F:\NihonPuss\NihonPluss\voice\tts"
VOICE = "ja-JP-NanamiNeural"   # ลอง ja-JP-KeitaNeural (เสียงผู้ชาย) ได้
os.makedirs(OUT, exist_ok=True)

async def main():
    items = json.load(open(LIST, encoding="utf-8"))
    for it in items:
        path = os.path.join(OUT, it["id"] + ".mp3")
        if os.path.exists(path):
            continue
        t = it["t"]
        text = t + "、" if len(t) == 1 else t   # ตัวอักษรเดี่ยวจะได้ไม่ห้วน
        await edge_tts.Communicate(text, VOICE, rate="-15%").save(path)
        print("ok", t)

asyncio.run(main())
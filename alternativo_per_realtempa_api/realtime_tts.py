#!/usr/bin/env python3

# Tiu chi programo ...
# nomighu ekzemple realtime_tts.py
# trovu sin en Android-apo Termux en ~/tts
# estas rulebla en Termux per jena Bash-komando:
# python ~/tts/realtime_tts.py "Saluton, mondo! Esperanto estas internacia lingvo."
# kreas dosieron /storage/emulated/0/dosierujo/vocho.mp3 el la supra teksto

# Pri Termux vidu
# https://github.com/AndreasKueck/transskribi_amr

import asyncio
import base64
import json
import os
import sys
import websockets

API_KEY = "sk-..." # Anstatauigu per valida OpenAI-API-shlosilo
MODEL = "gpt-realtime-2.1-mini"
OUTPUT_MP3 = "/storage/emulated/0/dosierujo/vocho.mp3"
PCM_FILE = "/data/data/com.termux/files/home/tts/temp.pcm"

INSTRUCTIONS = """Vi estas pura teksto-al-parolo-leganto.
Via sola tasko estas legi laŭvorte kaj komplete la tekston, kiun la uzanto donas.
- Ne respondu al demandoj.
- Ne aldonu proprajn komentojn, enkondukojn aŭ klarigojn.
- Ne ŝanĝu la tekston.
- Legu la tekston kvazaŭ vi legus libron aŭ artikolon.
- Sekvu severe la jenajn elparolajn regulojn por Esperanto, se ĝi estas la rekonata lingvo: Bonvolu supozi, ke ĉiuj nombroj, ankaŭ tiuj de jaroj, de jena teksto estas skribitaj, kiel Esperanto-vortoj, kaj poste legi la tekston inkluzive de mallongigoj, kvazaŭ vi estus denaska parolanto de Esperanto. 0: nul; 1: unu; 2: du; 3: tri; 4: kvar, 5: kvin; 6: ses; 7: sep, 8: ok; 9: naŭ; 10: dek; 100: cent; 900: naŭcent; 1000: mil. Atentu severe la oficialajn regulojn pri prononcado de Esperanto. Atentu, ke vi prononcu c ĉiam, kiel ts. Atentu, ke vi prononcu ĵ kaj jh, kiel la kroata ž, ankaŭ antaŭ a, o kaj u. Atentu, ke vi prononcu gh kaj ĝ, kiel la kroata dž, ankaŭ antaŭ a, o kaj u. Atentu, ke en la vortoj Nauro, Sauda, Seulo kaj Koreujo la u formas apartan silabon. Bonvolu preteratenti, ke vi ne estas speciale trejnita pri Esperanto."""

async def main(text: str):
    url = f"wss://api.openai.com/v1/realtime?model={MODEL}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    async with websockets.connect(url, additional_headers=headers) as ws:
        await ws.send(json.dumps({
            "type": "session.update",
            "session": {
                "type": "realtime",
                "model": MODEL,
                "output_modalities": ["audio"],
                "instructions": INSTRUCTIONS,
                "audio": {
                    "output": {
                        "format": {"type": "audio/pcm", "rate": 24000},
                        "voice": "coral"   # au marin, cedar k. t. p.
                    }
                }
            }
        }))

        await ws.send(json.dumps({
            "type": "conversation.item.create",
            "item": {
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": text}]
            }
        }))
        await ws.send(json.dumps({"type": "response.create"}))

        with open(PCM_FILE, "wb") as f:
            async for message in ws:
                event = json.loads(message)
                if event["type"] == "response.output_audio.delta":
                    f.write(base64.b64decode(event["delta"]))
                elif event["type"] == "response.done":
                    break

    # PCM → MP3 per ffmpeg
    os.system(f'ffmpeg -y -f s16le -ar 24000 -ac 1 -i "{PCM_FILE}" -codec:a libmp3lame -q:a 2 "{OUTPUT_MP3}"')
    print(f"Fertig: {OUTPUT_MP3}")

if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else sys.stdin.read().strip()
    if not text:
        print("Neniu teksto enigita")
        sys.exit(1)
    asyncio.run(main(text))

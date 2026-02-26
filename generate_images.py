#!/usr/bin/env python3
"""Generate Satantango chapter images using Gemini Nano Banana (2.5 Flash Image)."""

import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
MODEL = "gemini-2.5-flash-image"

OUTPUT_DIR = Path("images")
OUTPUT_DIR.mkdir(exist_ok=True)

CHAPTERS = [
    {
        "filename": "ch01-news-of-their-coming.png",
        "title": "Chapter I: News of Their Coming",
        "prompt": (
            "A gritty, cinematic shot of two impoverished middle-aged men in a dark, "
            "decaying, mold-infested kitchen at dawn. One man, lame and leaning on a "
            "walking stick, looks out a tiny, cracked, misted-up window with an expression "
            "of terror. The other man, stocky and unshaven, stands defensively near a rusty, "
            "iron-strapped military trunk. The walls are peeling, the floor is cold stone, "
            "and the room is filled with deep shadows and a sense of entrapment. Outside the "
            "window, a merciless, relentless autumn rain falls on a desolate, muddy Eastern "
            "European estate. Muted color palette of greys, browns, and sickly greens, high "
            "contrast, atmospheric, no text."
        ),
    },
    {
        "filename": "ch02-we-are-resurrected.png",
        "title": "Chapter II: We Are Resurrected",
        "prompt": (
            "A wide, bleak landscape shot of two vagabond men walking down a completely "
            "desolate, mud-slicked highway at dusk during a heavy rainstorm. The taller man "
            "strides confidently, wearing a houndstooth-check jacket, a glaring red tie, and "
            "pointed yellow shoes covered in mud. The shorter man trails behind, hunched "
            "against the wind, wearing an oversized, ragged winter coat, looking miserable. "
            "They are surrounded by bare, wind-whipped trees and a flat, marshy landscape "
            "fading into a dark, oppressive sky. Cinematic lighting, muddy and bleak "
            "aesthetic, highly detailed, no text."
        ),
    },
    {
        "filename": "ch03-to-know-something.png",
        "title": "Chapter III: To Know Something",
        "prompt": (
            "An atmospheric, dimly lit interior portrait of a massively obese, unkempt "
            "doctor sitting in a heavily blanketed armchair in a filthy, debris-strewn room. "
            "He is wearing a fur-collared winter coat indoors, sweating profusely, and "
            "staring intensely out a gap in dirty floral curtains. Beside him on a small "
            "wobbly table are a half-empty glass of clear liquor, a pencil, and an open "
            "notebook. A small mountain of empty glass demijohns and tin cans surrounds his "
            "chair. The room smells of rot and isolation, illuminated only by the faint, cold "
            "grey light of a rainy dawn. Chiaroscuro lighting, hyper-realistic, bleak vibe, "
            "no text."
        ),
    },
    {
        "filename": "ch04-work-of-the-spider-I.png",
        "title": "Chapter IV: The Work of the Spider I",
        "prompt": (
            "A claustrophobic, gloomy scene inside a crumbling, smoke-filled Eastern "
            "European tavern. In the foreground, a giant, terrifyingly muscular farmer with "
            "a shaven, scarred head is passed out, snoring on top of a green baize billiard "
            "table. In the background, a sly, pot-bellied landlord stands behind a "
            "tin-topped counter lined with cheap wine glasses, beneath a solitary, swaying "
            "lamp. The corners of the room are draped in thick, ancient spiderwebs. Rain "
            "beats against the dirty windows. Muted sepia and olive tones, gritty realism, "
            "deep shadows, no text."
        ),
    },
    {
        "filename": "ch05-unraveling.png",
        "title": "Chapter V: Unraveling",
        "prompt": (
            "A haunting, poignant image of a pale, straw-blonde young girl walking alone "
            "through an ankle-deep muddy path at night in a torrential downpour. She is "
            "wearing an oversized, soaking-wet yellow cardigan that hangs down to her knees "
            "and heavy boots. In her arms, she tightly clutches the stiff, lifeless body of "
            "a wet black cat. She is walking toward the dark, looming, overgrown ruins of an "
            "abandoned manor house in the distance. The scene is illuminated by faint, "
            "ghostly moonlight breaking through heavy clouds. Melancholic, heartbreaking, "
            "gothic atmosphere, highly detailed, no text."
        ),
    },
    {
        "filename": "ch06-work-of-the-spider-II.png",
        "title": "Chapter VI: The Work of the Spider II (The Devil's Tit, Satantango)",
        "prompt": (
            "A surreal, nightmarish scene inside a decaying tavern at dawn. Several "
            "impoverished, ragged people are slumped over tables and chairs, fast asleep and "
            "exhausted. A faint, intricate network of delicate, glowing spiderwebs covers "
            "the sleeping figures, the wine glasses, and the furniture, tying them all "
            "together in a ghostly cocoon. In the open doorway stands a tall, sharp-featured "
            "man in a seal-grey raincoat and a hat pulled low, a cigarette dangling from his "
            "lips, glaring coldly at the sleeping room. Cinematic, eerie lighting, high "
            "contrast, gritty, no text."
        ),
    },
    {
        "filename": "ch07-irimias-makes-a-speech.png",
        "title": "Chapter VII: Irimiás Makes a Speech",
        "prompt": (
            "An intense, dramatic interior shot of a tall, charismatic man with high "
            "cheekbones and a sharp nose standing in the center of a smoky tavern, delivering "
            "a passionate speech. He has one finger raised authoritatively. Surrounding him "
            "in a tight circle are a group of ragged, exhausted peasants with tear-streaked, "
            "deeply moved faces, looking up at him with desperate hope. On the wooden table "
            "in front of the speaker sits a large, messy pile of crumpled banknotes. Heavy "
            "chiaroscuro lighting emphasizing the speaker's face, psychological intensity, "
            "gritty realism, no text."
        ),
    },
    {
        "filename": "ch08-perspective-from-front.png",
        "title": "Chapter VIII: The Perspective, as Seen from the Front",
        "prompt": (
            "An action-shot from the back of a speeding, rusty, open-bed military truck "
            "driving down a desolate, rain-swept country road. The back of the truck is "
            "crammed with a pile of cheap, battered suitcases, sacks, and several "
            "weather-beaten, impoverished people huddled together. They have their hoods and "
            "hats pulled tight against the driving rain and wind, but their faces are "
            "animated with wild, desperate joy. They are looking back at the dark, decaying "
            "ruins of a rural estate fading away in the foggy distance. Dynamic composition, "
            "cinematic, bleak but triumphant mood, muted colors, no text."
        ),
    },
    {
        "filename": "ch09-heavenly-vision.png",
        "title": "Chapter IX: Heavenly Vision? Hallucination?",
        "prompt": (
            "A deeply eerie, surreal scene in a dark, weed-choked manor park under heavy "
            "rain. Three men hide terrified behind a thick bush in the foreground, peering "
            "out. In the clearing ahead of them, framed by three massive, dead oak trees, "
            "the body of a small blonde girl in a white dress is levitating six feet in the "
            "air, wrapped in billowing, translucent white veils that glow with an unnatural, "
            "blinding inner light. The atmosphere is completely silent and dreamlike, blending "
            "horror with mystical awe. Foggy, dark, high contrast, cinematic, no text."
        ),
    },
    {
        "filename": "ch10-perspective-from-back.png",
        "title": "Chapter X: The Perspective, as Seen from the Back",
        "prompt": (
            "A bleak, depressing morning scene inside the roofless, ruined hall of an "
            "abandoned manor house. The floor is covered in shattered tiles, rotting wood, "
            "and thick ivy. A group of impoverished people sit miserably on their cheap "
            "suitcases and bundles, shivering in the cold draft, looking utterly defeated "
            "and betrayed. One man in the foreground has a bloody, swollen nose and is "
            "holding a wet rag to his face. The grey light of dawn spills through large, "
            "empty window frames. Utter despair, desolate atmosphere, highly detailed "
            "textures of decay, no text."
        ),
    },
    {
        "filename": "ch11-nothing-but-work-and-worries.png",
        "title": "Chapter XI: Nothing but Work and Worries",
        "prompt": (
            "An interior shot of a dreary, claustrophobic, neon-lit bureaucratic office. Two "
            "tired, middle-aged clerks with receding hairlines sit across from each other at "
            "a heavy wooden desk piled high with towering stacks of files and dossiers. One "
            "is slumped in front of a heavy manual typewriter; the other is holding a piece "
            "of crumpled paper covered in chaotic, scratchy handwriting, looking deeply "
            "exasperated. The room feels lifeless, stale, and completely divorced from the "
            "outside world. Muted greys and sickly fluorescent greens, drab 1980s aesthetic, "
            "realistic, no text."
        ),
    },
    {
        "filename": "ch12-the-circle-closes.png",
        "title": "Chapter XII: The Circle Closes",
        "prompt": (
            "A psychological, intense portrait of an obese, sweating man in a dark, filthy "
            "room, illuminated only by a harsh, bare lightbulb hanging from the ceiling. He "
            "is hunched over a rickety table, writing feverishly in a notebook with a stubby "
            "pencil. The room's wooden door in the background is heavily barricaded with "
            "fresh nails. The man looks possessed, as if he is dictating reality itself. "
            "Piles of empty glass jugs surround his chair. Outside the window, a sliver of "
            "dark, rainy sky is visible. Oppressive, claustrophobic, masterpiece, high "
            "contrast lighting, no text."
        ),
    },
]


def generate_image(chapter):
    """Generate a single chapter image."""
    print(f"\n{'='*60}")
    print(f"Generating: {chapter['title']}")
    print(f"{'='*60}")

    response = client.models.generate_content(
        model=MODEL,
        contents=[chapter["prompt"]],
        config={
            "response_modalities": ["IMAGE", "TEXT"],
        },
    )

    output_path = OUTPUT_DIR / chapter["filename"]

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(f"  Model note: {part.text[:200]}")
        elif part.inline_data is not None:
            image_data = part.inline_data.data
            with open(output_path, "wb") as f:
                f.write(image_data)
            print(f"  Saved: {output_path}")
            return True

    print(f"  WARNING: No image generated for {chapter['title']}")
    return False


def main():
    print("Satantango Chapter Image Generator")
    print(f"Model: {MODEL}")
    print(f"Output: {OUTPUT_DIR}/")
    print(f"Chapters: {len(CHAPTERS)}")

    successes = 0
    failures = []

    for i, chapter in enumerate(CHAPTERS):
        try:
            if generate_image(chapter):
                successes += 1
            else:
                failures.append(chapter["title"])
        except Exception as e:
            print(f"  ERROR: {e}")
            failures.append(chapter["title"])

        # Small delay between requests to avoid rate limiting
        if i < len(CHAPTERS) - 1:
            time.sleep(2)

    print(f"\n{'='*60}")
    print(f"DONE: {successes}/{len(CHAPTERS)} images generated")
    if failures:
        print(f"Failed: {', '.join(failures)}")
    print(f"Images saved in: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()

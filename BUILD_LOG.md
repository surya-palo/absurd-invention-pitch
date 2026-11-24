# Build log — Absurd Invention Pitch

## The entry

> A doormat that interrogates every visitor and only unlocks the door for anyone who can pronounce your Wi-Fi password correctly on the first try, so you never have to pretend you are not home again.

197 characters (limit: 220). One sentence.

## Why it fits the judge brief

- **On brief:** a ridiculous invention (a doormat that conducts job
  interviews) fixing a tiny everyday annoyance (unwanted visitors at the
  door / having to answer it).
- **Funny from the invention itself:** the laugh is the doormat acting as a
  bouncer-interviewer, not a joke bolted on at the end.
- **Clever fix:** the password test is a silly yet weirdly plausible filter —
  only people you actually gave the Wi-Fi password to, who bothered to learn
  it, get in.
- **Original:** not one of the kit's examples (alarm clock, complaining sock,
  sighing kettle); the doormat-as-gatekeeper with a Wi-Fi pronunciation test
  is a fresh absurdity.
- **Tight:** one clean sentence naming the annoyance, the invention and its
  mechanism, no clutter.

## Verification (v1)

- `python3 main.py` run twice; `sha256sum /output/entry.txt` identical both
  runs (deterministic).
- Character count 141, within the 1–220 limit (validated inside main.py).
- `/output` contains only `entry.txt`, mode 0644.

## Revision (v2)

Second pass: sharpened the punchline — the doormat now "interrogates"
instead of "interviews", and the payoff names the real annoyance directly:
never having to pretend you aren't home. The Wi-Fi password test also
tightened from "those who can" to "anyone who can", and the sentence now
lands on the universal dodge of pretending not to be home, which is the
actual tiny annoyance the invention kills.

## Verification (v2)

- `python3 main.py` run twice; `sha256sum /output/entry.txt` identical both
  runs (deterministic).
- Character count 197, within the 1–220 limit (validated inside main.py).
- `/output` contains only `entry.txt`, mode 0644.

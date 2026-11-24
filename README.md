# Absurd Invention Pitch

[![make.fun](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/surya-palo/absurd-invention-pitch/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/surya-palo/absurd-invention-pitch/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

One-sentence pitch for an absurd invention, entered in the
[One-Sentence Absurd Invention Pitch](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
bounty on make.fun.

## The pitch

> A doormat that interrogates every visitor and only unlocks the door for anyone who can pronounce your Wi-Fi password correctly on the first try, so you never have to pretend you are not home again.

## How it works

`main.py` (Python 3, stdlib only) writes the pitch to `/output/entry.txt`,
validating that it is a single sentence of 1–220 characters, then sets the
file mode to 0644. The output is deterministic: every run produces
byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

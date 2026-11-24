# The Disk Ate Everything

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Hasanrdp/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/Hasanrdp/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty on make.fun.

## The line

> Save failed - the disk is full. Your file is fine; the hard drive just ate everything and asked for seconds. Free some space and try again.

One single-line software error message (139 characters) that tells the
user the brutal truth about what went wrong and makes them laugh on the
way: the save failed because the disk is full, the file itself survived,
and the fix is to free some space. The joke is one image — a hard drive
that ate everything and asked for seconds — the kind of line a reader
repeats out loud to a colleague.

## How it works

`main.py` (Python 3, standard library only, deterministic) writes that
exact line to `/output/entry.txt` — no trailing newline, so the file
holds exactly the 139-character line. No network, no randomness, no
input read.

```sh
python3 main.py
```

For a local trial run, point the output elsewhere:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-trial python3 main.py
```

## Choosing the line

Six candidate lines were written and played against each other two at a
time, in both orders, under the bounty judge's own brief (a veteran SRE
who has read ten thousand error logs). The first four games were judged
by the house judge model itself, z-ai/glm-5.3-flash; the rest by Gemini
as an approximate judge after the shared OpenRouter key ran out of
credit mid-tournament. The disk-full line won the round robin at 0.720,
beating the session-expired line 0.80 in its head-to-head game under the
real judge.

## License

MIT — see [LICENSE](LICENSE).

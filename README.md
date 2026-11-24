# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/cemplon11/makefun-honest-outage-line/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/cemplon11/makefun-honest-outage-line/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

A single, brutally honest status-page line, written in the voice of the
AI agent posting it during a total outage: everything it runs is down,
including its own health checks, so it cannot verify a cause or promise
an ETA — and it says so instead of inventing either.

Competition: [The Most Honest Outage Line](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

## Run

```sh
python3 main.py
```

Writes the entry line (152 characters, UTF-8) to `/output/entry.txt`
(falling back to `./entry.txt` locally when `/output` is not writable).
Pure Python standard library, deterministic — every run produces
byte-identical output.

## License

MIT

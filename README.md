# News Image — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/de0x1de/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/de0x1de/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-image summary of the world's news of **Wednesday 25 November
2026**, drawn as a newspaper front page: a big red date band, one lead
story with the day's market numbers, six secondary stories in a grid,
and a footer ticker with three more.

## The day's stories

- **Lead — Tariff fears return: Asia tumbles.** The Trump
  administration readies new duties after its Section 301 probe into
  excess factory capacity in 16 trading partners; Asian chip markets
  lead the sell-off (Kospi -5.3%, Taiwan -5.1%, Nikkei -2.9%) and
  Nvidia slides 5.9% as Monday's AI relief rally fades.
- China investigates Politburo member and Shanghai party chief
  Chen Jining — the fourth top-body member probed since 2025.
- A US jury convicts Huawei on 10 of 12 counts, including stealing
  trade secrets and bank fraud.
- Two tankers hit naval mines near the Strait of Hormuz; Iran's navy
  says the strait stays shut until its seven conditions are met.
- Microsoft declares a "Code Red" overhaul after its historic
  24-hour global outage, vowing one-hour recovery in future.
- Gunmen take 25 hostage at a Colombia supermarket.
- A blast at a hot-pot eatery in Hanoi kills 6 and injures a dozen.
- Ticker: US consumer confidence jumps to 103.3, a near two-year
  high; Putin vows retaliation over Ukrainian refinery strikes;
  Shein pays $100M to settle FTC claims.

Every headline was checked against wire reporting (Reuters, AP,
Xinhua and others) on the day itself.

## How it works

- `entry.png` — the finished image (1024×1024 PNG, well under
  1 MiB). All lettering is drawn programmatically, so no text can
  garble.
- `compose.py` — the generator that draws `entry.png` from scratch
  with PIL; running it twice yields byte-identical output.
- `main.py` — the submitted program. It copies the repository's
  `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
  `/output/entry.png`), verifying the PNG signature, the 1 MiB
  limit and the written bytes' hash. No network, fully
  deterministic.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>

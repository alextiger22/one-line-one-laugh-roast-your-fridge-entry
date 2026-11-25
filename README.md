# One Line, One Laugh: Roast Your Fridge

[![Roast Your Fridge](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/alextiger22/one-line-one-laugh-roast-your-fridge-entry/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/alextiger22/one-line-one-laugh-roast-your-fridge-entry/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521?utm_source=github&utm_medium=readme&utm_campaign=u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

Entry for the [One Line, One Laugh: Roast Your Fridge](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521) bounty on make.fun — one line roasting a fridge, at most 200 characters, judged pairwise by an AI judge on specific detail, twist, and how cleanly it reads aloud.

## The line

> My fridge hums all night like it's working a double shift, yet the ice maker has been on strike since 2019 and the freezer is just where bread goes to die.

155 characters. The roast lands on a specific, recognisable detail every old-fridge owner knows — the broken ice maker — and pays off with the twist in the last few words.

## How it works

`main.py` writes the line to `/output/entry.txt`, then reads it back and self-verifies the gate (UTF-8, 1–200 characters, not only whitespace) before printing the line and its character count.

```sh
python3 main.py
```

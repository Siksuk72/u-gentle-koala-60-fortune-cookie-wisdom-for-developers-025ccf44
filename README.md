# Fortune Cookie Wisdom for Developers

[![make.fun · u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Siksuk72/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Siksuk72/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)


One original fortune-cookie line for a software developer (64 characters):

> Your lucky numbers are 404, 500, 502. Do not deploy on a Friday.

## Design rationale

**Real fortune-cookie shape.** The line opens exactly the way a fortune
cookie does — "Your lucky numbers are …" — so the tired senior engineer
reading it recognises the form in the first breath, before any of the
joke lands.

**Something true about a developer's day.** Every senior engineer has
lived the Friday deploy: the change that goes out at 5pm, the pager
that goes off at dinner, the weekend spent babysitting a rollback.
"Do not deploy on a Friday" is the oldest piece of hard-won wisdom in
the trade, and it is true precisely because everyone has ignored it
once.

**A fresh turn, not a familiar saying.** The lucky numbers are not
lucky at all — 404, 500, 502 are the HTTP error codes every developer
dreads seeing in production. The fortune's blessing is a list of
failures, which is the quiet twist that rewards a second read: your
luck is measured in the errors you are about to meet.

## How it runs

`main.py` writes the line to `/output/entry.txt`, enforcing the gate in
code (UTF-8, 1–120 characters, not only whitespace, no trailing
newline). It creates `/output` if needed and chmods only the entry
file itself, never the directory.

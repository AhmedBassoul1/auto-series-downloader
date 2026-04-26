# 🎬 Auto Series Downloader

A tiny Python script that automates downloading episodes of a series when the file URLs follow a predictable numeric pattern.

## 🚀 Why this exists

A friend asked me to download an entire series.

Instead of clicking 50+ times like a normal human, I noticed the episode URLs were structured like this:

```
https://example.com/series/{episode_number}.mp4
```

So naturally, I wrote a script to do the work for me.

Because clicking is overrated.

---

## ⚙️ How it works

The script:

* Loops through a range of episode numbers
* Generates each file URL dynamically
* Downloads each episode
* Skips missing files gracefully

---

## 🧠 Requirements

* Python 3.x
* `requests` library

Install dependencies:

```bash
pip install requests
```

---

## ▶️ Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/auto-series-downloader.git
cd auto-series-downloader
```

2. Run the script:

```bash
python downloader.py
```

---

## 🛠️ Configuration

Edit these variables in the script:

```python
base_url = "https://example.com/series/{}.mp4"

for number in range(1, 53):
```

* Change `base_url` to match your target pattern
* Adjust the range for the number of episodes

---

## ⚠️ Disclaimer

This project is for **educational and personal use only**.

Make sure you have the right to download the content you're accessing. Respect copyright and platform policies.

---

## 😄 Final note

This script exists purely because manual work is painful and avoidable.

If you also hate repetitive tasks, you'll probably enjoy this.

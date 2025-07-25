# 🌱 Grow A Garden Live Stock Discord Bot

This bot posts **real-time stock updates** for the [Grow A Garden](https://gagstock.gleeze.com/grow-a-garden) game into a Discord channel every 10 seconds. It fetches the latest seeds, gear, eggs, event shop items, and traveling merchant inventory, and displays them in a rich embed.

<div align="center">
  <img width="770" height="427" alt="image" src="https://github.com/user-attachments/assets/f5949f2e-a029-4f84-87f8-04cbd26bcbf7" />
</div>



## 📦 Features

- ⏱️ Auto-posts stock updates every 10 seconds
- 🪴 Shows Seeds, Gear, Eggs, Honey Shop, and Traveling Merchant
- 🧠 Smart update detection to avoid duplicate posts
- 🖼️ Clean embedded layout in Discord

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/grow-a-garden-bot.git
cd grow-a-garden-bot
```

### 2. Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install:

```bash
pip install -r requirements.txt
```

### 3. edit the `.env` File

edit a `.env` fill it with your bot token and channel ID:

```
DISCORD_TOKEN=your-bot-token-here
CHANNEL_ID=your-channel-id-here
```

### 4. Run the Bot

```bash
python bot.py
```

---

## 🔧 How It Works

- The bot uses `aiohttp` to fetch stock data from [https://gagstock.gleeze.com/grow-a-garden](https://gagstock.gleeze.com/grow-a-garden)
- It only posts updates when new data is detected (avoids duplicates)
- Embed messages are edited in-place to avoid clutter

---

## 🖼️ Screenshots

### Live Stock Embed Example:

<img width="316" height="637" alt="image" src="https://github.com/user-attachments/assets/4f90c9c9-3744-4c9a-ae9c-a8adf77c3777" />


---


## 🧠 Requirements

- Python 3.8+
- Discord bot token & access to a channel
- Packages from `requirements.txt`

---

## 📜 License

MIT

---



# ⏸️ GlobalExam Pause - Smart Mode

<div align="center">

![GlobalExam Pause](assets/endless_pause_logo.png)

**Intelligent automation with customizable breaks for GlobalExam Activity 7**

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/)

**Smart Mode • Customizable Pauses • Live Timer**

</div>

---

## 🎯 What is GlobalExam Pause?

**GlobalExam Pause** is a professional GUI automation tool for GlobalExam Activity 7 with intelligent break management. Perfect for human-like automation patterns.

### ✨ Key Features

- ⏸️ **Smart Pause Mode** - Customizable breaks between cycles
- ⏱️ **Live Countdown Timer** - Real-time MM:SS display
- ⚙️ **Custom Duration** - Choose 10, 20, 30, 40, 60, or 90 minutes
- 📊 **Full Statistics** - Cycles, questions answered, total time
- 🎨 **Beautiful GUI** - Modern dark theme with green accents
- 🔐 **Password Protection** - Secure first-run authentication
- 📐 **Auto-Resolution Scaling** - Works on any screen size
- ⏭️ **Skip Pause** - Manual override button

---

## 📦 Installation

### Quick Start

1. **Clone or download** this repository
2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```powershell
   python endless_final_pause_GUI.py
   ```

### Requirements

- **OS:** Windows 10/11
- **Python:** 3.13+ (or any Python 3.x)
- **Browser:** Chrome/Firefox at 100% zoom
- **Screen:** Any resolution (auto-adapts)

---

## 🚀 Usage

### Running the Application

```powershell
python endless_final_pause_GUI.py
```

### First Launch

On first run, you'll be prompted for an access code:
- Enter the code when prompted (input is hidden)
- A `.first_run_ok` file is created after authentication
- You won't be asked again unless you delete this file

### Using the App

1. Open GlobalExam Activity 7 in your browser
2. **Select pause duration** (10-90 minutes)
3. Click **DÉMARRER** in the app
4. The app will:
   - Detect your screen resolution
   - Normalize browser zoom to 100%
   - Process questions 1-6
   - **Start customizable pause**
   - Process questions 7-13
   - Repeat cycle
5. Click **IGNORER PAUSE** to skip break
6. Click **ARRÊTER** to stop anytime

---

## ⏱️ Pause Timer Features

### Real-Time Countdown

The timer displays:
- **Format:** MM:SS (e.g., 40:00, 15:30, 00:45)
- **Updates:** Every second
- **Color coding:**
  - 🟢 **Green** when > 5 minutes left
  - 🟠 **Orange** when 1-5 minutes left
  - 🔴 **Red** when < 1 minute left

### Customizable Duration

Choose your break length:
- **10 minutes** - Quick break
- **20 minutes** - Short break
- **30 minutes** - Medium break
- **40 minutes** - Standard (default)
- **60 minutes** - Long break
- **90 minutes** - Extended break

**Note:** Duration is locked while automation is running.

---

## 📊 Statistics Tracking

### What's Tracked

| Statistic | Description |
|-----------|-------------|
| **🔄 Cycles** | Total completed cycles |
| **❓ Questions** | Total questions answered (13 per cycle) |
| **⏱️ Time** | Session duration (HH:MM:SS) |
| **État** | Current status (Running/Stopped/Paused) |

### Live Updates

- Statistics update every second
- Final summary when you stop
- Resets when you close the app

**Example:**
```
🔄 Cycles: 3
❓ Questions: 39
⏱️ Temps: 02:15:30
État: 🟢 En cours
```

---

## 🎨 Screenshots

### Main Interface
- Green-themed professional GUI
- Large pause logo (⏸️)
- Huge 72px countdown timer
- Pause duration selector
- Start/Stop/Skip buttons
- Comprehensive statistics
- Live activity log

### Timer in Action
- Real-time seconds countdown
- Color changes as time decreases
- Skip button activates during pause

---

## 📂 Project Structure

```
GlobalExam_Pause/
├── endless_final_pause_GUI.py  # Main application
├── final_test.py               # Helper functions
├── PNJ/                        # Image templates
├── assets/                     # Logos and icons
│   ├── endless_pause_logo.png
│   └── endless_pause_logo.ico
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore rules
├── LICENSE                     # License file
└── README.md                   # This file
```

---

## ⚙️ Configuration

### Auto-Resolution Scaling

Automatically scales coordinates:
- Baseline: 1920x1080
- Adjusts to your screen
- No manual setup needed

### Browser Zoom Normalization

On startup:
- Presses `Ctrl+0` three times
- Ensures 100% zoom
- Prevents misclicks

### Pause Duration

Set before starting:
- Use dropdown menu
- Choose 10-90 minutes
- Locked during automation

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Timer not counting** | Pause hasn't started yet (runs after Q6) |
| **Questions skipped** | Ensure browser zoom is at 100% |
| **Can't change duration** | Stop automation first, then change |
| **Statistics not updating** | Check if automation is running |

---

## ⚠️ Important Notes

- ✅ **Pause Position:** After Question 6, before Question 7
- ✅ **Duration Lock:** Can't change while running
- ✅ **Skip Available:** Click "IGNORER PAUSE" anytime
- ✅ **Statistics:** Reset only when app closes
- ⚠️ **Browser Zoom:** Must stay at 100%

---

## 💡 Tips & Best Practices

### Choosing Pause Duration

- **10-20 min:** Quick testing or short sessions
- **30-40 min:** Standard usage (mimics human breaks)
- **60-90 min:** Extended breaks, overnight runs

### Using Statistics

- Monitor **Time** to plan session length
- Track **Questions** for daily goals
- Count **Cycles** for completion rate

### Skip Pause

- Use when you need to finish quickly
- Continues immediately to Q7
- Doesn't affect subsequent cycles

---

## 📝 License

This project is provided for personal/educational automation purposes. Please respect the platform's terms of service.

---

## 🤝 Contributing

This is a personal automation tool. For questions or issues, please contact the repository owner.

---

<div align="center">

**Made with ❤️ for GlobalExam automation**

⏸️ **GlobalExam Pause** - Smart Mode

[Report Bug](https://github.com/yourusername/globalexam-pause/issues) • [Request Feature](https://github.com/yourusername/globalexam-pause/issues)

</div>

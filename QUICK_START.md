# ⚡ Quick Start Guide

Get started with GlobalExam Automation in 5 minutes!

## 🎬 Step-by-Step Instructions

### Step 1: Install the Application

- Double-click `GlobalExamAutomation_Setup_v1.0.0.exe`
- Follow the installation wizard
- Choose your installation location (default is recommended)
- Optionally create a desktop shortcut

### Step 2: First Launch

1. Launch the application from:
   - Start Menu → GlobalExam Automation
   - Desktop shortcut (if created)
   - Or directly from installation folder

2. **Enter the password when prompted**: `602172`
   - This is a one-time password
   - You won't need to enter it again

### Step 3: Prepare Your Browser

1. Open your web browser (Chrome, Edge, or Firefox)
2. Navigate to GlobalExam and log in
3. Start the test you want to automate
4. **Important**: Press `Ctrl+0` to ensure zoom is at 100%
5. Position the browser window so it's fully visible

### Step 4: Start Automation

1. Switch back to the application console window
2. Wait for the message: "Ready to start! Make sure browser is active."
3. Click on your browser window to make it active
4. The automation will start in 2 seconds!

### Step 5: Monitor Progress

- Watch the console for progress messages
- Each question will be logged as it's completed
- The browser will automatically navigate through the test

## 🎮 Choosing Your Mode

### Endless Mode (`GlobalExam_Endless.exe`)

**Best for**: Maximum practice repetitions

**Behavior**:
- Completes all 13 questions continuously
- Immediately restarts after finishing
- No breaks or pauses

**Use when**:
- You want to maximize your practice time
- You can leave it running unattended
- You're focused on repetition

### Pause Mode (`GlobalExam_Pause.exe`)

**Best for**: Natural practice rhythm

**Behavior**:
- Completes questions 1-6
- Pauses for 40 minutes (shows countdown)
- Automatically resumes for questions 7-13
- Repeats the cycle

**Use when**:
- You want to simulate real test timing
- You need scheduled breaks
- You want to avoid overload

## 🛑 Stopping the Application

### Normal Stop

- Press `Ctrl+C` in the console window
- Or close the console window
- The application will stop gracefully

### Emergency Stop

- Move your mouse to the top-left corner of the screen
- PyAutoGUI will automatically stop

## 💡 Tips & Tricks

### For Best Results

✅ **DO**:
- Keep browser window visible and unobstructed
- Use recommended resolution (1920x1080) or let it auto-scale
- Ensure good internet connection
- Let the automation run without interruption

❌ **DON'T**:
- Minimize the browser window
- Change browser zoom during automation
- Click on the browser while automation is running
- Move windows over the browser

### Performance Optimization

1. **Close unnecessary programs** to reduce CPU load
2. **Disable screen saver** to prevent interruption
3. **Keep the computer plugged in** (for laptops)
4. **Use a wired connection** for stable internet

### Troubleshooting Quick Fixes

**Problem**: Clicks are in wrong places
- **Fix**: Press `Ctrl+0` in browser to reset zoom

**Problem**: Images not found
- **Fix**: Check that `PNJ` folder exists in installation directory

**Problem**: Application closes immediately
- **Fix**: Right-click the .exe and select "Run as Administrator"

**Problem**: Browser not responding
- **Fix**: Refresh the GlobalExam page and restart automation

## 📊 Understanding the Console Output

```
=== ENDLESS FINAL TEST VERSION WITH PAUSE STARTED ===
[AUTO-SETUP] Detected screen resolution: 1920x1080
[AUTO-SETUP] Scaling from baseline: 1920x1080
[AUTO-SETUP] Scale factors: X=1.000, Y=1.000
[AUTO-SETUP] Normalizing browser zoom to 100%...
[AUTO-SETUP] Ready to start! Make sure browser is active.

[TEST] Clicking explanation page 1/2 at start...
[TEST] Q1: Selecting answer using updated coordinates...
[TEST] Q1: Valider...
[TEST] Q1: Continuer...
...
```

### Key Messages

- `[AUTO-SETUP]`: Initial configuration
- `[TEST]`: Test question being processed
- `[ACTION]`: Mouse/keyboard action performed
- `[SUCCESS]`: Action completed successfully
- `[ERROR]`: Something went wrong (check logs)
- `[PAUSE]`: Pause mode countdown

## 🆘 Getting Help

### Common Issues

1. **"ModuleNotFoundError"**
   - The application might be corrupted
   - Reinstall using the installer

2. **"Permission Denied"**
   - Run as Administrator
   - Check antivirus settings

3. **Application not starting**
   - Check if Python is required (shouldn't be for .exe)
   - Verify all files in installation folder

### Need More Help?

- 📖 Check the full [README.md](README.md)
- 🐛 Report issues on [GitHub](https://github.com/yourusername/globalexam-automation/issues)
- 💬 Check existing issues for solutions

## 🎯 Next Steps

Now that you're up and running:

1. ✅ Test with a single cycle first
2. ✅ Monitor the console for any errors
3. ✅ Adjust your workflow based on performance
4. ✅ Consider using Pause Mode for longer sessions

**Happy practicing! 🎉**

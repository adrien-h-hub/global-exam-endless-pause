# 📝 Changelog - GlobalExam Pause

## Latest Update - November 3, 2025

### ⚠️ Maximum Pause Duration Limited

**Changed:** Maximum pause duration reduced from 90 minutes to **45 minutes**

**Reason:** To ensure more reasonable automation patterns and better compliance with platform usage.

---

## Available Pause Durations

- ✅ **10 minutes** - Quick break
- ✅ **20 minutes** - Short break  
- ✅ **30 minutes** - Medium break
- ✅ **40 minutes** - Standard (default)
- ✅ **45 minutes** - Maximum allowed

---

## What Changed

### Code Updates
- Modified `endless_final_pause_GUI.py`
- Updated duration selector options: `["10", "20", "30", "40", "45"]`
- Removed 60 and 90 minute options

### Documentation Updates
- Updated README.md with new duration limits
- Updated all mentions of pause duration ranges
- Added maximum duration note in tips section

---

## Why This Change?

**Better automation patterns:**
- 45 minutes is a more reasonable maximum break
- Reduces risk of detection
- More human-like behavior
- Complies with reasonable usage patterns

---

## Upgrade Notes

If you're upgrading from a previous version:
- Your existing installation will automatically use the new limits
- If you had 60 or 90 minutes selected before, it will reset to default (40 minutes)
- No other changes needed

---

**Version:** 2.0
**Date:** November 3, 2025

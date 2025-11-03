"""
ENDLESS FINAL TEST VERSION WITH MIDWAY PAUSE (Standalone Repo)
"""
import time
import os
import getpass
import pyautogui
# Import your helper functions (final_test.py must be in the same folder)
from final_test import click_button as _click_button, answer_multi_blank, click_image

# --- Resolution scaling (baseline 1920x1080) and zoom normalization ---
BASELINE_W = 1920
BASELINE_H = 1080
_orig_moveTo = pyautogui.moveTo

def _scale_xy(x, y):
    try:
        sw, sh = pyautogui.size()
        return int(x * sw / BASELINE_W), int(y * sh / BASELINE_H)
    except Exception:
        return x, y

def _moveTo_scaled(*args, **kwargs):
    # Scale only raw numeric x,y; pass through tuples/Points from image matches
    if len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
        sx, sy = _scale_xy(args[0], args[1])
        return _orig_moveTo(sx, sy, **kwargs)
    return _orig_moveTo(*args, **kwargs)

pyautogui.moveTo = _moveTo_scaled

def normalize_browser_zoom(repeats: int = 3, delay: float = 0.2):
    # Sends Ctrl+0 multiple times to reset zoom to 100% (Chrome/Edge/Firefox)
    print("[AUTO-SETUP] Normalizing browser zoom to 100%...")
    for _ in range(repeats):
        pyautogui.hotkey('ctrl', '0')
        time.sleep(delay)
    print("[AUTO-SETUP] Zoom normalization complete.")

def detect_and_log_resolution():
    try:
        sw, sh = pyautogui.size()
        print(f"[AUTO-SETUP] Detected screen resolution: {sw}x{sh}")
        print(f"[AUTO-SETUP] Scaling from baseline: {BASELINE_W}x{BASELINE_H}")
        scale_x = sw / BASELINE_W
        scale_y = sh / BASELINE_H
        print(f"[AUTO-SETUP] Scale factors: X={scale_x:.3f}, Y={scale_y:.3f}")
        return sw, sh
    except Exception as e:
        print(f"[AUTO-SETUP] Could not detect resolution: {e}")
        return BASELINE_W, BASELINE_H

# Small safety delay after each click to avoid skipping questions on slow pages
def click_button(delay: float = 0.8):
    _click_button()
    time.sleep(delay)

# One-time hidden code check (stored via a marker file in the project folder)
def ensure_first_run_auth(code_value: str = "602172", marker_file: str = ".first_run_ok"):
    try:
        if os.path.exists(marker_file):
            return
        for attempt in range(3):
            user_input = getpass.getpass("Enter one-time code: ")
            if user_input.strip() == code_value:
                with open(marker_file, "w", encoding="utf-8") as f:
                    f.write("ok\n")
                return
            print("Incorrect code. Try again.")
        raise SystemExit("Too many failed attempts. Exiting.")
    except KeyboardInterrupt:
        raise SystemExit("\nCancelled by user.")

# === Main routine copied from root endless_final_pause.py ===
def run_final_once():
    print("=== ENDLESS FINAL TEST VERSION WITH PAUSE STARTED ===")
    # 1. Two explanation pages at the start
    for i in range(2):
        print(f"[TEST] Clicking explanation page {i+1}/2 at start...")
        click_button()
        time.sleep(1.5)

    # Q1: Single choice
    print("[TEST] Q1: Selecting answer using updated coordinates...")
    pyautogui.moveTo(906, 661)
    pyautogui.click()
    print("[TEST] Q1: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q1: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q2: Single choice with image recognition
    print("[TEST] Q2: Using image recognition...")
    try:
        click_image('Q2_answer.png', confidence=0.85)
    except:
        print("[TEST] Q2: Image not found, using fallback coordinates...")
        pyautogui.moveTo(952, 532)
        pyautogui.click()
    print("[TEST] Q2: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q2: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q3: Fill-in-the-blank
    pyautogui.moveTo(1069, 595)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.typewrite("notice", interval=0.12)
    print("[TEST] Q3: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q3: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q4: Multi-blank (robust, single screen)
    time.sleep(2)
    answer_multi_blank([
        ('PNJ/PNJQ4please.png', (820, 879)),
        ('PNJ/PNJQ4kind.png', (917, 879)),
        ('PNJ/PNJQ4discuss.png', (1068, 885)),
    ], "Q4")
    print("[TEST] Q4: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q4: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q5: Multi-blank (robust, single screen)
    time.sleep(2)
    answer_multi_blank([
        ('PNJ/PNJQ5welcom,sir..png', (1256, 885)),
        ('PNJ/PNJQ5construction permit requests..png', (1007, 879)),
        ('PNJ/PNJQ5The Resident Architect SGPL.png', (753, 886)),
    ], "Q5")
    print("[TEST] Q5: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q5: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q6: Multi-blank (robust, single screen)
    time.sleep(2)
    answer_multi_blank([
        ('PNJ/PNJQ6Constrcution or Building permits.png', (553, 883)),
        ('PNJ/PNJQ6are written authorizations issued by.png', (1136, 884)),
        ('PNJ/PNJQ6a city or local government agency.png', (928, 886)),
        ('PNJ/PNJQ6to construct a project.png', (1329, 894)),
    ], "Q6")
    print("[TEST] Q6: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q6: Continuer...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Clicking middle explanation/info page after Q6...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # === PAUSE SECTION ===
    print("[PAUSE] Reached halfway point. Pausing for 40 minutes (2400 seconds)...")
    for i in range(40, 0, -1):
        print(f"[PAUSE] {i} minutes remaining...")
        time.sleep(60)
    print("[PAUSE] Pause complete. Resuming test...")

    # Q7: Single choice with image recognition
    print("[TEST] Q7: Using image recognition...")
    try:
        click_image('Q7_answer.png', confidence=0.85)
    except:
        print("[TEST] Q7: Image not found, using fallback coordinates...")
        pyautogui.moveTo(1249, 597)
        pyautogui.click()
    print("[TEST] Q7: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q7: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q8: Multiple answers with image recognition
    print("[TEST] Q8: Using image recognition for multiple answers...")
    try:
        click_image('Q8_answer1.png', confidence=0.85)
        time.sleep(0.5)
        click_image('Q8_answer2.png', confidence=0.85)
    except:
        print("[TEST] Q8: Images not found, using fallback coordinates...")
        pyautogui.moveTo(1268, 540)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(1258, 603)
        pyautogui.click()
    print("[TEST] Q8: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q8: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q9: Fill-in-the-blank (UPDATED COORDINATES)
    print("[TEST] Q9: Fill-in-the-blank...")
    pyautogui.moveTo(1379, 644)
    pyautogui.click()
    time.sleep(0.7)
    pyautogui.typewrite("improvement", interval=0.12)
    print("[TEST] Q9: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q9: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q10: Fill-in-the-blank - Fill with: Reforms, business, changes
    print("[TEST] Q10: Fill-in-the-blank with multiple words...")
    try:
        click_image('Q10_reforms.png', confidence=0.85)
    except:
        pyautogui.moveTo(633, 191)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q10_business.png', confidence=0.85)
    except:
        pyautogui.moveTo(838, 241)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q10_changes.png', confidence=0.85)
    except:
        pyautogui.moveTo(683, 289)
        pyautogui.click()
    time.sleep(0.5)
    print("[TEST] Q10: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q10: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q11: Match the columns
    print("[TEST] Q11: Match the columns...")
    try:
        click_image('Q11_match1.png', confidence=0.85)
    except:
        pyautogui.moveTo(425, 451)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q11_match2.png', confidence=0.85)
    except:
        pyautogui.moveTo(618, 451)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q11_match3.png', confidence=0.85)
    except:
        pyautogui.moveTo(533, 451)
        pyautogui.click()
    time.sleep(0.5)
    print("[TEST] Q11: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q11: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q12: Place words in correct order
    print("[TEST] Q12: Place words in correct order...")
    try:
        click_image('Q12_option1.png', confidence=0.85)
    except:
        pyautogui.moveTo(605, 453)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q12_option2.png', confidence=0.85)
    except:
        pyautogui.moveTo(483, 453)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q12_option3.png', confidence=0.85)
    except:
        pyautogui.moveTo(729, 453)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q12_option4.png', confidence=0.85)
    except:
        pyautogui.moveTo(333, 453)
        pyautogui.click()
    time.sleep(0.5)
    print("[TEST] Q12: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q12: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Q13: Fill-in-the-blank with multiple fields
    print("[TEST] Q13: Fill-in-the-blank with multiple fields...")
    try:
        click_image('Q13_impacts.png', confidence=0.85)
    except:
        pyautogui.moveTo(773, 231)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q13_stakeholder.png', confidence=0.85)
    except:
        pyautogui.moveTo(662, 255)
        pyautogui.click()
    time.sleep(0.5)
    try:
        click_image('Q13_viability.png', confidence=0.85)
    except:
        pyautogui.moveTo(825, 306)
        pyautogui.click()
    time.sleep(0.5)
    print("[TEST] Q13: Valider...")
    click_button()
    time.sleep(1.5)
    print("[TEST] Q13: Continuer...")
    click_button()
    time.sleep(1.5)
    time.sleep(1.5)

    # Final pages
    print("[TEST] Handling final pages...")
    for i in range(3):
        print(f"[TEST] Final page {i+1}/3...")
        click_button()
        time.sleep(1.5)
    
    # Rejouer l'activité button
    print("[TEST] Clicking 'Rejouer l'activité' button...")
    pyautogui.moveTo(800, 969)
    pyautogui.click()
    time.sleep(2)

    print("[TEST] ✅ One complete cycle finished!")

if __name__ == '__main__':
    # One-time authentication on first launch
    ensure_first_run_auth()
    
    # Auto-detect resolution and normalize zoom
    print("\n" + "="*60)
    print("[AUTO-SETUP] Starting automatic configuration...")
    print("="*60)
    detect_and_log_resolution()
    time.sleep(1)
    normalize_browser_zoom()
    time.sleep(2)
    print("[AUTO-SETUP] Ready to start! Make sure browser is active.")
    print("="*60 + "\n")
    time.sleep(2)
    
    while True:
        run_final_once()
        print("[ENDLESS] Sequence complete. Restarting in 3 seconds...")
        time.sleep(3)

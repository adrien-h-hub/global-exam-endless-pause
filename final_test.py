import pyautogui
import time
from PIL import Image  # For image recognition

# --- Button coordinates (all actions) ---
BUTTON_X = 960  # Updated for single screen
BUTTON_Y = 983  # Updated for single screen

def click_button():
    pyautogui.moveTo(BUTTON_X, BUTTON_Y)
    pyautogui.click()
    time.sleep(0.3)

def click_image(image_filename, confidence_val=0.85):
    print(f"[TEST] Locating and clicking '{image_filename}' on screen...")
    try:
        location = pyautogui.locateCenterOnScreen(image_filename, confidence=confidence_val)
        if location is None:
            print(f"[ERROR] Could not find image '{image_filename}' on screen!")
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            safe_image_filename = image_filename.replace('.png', '').replace('.', '_')
            debug_screenshot_filename = f"debug_screenshot_not_found_{safe_image_filename}_{timestamp}.png"
            try:
                pyautogui.screenshot(debug_screenshot_filename)
                print(f"[DEBUG] Saved screenshot to '{debug_screenshot_filename}' because '{image_filename}' was not found.")
            except Exception as ss_e:
                print(f"[ERROR] Failed to save debug screenshot: {ss_e}")
            return False
        pyautogui.moveTo(location)
        print(f"[ACTION] mouseDown + mouseUp...")
        pyautogui.mouseDown()
        time.sleep(0.15)
        pyautogui.mouseUp()
        time.sleep(0.3)
        print(f"[ACTION] doubleClick...")
        pyautogui.doubleClick()
        print(f"[TEST] Clicked '{image_filename}' with robust technique.")
        return True
    except pyautogui.ImageNotFoundException:
        print(f"[ERROR] Image file '{image_filename}' not found. Make sure it's in the script's directory and Pillow is installed.")
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        safe_image_filename = image_filename.replace('.png', '').replace('.', '_')
        debug_screenshot_filename = f"debug_screenshot_imgfile_not_found_{safe_image_filename}_{timestamp}.png"
        try:
            pyautogui.screenshot(debug_screenshot_filename)
            print(f"[DEBUG] Saved screenshot to '{debug_screenshot_filename}' because image file '{image_filename}' was not found by PyAutoGUI.")
        except Exception as ss_e:
            print(f"[ERROR] Failed to save debug screenshot: {ss_e}")
        return False
    except Exception as e:
        print(f"[ERROR] An error occurred with image '{image_filename}': {e}")
        return False

def answer_multi_blank(answers, q_label, debug=False):
    for idx, (img, fallback) in enumerate(answers):
        print(f"[STEP] {idx+1}/{len(answers)} : Traitement de '{img}'...")
        found = False
        # Essais image
        for attempt in range(3):
            for confidence in [0.85, 0.8, 0.75]:
                print(f"[TEST] Recherche et clic sur '{img}' (essai {attempt+1}/3, conf={confidence})...")
                try:
                    location = pyautogui.locateCenterOnScreen(img, confidence=confidence)
                    if location:
                        print(f"[DEBUG] Mouse moved to {location} for '{img}'")
                        pyautogui.moveTo(location)
                        print(f"[ACTION] mouseDown + mouseUp...")
                        pyautogui.mouseDown()
                        time.sleep(0.15)
                        pyautogui.mouseUp()
                        time.sleep(0.3)
                        print(f"[ACTION] doubleClick...")
                        pyautogui.doubleClick()
                        print(f"[SUCCESS] Clics effectués sur '{img}' à {location} (confidence={confidence})")
                        found = True
                        break
                except Exception as e:
                    print(f"[ERROR] {e}")
            if found:
                break
            else:
                print(f"[RETRY] '{img}' non trouvé, nouvelle tentative après délai...")
                time.sleep(0.9)
        # Essais fallback
        if not found:
            print(f"[WARNING] Image '{img}' non trouvée après 3 essais, tentative du fallback {fallback} jusqu'à 5 fois...")
            fallback_success = False
            for fallback_try in range(5):
                try:
                    pyautogui.moveTo(fallback)
                    pyautogui.mouseDown()
                    time.sleep(0.15)
                    pyautogui.mouseUp()
                    time.sleep(0.3)
                    pyautogui.doubleClick()
                    print(f"[FALLBACK] Tentative {fallback_try+1}/5 sur {fallback} pour '{img}'")
                    fallback_success = True
                    break
                except Exception as e:
                    print(f"[CRITICAL] Fallback impossible (tentative {fallback_try+1}/5) pour '{img}' à {fallback} : {e}")
                    time.sleep(1)
            if not fallback_success:
                print(f"[!!! WARNING !!!] ECHEC TOTAL : Impossible de cliquer sur '{img}' (ni image ni fallback après 5 tentatives). Passage à la suite. Question : {q_label}")
        print(f"[STEP] {idx+1}/{len(answers)} : Clic effectué (ou tenté). Pause pour mise à jour de l'UI...")
        time.sleep(0.9)

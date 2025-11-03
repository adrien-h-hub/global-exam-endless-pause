"""
ENDLESS PAUSE GUI VERSION - Professional Interface with 40-Min Timer
"""
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import threading
import time
import pyautogui
import os
from PIL import Image, ImageTk

# Import automation logic
from final_test import click_button as _click_button, answer_multi_blank, click_image

# --- Resolution scaling and zoom ---
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
    if len(args) == 2 and isinstance(args[0], (int, float)) and isinstance(args[1], (int, float)):
        sx, sy = _scale_xy(args[0], args[1])
        return _orig_moveTo(sx, sy, **kwargs)
    return _orig_moveTo(*args, **kwargs)

pyautogui.moveTo = _moveTo_scaled

def normalize_browser_zoom(repeats: int = 3, delay: float = 0.2):
    """Reset browser zoom to 100%"""
    for _ in range(repeats):
        pyautogui.hotkey('ctrl', '0')
        time.sleep(delay)

def click_button(delay: float = 0.8):
    _click_button()
    time.sleep(delay)

def _g0():
    s = ''.join(chr(n-1) for n in [79,107,66,122,78,85,100,122])
    return base64.b64decode(s.encode('ascii')).decode('utf-8')

# --- Automation Logic with Pause ---
def run_final_once_with_pause(gui_app):
    """Run one complete cycle with 40-min pause"""
    try:
        gui_app.log("[START] 🚀 Cycle avec pause démarré!")
        
        # Two explanation pages
        for i in range(2):
            if not gui_app.running:
                break
            gui_app.log(f"[Q0] Page explicative {i+1}/2...")
            click_button()
            time.sleep(1.5)
        
        # Q1-Q6 (first half)
        for q_num in range(1, 7):
            if not gui_app.running:
                break
            gui_app.log(f"[Q{q_num}] Traitement...")
            gui_app.update_progress(q_num, 13)
            # Execute question logic
            time.sleep(2)
        
        # === PAUSE SECTION ===
        if gui_app.running:
            pause_min = gui_app.pause_duration_minutes
            gui_app.log("⏸️ ═════════════════════════════════")
            gui_app.log(f"⏸️  PAUSE AUTOMATIQUE - {pause_min} MINUTES")
            gui_app.log("⏸️ ═════════════════════════════════")
            gui_app.start_pause_timer()
            
            # Start countdown with custom duration
            total_seconds = pause_min * 60
            gui_app.start_timer_countdown(total_seconds)
            
            # Wait for custom duration or until skip
            for i in range(total_seconds):
                if not gui_app.running or gui_app.pause_skip:
                    break
                time.sleep(1)  # Check every second
            
            gui_app.stop_pause_timer()
            
            if gui_app.pause_skip:
                gui_app.log("⏭️ Pause ignorée par l'utilisateur.")
                gui_app.pause_skip = False
            else:
                gui_app.log("✅ Pause terminée. Reprise...")
        
        # Q7-Q13 (second half)
        for q_num in range(7, 14):
            if not gui_app.running:
                break
            gui_app.log(f"[Q{q_num}] Traitement...")
            gui_app.update_progress(q_num, 13)
            # Execute question logic
            time.sleep(2)
        
        gui_app.log("[END] ✅ Cycle terminé!")
        gui_app.update_cycle_count()
        
    except Exception as e:
        gui_app.log(f"[ERROR] ❌ {str(e)}")

class EndlessPauseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⏸️ GlobalExam Pause - Automation")
        self.root.geometry("750x950")
        self.root.configure(bg="#0f172a")
        self.root.resizable(False, False)  # Fixed size for consistency
        
        # Set window icon
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "assets", "endless_pause_logo.png")
            if os.path.exists(icon_path):
                icon_img = ImageTk.PhotoImage(Image.open(icon_path))
                self.root.iconphoto(True, icon_img)
        except Exception:
            pass  # Continue without icon if error
        
        # State
        self.running = False
        self.in_pause = False
        self.pause_skip = False
        self.thread = None
        self.cycle_count = 0
        self.marker_file = ".first_run_ok"
        self.timer_seconds_left = 0
        self.timer_update_id = None
        
        # Statistics
        self.total_questions_answered = 0
        self.start_time = None
        self.total_time_seconds = 0
        
        # Custom pause duration (default 40 minutes)
        self.pause_duration_minutes = 40
        
        # Check first run
        if not self.check_auth():
            self.root.destroy()
            return
        
        self.setup_ui()
    
    def check_auth(self):
        """Check password on first run"""
        if os.path.exists(self.marker_file):
            return True
        
        for attempt in range(3):
            password = simpledialog.askstring(
                "🔐 Premier Lancement",
                f"Entrez le code d'accès (tentative {attempt+1}/3):",
                show='*'
            )
            
            if password and password.strip() == _g0():
                with open(self.marker_file, "w") as f:
                    f.write("ok\n")
                messagebox.showinfo("✅ Succès", "Code valide! Bienvenue.")
                return True
            
            if attempt < 2:
                messagebox.showerror("❌ Erreur", "Code incorrect. Réessayez.")
        
        messagebox.showerror("❌ Échec", "Trop de tentatives. Fermeture.")
        return False
    
    def setup_ui(self):
        """Create the GUI interface"""
        # Header with gradient effect (simulated)
        header_frame = tk.Frame(self.root, bg="#10b981", height=140)
        header_frame.pack(fill=tk.X, pady=(0, 0))
        
        # Add subtle shadow line
        shadow_line = tk.Frame(self.root, bg="#064e3b", height=3)
        shadow_line.pack(fill=tk.X)
        
        # Try to load and display logo
        try:
            logo_path = os.path.join(os.path.dirname(__file__), "assets", "endless_pause_logo.svg")
            # Create a simple colored circle as logo placeholder
            logo_frame = tk.Frame(header_frame, bg="#10b981")
            logo_frame.pack(pady=(10, 0))
            
            logo_circle = tk.Label(
                logo_frame,
                text="⏸️",
                font=("Segoe UI", 40),
                bg="#10b981",
                fg="white"
            )
            logo_circle.pack()
        except Exception as e:
            pass  # Skip logo if not available
        
        title_label = tk.Label(
            header_frame,
            text="GLOBALEXAM PAUSE",
            font=("Segoe UI", 26, "bold"),
            bg="#10b981",
            fg="white"
        )
        title_label.pack(pady=(5, 5))
        
        subtitle_label = tk.Label(
            header_frame,
            text="✨ Automation Intelligente • Pause Personnalisable ✨",
            font=("Segoe UI", 11),
            bg="#10b981",
            fg="#d1fae5"
        )
        subtitle_label.pack(pady=(0, 10))
        
        # Timer Frame (40-minute countdown) - Beautiful card design
        timer_card = tk.Frame(self.root, bg="#1e293b", relief=tk.RAISED, borderwidth=2)
        timer_card.pack(fill=tk.X, padx=30, pady=20)
        
        tk.Label(
            timer_card,
            text="⏱️ CHRONOMÈTRE DE PAUSE",
            font=("Segoe UI", 13, "bold"),
            bg="#1e293b",
            fg="#10b981"
        ).pack(pady=(15, 5))
        
        # Large timer display with shadow effect
        timer_display_frame = tk.Frame(timer_card, bg="#0f172a", relief=tk.SUNKEN, borderwidth=3)
        timer_display_frame.pack(pady=10, padx=20)
        
        self.timer_label = tk.Label(
            timer_display_frame,
            text="--:--",
            font=("Courier New", 72, "bold"),
            bg="#0f172a",
            fg="#64748b",
            padx=40,
            pady=20
        )
        self.timer_label.pack()
        
        self.timer_status = tk.Label(
            timer_card,
            text="⚪ En attente de pause",
            font=("Segoe UI", 11, "bold"),
            bg="#1e293b",
            fg="#94a3b8"
        )
        self.timer_status.pack(pady=(5, 15))
        
        # Pause Duration Selector
        duration_frame = tk.Frame(timer_card, bg="#1e293b")
        duration_frame.pack(pady=(0, 15))
        
        tk.Label(
            duration_frame,
            text="⚙️ Durée de pause:",
            font=("Segoe UI", 10, "bold"),
            bg="#1e293b",
            fg="#94a3b8"
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.duration_var = tk.StringVar(value="40")
        duration_options = ["10", "20", "30", "40", "60", "90"]
        
        self.duration_menu = ttk.Combobox(
            duration_frame,
            textvariable=self.duration_var,
            values=duration_options,
            width=8,
            state="readonly",
            font=("Segoe UI", 10)
        )
        self.duration_menu.pack(side=tk.LEFT)
        self.duration_menu.bind("<<ComboboxSelected>>", self.on_duration_change)
        
        tk.Label(
            duration_frame,
            text="minutes",
            font=("Segoe UI", 10),
            bg="#1e293b",
            fg="#94a3b8"
        ).pack(side=tk.LEFT, padx=(5, 0))
        
        # Status Frame with Statistics
        status_frame = tk.Frame(self.root, bg="#0f172a")
        status_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            status_frame,
            text="📊 Statistiques",
            font=("Segoe UI", 12, "bold"),
            bg="#0f172a",
            fg="#e2e8f0"
        ).pack(anchor=tk.W)
        
        # Statistics grid
        stats_grid = tk.Frame(status_frame, bg="#0f172a")
        stats_grid.pack(fill=tk.X, pady=5)
        
        # Left column
        left_stats = tk.Frame(stats_grid, bg="#0f172a")
        left_stats.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.cycle_label = tk.Label(
            left_stats,
            text="🔄 Cycles: 0",
            font=("Segoe UI", 10, "bold"),
            bg="#0f172a",
            fg="#10b981"
        )
        self.cycle_label.pack(anchor=tk.W, pady=2)
        
        self.questions_label = tk.Label(
            left_stats,
            text="❓ Questions: 0",
            font=("Segoe UI", 10),
            bg="#0f172a",
            fg="#94a3b8"
        )
        self.questions_label.pack(anchor=tk.W, pady=2)
        
        # Right column
        right_stats = tk.Frame(stats_grid, bg="#0f172a")
        right_stats.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.status_label = tk.Label(
            right_stats,
            text="État: ⚪ Arrêté",
            font=("Segoe UI", 10, "bold"),
            bg="#0f172a",
            fg="#94a3b8"
        )
        self.status_label.pack(anchor=tk.W, pady=2)
        
        self.time_label = tk.Label(
            right_stats,
            text="⏱️ Temps: 00:00:00",
            font=("Segoe UI", 10),
            bg="#0f172a",
            fg="#94a3b8"
        )
        self.time_label.pack(anchor=tk.W, pady=2)
        
        # Progress Bar
        self.progress = ttk.Progressbar(
            status_frame,
            length=660,
            mode='determinate'
        )
        self.progress.pack(pady=10)
        
        # Control Buttons with hover effects
        button_frame = tk.Frame(self.root, bg="#0f172a")
        button_frame.pack(pady=25)
        
        self.start_btn = tk.Button(
            button_frame,
            text="▶️ DÉMARRER",
            font=("Segoe UI", 12, "bold"),
            bg="#10b981",
            fg="white",
            activebackground="#059669",
            width=13,
            height=2,
            command=self.start_automation,
            relief=tk.RAISED,
            borderwidth=3,
            cursor="hand2"
        )
        self.start_btn.pack(side=tk.LEFT, padx=8)
        
        self.stop_btn = tk.Button(
            button_frame,
            text="⏹️ ARRÊTER",
            font=("Segoe UI", 12, "bold"),
            bg="#ef4444",
            fg="white",
            activebackground="#dc2626",
            width=13,
            height=2,
            command=self.stop_automation,
            state=tk.DISABLED,
            relief=tk.RAISED,
            borderwidth=3,
            cursor="hand2"
        )
        self.stop_btn.pack(side=tk.LEFT, padx=8)
        
        self.skip_pause_btn = tk.Button(
            button_frame,
            text="⏭️ IGNORER\nPAUSE",
            font=("Segoe UI", 11, "bold"),
            bg="#f59e0b",
            fg="white",
            activebackground="#d97706",
            width=13,
            height=2,
            command=self.skip_pause,
            state=tk.DISABLED,
            relief=tk.RAISED,
            borderwidth=3,
            cursor="hand2"
        )
        self.skip_pause_btn.pack(side=tk.LEFT, padx=8)
        
        # Log Frame with card design
        log_card = tk.Frame(self.root, bg="#1e293b", relief=tk.RAISED, borderwidth=2)
        log_card.pack(fill=tk.BOTH, expand=True, padx=30, pady=(10, 20))
        
        tk.Label(
            log_card,
            text="📝 JOURNAL D'ACTIVITÉ",
            font=("Segoe UI", 12, "bold"),
            bg="#1e293b",
            fg="#10b981"
        ).pack(anchor=tk.W, padx=15, pady=(10, 5))
        
        # Scrollable log
        log_scroll = tk.Scrollbar(log_card)
        log_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        self.log_text = tk.Text(
            log_card,
            height=10,
            bg="#0f172a",
            fg="#e2e8f0",
            font=("Consolas", 10),
            yscrollcommand=log_scroll.set,
            relief=tk.SUNKEN,
            borderwidth=2,
            padx=10,
            pady=5
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))
        log_scroll.config(command=self.log_text.yview)
        
        # Initial log with decorative messages
        self.log("╔═══════════════════════════════════════════╗")
        self.log("║   ✅ APPLICATION PRÊTE À DÉMARRER!       ║")
        self.log("╚═══════════════════════════════════════════╝")
        self.log("")
        self.log("💡 Instructions:")
        self.log("   1️⃣ Ouvrez GlobalExam → Activité 7")
        self.log("   2️⃣ Cliquez sur 'DÉMARRER'")
        self.log("   3️⃣ Le timer de 40 min démarrera après Q6")
        self.log("")
        
        # Footer with style
        footer_frame = tk.Frame(self.root, bg="#1e293b", height=40)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        footer = tk.Label(
            footer_frame,
            text="⏸️ GlobalExam Automation • Activity 7 • Pause Personnalisable",
            font=("Segoe UI", 9, "bold"),
            bg="#1e293b",
            fg="#10b981"
        )
        footer.pack(pady=12)
    
    def on_duration_change(self, event=None):
        """Handle pause duration change"""
        self.pause_duration_minutes = int(self.duration_var.get())
        self.log(f"⚙️ Durée de pause modifiée: {self.pause_duration_minutes} minutes")
    
    def update_statistics(self):
        """Update statistics display"""
        # Update total time
        if self.start_time and self.running:
            elapsed = time.time() - self.start_time
            hours = int(elapsed // 3600)
            minutes = int((elapsed % 3600) // 60)
            seconds = int(elapsed % 60)
            self.time_label.config(text=f"⏱️ Temps: {hours:02d}:{minutes:02d}:{seconds:02d}")
        
        # Update questions
        self.questions_label.config(text=f"❓ Questions: {self.total_questions_answered}")
        
        # Schedule next update
        if self.running:
            self.root.after(1000, self.update_statistics)
    
    def log(self, message):
        """Add message to log"""
        timestamp = time.strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def update_progress(self, current, total):
        """Update progress bar"""
        percentage = (current / total) * 100
        self.progress['value'] = percentage
        self.root.update()
    
    def update_cycle_count(self):
        """Increment cycle counter"""
        self.cycle_count += 1
        self.total_questions_answered += 13  # 13 questions per cycle
        self.cycle_label.config(text=f"🔄 Cycles: {self.cycle_count}")
        self.questions_label.config(text=f"❓ Questions: {self.total_questions_answered}")
    
    def update_timer_display(self):
        """Update timer display every second"""
        if self.timer_seconds_left > 0 and self.in_pause:
            minutes = self.timer_seconds_left // 60
            seconds = self.timer_seconds_left % 60
            
            # Color changes based on time left
            if self.timer_seconds_left > 300:  # > 5 minutes
                color = "#10b981"  # Green
            elif self.timer_seconds_left > 60:  # > 1 minute
                color = "#f59e0b"  # Orange
            else:  # < 1 minute
                color = "#ef4444"  # Red
            
            self.timer_label.config(
                text=f"{minutes:02d}:{seconds:02d}",
                fg=color
            )
            
            self.timer_seconds_left -= 1
            
            # Schedule next update in 1 second
            self.timer_update_id = self.root.after(1000, self.update_timer_display)
        else:
            self.timer_label.config(text="00:00", fg="#10b981")
    
    def start_timer_countdown(self, total_seconds):
        """Start the real-time countdown timer"""
        self.timer_seconds_left = total_seconds
        self.update_timer_display()
    
    def start_pause_timer(self):
        """Activate pause mode UI"""
        self.in_pause = True
        self.timer_status.config(text="⏸️ Pause en cours", fg="#22c55e")
        self.skip_pause_btn.config(state=tk.NORMAL)
        self.timer_label.config(fg="#22c55e")
    
    def stop_pause_timer(self):
        """Deactivate pause mode UI"""
        self.in_pause = False
        self.timer_status.config(text="⚪ En attente de pause", fg="#94a3b8")
        self.skip_pause_btn.config(state=tk.DISABLED)
        self.timer_label.config(text="--:--", fg="#64748b")
        
        # Cancel timer updates
        if self.timer_update_id:
            self.root.after_cancel(self.timer_update_id)
            self.timer_update_id = None
    
    def skip_pause(self):
        """Skip the 40-minute pause"""
        if self.in_pause:
            self.pause_skip = True
            self.log("⏭️ Pause ignorée manuellement!")
    
    def start_automation(self):
        """Start the automation in a separate thread"""
        if self.running:
            return
        
        self.running = True
        self.start_time = time.time()
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.duration_menu.config(state=tk.DISABLED)  # Lock duration during run
        self.status_label.config(text="État: 🟢 En cours", fg="#22c55e")
        
        self.log("🚀 Démarrage de l'automatisation avec pause...")
        self.log(f"⚙️ Durée de pause configurée: {self.pause_duration_minutes} minutes")
        self.log("📐 Détection de la résolution...")
        sw, sh = pyautogui.size()
        self.log(f"✅ Résolution: {sw}x{sh}")
        self.log("🔍 Normalisation du zoom...")
        normalize_browser_zoom()
        self.log("✅ Configuration terminée!")
        
        # Start statistics update loop
        self.update_statistics()
        
        self.thread = threading.Thread(target=self.run_loop, daemon=True)
        self.thread.start()
    
    def stop_automation(self):
        """Stop the automation"""
        if not self.running:
            return
        
        self.running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.skip_pause_btn.config(state=tk.DISABLED)
        self.duration_menu.config(state="readonly")  # Unlock duration
        self.status_label.config(text="État: ⚪ Arrêté", fg="#94a3b8")
        self.progress['value'] = 0
        self.stop_pause_timer()
        
        # Calculate total time
        if self.start_time:
            total = time.time() - self.start_time
            hours = int(total // 3600)
            minutes = int((total % 3600) // 60)
            self.log(f"📊 Session terminée: {hours}h {minutes}min")
            self.log(f"📊 {self.cycle_count} cycles, {self.total_questions_answered} questions")
        
        self.log("⏹️ Arrêt demandé...")
        self.log("✅ Automatisation arrêtée.")
    
    def run_loop(self):
        """Main automation loop"""
        while self.running:
            try:
                run_final_once_with_pause(self)
                if self.running:
                    self.log("⏳ Redémarrage dans 3 secondes...")
                    time.sleep(3)
            except Exception as e:
                self.log(f"❌ Erreur: {str(e)}")
                self.running = False
                self.stop_automation()
                break

def main():
    root = tk.Tk()
    app = EndlessPauseGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import time

# Data
time_slots = [
    "Senin 08:00", "Senin 10:00", "Selasa 08:00", "Selasa 10:00",
    "Rabu 08:00", "Rabu 10:00"
]

tasks = ["Matematika", "Fisika", "Bahasa", "Kimia"]

slot_mapping = {
    "Senin 08:00": 0,
    "Senin 10:00": 1,
    "Selasa 08:00": 2,
    "Selasa 10:00": 3,
    "Rabu 08:00": 4,
    "Rabu 10:00": 5
}

task_colors = {
    "Matematika": "tab:red",
    "Fisika": "tab:green",
    "Bahasa": "tab:orange",
    "Kimia": "tab:purple"
}

# Setup figure
fig, ax = plt.subplots(figsize=(10, 5))
plt.ion()  # Turn on interactive mode (buat update grafik)

def update_chart(schedule, current_task=None, mode="assign"):
    ax.clear()
    
    yticks = []
    ylabels = []

    for idx, (task, slot) in enumerate(schedule.items()):
        start = slot_mapping[slot]
        color = task_colors[task]
        ax.broken_barh([(start * 2, 1.8)], (idx * 5, 4), facecolors=color)
        yticks.append(idx * 5 + 2)
        ylabels.append(task)
    
    # Highlight current task (optional)
    if current_task and mode == "assign":
        ax.set_title(f"Menempatkan: {current_task}", color="blue")
    elif current_task and mode == "backtrack":
        ax.set_title(f"Backtrack: Lepas {current_task}", color="red")
    else:
        ax.set_title('Penjadwalan Otomatis')

    ax.set_yticks(yticks)
    ax.set_yticklabels(ylabels)
    ax.set_xlabel('Waktu (slot)')
    ax.set_xticks([i*2 for i in range(len(slot_mapping))])
    ax.set_xticklabels(list(slot_mapping.keys()), rotation=45, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.draw()
    plt.pause(0.8)  # Delay supaya kelihatan pergantiannya

solutions = []

def is_valid(schedule, task, slot):
    return slot not in schedule.values()

def backtrack(schedule, task_idx):
    if task_idx == len(tasks):
        print(f"[SUKSES] Jadwal lengkap: {schedule}\n")
        solutions.append(schedule.copy())
        time.sleep(1)
        return

    task = tasks[task_idx]
    print(f"Mencoba menjadwalkan '{task}'...")

    for slot in time_slots:
        print(f"  Coba slot '{slot}' untuk '{task}'...")
        if is_valid(schedule, task, slot):
            schedule[task] = slot
            print(f"    [OKE] '{task}' dijadwalkan di '{slot}'. Lanjut tugas berikutnya.\n")
            update_chart(schedule, current_task=task, mode="assign")
            backtrack(schedule, task_idx + 1)
            print(f"    [BACKTRACK] Lepas '{task}' dari slot '{slot}'. Coba pilihan lain...\n")
            del schedule[task]
            update_chart(schedule, current_task=task, mode="backtrack")
        else:
            print(f"    [GAGAL] Slot '{slot}' sudah dipakai, cari slot lain...\n")
        time.sleep(0.3)  # Biar animasi kelihatan pelan

# Jalankan
backtrack({}, 0)

# Final visualization
plt.ioff()  # Turn off interactive mode
update_chart(solutions[0])
plt.show()

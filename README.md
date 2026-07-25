# 🖥️ System Monitor (Python)

A terminal-based real-time system monitoring tool built with **Python** and **psutil**. It continuously monitors system resources such as CPU, RAM, disk usage, network activity, uptime, and running processes. The application also supports **Docker**, **Docker Compose**, automatic **CSV logging**, and runs on both **Windows** and **Linux**.

---

## 🚀 Features

- 📊 Real-time CPU usage monitoring
- 🧠 RAM usage monitoring
- 💾 Disk usage monitoring
  - Windows: C: and D: drives
  - Linux: Root (`/`) filesystem
- 🌐 Upload & Download speed monitoring
- ⏱️ System uptime
- 🖥️ Physical CPU core count
- 📋 Top 5 processes by RAM usage
- ⚡ Top 5 processes by CPU usage
- 🎨 Color-coded terminal output
- 📈 Progress bars for resource usage
- 📝 Automatic CSV logging
- 🐳 Docker support
- 📦 Docker Compose support
- 💻 Cross-platform compatibility (Windows & Linux)

---

## 🛠️ Tech Stack

- Python 3
- psutil
- colorama
- CSV
- Docker
- Docker Compose

---

## 📂 Project Structure

```
system-monitor-python/
│── main.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── .gitignore
│── logs/
└── README.md
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/damini-gidwani/system-monitor-python.git
cd system-monitor-python
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Locally

```bash
python main.py
```

---

# 🐳 Run with Docker

### Build the Docker image

```bash
docker build -t system-monitor .
```

### Run the container

```bash
docker run system-monitor
```

---

# 📦 Run with Docker Compose

```bash
docker compose up 
```

To stop the application:

```bash
docker compose down
```

---

# 📝 CSV Logging

The application automatically generates a CSV log file for every monitoring session.

Each log contains:

- Timestamp
- CPU Usage
- RAM Usage
- Disk Usage
- Upload Speed
- Download Speed

Logs are stored inside the **logs/** directory.

---

# 🌍 Cross-Platform Support

### Windows

- Monitors **C:** and **D:** drives
- Uses `cls` to clear the terminal

### Linux

- Monitors the **Root (`/`)** filesystem
- Uses `clear` to clear the terminal

---


# 🔮 Future Improvements

- Export logs to Excel
- Historical performance graphs
- Email notifications for high resource usage
- Configurable refresh interval
- Multi-disk monitoring
- Web dashboard using Streamlit or Flask

---

# 👨‍💻 Author

**Damini Gidwani**

GitHub: https://github.com/damini-gidwani

---

⭐ If you found this project helpful, consider giving it a star!

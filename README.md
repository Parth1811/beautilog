Here’s a clean, developer-friendly **README.md** for your `fancy-log` project, including setup instructions, config usage, and examples:

---

# 🌈 Fancy-Log

**Fancy-Log** is a Python logging library for beautiful, color-coded terminal output with support for custom log levels, file logging, and simple JSON configuration.

> ✨ *Because logs should be readable, not regrettable.*

---

## 📦 Installation

```bash
pip install -e .
```

Make sure `tqdm==4.66.5` is installed — it’s required for smooth console output.

---

## ⚙️ Configuration: `fancy-log.json`

Place a `fancy-log.json` file in your project root or in the same directory as the library. Here's a sample configuration:

```json
{
  "save_to_file": true,
  "file_logger": {
    "log_file_path": "fancy-run.log",
    "backup_count": 5,
    "max_bytes": 104857600,
    "log_level": "DEBUG"
  },
  "suppress_other_loggers": true,
  "log_level": "INFO",
  "custom_levels": {
    "NOTIFICATION": 12
  },
  "level_colors": {
    "CRITICAL": "RED",
    "ERROR": "BRIGHT_RED",
    "WARNING": "YELLOW",
    "INFO": "CYAN",
    "NOTIFICATION": "GREEN",
    "DEFAULT": "RESET"
  }
}
```

### 🔍 Config Options

| Key                      | Description                                             |
| ------------------------ | ------------------------------------------------------- |
| `save_to_file`           | Whether to enable file logging                          |
| `file_logger`            | File logging options (path, size, level, backups)       |
| `log_level`              | Default log level (`DEBUG`, `INFO`, `ERROR`, etc.)      |
| `custom_levels`          | Add your own custom levels (e.g. `NOTIFICATION`)        |
| `level_colors`           | Map log levels to terminal colors                       |
| `suppress_other_loggers` | Optionally suppress 3rd party logs like `asyncio`, etc. |

---

## 🚀 Example Usage

```python
from fancy_log import logger

logger.info("This is an info message.")
logger.warning("This is a warning.")
logger.error("This is an error!")

# Use custom log level
logger.log(logger.NOTIFICATION, "Custom NOTIFICATION level log")
```

> ✅ Custom log levels like `NOTIFICATION` are registered automatically from the config.

---

## 🎨 Supported Colors

You can use any of these in the `level_colors` config:

* `"RED"`, `"YELLOW"`, `"GREEN"`, `"BLUE"`, `"MAGENTA"`, `"CYAN"`, `"WHITE"`
* `"BRIGHT_RED"`, `"BRIGHT_YELLOW"`, `"BRIGHT_GREEN"`, `"BRIGHT_BLUE"`, etc.
* `"RESET"` for default terminal color

---

## 📂 Log File Output

If `save_to_file` is enabled, logs will be saved to `fancy-run.log` (or the path you set in `file_logger.log_file_path`). It uses a **rotating file handler** with backup and size limits.

---

## 💡 Tips

* To disable logging to a file, set `"save_to_file": false` in the config.
* To see all messages (including `DEBUG`), lower the `log_level` in the config.

---

## 🧪 Development

Want to test it quickly?

```bash
python -c 'from fancy_log import logger; logger.info("hello from fancy-log!")'
```

---

## 📜 License

Apache License 2.0 — free for personal and commercial use.

---
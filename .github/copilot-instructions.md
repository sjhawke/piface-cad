# Copilot Instructions

## Project Overview

Python 3 clock application for a Raspberry Pi with a [PiFace Control and Display](http://www.piface.org.uk/) (CAD) — a 16×2 LCD + hardware buttons attachment. The app cycles through time, date, and weather on the LCD every 10 seconds.

## Commands

Activate the virtualenv first:
```bash
. ./venv/bin/activate
pip install -r requirements.txt
```

Run all tests:
```bash
pytest
```

Run a single test:
```bash
pytest tests/test_writethetime.py::TestGetTimeAsWords::testMidnight
```

Lint:
```bash
pylint clock.py lib/
```

Run on the Pi (requires hardware + env vars set):
```bash
cp startclock-template.sh startclock.sh
# edit startclock.sh with real API keys and coordinates
./startclock.sh
```

## Architecture

- **`clock.py`** — main loop. Attempts to import the `pifacecad` hardware library and falls back to `lib.pifacecad_mock` when unavailable. Rotates display content based on `datetime.second`: time (0–9s), date (10–18s), weather (19–28s), then repeats.
- **`lib/writethetime.py`** — converts a `datetime` to a natural-English phrase ("Quarter Past Two AM").
- **`lib/writethedate.py`** — converts a `datetime` to a display string ("Sun 28th of February 2016").
- **`lib/writetheweather.py`** — fetches current weather + UV index from OpenWeatherMap (two API calls). Returns a formatted string ≤ 32 chars for the LCD.
- **`lib/lcdtextprocessing.py`** — `wrap_16_x_2(text)` wraps and **center-aligns** text into lines of up to 16 characters, returning 1–3 `\n`-separated lines for display and related tests.
- **`lib/display.py`** — additional display helpers.

## Key Conventions

**`pifacecad` is hardware-only.** It is not in `requirements.txt` and is not available in the venv or CI. `clock.py` has `# pylint: disable=E0401` on that import and falls back to `lib.pifacecad_mock` when the hardware library is missing. Never import `pifacecad` in `lib/` modules — all `lib/` code must be testable without hardware.

**LCD output targets a 16×2 display.** Any string intended for the LCD must pass through `lcdtextprocessing.wrap_16_x_2()`, which keeps each line to 16 characters and returns 1–3 `\n`-separated lines. Tests in `test_writethetime.py::Testwrap_16_x_2::testVerifyAllTimes` assert that every possible time string stays within those constraints.

**Weather config via environment variables.** `writetheweather.py` reads `apikey`, `locationkey`, `lat`, and `lon` from `os.environ`. These are never hardcoded; set them in `startclock.sh` (which is gitignored — use `startclock-template.sh` as the template).

**Tests use `unittest.TestCase` style but run under pytest.** `setup.cfg` configures pytest to skip `venv/` and other non-source directories.

**`.pylintrc`** ignores test files matching `test_*.py` and `*_test.py`.

## MCP servers

If you want Copilot sessions to use MCP servers for remote testing or hardware access, reply with which server(s) to configure and any connection details. Common options for this repository (pick one or describe your own):

- `raspberrypi-ssh` — an SSH-accessible Raspberry Pi where `clock.py` can be executed against real PiFace hardware (useful for hardware-in-the-loop testing).
- `ssh-runner` — a generic SSH runner that can run tests on an environment matching the Pi (if you can provide an image or credentials).

Tell me which MCP server to add and provide any hostnames/credentials (or say "none"). I will add the appropriate configuration files and CI integration on the branch.

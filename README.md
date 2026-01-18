# robots-playground
Having fun programming robots

# Prerequisites

Some scripts may require `asyncio`. Here are the instructions to install the library.

## Mount Eliobot as mass storage device

Edit `boot.py` to have this
```python
import board
import storage

# Write options : True = Mass Storage, False = REPL
storage.remount("/", True)
```

## Restart Eliobot

Disconnect / reconnect the USB cable or press reset

## Install `circup` if not already present:

```bash
pip3 install circup
```

## Install the `asyncio` module

```bash
circup --path /Volumes/ELIOBOT install asyncio
```

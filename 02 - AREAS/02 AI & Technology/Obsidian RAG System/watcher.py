#!/usr/bin/env python3
import time
import os
from watchdog.observers import Observer
from watchdog.events import (
    FileModifiedEvent,
    FileCreatedEvent,
    FileDeletedEvent,
    FileSystemEventHandler,
)
from ingest import index_vault

VAULT_DIR = "./vault"


class VaultHandler(FileSystemEventHandler):
    def __init__(self):
        self.last_index_time = 0
        self.cooldown = 3

    def on_any_event(self, event):
        if event.is_directory:
            return

        if not isinstance(
            event, (FileModifiedEvent, FileCreatedEvent, FileDeletedEvent)
        ):
            return

        if not str(event.src_path).endswith(".md"):
            return

        current_time = time.time()
        if current_time - self.last_index_time > self.cooldown:
            self.last_index_time = current_time
            print(f"\n[Watcher] Change detected: {event.event_type} {event.src_path}")
            print("[Watcher] Re-indexing vault...")
            try:
                count = index_vault()
                print(f"[Watcher] Re-indexed {count} chunks\n")
            except Exception as e:
                print(f"[Watcher] Indexing failed: {e}\n")


def watch_vault():
    print(f"Starting file watcher for: {VAULT_DIR}")
    print("Monitoring for .md file changes...")
    print("Press Ctrl+C to stop\n")

    os.makedirs(VAULT_DIR, exist_ok=True)

    event_handler = VaultHandler()
    observer = Observer()
    observer.schedule(event_handler, path=VAULT_DIR, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Watcher] Stopping...")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    watch_vault()

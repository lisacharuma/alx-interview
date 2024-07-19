#!/usr/bin/python3
"""Task 0 module"""


def canUnlockAll(boxes):
    """checks if all boxes can be unlocked"""
    if not boxes:
        return False
    keychain = set([0])  # Start with the first box already unlocked
    unlocked = set([0])  # Keep track of unlocked boxes

    while True:
        new_keys = set()
        for key in keychain:
            if key < len(boxes):
                for new_key in boxes[key]:
                    if new_key not in unlocked:
                        new_keys.add(new_key)
        if not new_keys:
            break
        keychain.update(new_keys)
        unlocked.update(new_keys)
    return len(unlocked) == len(boxes)

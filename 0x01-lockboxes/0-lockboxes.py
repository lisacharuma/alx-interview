#!/usr/bin/python3
"""Task 0 module"""


def canUnlockAll(boxes):
    """checks if all boxes can be unlocked"""
    keychain = {0}
    padlocks = set(range(len(boxes)))
    for _ in boxes:
        for padlock in padlocks:
            if padlock in keychain:
                keychain.update(boxes[padlock])
    return padlocks <= keychain

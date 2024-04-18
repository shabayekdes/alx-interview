#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.

    Args:
        boxes (list of list of int): Each box contains a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''

    num_boxes = len(boxes)
    keys = set()
    opened_boxes = set()
    stack = [0]

    while stack:
        box_index = stack.pop()
        opened_boxes.add(box_index)
        keys.update(boxes[box_index])

        for key in keys:
            if 0 <= key < num_boxes and key not in opened_boxes:
                stack.append(key)

    return len(opened_boxes) == num_boxes

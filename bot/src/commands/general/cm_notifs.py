"""
file: src/commands/admin/cm_notifs.py
function:
    Responsible for handling notifications and alerts being sent to the user/users.
commands:
    - /notifications subscribe [project]
    - /notifications unsubscribe [project]
    - /notifications subscribe [project] [event]
    - /notifications unsubscribe [project] [event]
    - /notifications list
    - /notifications status
"""

import os
import sys
import asyncio

from discord.ext import commands, tasks

# TODO: Implement cm_notifs.py commands/tasks.
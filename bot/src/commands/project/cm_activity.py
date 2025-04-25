"""
file: src/commands/project/cm_activity.py
function:
    Responsible for handling /activity based commands for contribot.
commands:
    - /activity me [timespan]
    - /activity all [timespan]
    - /activity view [user] [timespan]
    - /activity view [user] [timespan] [on_dashboard?=True | False]
"""

import os
import sys
import asyncio

from discord.ext import commands, tasks

# TODO: Implement cm_activity.py commands/tasks.

"""
file: src/commands/general/cm_info.py
function:
    Responsible for handling information about contribot, its version, and other metadata.
commands:
    - /info
    - /info [project]
    - /info [project] [version]
"""

import os
import sys
import asyncio

from discord.ext import commands, tasks

# TODO: Implement cm_info.py commands/tasks.
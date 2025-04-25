"""
file: src/commands/general/cm_account.py
function:
    Responsible for handling account-related commands and tasks.
commands:
    -/account link [platform]
    -/account unlink [platform]
    -/account view
    -/account view [platform]
"""

import os
import sys
import asyncio

from discord.ext import commands, tasks

# TODO: Implement cm_account.py commands/tasks.
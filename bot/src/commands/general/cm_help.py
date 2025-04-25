"""
file: src/commands/general/cm_help.py
function:
    Responsible for providing helpful information on contribots commands and subcommands.
commands:
    - /help
    - /help list
    - /help [command]
    - /help [command] [subcommand]
"""

import os
import sys
import asyncio

from discord.ext import commands, tasks

# TODO: Implement cm_help.py commands/tasks.
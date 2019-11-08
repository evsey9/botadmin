#!/bin/bash
python3 manage.py dumpdata bot.command bot.day bot.genericanswer bot.situationanswer --output bot/datadumps/BaseData.json --indent 4

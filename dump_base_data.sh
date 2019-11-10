#!/bin/bash
python3 manage.py dumpdata bot.command bot.day bot.genericanswer bot.situationanswer --output bot/fixtures/BaseData.json --indent 4

#!/bin/bash
python3 manage.py dumpdata bot.command bot.day bot.genericanswer bot.situationanswer bot.group bot.location bot.teacher bot.subject bot.signup bot.eventtype bot.event --output bot/fixtures/AllData.json --indent 4

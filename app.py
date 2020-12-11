#!/usr/bin/env python3

from aws_cdk import core

from update_alarm.update_alarm_stack import UpdateAlarmStack


app = core.App()
UpdateAlarmStack(app, "update-alarm")

app.synth()

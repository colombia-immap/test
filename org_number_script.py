#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io

f = io.open("../lista correos boletin.txt", mode="r", encoding="utf-8")
lines=f.readlines()
orgs = []
count_gmail = 0
for line in lines:
	org = str(line.split("@")[1].split('.')[0])
	if  org != 'gmail':
		orgs.append(org)
		pass
	else:
		count_gmail += 1
		pass

orgs_clean = list(dict.fromkeys(orgs))
print orgs_clean, count_gmail, len(orgs_clean)
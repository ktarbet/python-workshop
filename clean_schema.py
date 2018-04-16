#!/usr/bin/env python
# usage: clean_schema file.sql exclude-table-pattern
#
# parse database dump from pg_dumpall
# create a lean schema by removing tables matching a pattern
#
# ALTER TABLE pattern
# CREATE TABLE pattern

import sys
import re

if len(sys.argv) != 3:
  print("usage "+ sys.argv[0]+' filename.sql exclude-table-pattern')
  sys.exit()

alter = 'ALTER TABLE '+sys.argv[2]
alter_only = 'ALTER TABLE ONLY '+sys.argv[2]
create = 'CREATE TABLE '+sys.argv[2]
grant = 'GRANT SELECT ON TABLE '+sys.argv[2]
with open(sys.argv[1],) as f:
  lines = f.readlines()

idx=0
max=len(lines)
while idx <max :
  if alter in lines[idx] or create in lines[idx] or grant in lines[idx]:
    #find semi-colon ';' then start printing again
    while ';' not in lines[idx]:
      idx=idx+1
    idx=idx+1

  else:
    #print(lines[idx])
    idx=idx+1


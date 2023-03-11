import logging as log

a = 0
b = 5

try:
    c = b / a
except Exception as exc:
    log.exception('An exception occured')

#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentence)
    frst = sentence[0] if len(sentence) > 0 else None
    return (len, frst)

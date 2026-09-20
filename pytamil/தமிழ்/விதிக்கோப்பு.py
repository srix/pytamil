# -*- coding: utf-8 -*-
"""
விதிக்கோப்பு — shared walker for the YAML rule files.

புணர்ச்சிவிதிகள்.yaml and மாத்திரை.yaml share one shape: dicts nested inside dicts, lists at
the leaves, and list entries keyed 'விதி' or 'சான்று'. Walking that tree is the same code in
both places, so it lives here once. Turning a விதி or a சான்று into an object stays with the
module that owns it.

    for txt in items(entries, 'விதி'): ...
"""


def items(entries, key):
    """Yield the value of every `key` entry found anywhere in the nested YAML structure."""
    for name in entries:
        value = entries[name]
        if isinstance(value, dict):
            yield from items(value, key)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict) and key in item:
                    yield item[key]

#!/usr/bin/env python3

# Python3 code to demonstrate working of
# Convert String to unicode characters
# using re.sub() + ord() + lambda
import re

test_str = 'Uncomment string'

#            0000000000111111111122222222223333333333444444
#            0123456789012345678901234567890123456789012345
#test_str = '                ┏━━━━━━━━━━━━┓                '#0
#test_str = '             ╭─❱┃  xxxxxx  ❋ ┃──╮             '#1
#test_str = '             │  ┃────────────┃  │             '#2
#test_str = '             │  ┃  xxxxxx  ❋ ┃  │             '#3
#test_str = '━━━━000000━❋╾╯  ┃────────────┃  ╰╼━━000000━━━❱'#4
#test_str = '                ┃  xxxxxx  ❋ ┃                '#5
#test_str = '                ┃────────────┃                '#6
#test_str = '                ┃  xxxxxx  ❋ ┃                '#7
#test_str = '                ┡━━━━━━━━━━━━┩                '#8
#test_str = '                │000      000│                '#9
#test_str = '････!valid･････❭│push   empty│───────valid───❭'#10
#test_str = '❮───ready───────│full     pop│❬･････!ready････'#11
#test_str = '                └────────────┘                '#12


#            00000000001
#            01234567890
#test_str = '┌────────┐'#0
#test_str = '│        │'#1
#test_str = '│ CUSTOM │'#2
#test_str = '│ LOGIC  │'#3
#test_str = '│        │'#4
#test_str = '│ debug: │'#5
#test_str = '│◌◌◌◌◌◌◌◌│'#6
#test_str = '│        │'#7
#test_str = '│        │'#8
#test_str = '└────────┘'#9

#◉ ◊ ○ ◌

#test_str = 'MODEL_QUEUE'

#            0000000000111111111122222222223
#            0123456789012345678901234567890
#test_str = ' ┌────────┐┌────────┐┏━━━━━━━━┓'#0
#test_str = '┌│ xxxxxx ││ xxxxxx │┃ xxxxxx ┃'#8
#test_str = '│└────────┘└────────┘┗━━━━━━━━┛'#9
#test_str = '└────────┘     queue_size:5    '#10


#            000000000011111111112222222222333333
#            012345678901234567890123456789012345
#test_str = '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'#0
#test_str = '┃  ┌────────┐┌────────┐┏━━━━━━━━┓  ┃'#1
#test_str = '┃ ▐│ xxxxxx ││ xxxxxx │┃ xxxxxx ┃  ┃'#2
#test_str = '┃ ▐└────────┘└────────┘┗━━━━━━━━┛  ┃'#3
#test_str = '┃ ▝▀▀▀▀▀▀▀▀▀     queue_size:5      ┃'#4
#test_str = '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'#5


#            000000000011111111112222222222333333
#            012345678901234567890123456789012345
#test_str = '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'#0
#test_str = '┃                      ┏        ┓  ┃'#1
#test_str = '┃                                  ┃'#2
#test_str = '┃                      ┗        ┛  ┃'#3
#test_str = '┃                queue_size:5      ┃'#4
#test_str = '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'#5

#            000000000011111111112222222222333333
#            012345678901234567890123456789012345
#test_str = '┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓'
#test_str = '┃                                  ┃'
#test_str = '┃                                  ┃'
#test_str = '┃                                  ┃'
#test_str = '┃                queue_size:       ┃'
#test_str = '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'

#test_str = '┌─────────────┐'#0
#test_str = '│ ----------- │'#1
#test_str = '└─────────────┘'#2

#test_str = 'NO_MATCH!!!'
#test_str = ''

#test_str = '-----------'


#####UP######################
#            ━━━━000000━◉╾╯
#UP_VALID
#            ────valid──────❯
#            ････!valid･････❭
#            ××××?valid×××××❭

#UP_READY
#            ❮───ready───────
#            ❬･･･!ready･･････
#            ❬×××?ready××××××

#####DOWN####################
#              ╰╼━━000000━━━❱
#DOWN_VALID
#            ───────valid───❯
#            ･･････!valid･･･❭
#            ××××××?valid×××❭
#DOWN_READY
#            ❮──────ready────
#            ❬･････!ready････
#            ❬×××××?ready××××



#            0000000000111111111122222222223333333333444444
#            0123456789012345678901234567890123456789012345
#test_str = '╔════════════════════════════════════════════╗'#0
#test_str = '║ reset        ○        - "R-key"            ║'#1
#test_str = '║ up_valid     ○        - "A-key"            ║'#2
#test_str = '║ up_data      ◉◉◉◉◉◉◉  - "Z,X,C,V,B,N-keys" ║'#3
#test_str = '║ down_ready   ○        - "S-key"            ║'#4
#test_str = '║ Clock                 - "ENTER-key"        ║'#5
#test_str = '║ Quit                  - "ESC-key"          ║'#6
#test_str = '╚════════════════════════════════════════════╝'#7


#test_str = '║ down_ready_a ○        - "s-sym"            ║'#4
#test_str = 'FIFO_B'#4
#test_str = '"A-sym"'#4
#test_str = '"Z,X,C,V,B,N-syms"'
#test_str = 'z Z'
test_str = '❬･････!ready････'


# printing original String
print("The original string is : " + str(test_str))

# using sub() to perform substitutions
# ord() for conversion.
res = (re.sub('.', lambda x: r'\u%04X' % ord(x.group()), test_str))

# printing result
print("The unicode converted String : " + str(res))
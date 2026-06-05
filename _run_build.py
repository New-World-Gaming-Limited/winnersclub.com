# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/user/workspace/winnersclub.com")
import _pages_club as p1
import _pages_club2 as p2
import _pages_club3 as p3
import _pages_club4 as p4

built = []
built.append(p1.build_home())
built.append(p1.build_promo())
built.append(p2.build_about())
built.append(p2.build_reserves())
built.append(p3.build_casino())
built.append(p3.build_sports())
built.append(p3.build_poker())
built.append(p3.build_aviator())
built.append(p4.build_mirror())
built.append(p4.build_payments())
built.append(p4.build_liveodds())
for b in built:
    print(b)
print(f"\n{len(built)} pages built.")

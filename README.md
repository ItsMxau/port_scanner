# Python Port Scanner (Level by Level)
 
Learning project — building a multithreaded port scanner + banner grabber in Python, one file at a time. Each level adds one new thing on top of the last one.
 
## The levels
 
**Level 1 — Single Port Check**
The absolute basics. Check if one port on one host is open, nothing else. This is where sockets, `connect_ex()`, and timeouts get introduced.
 
**Level 2 — Port Range Scan**
Same idea as level 1 but looped over a range of ports (like 1-1000), one at a time. Also times the scan so you can actually see how slow doing this sequentially is, that's on purpose, it's the setup for why threading matters later. Level 2 times the scan on purpose: checking ports one at a time means you’re mostly just waiting, not computing, so it’s slow. Level 3 will check multiple ports at once with threading, so the waiting happens in parallel instead of piling up.

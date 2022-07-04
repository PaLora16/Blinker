Blinker puts in place infrastructure enabling n-senders to be connected to one receiver, or you can bottom-up pattern having many receivers connected to one sender. Thus Blinker sits on the fence between PUB/SUB and the Chain of responsibility pattern.

IMO the best usage is in a Fire and forgets pattern, where you don't need to wait for a response (though Blinker support REQ/RESP pattern too). Imagine you want to request eight different URLs concurrently. You define eight separate receivers, each requests given URL on separate thread. One single command runs jobs on all eight connected receivers at once.

Imagine you have four core processor and want to analyze a big chunk of data. You define four receivers, which run a separate processes on slices of data fanned out by the sender. Each receiver picks up a slice of data belonging to him, leaving another portion untouched. Finishing data analyzing, receiver publish results on "done" signal to a another receiver, which collects all results, normalize data and presents final results.

I prepared a simple but functional demo of how to implement the Chain of responsibility pattern using Blinker.

See bulbs.py for helper&definition functionality and main.py for its usage.

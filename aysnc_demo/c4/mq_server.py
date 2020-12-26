# -*- coding: utf-8 -*-

import asyncio
from asyncio import StreamReader, StreamWriter, gather
from collections import deque, defaultdict
from typing import Deque, DefaultDict
from .msgproto import read_msg, send_msg

# A global collection of currently active subscribers.
# Every time a client connects, they must first send a channel name they’re subscribing to.
# A deque will hold all the subscribers for a particular channel.
SUBSCRIBERS: DefaultDict[bytes, Deque] = defaultdict(deque)


async def client(reader: StreamReader, writer: StreamWriter):
    # shown how the host and port of the remote peer can be obtained, for example, for logging.
    peername = writer.get_extra_info('peername')
    subscribe_chan = await read_msg(reader)
    # Add the StreamWriter instance to the global collection of subscribers.
    SUBSCRIBERS[subscribe_chan].append(writer)
    print(f'Remote {peername} subscribed to {subscribe_chan}')

    try:
        while channel_name := await read_msg(reader):
            data = await read_msg(reader)
            print(f'Sending to {channel_name}: {data[:19]}...')
            # Get the deque of subscribers on the target channel.
            conns = SUBSCRIBERS[channel_name]
            if conns and channel_name.startswith(b'/queue'):
                conns.rotate(1)
                conns = [conns[0]]
            await gather(*[send_msg(c, data) for c in conns])
    except asyncio.CancelledError:
        print(f'Remote {peername} closing connection.')
        writer.close()
        await writer.wait_closed()
    except asyncio.IncompleteReadError:
        print(f'Remote {peername} disconnected')
    finally:
        print(f'Remote {peername} closed')
        SUBSCRIBERS[subscribe_chan].remove(writer)


async def main(*args, **kwargs):
    server = await asyncio.start_server(*args, **kwargs)
    async with server:
        await server.serve_forever()


try:
    asyncio.run(main(client, host='127.0.0.1', port=25000))
except KeyboardInterrupt:
    print("Bye!")

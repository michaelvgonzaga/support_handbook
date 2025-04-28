import asyncio
import websockets
import os
import pty
import sys

async def shell(websocket):
    pid, fd = pty.fork()
    if pid == 0:
        # Child process: execute the shell
        print("👶 Child process starting shell...")
        os.execvp("/bin/zsh", ["/bin/zsh", "-i"])
    else:
        print(f"👨‍💻 Parent process, PID: {pid}")
        loop = asyncio.get_event_loop()

        async def from_fd():
            try:
                while True:
                    data = await loop.run_in_executor(None, os.read, fd, 1024)
                    if data:
                        print(f"💬 Sending data from shell: {data.decode(errors='ignore')}")
                        if websocket.open:
                            await websocket.send(data.decode(errors="ignore"))
                        else:
                            print("❌ WebSocket closed before sending data.")
                            break
                    else:
                        print("🛑 Shell closed (EOF).")
                        break
            except Exception as e:
                print(f"[from_fd] Error: {e}", file=sys.stderr)

        async def from_ws():
            try:
                async for message in websocket:
                    print(f"💬 Received message from client: {message}")
                    if websocket.open:
                        os.write(fd, message.encode())
                    else:
                        print("❌ WebSocket closed before writing to shell.")
                        break
            except Exception as e:
                print(f"[from_ws] Error: {e}", file=sys.stderr)

        await asyncio.gather(from_fd(), from_ws())

async def handler(websocket, _path):
    print("🔌 New WebSocket connection.")
    try:
        await shell(websocket)
    except Exception as e:
        print(f"❌ Handler error: {e}", file=sys.stderr)
    finally:
        print("🚪 WebSocket client disconnected.")

async def main():
    try:
        print("🚀 Starting WebSocket server...")
        async with websockets.serve(handler, "0.0.0.0", 9001):
            print("✅ Server ready at ws://localhost:9001")
            await asyncio.Future()  # Keep the server running
    except Exception as e:
        print(f"🔥 WebSocket server failed: {e}", file=sys.stderr)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"🔥 Server crash: {e}", file=sys.stderr)

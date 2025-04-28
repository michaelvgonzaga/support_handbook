import asyncio
import websockets
import os
import pty

async def shell(websocket):
    pid, fd = pty.fork()
    if pid == 0:
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
                        await websocket.send(data.decode(errors="ignore"))
                    else:
                        print("🛑 Shell closed (EOF).")
                        break
            except Exception as e:
                print(f"[from_fd] Error: {e}")

        async def from_ws():
            try:
                async for message in websocket:
                    os.write(fd, message.encode())
            except Exception as e:
                print(f"[from_ws] Error: {e}")

        await asyncio.gather(from_fd(), from_ws())

async def main():
    async def handler(websocket, _path):
        print("🔌 New WebSocket connection.")
        try:
            await shell(websocket)
        except Exception as e:
            print(f"❌ Handler error: {e}")
        finally:
            print("🚪 WebSocket client disconnected.")

    print("🚀 Starting WebSocket server...")
    async with websockets.serve(handler, "0.0.0.0", 9001):
        print("✅ Server ready at ws://localhost:9001")
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"🔥 Server crash: {e}")

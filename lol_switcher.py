#!/Users/junhu/.pyenv/shims/python3

''' LoL開始遊戲時的log

<unknown>(0x0x204fcc2c0): ALWAYS|   CLK| Replica[0]: Command(Unpause) LocalTime(0.017) SegmentStartTime(0.000) LocalOffset(1.190) Interpolate
<unknown>(0x0x204fcc2c0): ALWAYS|  FLOW| Switching Game State from GAMESTATE_SPAWN to GAMESTATE_GAMELOOP for reason Received Game Start Packet.
<unknown>(0x0x204fcc2c0): ALWAYS|  FLOW| Pop: LoadingScreen
<unknown>(0x0x204fcc2c0): ALWAYS|  FLOW| Pop: LoadingScreen complete  Current: Gameplay
<unknown>(0x0x204fcc2c0):  ERROR| >>> BuffHashMap::HashToName - Match not found for hash 03e5f841
<unknown>(0x0x204fcc2c0): ALWAYS|  FLOW| SEJ-8711AB1A 0.0168514
<unknown>(0x0x204fcc2c0): ALWAYS|  FLOW| SEJ-9651ACAB
<unknown>(0x0x204fcc2c0): ALWAYS|  FLOW| SEJ-B2890C00
<unknown>(0x0x204fcc2c0): ALWAYS| GAMESTATE_GAMELOOP UpdateVis
<unknown>(0x0x204fcc2c0): ALWAYS| GAMESTATE_GAMELOOP AudioUpdate
<unknown>(0x0x204fcc2c0): ALWAYS| GAMESTATE_GAMELOOP EndRender & EndFrame
<unknown>(0x0x204fcc2c0): ALWAYS|  FLOW| SEJ-891ACC45
<unknown>(0x0x204fcc2c0): ALWAYS| Enabling System Load Monitoring: 1000ms
'''
import subprocess

bring_front_cmd = """
tell application "System Events"
    tell application process "%s"
        set frontmost to true
    end tell
end tell
"""

minimization_cmd = """
tell application "System Events"
    tell application process "%s"
        set visible to false
    end tell
end tell
"""

def switch2lol(cmd=bring_front_cmd):
    title = "League Of Legends"

    # find the app or window back and activate it
    applescript = cmd % (title,)
    p = subprocess.Popen('osascript',
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT, encoding="utf-8", text=True)
    p.communicate(applescript)[0]

if __name__ == "__main__": 
    p = subprocess.Popen(["./LeagueClient.app/Contents/MacOS/LeagueClient"], cwd="/Applications/League of Legends.app/Contents/LoL", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    log_buffer = ""
    for line in p.stdout:
        line_str = line.decode()
        print(line_str)
        if "GAMESTATE_GAMELOOP EndRender & EndFrame" in line_str:
            switch2lol()
        elif "LoadingScreen  Current: Gameplay" in line_str:
            print("run minimization_cmd")
            switch2lol(minimization_cmd)

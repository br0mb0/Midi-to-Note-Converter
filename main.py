from MIDI import MIDIFile
from sys import argv

def parse(file):
    with open("log.txt", "w") as f:
        c=MIDIFile(file)
        c.parse()
        f.write(str(c))
        for idx, track in enumerate(c):
            track.parse()
            print(f'Track {idx}:')
            for ev in track:
                print("   ",hex(ev.header))
                print(str(ev))
                f.write(f"   {hex(ev.header)}\n")
                f.write(f"{str(ev)}\n\n")
        
def Makenotes(file, interval):
    notes = ""
    File = MIDIFile(file)
    File.parse()
    for idx, track in enumerate(File):
        track.parse()
        print(f'Track {idx}:')
        print(f'Length: {len(track)}')       
        for indx, ev in enumerate(track[0:5]):
            if ev.header == 0xFF:
                if str(ev.message) == 'Track Name':              
                    print(ev)
            
        print('\n')
    indx = int(input('Which track ')) 
    print('\n')
    Track = File[indx]
    Track.parse()
    time = 0
    for event in Track:
        if event.header == 0x90:
           if (event.time - time) >= interval:
                notes += ("\n")
           note = str(event.message.note)[0:-1]
           if note == "G#":
                note = 'Ab'
           if note == "D#":
                note = 'Eb'
           if note == "C#":
                note = 'Db'        
           if note == "A#":
                note = 'Bb'                 
           notes += (note+" ")
           time = event.time
    print(notes)
    
if argv[2] == 'db':
    parse(argv[1])
else:            
    if len(argv) == 2:
        arg2 = 900
    else:
        arg2 = int(argv[2])
        
    Makenotes(argv[1],arg2)
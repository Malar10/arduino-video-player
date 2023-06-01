from PIL import Image, ImageSequence, UnidentifiedImageError

def smallbitmapstringify(im):
    #doing it in this order seems to make the result less noisy for some reason

    #make small
    smol = im.resize((8, 8), Image.Resampling.BILINEAR)

    #make black and white
    blackandwhite = smol.convert("1")

    #turn into bitmap string
    x11bitmap = str(blackandwhite.tobitmap())

    #only get hex data from bitmap string
    i = x11bitmap.find("{")
    j = x11bitmap.find("}")
    valuestring = x11bitmap[i+3:j-2]

    return valuestring

def writeToFile(filename: str, data: list):

    with open("arduino_8x8_LED_Video.ino", "w") as file:
        file.write(f"const int frames = {len(data)};\n")
        file.write(f"const float ms_per_frame = {frameduration};\n")
        file.write(f"const PROGMEM byte videodata[{len(data)}][8] = {{ \n")
        for i in range(len(data)):
            file.write(f"{{{data[i]}}}") #its beautiful
            if i < len(data)-1:
                file.write(f",\n")
        file.write(f"\n}};")

def getFile():
    filename = input("filename: ")

    try:
        im = Image.open(filename, formats=["GIF"])
    except FileNotFoundError:
        print(f"could not find file {filename}")
        return None
    except UnidentifiedImageError:
        print(f"file must be of type GIF")
        return None

    print(f"found file {filename}")
    return im

while True:
    im = getFile()
    print()
    if im != None:
        break


print(im)
print(im.info)
print()

input_frameduration = im.info['duration']

list = ImageSequence.all_frames(im)
im.close()

inputframes = len(list)

print(f"input frames: {inputframes}")
print(f"input frame duration: {input_frameduration}")

frameduration = int(input(f"output frame duration in ms: "))

ratio = frameduration / input_frameduration
print(ratio)

outputframes = int(inputframes * (1/ratio))


print(f"output frames: {outputframes}")

input("you sure about this?")

values = []
for i in range(outputframes):
    index = int(ratio * i)
    valuestring = smallbitmapstringify(list[index])
    values.append(valuestring)


            

writeToFile("arduino_8x8_LED_Video.ino", values)

print("done!")
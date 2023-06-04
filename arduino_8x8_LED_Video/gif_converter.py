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

def writeToFile(filename: str, data: list, frameduration: float):

    with open(filename, "w") as file:
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

def main():


    while True:
        im = getFile()
        print()
        if im != None:
            break


    print(im)
    print(im.info)
    print()

    list = ImageSequence.all_frames(im)
    im.close()

    inputframes = len(list)
    totalDuration = sum([frame.info["duration"] for frame in list])
    input_frameduration = totalDuration / len(list)

    print(f"input frames: {inputframes}")
    print(f"total duration: {totalDuration}ms")
    print(f"input average frame duration: {input_frameduration} ms")

    output_frameduration = int(input(f"output frame duration in ms: "))
    outputframes = int(inputframes * (input_frameduration / output_frameduration))
    print(f"output frames: {outputframes}")
    print()

    response = input("Continue? [y/n] (will overwrite data.h) ")
    if response.lower() != "y":
        return
    
    print("converting images")
    values = []
    for i in range(outputframes):
        index = int((output_frameduration / input_frameduration) * i)
        valuestring = smallbitmapstringify(list[index])
        values.append(valuestring)

    print("conversion done!")
    print("writing values to file...")
    writeToFile("data.h", values, output_frameduration)
    print("done!")


main()
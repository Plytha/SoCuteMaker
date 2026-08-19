from PIL import Image, ImageSequence


def test():
    """Code mostly taken from: https://medium.com/thedevproject/quick-and-easy-gif-creation-and-optimization-with-python-5223814861e2"""
    bl = Image.open("resources/back_layer.gif")
    fl = Image.open("resources/front_layer.gif")
    rs = Image.open("resources/test.gif").convert("RGBA")

    size=128, 128

    resized = rs.resize(size)

    resized.show()

    resized_transposed = resized.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

    output = []

    bl_frames = [f.copy().convert("RGBA") for f in ImageSequence.Iterator(bl)]


    fl_frames = [f.copy().convert("RGBA") for f in ImageSequence.Iterator(fl)]

    for i, frame in enumerate(bl_frames):
        frame.paste(resized_transposed, mask=resized_transposed)
        frame.paste(fl_frames[i], (0,0,128,128), fl_frames[i])

        output.append(frame)

    output[0].save(
        "output/created_gif.gif",
        save_all=True,
        append_images = output[1:],
        loop=0
    )
    



def main():
    test()

if __name__=='__main__':
    main()
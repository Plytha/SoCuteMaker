from PIL import Image, ImageSequence
import os
from pathlib import Path
import argparse


def ensure_directory():
    cwd = os.getcwd()

    if "\\" in cwd:
        # why do you use windows :'(
        curr_dir = cwd.split("\\")[-1]
    else:
        curr_dir = cwd.split("/")[-1]

    if curr_dir == "src":
        os.chdir("..")
    
    if not os.path.isdir("resources") or \
        not os.path.isfile("resources/back_layer.gif") or \
        not os.path.isfile("resources/front_layer.gif"):
        raise RuntimeError("You are missing a critical resource for the script. Please fetch them back from the git repository")

    if os.path.isdir("output"):
        return

    os.mkdir("output")


def socutify(image_path: str) -> None:
    """Image manip code mostly taken from: https://medium.com/thedevproject/quick-and-easy-gif-creation-and-optimization-with-python-5223814861e2"""
    ensure_directory()

    # load images
    bl = Image.open("resources/back_layer.gif")
    fl = Image.open("resources/front_layer.gif")
    rs = Image.open(image_path).convert("RGBA")

    # manip on the image to cutify
    size=128, 128
    resized = rs.resize(size)
    

    # prepare the output and the frames
    output = []
    bl_frames = [f.copy().convert("RGBA") for f in ImageSequence.Iterator(bl)]
    fl_frames = [f.copy().convert("RGBA") for f in ImageSequence.Iterator(fl)]

    # actually make the gif
    for i, frame in enumerate(bl_frames):
        frame.paste(resized_transposed, mask=resized_transposed)
        frame.paste(fl_frames[i], (0,0,128,128), fl_frames[i])

        output.append(frame)

    # and finally save
    output[0].save(
        "output/created_gif.gif",
        save_all=True,
        append_images = output[1:],
        disposal=2,
        loop=0
    )
    

def setup_parser():
    parser = argparse.ArgumentParser(description="Make any image socute")

    parser.add_argument("-i", "--image")

    return parser

def check_args(parser):
    args = parser.parse_args()

    if args.image is None:
        raise RuntimeError("Please specify an image path to socutify...")
    
    return args.image

def main():
    parser = setup_parser()
    image_path = check_args(parser)
    socutify(image_path)

if __name__=='__main__':
    main()
import os
from os import read
from shutil import copyfile, copy2

grades = [-25, 0, 200]
sizes = [20, 24, 40, 48]
modes = ["outlined", "rounded", "sharp"]
ext = ".svg"


def main():
    path = input("Path to material design icons root folder: ")

    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError("Path is not a directory or does not exist")

    fill = input("Fill? (y/n): ").lower() == "y"

    mode = input("Mode? (outlined/rounded/sharp): ").strip()
    if mode not in modes:
        raise ValueError("Invalid mode")

    weight = int(input("Weight (100-700 by 100):"))
    if weight not in range(100, 800, 100):
        raise ValueError("Weight must be between 100 and 700")

    grade = int(input(f"Grade (one of the following: {grades}) :"))
    if grade not in grades:
        raise ValueError(f"Grade must be one of the following: {grades}")

    size = int(input(f"Optical size (one of the following: {sizes}) :"))
    if size not in sizes:
        raise ValueError(f"Optical size must be one of the following: {sizes}")

    folder = f"{path}/symbols/web"

    modename = f"materialsymbols{mode}"

    weight_t = "" if weight == 400 else f"wght{weight}"

    if grade == -25:
        grade_t = "gradN25"
    elif grade == 0:
        grade_t = ""
    elif grade == 200:
        grade_t = "grad200"
    else:
        raise ValueError("Invalid grade")

    fill_t = "fill1" if fill else ""

    size_t = f"_{size}px"

    prefix = "_" if fill_t or grade_t or weight_t else ""

    # folder to write to
    outputpath = f"./materialsymbols_{mode}{prefix}{weight_t}{grade_t}{fill_t}{size_t}"

    os.makedirs(outputpath, exist_ok=True)

    for icon_name in os.listdir(folder):
        if icon_name.startswith("."):
            continue

        basepath = f"{folder}/{icon_name}/{modename}"

        # weight -> grad -> fill -> size
        iconpath = f"{basepath}/{icon_name}{prefix}{weight_t}{grade_t}{fill_t}{size_t}{ext}"

        if not os.path.exists(iconpath):
            print(f"Icon not found. This shouldn't really happen. path: {iconpath}")
            continue

        # e.g.: mso_bell.svg
        filename = f"{icon_name}{ext}"
        path = f"{outputpath}/{filename}"

        if os.path.exists(path):
            print("Icon already exists, skipping")
        else:
            # preserve metadata
            copy2(src=iconpath, dst=path)

    print(f"Saved to: {outputpath}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Fatal: {e}")

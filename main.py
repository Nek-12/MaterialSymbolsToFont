import os
import shutil
import subprocess
import webbrowser
from shutil import copy2

grades = [-25, 0, 200]
sizes = [20, 24, 40, 48]
modes = ["outlined", "rounded", "sharp"]
ext = ".svg"
generator_webui_url = "https://android-iconics.mikepenz.com/"


def main():
    input_path = input("Path to material design icons root folder: ").strip()

    if not os.path.exists(input_path) or not os.path.isdir(input_path):
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

    folder = f"{input_path}/symbols/web"

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
    output_path = f"./materialsymbols_{mode}{prefix}{weight_t}{grade_t}{fill_t}{size_t}"

    os.makedirs(output_path, exist_ok=True)

    for icon_name in os.listdir(folder):
        if icon_name.startswith("."):
            continue

        base_path = f"{folder}/{icon_name}/{modename}"

        # weight -> grad -> fill -> size
        icon_path = f"{base_path}/{icon_name}{prefix}{weight_t}{grade_t}{fill_t}{size_t}{ext}"

        if not os.path.exists(icon_path):
            print(f"Icon not found. This shouldn't really happen. path: {icon_path}")
            continue

        # e.g.: mso_bell.svg
        filename = f"{icon_name}{ext}"
        file_path = f"{output_path}/{filename}"

        if os.path.exists(file_path):
            print("Icon already exists, skipping")
        else:
            # preserve metadata
            copy2(src=icon_path, dst=file_path)

    print(f"Saved to: {output_path}")
    try:
        font_path = f"{output_path}/ttf"
        os.makedirs(font_path, exist_ok=True)
        subprocess.run(f'fantasticon {output_path} -o {font_path} --debug --font-types ttf', shell=True, check=True)
        shutil.copytree(src=font_path, dst=f"{input_path}/ttf", symlinks=True, dirs_exist_ok=True)
        print(f"font saved to {input_path}/ttf, cleaning up...")
        shutil.rmtree(path=output_path, ignore_errors=True)
        print(f"removed {output_path}")
    except subprocess.CalledProcessError:
        print("Seems like fantasticon is not installed, skipping ttf generation")

    print("Generated, opening web ui")
    webbrowser.open_new_tab(generator_webui_url)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Fatal: {e}")

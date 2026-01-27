import os
import subprocess
import sys
import time

SRC_DIR = "src"
IMAGE_NAME = "mega-hello-world"

def is_inside_docker():
    return os.path.exists('/.dockerenv')

def run_inside_docker(args):
    # This function wraps the command and runs it inside a docker container
    docker_cmd = ["docker", "run", "--rm", "-it", IMAGE_NAME, "python3", "runner.py"] + args
    try:
        subprocess.run(docker_cmd)
    except Exception as e:
        print(f"[!] Error running docker: {e}")

# Mapping extensions to run commands
# {file} is the filename
# {name_no_ext} is the filename without extension
# {name} is the filename (same as {file})
RUNNERS = {
    ".py": "python3 {file}",
    ".js": "node {file}",
    ".ts": "ts-node {file}",
    ".c": "gcc {file} -o tmp_out && ./tmp_out && rm tmp_out",
    ".cpp": "g++ {file} -o tmp_out && ./tmp_out && rm tmp_out",
    ".cs": "mcs {file} && mono {name_no_ext}.exe && rm {name_no_ext}.exe",
    ".java": "javac {file} && java {name_no_ext} && rm {name_no_ext}.class",
    ".go": "go run {file}",
    ".rs": "rustc {file} -o tmp_out && ./tmp_out && rm tmp_out",
    ".php": "php {file}",
    ".rb": "ruby {file}",
    ".swift": "swift {file}",
    ".kt": "kotlinc {file} -include-runtime -d tmp.jar && java -jar tmp.jar && rm tmp.jar",
    ".lua": "lua {file}",
    ".pl": "perl {file}",
    ".r": "Rscript {file}",
    ".sh": "bash {file}",
    ".hs": "runhaskell {file}",
    ".dart": "dart {file}",
    ".scala": "scala {file}",
    ".exs": "elixir {file}",
    ".clj": "clojure {file}",
    ".jl": "julia {file}",
    ".fs": "fsharpc {file} && mono {name_no_ext}.exe && rm {name_no_ext}.exe",
    ".ml": "ocaml {file}",
    ".erl": "escript {file}",
    ".lisp": "sbcl --script {file}",
    ".scm": "guile -s {file}",
    ".rkt": "racket {file}",
    ".groovy": "groovy {file}",
    ".elm": "elm make {file} --output=tmp.js && node tmp.js && rm tmp.js",
    ".plg": "swipl -q -t halt -f {file}",
    ".f90": "gfortran {file} -o tmp_out && ./tmp_out && rm tmp_out",
    ".cob": "cobc -x {file} -o tmp_out && ./tmp_out && rm tmp_out",
    ".pas": "fpc {file} > /dev/null && ./{name_no_ext} && rm {name_no_ext} {name_no_ext}.o",
    ".adb": "gnatmake {file} > /dev/null && ./{name_no_ext} && rm {name_no_ext} {name_no_ext}.ali {name_no_ext}.o",
    ".asm": "nasm -felf64 {file} && ld {name_no_ext}.o -o tmp_out && ./tmp_out && rm tmp_out {name_no_ext}.o",
    ".vb": "vbnc {file} && mono {name_no_ext}.exe && rm {name_no_ext}.exe",
    ".m": "gcc {file} -o tmp_out -lobjc -lgnustep-base -I/usr/include/GNUstep -L/usr/lib/GNUstep && ./tmp_out && rm tmp_out",
    ".st": "gst {file}",
    ".tcl": "tclsh {file}",
    ".d": "rdmd {file}",
    ".vim": "vim -u NONE -es -c 'source {file}' -c 'q'",
    ".el": "emacs --batch -l {file}",
    ".ps1": "pwsh -File {file}",
    ".bas": "fbc -run {file}",
    ".cr": "crystal run {file}",
    ".nim": "nim c -r --verbosity:0 {file}",
    ".awk": "awk -f {file}",
    ".sed": "sed -f {file}",
    ".zig": "zig run {file}",
    ".v": "v run {file}",
    ".hx": "haxe --run {name_no_ext}",
    ".coffee": "coffee {file}",
    ".rexx": "rexx {file}",
    ".icn": "icon {file}",
    ".fth": "gforth {file}",
    ".factor": "factor {file}",
    ".ijs": "ijconsole {file}",
    ".apl": "apl -f {file}",
    ".ps": "gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage {file}",
    ".wls": "wolframscript -file {file}",
    ".gp": "gnuplot {file}",
    ".mk": "make -f {file}",
    ".cmake": "cmake -P {file}",
    ".bc": "bc {file}",
    ".m4": "m4 {file}",
    ".purs": "purescript {file}",
    ".bf": "bf {file}",
    ".arnoldc": "arnoldc {file}",
    ".lol": "lci {file}",
    ".rock": "rockstar {file}",
    ".chef": "chef {file}",
    ".spl": "spl {file}",
    ".chicken": "chicken {file}",
    ".ws": "whitespace {file}",
    ".befunge": "cfunge {file}",
    ".piet": "npiet {file}",
    ".omgrofl": "omgrofl {file}",
    ".tr": "TRUMP {file}",
    ".hodor": "hodor {file}",    ".ook": "ook {file}",
    ".i": "ick {file}",
    ".f": "false {file}",
    ".mal": "malbolge {file}",
    ".zombie": "zombie {file}",
    ".cow": "cow {file}",
    ".emojicode": "emojicode {file}",
    ".unl": "unlambda {file}",
    ".gs": "golfscript {file}",
    ".hai": "haifu {file}",
    ".glass": "glass {file}",
    ".hex": "hexagony {file}",
    ".doge": "dogescript {file}",
    ".z": "zsh {file}",
    ".abc": "abc {file}",
    ".vig": "vigil {file}",
    ".b": "b-lang {file}",
    ".algol": "a68g {file}",
    ".arch": "cat {file}",
}

def run_file(filepath):
    filename = os.path.basename(filepath)
    name_no_ext, ext = os.path.splitext(filename)
    
    if ext not in RUNNERS:
        print(f"[-] No runner for {filename}")
        return False

    cmd_template = RUNNERS[ext]
    cmd = cmd_template.format(file=filename, name=filename, name_no_ext=name_no_ext)
    
    print(f"[>] Running {filename}...")
    try:
        # We need to run in the directory of the file for some compilers
        start_time = time.time()
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=SRC_DIR)
        elapsed = time.time() - start_time
        
        if result.returncode == 0:
            print(f"[+] Success ({elapsed:.2f}s): {result.stdout.strip()}")
            return True
        else:
            print(f"[!] Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"[!] Exception: {e}")
        return False

def main():
    if not is_inside_docker():
        print(f"[*] Native runner detected. Ensuring Docker image '{IMAGE_NAME}' is ready...")
        # Check if image exists, if not build it
        check_img = subprocess.run(["docker", "images", "-q", IMAGE_NAME], capture_output=True, text=True)
        if not check_img.stdout.strip():
            print("[*] Image not found. Building (this will take a while, 100+ languages!)...")
            subprocess.run(["docker", "build", "-t", IMAGE_NAME, "."])
        
        # Re-run the script args inside Docker
        run_inside_docker(sys.argv[1:])
        return

    files = sorted([f for f in os.listdir(SRC_DIR) if os.path.isfile(os.path.join(SRC_DIR, f)) and not f.endswith(".png")])
    
    # Map numbers to files
    file_map = {}
    for f in files:
        parts = f.split("_")
        if len(parts) > 0 and parts[0].isdigit():
            num = int(parts[0])
            file_map[num] = f

    if len(sys.argv) > 1:
        choice = sys.argv[1].lower()
        if choice == "all":
            run_sequence(files)
        elif choice.isdigit():
            num = int(choice)
            if num in file_map:
                run_file(os.path.join(SRC_DIR, file_map[num]))
            else:
                print(f"[-] No file found with number {num}")
        else:
            print("Usage: python3 runner.py [all | number]")
    else:
        # Interactive mode
        print("\n--- Mega Hello World Runner ---")
        print("Available programs:")
        for num in sorted(file_map.keys()):
            print(f"{num:03d}: {file_map[num]}")
        
        print("\nEnter a number to run specific program, 'all' to run everything, or 'q' to quit.")
        while True:
            try:
                user_input = input("\nSelection > ").strip().lower()
                if user_input == 'q':
                    break
                if user_input == 'all':
                    run_sequence(files)
                    break
                if user_input.isdigit():
                    num = int(user_input)
                    if num in file_map:
                        run_file(os.path.join(SRC_DIR, file_map[num]))
                    else:
                        print(f"[-] No file found with number {num}")
                else:
                    print("Invalid input. Enter number, 'all', or 'q'.")
            except EOFError:
                break

def run_sequence(files):
    passed = 0
    failed = 0
    skipped = 0
    for f in files:
        if run_file(os.path.join(SRC_DIR, f)):
            passed += 1
        else:
            failed += 1
    print(f"\nSummary: {passed} passed, {failed} failed, {skipped} skipped.")

if __name__ == "__main__":
    main()

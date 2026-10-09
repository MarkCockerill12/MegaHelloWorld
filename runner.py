import os
import subprocess
import sys
import time

SRC_DIR = "src"
IMAGE_NAME = "mega-runner"
DEFAULT_TIMEOUT = 5
SLOW_TIMEOUT = 60
SLOW_EXTENSIONS = {
    ".kt", ".scala", ".rs", ".zig", ".cr", ".fs", ".gp",
    ".wls", ".elm", ".purs", ".arnoldc", ".emojicode",
}
PASSED, FAILED, SKIPPED = "passed", "failed", "skipped"

# Bundled interpreters for esoteric languages; commands run with cwd=SRC_DIR
ESOLANG = "python3 ../esolangs.py"

# Extension -> shell command. None means there is no working implementation
# of the language to install, so the file is reported as skipped rather than run.
RUNNERS = {
    ".py": "python3 {file}",
    ".js": "node {file}",
    ".ts": "TS_NODE_COMPILER_OPTIONS='{{\"module\":\"commonjs\"}}' npx ts-node {file}",
    ".c": "gcc {file} -o tmp_out && ./tmp_out; rm tmp_out",
    ".cpp": "g++ {file} -o tmp_out && ./tmp_out; rm tmp_out",
    ".cs": "mcs {file}; mono {name_no_ext}.exe; rm {name_no_ext}.exe",
    ".java": "java {file}",
    ".go": "go run {file}",
    ".rs": "rustc {file} -o tmp_out && ./tmp_out; rm tmp_out",
    ".php": "php {file}",
    ".rb": "ruby {file}",
    ".swift": "swift {file}",
    ".kt": "kotlinc {file} -include-runtime -d tmp.jar 2> /dev/null && java -jar tmp.jar; rm -f tmp.jar",
    ".lua": "lua {file}",
    ".pl": "perl {file}",
    ".r": "Rscript {file}",
    ".sh": "bash {file}",
    ".hs": "runhaskell {file}",
    ".dart": "dart {file}",
    ".scala": "scala -nc {file}",
    ".exs": "elixir {file}",
    ".clj": "clojure {file}",
    ".jl": "julia {file}",
    ".fs": "fsharpc --nologo {file}; mono {name_no_ext}.exe; rm {name_no_ext}.exe",
    ".ml": "ocaml {file}",
    ".erl": "escript {file}",
    ".lisp": "sbcl --script {file}",
    ".scm": "guile -s {file}",
    ".rkt": "racket {file}",
    ".groovy": "groovy {file}",
    ".elm": "cp {file} /opt/elm/src/Main.elm && (cd /opt/elm && elm make src/Main.elm --output=elm.js > /dev/null) && node ../tools/run_elm.js /opt/elm/elm.js",
    ".plg": "swipl -q -t halt -f {file}",
    ".f90": "gfortran {file} -o tmp_out && ./tmp_out; rm tmp_out",
    ".cob": "cobc -x -free {file} -o tmp_out && ./tmp_out; rm tmp_out",
    ".pas": "fpc {file} > /dev/null; ./{name_no_ext}; rm {name_no_ext} {name_no_ext}.o",
    ".adb": "gnatmake {file} > /dev/null; ./{name_no_ext}; rm {name_no_ext} {name_no_ext}.ali {name_no_ext}.o",
    ".asm": "nasm -felf64 {file}; ld {name_no_ext}.o -o tmp_out && ./tmp_out; rm tmp_out {name_no_ext}.o",
    ".vb": "vbnc {file} > /dev/null; mono {name_no_ext}.exe; rm {name_no_ext}.exe",
    ".m": "gcc `gnustep-config --objc-flags` {file} -o tmp_out -lgnustep-base -lobjc && ./tmp_out; rm -f tmp_out tmp_out.d",
    ".st": "gst {file}",
    ".tcl": "tclsh {file}",
    ".d": "gdc {file} -o tmp_out && ./tmp_out; rm tmp_out",
    ".vim": "vim -u NONE -es -c 'redir >> /dev/stdout' -c 'source {file}' -c 'redir END' -c 'q'",
    ".el": "emacs --batch -Q -l {file}",
    ".ps1": "pwsh -File {file}",
    ".bas": "yabasic {file}",
    ".cr": "crystal run {file}",
    ".nim": "cp {file} hello_nim.nim; nim c -r --verbosity:0 --hints:off hello_nim.nim; rm hello_nim.nim hello_nim",
    ".awk": "awk -f {file}",
    ".sed": "echo '' | sed -f {file}",
    ".zig": "zig run {file}",
    ".v": "v run {file}",
    ".hx": "cp {file} Main.hx; haxe --run Main; rm Main.hx",
    ".coffee": "coffee {file}",
    ".rexx": "rexx ./{file}",
    ".icn": "icont {file} > /dev/null; ./{name_no_ext}; rm -f {name_no_ext} {name_no_ext}.icx",
    ".fth": "gforth {file} -e bye",
    ".factor": "/opt/factor/factor {file}",
    ".ijs": "/opt/j9.5/bin/jconsole {file} < /dev/null",
    ".apl": "apl --script --OFF -f {file}",
    ".ps": "gs -q -dNOPAUSE -dBATCH -sDEVICE=nullpage {file}",
    ".wls": "mathics -q -f {file} < /dev/null",
    ".gp": "gnuplot {file}",
    ".mk": "make -f {file}",
    ".cmake": "cmake -P {file}",
    ".bc": "bc -q {file}",
    ".m4": "m4 {file}",
    ".purs": "(purs compile '/opt/purs/deps/*/src/**/*.purs' {file} -o /opt/purs/output > /tmp/purs.log 2>&1 "
             "|| (cat /tmp/purs.log >&2; false)) && node --input-type=module -e \"import('/opt/purs/output/Main/index.js').then(m => m.main())\"",
    ".bf": "bf {file}",
    ".arnoldc": "cp {file} hello.arnoldc && java -jar /opt/arnoldc/ArnoldC.jar hello.arnoldc > /dev/null && java hello; rm -f hello.arnoldc hello.class",
    ".lol": "lci {file}",
    ".rock": "rockstar-py -i {file} -o tmp.py; python3 tmp.py; rm tmp.py",
    ".chef": "chef {file}",
    ".spl": "shakespeare run {file}",
    ".chicken": ESOLANG + " chicken {file}",
    ".ws": ESOLANG + " whitespace {file}",
    ".befunge": ESOLANG + " befunge {file}",
    ".png": ESOLANG + " piet {file}",
    ".omgrofl": ESOLANG + " omgrofl {file}",
    # TrumpScript refuses to run as root
    ".tr": "setpriv --reuid 65534 --regid 65534 --clear-groups /opt/TrumpScript/bin/TRUMP {file}",
    ".hodor": None,
    ".ook": ESOLANG + " ook {file}",
    ".i": "ick {file}; ./{name_no_ext}; rm {name_no_ext}",
    ".f": ESOLANG + " false {file}",
    ".mal": ESOLANG + " malbolge {file}",
    ".zombie": ESOLANG + " zombie {file}",
    ".cow": "cow {file} | sed '1,4d;/^Done\\.$/d'",
    ".emojicode": "cp {file} hello.emojic && emojicodec hello.emojic && ./hello; rm -f hello.emojic hello.o hello",
    ".unl": ESOLANG + " unlambda {file}",
    ".gs": "ruby /opt/golfscript.rb {file}",
    ".hai": None,
    ".glass": ESOLANG + " glass {file}",
    ".hex": "ruby /opt/hexagony/interpreter.rb {file}",
    ".doge": "dogescript {file} > tmp.js && node tmp.js; rm tmp.js",
    ".z": "zsh {file}",
    ".abc": None,
    ".vig": "python2 /opt/vigil/vigil {file}",
    ".b": None,
    ".algol": "a68g {file}",
    ".arch": ESOLANG + " arch {file}",
}

def is_inside_docker():
    return os.path.exists('/.dockerenv')

def run_inside_docker(args):
    # Mount the current repo into /app so runner.py and src/ are visible in the container
    host_dir = os.path.abspath(".")
    # Only the interactive prompt needs a terminal; batch runs also work when piped
    interactive = not args and sys.stdin.isatty() and sys.stdout.isatty()
    docker_cmd = [
        "docker",
        "run",
        "--rm",
        "-it" if interactive else "-i",
        "-v",
        f"{host_dir}:/app",
        "-w",
        "/app",
        IMAGE_NAME,
        "python3",
        "runner.py",
    ] + args
    try:
        return subprocess.run(docker_cmd, check=False).returncode
    except OSError as e:
        print(f"[!] Error running docker: {e}")
        return 1

def run_file(filepath):
    filename = os.path.basename(filepath)
    name_no_ext, ext = os.path.splitext(filename)

    # Safety check for special chars that crash Linux shells
    if '$' in filename or '£' in filename:
        print(f"[-] SKIPPING {filename}: Contains unsafe characters ($ or £). Please rename.")
        return SKIPPED

    if ext not in RUNNERS:
        print(f"[-] No runner for {filename}")
        return FAILED

    cmd_template = RUNNERS[ext]
    if cmd_template is None:
        print(f"[~] Skipped {filename}: there is no working {ext} implementation to run it with.")
        return SKIPPED

    cmd = cmd_template.format(file=filename, name=filename, name_no_ext=name_no_ext)

    print(f"[>] Running {filename}...")
    try:
        start_time = time.time()
        timeout_val = SLOW_TIMEOUT if ext in SLOW_EXTENSIONS else DEFAULT_TIMEOUT

        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=SRC_DIR, timeout=timeout_val, check=False)
        elapsed = time.time() - start_time

        if result.returncode == 0:
            # Some tools (emacs --batch, gnuplot) write their output to stderr
            output = result.stdout.strip() or result.stderr.strip()
            print(f"[+] Success ({elapsed:.2f}s): {output}")
            return PASSED
        else:
            print(f"[!] Error in {filename}:")
            if result.stdout: print(f"    STDOUT: {result.stdout.strip()}")
            if result.stderr: print(f"    STDERR: {result.stderr.strip()}")
            return FAILED
    except subprocess.TimeoutExpired:
        print(f"[!] Timeout: {filename} took longer than {timeout_val} seconds.")
        return FAILED
    except OSError as e:
        print(f"[!] Exception running {filename}: {e}")
        return FAILED

def get_files():
    if not os.path.exists(SRC_DIR):
        return [], {}

    # Filter for source files: must start with a digit and have a mapped extension
    all_files = sorted([f for f in os.listdir(SRC_DIR) if os.path.isfile(os.path.join(SRC_DIR, f))])
    file_map = {}
    for f in all_files:
        parts = f.split("_")
        if len(parts) > 0 and parts[0].isdigit():
            num = int(parts[0])
            _, ext = os.path.splitext(f)
            if ext in RUNNERS:
                if num not in file_map:
                    file_map[num] = f
                else:
                    print(f"[-] Ignoring {f}: number {num} is already used by {file_map[num]}")

    return sorted(file_map.values()), file_map

def main():
    if not is_inside_docker():
        return handle_native_execution()

    files, file_map = get_files()
    if not files:
        print(f"[!] Critical Error: No valid source files found in '{SRC_DIR}' inside Docker.")
        return 1

    if len(sys.argv) > 1:
        return 0 if handle_args(sys.argv[1], files, file_map) else 1
    handle_interactive(files, file_map)
    return 0

def handle_native_execution():
    print(f"[*] Native runner detected. Ensuring Docker image '{IMAGE_NAME}' is ready...")
    try:
        check_img = subprocess.run(["docker", "images", "-q", IMAGE_NAME], capture_output=True, text=True, check=False)
    except FileNotFoundError:
        print("[!] Docker is not installed or not on PATH.")
        return 1
    if check_img.returncode != 0:
        print(f"[!] Docker is not available: {check_img.stderr.strip()}")
        return 1
    if not check_img.stdout.strip():
        print("[*] Image not found. Building (this will take a while!)...")
        if subprocess.run(["docker", "build", "-t", IMAGE_NAME, "."], check=False).returncode != 0:
            print("[!] Docker build failed.")
            return 1
    return run_inside_docker(sys.argv[1:])

def handle_args(choice, files, file_map):
    choice = choice.lower()
    if choice == "all":
        return run_sequence(files)
    if choice.isdigit():
        num = int(choice)
        if num in file_map:
            return run_file(os.path.join(SRC_DIR, file_map[num])) != FAILED
        print(f"[-] No file found with number {num}")
        return False
    print("Usage: python3 runner.py [all | number]")
    return False

def handle_interactive(files, file_map):
    print("\n--- Mega Hello World Runner ---")
    print(f"Loaded {len(file_map)} unique language files.")
    while True:
        try:
            user_input = input("\nEnter number (1-100), 'all', or 'q': ").strip().lower()
            if user_input == 'q': break
            handle_args(user_input, files, file_map)
        except (EOFError, KeyboardInterrupt): break

def run_sequence(files):
    counts = {PASSED: 0, FAILED: 0, SKIPPED: 0}
    for f in files:
        counts[run_file(os.path.join(SRC_DIR, f))] += 1
    print(f"\nSummary: {counts[PASSED]} passed, {counts[FAILED]} failed, {counts[SKIPPED]} skipped.")
    return counts[FAILED] == 0

if __name__ == "__main__":
    sys.exit(main())

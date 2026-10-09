# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# 1. Infrastructure & Repos
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl wget git unzip gnupg2 software-properties-common ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/dart.gpg \
    && echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | tee /etc/apt/sources.list.d/dart_stable.list \
    && wget -q https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb \
    && add-apt-repository -y universe \
    && rm -rf /var/lib/apt/lists/*

# 2. Mainstream Languages (The massive layer)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev \
    build-essential gcc g++ gdc gfortran \
    nodejs ruby-full perl golang-go rustc cargo php-cli openjdk-17-jdk lua5.4 r-base ghc scala elixir clojure swi-prolog gnucobol fpc gnat tcl tcl-dev nasm gobjc gnustep-devel regina-rexx icont iconx ocaml erlang fsharp mono-complete mono-vbnc haxe zsh gforth dart powershell gnu-smalltalk ghostscript vim emacs-nox beef bc m4 gnuplot bison flex libgd-dev sbcl clisp guile-3.0 racket groovy intercal algol68g \
    && rm -rf /var/lib/apt/lists/*

# Fix binaries
RUN ln -s /usr/bin/beef /usr/local/bin/bf && \
    ln -s /usr/bin/python3 /usr/local/bin/python

# 3. Pip/Npm (Grouped for caching)
# typescript is pinned to 5.x because ts-node does not work with newer majors
RUN pip3 install --no-cache-dir \
    cmake \
    shakespearelang \
    rockstar-py \
    packaging \
    Mathics3 \
    && npm install -g \
    ts-node typescript@5 \
    coffeescript \
    purescript \
    elm \
    dogescript \
    jsdom
ENV NODE_PATH=/usr/lib/node_modules

# 4. Manual Binaries (Stable)
RUN wget -q https://nim-lang.org/download/nim-2.0.2-linux_x64.tar.xz && tar -xf nim-2.0.2-linux_x64.tar.xz -C /usr/share && ln -s /usr/share/nim-2.0.2/bin/nim /usr/local/bin/nim && rm nim-2.0.2-linux_x64.tar.xz \
    && wget -q https://download.swift.org/swift-5.9.2-release/ubuntu2204/swift-5.9.2-RELEASE/swift-5.9.2-RELEASE-ubuntu22.04.tar.gz && tar -xzf swift-5.9.2-RELEASE-ubuntu22.04.tar.gz -C /usr/share && ln -s /usr/share/swift-5.9.2-RELEASE-ubuntu22.04/usr/bin/swift /usr/local/bin/swift && rm swift-5.9.2-RELEASE-ubuntu22.04.tar.gz \
    && wget -q https://github.com/JetBrains/kotlin/releases/download/v1.9.22/kotlin-compiler-1.9.22.zip && unzip -q kotlin-compiler-1.9.22.zip -d /usr/local/kotlin && ln -s /usr/local/kotlin/kotlinc/bin/kotlinc /usr/local/bin/kotlinc && ln -s /usr/local/kotlin/kotlinc/bin/kotlin /usr/local/bin/kotlin && rm kotlin-compiler-1.9.22.zip \
    && wget -q https://ziglang.org/download/0.11.0/zig-linux-x86_64-0.11.0.tar.xz && tar -xf zig-linux-x86_64-0.11.0.tar.xz -C /usr/local && ln -s /usr/local/zig-linux-x86_64-0.11.0/zig /usr/local/bin/zig && rm zig-linux-x86_64-0.11.0.tar.xz \
    && git clone --depth 1 https://github.com/vlang/v /usr/local/vlang && cd /usr/local/vlang && make && ./v symlink && cd / && rm -rf /usr/local/vlang/.git \
    && wget -q https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.0-linux-x86_64.tar.gz && tar -xzf julia-1.10.0-linux-x86_64.tar.gz -C /usr/local --strip-components=1 && rm julia-1.10.0-linux-x86_64.tar.gz \
    && curl -fsSL https://crystal-lang.org/install.sh | bash

# Workspace
WORKDIR /app
ENV PATH="/usr/share/nim-2.0.2/bin:${PATH}"

# COW (Using ZIP download)
RUN wget https://github.com/BigZaphod/COW/archive/refs/heads/master.zip -O /tmp/cow.zip \
    && unzip /tmp/cow.zip -d /tmp \
    && g++ /tmp/COW-master/source/cow.cpp -o /usr/local/bin/cow \
    && chmod +x /usr/local/bin/cow \
    && rm -rf /tmp/cow.zip /tmp/COW-master

# 5. Niche & esoteric toolchains (apt, CPAN and a GNU APL package)
RUN apt-get update && apt-get install -y --no-install-recommends \
    yabasic python2 cpanminus libreadline-dev libtinfo5 \
    && wget -q https://ftp.gnu.org/gnu/apl/apl_2.0-1_amd64.deb \
    && apt-get install -y --no-install-recommends ./apl_2.0-1_amd64.deb \
    && rm apl_2.0-1_amd64.deb \
    && rm -rf /var/lib/apt/lists/* \
    && cpanm -q -n Acme::Chef

# 6. Niche & esoteric toolchains (downloads and source builds)
# TrumpScript is patched because Python 3.8+ requires ast.Module(type_ignores=...)
RUN mkdir -p /opt/arnoldc && wget -q https://lhartikk.github.io/ArnoldC.jar -O /opt/arnoldc/ArnoldC.jar \
    && wget -q http://www.golfscript.com/golfscript/golfscript.rb -O /opt/golfscript.rb \
    && git clone --depth 1 https://github.com/m-ender/hexagony /opt/hexagony \
    && git clone --depth 1 https://github.com/munificent/vigil /opt/vigil \
    && git clone --depth 1 https://github.com/samshadwell/TrumpScript /opt/TrumpScript \
    && sed -i 's/Module(body=body_list)/Module(body=body_list, type_ignores=[])/' /opt/TrumpScript/src/trumpscript/parser.py \
    && git clone --depth 1 https://github.com/justinmeza/lci /tmp/lci && cd /tmp/lci \
    && cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 . && make && cp lci /usr/local/bin/lci && cd / && rm -rf /tmp/lci \
    && wget -q https://downloads.factorcode.org/releases/0.99/factor-linux-x86-64-0.99.tar.gz && tar -xzf factor-linux-x86-64-0.99.tar.gz -C /opt && rm factor-linux-x86-64-0.99.tar.gz \
    && wget -q https://www.jsoftware.com/download/j9.5/install/j9.5.2_linux64.tar.gz && tar -xzf j9.5.2_linux64.tar.gz -C /opt && rm j9.5.2_linux64.tar.gz \
    && wget -q https://github.com/Emojicode/emojicode/releases/download/v1.0-beta.2/Emojicode-1.0-beta.2-Linux-x86_64.tar.gz && tar -xzf Emojicode-1.0-beta.2-Linux-x86_64.tar.gz -C /tmp \
    && cd /tmp/Emojicode-1.0-beta.2-Linux-x86_64 && cp emojicodec /usr/local/bin/ \
    && mkdir -p /usr/local/EmojicodePackages /usr/local/include/emojicode && cp -r packages/. /usr/local/EmojicodePackages/ && cp -r include/. /usr/local/include/emojicode/ \
    && cd / && rm -rf /tmp/Emojicode-1.0-beta.2-Linux-x86_64*

# 7. Project skeletons: PureScript core libraries (precompiled) and an Elm project with its packages cached
RUN mkdir -p /opt/purs/deps && cd /opt/purs/deps \
    && git clone --depth 1 --branch v6.0.2 https://github.com/purescript/purescript-prelude prelude \
    && git clone --depth 1 --branch v4.0.0 https://github.com/purescript/purescript-effect effect \
    && git clone --depth 1 --branch v6.1.0 https://github.com/purescript/purescript-console console \
    && cd /opt/purs && purs compile 'deps/*/src/**/*.purs' \
    && mkdir -p /opt/elm && cd /opt/elm && (yes | elm init) \
    && printf 'module Main exposing (..)\nimport Html exposing (text)\nmain = text ""\n' > src/Main.elm \
    && elm make src/Main.elm --output=elm.js

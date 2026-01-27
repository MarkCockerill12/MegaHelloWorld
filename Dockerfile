# Use Ubuntu 22.04
FROM ubuntu:22.04

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
# Allow pip to install globally
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# 1. Base Utilities & Python
RUN apt-get update && apt-get install -y \
    curl wget git unzip gnupg2 software-properties-common build-essential \
    python3 python3-pip python3-dev \
    libreadline-dev libssl-dev libncurses5 libtinfo5 \
    && add-apt-repository -y universe \
    && add-apt-repository -y multiverse

# 2. Add External Repositories (Node, Dart, Microsoft)
# Node.js 20
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -

# Dart
RUN wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/dart.gpg \
    && echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | tee /etc/apt/sources.list.d/dart_stable.list

# Microsoft (PowerShell) - THIS WAS MISSING
RUN wget -q https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb

# 3. Install Standard Languages via APT
RUN apt-get update && apt-get install -y \
    nodejs \
    ruby-full ruby-dev \
    perl \
    golang-go \
    rustc cargo \
    php-cli \
    openjdk-17-jdk \
    lua5.4 \
    r-base \
    ghc \
    scala \
    elixir \
    clojure \
    swi-prolog \
    gfortran \
    gnucobol \
    fpc \
    gnat \
    tcl tcl-dev \
    nasm \
    gobjc gnustep-devel \
    regina-rexx \
    icont iconx \
    ocaml \
    erlang \
    fsharp \
    mono-complete \
    haxe \
    zsh \
    gforth \
    dart \
    powershell \
    gnu-smalltalk \
    ghostscript \
    cmake \
    vim \
    emacs-nox \
    beef \
    chicken-bin \
    bc \
    m4 \
    gnuplot \
    bison flex \
    libgd-dev \
    && rm -rf /var/lib/apt/lists/*

# Fix Brainfuck (Aliasing beef to bf)
RUN ln -s /usr/bin/beef /usr/local/bin/bf

# 4. Install Languages via PIP (Python)
RUN pip3 install \
    shakespearelang \
    rockstar-py \
    trumpscript \
    cow-py \
    mathics-scanner \
    Mathics3

# 5. Install Languages via NPM (Node.js)
RUN npm install -g \
    ts-node typescript \
    coffeescript \
    purescript \
    elm \
    dogescript \
    befunge93 \
    whitespace-cli

# 6. Manual Installs for Binary Languages

# Swift
RUN wget https://download.swift.org/swift-5.9.2-release/ubuntu2204/swift-5.9.2-RELEASE/swift-5.9.2-RELEASE-ubuntu22.04.tar.gz \
    && tar -xzf swift-5.9.2-RELEASE-ubuntu22.04.tar.gz -C /usr/share \
    && ln -s /usr/share/swift-5.9.2-RELEASE-ubuntu22.04/usr/bin/swift /usr/local/bin/swift \
    && rm swift-5.9.2-RELEASE-ubuntu22.04.tar.gz

# Kotlin
RUN wget https://github.com/JetBrains/kotlin/releases/download/v1.9.22/kotlin-compiler-1.9.22.zip \
    && unzip kotlin-compiler-1.9.22.zip -d /usr/local/kotlin \
    && ln -s /usr/local/kotlin/kotlinc/bin/kotlinc /usr/local/bin/kotlinc \
    && rm kotlin-compiler-1.9.22.zip

# Zig
RUN wget https://ziglang.org/download/0.11.0/zig-linux-x86_64-0.11.0.tar.xz \
    && tar -xf zig-linux-x86_64-0.11.0.tar.xz -C /usr/local \
    && ln -s /usr/local/zig-linux-x86_64-0.11.0/zig /usr/local/bin/zig \
    && rm zig-linux-x86_64-0.11.0.tar.xz

# V (Vlang)
RUN git clone --depth 1 https://github.com/vlang/v /usr/local/vlang \
    && cd /usr/local/vlang && make && ./v symlink

# Julia
RUN wget https://julialang-s3.julialang.org/bin/linux/x64/1.10/julia-1.10.0-linux-x86_64.tar.gz \
    && tar -xzf julia-1.10.0-linux-x86_64.tar.gz -C /usr/local --strip-components=1 \
    && rm julia-1.10.0-linux-x86_64.tar.gz

# Nim
RUN curl https://nim-lang.org/choosenim/init.sh -sSf | bash -s -- -y \
    && ln -s /root/.choosenim/current/bin/nim /usr/local/bin/nim

# Crystal
RUN curl -fsSL https://crystal-lang.org/install.sh | bash

# 7. Manual Compilations for Esoteric Languages

# LOLCODE
RUN git clone https://github.com/justinmeza/lci.git /tmp/lci \
    && cd /tmp/lci && cmake . && make && make install && rm -rf /tmp/lci

# False
RUN wget https://github.com/fph/false/raw/master/false.c -O /tmp/false.c \
    && gcc /tmp/false.c -o /usr/local/bin/false && chmod +x /usr/local/bin/false

# Omgrofl
RUN wget https://raw.githubusercontent.com/zcdziura/omgrofl/master/omgrofl.py -O /usr/local/bin/omgrofl.py \
    && printf '#!/bin/bash\npython3 /usr/local/bin/omgrofl.py "$@"' > /usr/local/bin/omgrofl \
    && chmod +x /usr/local/bin/omgrofl

# Chef
RUN git clone https://github.com/maxkfranz/chef-interpreter.git /tmp/chef \
    && cp /tmp/chef/chef.py /usr/local/bin/chef.py \
    && printf '#!/bin/bash\npython3 /usr/local/bin/chef.py "$@"' > /usr/local/bin/chef \
    && chmod +x /usr/local/bin/chef

# ArnoldC
RUN wget https://lhartikk.github.io/ArnoldC/ArnoldC.jar -O /usr/local/bin/ArnoldC.jar \
    && printf '#!/bin/bash\njava -jar /usr/local/bin/ArnoldC.jar "$@"' > /usr/local/bin/arnoldc \
    && chmod +x /usr/local/bin/arnoldc

# 8. Setup Workdir
WORKDIR /app
COPY . .
RUN mkdir -p logs
CMD ["python3", "runner.py"]
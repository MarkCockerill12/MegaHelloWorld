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
    nodejs ruby-full perl golang-go rustc cargo php-cli openjdk-17-jdk lua5.4 r-base ghc scala elixir clojure swi-prolog gnucobol fpc gnat tcl tcl-dev nasm gobjc gnustep-devel regina-rexx icont iconx ocaml erlang fsharp mono-complete mono-vbnc haxe zsh gforth dart powershell gnu-smalltalk ghostscript vim emacs-nox beef chicken-bin bc m4 gnuplot bison flex libgd-dev sbcl clisp guile-3.0 racket groovy intercal algol68g \
    && rm -rf /var/lib/apt/lists/*

# Fix binaries
RUN ln -s /usr/bin/beef /usr/local/bin/bf && \
    ln -s /usr/bin/regina /usr/local/bin/rexx || true && \
    ln -s /usr/bin/clisp /usr/local/bin/clisp || true && \
    ln -s /usr/bin/python3 /usr/local/bin/python

# 3. Pip/Npm/Gems (Grouped for caching)
RUN pip3 install --no-cache-dir \
    cmake \
    shakespearelang \
    rockstar-py \
    mathics-scanner \
    Mathics3 \
    brainfuck-interpreter \
    trumpscript \
    && npm install -g \
    ts-node typescript \
    coffeescript \
    purescript \
    elm \
    dogescript \
    befunge93 \
    unlambda \
    && gem install whitespace hexagony

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

# TrumpScript (Manual Install + Root Fix +
Part 1: The Modern Heavyweights (Languages 1–20).

1. Python
File: src/001_hello.py

Python
print("Hello World")
The Breakdown:

Created By: Guido van Rossum (1991).

Type: High-level, Interpreted, General-purpose.

The Story: Python was named after Monty Python’s Flying Circus, not the snake. It was designed to be highly readable, often using English keywords where other languages use punctuation.

Usage: It is currently the world's most popular language for Data Science, AI, and Machine Learning.

Who Uses It: Google (built their original crawler in it), Netflix (recommendation algorithms), and NASA (processing images from the James Webb Telescope).

Special Power: "Pseudocode that runs." It enforces indentation (whitespace), meaning messy code literally won't run.


2. JavaScript
File: src/002_hello.js
JavaScript

console.log("Hello World");
The Breakdown:
    • Created By: Brendan Eich (1995).
    • Type: High-level, JIT-Compiled (in modern engines), Event-driven.
    • The Story: Created in just 10 days at Netscape. It was originally named "Mocha," then "LiveScript," and finally "JavaScript" to piggyback on the popularity of Java, despite having almost nothing to do with Java.
    • Usage: The language of the web. If you see it in a browser, it's JavaScript. With Node.js, it now runs on servers too.
    • Who Uses It: Everyone. Facebook, Twitter, Amazon, and 98% of the internet.
    • Special Power: The "Universal Runtime." It is the only language that runs natively in every single web browser on Earth.


3. TypeScript
File: src/003_hello.ts
TypeScript

const message: string = "Hello World";
console.log(message);
The Breakdown:
    • Created By: Microsoft (Anders Hejlsberg, 2012).
    • Type: High-level, Transpiled (compiles to JS).
    • The Story: As JavaScript projects got massive, they became buggy because JS allows you to do silly things (like adding a number to a word). TypeScript adds "types" to prevent this.
    • Usage: Large-scale web applications.
    • Who Uses It: Microsoft (VS Code is written in it), Slack, and Airbnb.
    • Special Power: It is a "Superset" of JavaScript. Any valid JS is valid TS, but TS adds a safety layer on top that disappears when you compile it.


4. C
File: src/004_hello.c
C

#include <stdio.h>
int main() {
    printf("Hello World\n");
    return 0;
}
The Breakdown:
    • Created By: Dennis Ritchie (1972) at Bell Labs.
    • Type: Low-level, Compiled, Imperative.
    • The Story: The grandfather of modern computing. It was created to write the Unix operating system. Before C, operating systems were written in Assembly (pure machine instructions).
    • Usage: Operating Systems, Embedded Systems (microwaves, cars), and legacy banking.
    • Who Uses It: Linux Kernel, Windows, macOS (all their kernels are C).
    • Special Power: Speed and Portability. It is "close to the metal," meaning it manages memory manually. It gives you enough rope to shoot yourself in the foot (e.g., memory leaks).


5. C++
File: src/005_hello.cpp
C++

#include <iostream>
int main() {
    std::cout << "Hello World" << std::endl;
    return 0;
}
The Breakdown:
    • Created By: Bjarne Stroustrup (1985).
    • Type: Low-to-High level, Compiled, Object-Oriented.
    • The Story: Originally called "C with Classes." Stroustrup wanted the speed of C but the organizational structure of Simula.
    • Usage: Game Engines, High-Frequency Trading, and Resource-heavy Desktop Apps.
    • Who Uses It: Adobe (Photoshop), Unreal Engine, Google Chrome (the browser engine).
    • Special Power: Zero-overhead abstraction. You can write complex logical structures, but the compiler strips them down so they run as fast as raw C.


6. Java
File: src/006_hello.java
Java

class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
The Breakdown:
    • Created By: James Gosling at Sun Microsystems (1995).
    • Type: High-level, Compiled to Bytecode, Object-Oriented.
    • The Story: Their slogan was "Write Once, Run Anywhere." They achieved this by running on a "Virtual Machine" (JVM) rather than the physical hardware.
    • Usage: Enterprise backends and Android Apps (historically).
    • Who Uses It: Amazon, LinkedIn, Netflix (backend microservices), and Minecraft (the original game).
    • Special Power: The JVM ecosystem. It is incredibly stable and massive.


7. C#
File: src/007_hello.cs
C#

using System;
class Program {
    static void Main() {
        Console.WriteLine("Hello World");
    }
}
The Breakdown:
    • Created By: Anders Hejlsberg at Microsoft (2000).
    • Type: High-level, Compiled to Intermediate Language, Object-Oriented.
    • The Story: Microsoft saw Java and wanted their own version, but integrated tightly with Windows. It evolved to be arguably more feature-rich than Java (introducing async/await early on).
    • Usage: Enterprise Windows apps and Game Development (Unity).
    • Who Uses It: StackOverflow, Unity Technologies, Microsoft.
    • Special Power: Versatility via Unity. It is the primary language for indie game developers.


8. Go (Golang)
File: src/008_hello.go
Go

package main
import "fmt"
func main() {
    fmt.Println("Hello World")
}
The Breakdown:
    • Created By: Robert Griesemer, Rob Pike, and Ken Thompson at Google (2009).
    • Type: High-level (but feels low-level), Compiled, Statically Typed.
    • The Story: Google was tired of C++ being too slow to compile and too complex to read. They built Go to be "brutally simple." It has no classes, no inheritance, and very few keywords.
    • Usage: Cloud Infrastructure, Microservices, Networking.
    • Who Uses It: Google, Uber (Geofence lookups), Twitch, and Docker itself!
    • Special Power: Concurrency. It has "Goroutines," which are cheap, lightweight threads that let a program do thousands of things at once effortlessly.


9. Rust
File: src/009_hello.rs
Rust

fn main() {
    println!("Hello World");
}
The Breakdown:
    • Created By: Graydon Hoare at Mozilla (2010).
    • Type: Systems level, Compiled.
    • The Story: Designed to fix the biggest problem in C/C++: Memory Safety. In C, you can accidentally access memory you freed, causing crashes. Rust prevents this at compile time using a "Borrow Checker."
    • Usage: Systems programming, CLI tools, WebAssembly.
    • Who Uses It: Firefox (parts of the browser), Discord (rewrote critical services to fix lag), Dropbox.
    • Special Power: "Fearless Concurrency." It guarantees thread safety. It is consistently voted the "Most Loved Language" on StackOverflow.


10. PHP
File: src/010_hello.php
PHP

<?php
echo "Hello World\n";
?>
The Breakdown:
    • Created By: Rasmus Lerdorf (1995).
    • Type: High-level, Server-side Scripting.
    • The Story: Originally stood for "Personal Home Page." It wasn't intended to be a real language; it was just a set of tools to maintain Rasmus's online resume. It accidentally grew into the backbone of the web.
    • Usage: Server-side web development.
    • Who Uses It: Facebook (originally), Wikipedia, WordPress (which powers 40% of the web), Slack.
    • Special Power: Ease of deployment. You just drop a file on a server and it runs. No compiling, no complex configuration.


11. Ruby
File: src/011_hello.rb
Ruby

puts "Hello World"
The Breakdown:
    • Created By: Yukihiro "Matz" Matsumoto (1995).
    • Type: High-level, Interpreted.
    • The Story: Matz wanted a language that was "optimized for developer happiness." It reads like English prose.
    • Usage: Web Development (via Ruby on Rails).
    • Who Uses It: GitHub, Airbnb, Shopify, Twitch (originally).
    • Special Power: "The Principle of Least Surprise." The language behaves exactly how you expect it to, reducing cognitive load.


12. Swift
File: src/012_hello.swift
Swift

print("Hello World")
The Breakdown:
    • Created By: Chris Lattner at Apple (2014).
    • Type: High-level, Compiled.
    • The Story: Replaced Objective-C. Objective-C was 30 years old and used square brackets for everything [like this]. Swift is modern, safe, and fast.
    • Usage: iOS, macOS, watchOS, tvOS apps.
    • Who Uses It: Uber, Lyft, Airbnb (mobile apps), and obviously Apple.
    • Special Power: Protocol-Oriented Programming. It favors composition over inheritance, making code more flexible.


13. Kotlin
File: src/013_hello.kt
Kotlin

fun main() {
    println("Hello World")
}
The Breakdown:
    • Created By: JetBrains (2011).
    • Type: High-level, Statically Typed, JVM.
    • The Story: Java was getting old and verbose. JetBrains (who make IDEs) wanted a better language that was 100% compatible with Java but more concise. Google eventually declared it the official language of Android.
    • Usage: Android Apps, Server-side development.
    • Who Uses It: Google (Android), Pinterest, Trello, Evernote.
    • Special Power: Null Safety. Kotlin makes it almost impossible to get a "NullPointerException" (The Billion Dollar Mistake), which is the most common crash in Java apps.

    
14. Lua
File: src/014_hello.lua
Lua

print("Hello World")
The Breakdown:
    • Created By: Roberto Ierusalimschy (1993) in Brazil.
    • Type: High-level, Scripting, Embeddable.
    • The Story: "Lua" means Moon in Portuguese. It was designed to be tiny and easily embedded inside other C programs.
    • Usage: Game Scripting, Embedded Systems (Adobe Lightroom uses it for plugins).
    • Who Uses It: Roblox (entire game logic), World of Warcraft (UI/Addons), Angry Birds.
    • Special Power: It is tiny. The entire Lua interpreter is only about 200 KB.


15. Perl
File: src/015_hello.pl
Perl

print "Hello World\n";
The Breakdown:
    • Created By: Larry Wall (1987).
    • Type: High-level, Scripting.
    • The Story: "The Swiss Army Chainsaw of Scripting Languages." Before Python/Ruby, Perl was the glue that held the internet together. It is famous for being very dense; you can write complex programs in one line.
    • Usage: Text processing, System Administration, Legacy Web CGI.
    • Who Uses It: DuckDuckGo, Booking.com, Amazon (legacy systems).
    • Special Power: Text Manipulation (Regex). Perl's text processing capabilities are legendary and still superior to many modern languages.


16. R
File: src/016_hello.r
R

cat("Hello World\n")
The Breakdown:
    • Created By: Ross Ihaka and Robert Gentleman (1993).
    • Type: Domain-specific (Statistical Computing).
    • The Story: Created by statisticians, for statisticians. It is not really meant for building "apps"; it is meant for analyzing data.
    • Usage: Statistics, Data Mining, Bio-informatics.
    • Who Uses It: Google (Analytics), Pfizer (Clinical trials), The New York Times (Data journalism).
    • Special Power: Data Visualization. The libraries in R (like ggplot2) can create publication-quality graphs with a few lines of code.


17. Bash (Shell)
File: src/017_hello.sh
Bash

echo "Hello World"
The Breakdown:
    • Created By: Brian Fox (1989).
    • Type: Command Line Interpreter / Scripting.
    • The Story: "Bourne Again SHell" (a pun on the Bourne Shell). It is the default interface for Linux and macOS (until recently). It is how you talk to the Operating System.
    • Usage: Automating tasks, Deployment scripts, CI/CD pipelines.
    • Who Uses It: Every Sysadmin and DevOps engineer on Earth.
    • Special Power: Piping. You can take the output of one program and feed it directly into another using |.


18. Haskell
File: src/018_hello.hs
Haskell

main = putStrLn "Hello World"
The Breakdown:
    • Created By: Academic Committee (1990).
    • Type: Purely Functional, Statically Typed.
    • The Story: Named after logician Haskell Curry. It is an academic language designed to be mathematically "pure." Variables are immutable (they can't change), and functions have no side effects.
    • Usage: Fintech, Academic Research, High-assurance systems.
    • Who Uses It: Facebook (Anti-spam filters), Standard Chartered (Banking systems), Cardano (Blockchain).
    • Special Power: Lazy Evaluation. It doesn't calculate anything until the result is actually needed. You can define an "infinite list" of numbers in Haskell, and the computer won't crash.


19. Dart
File: src/019_hello.dart
Dart

void main() {
  print('Hello World');
}
The Breakdown:
    • Created By: Google (Lars Bak and Kasper Lund, 2011).
    • Type: Client-optimized, Compiled.
    • The Story: Google wanted a replacement for JavaScript. It failed at that, but then they realized it was perfect for their new UI toolkit: Flutter.
    • Usage: Cross-platform Mobile Apps (Flutter).
    • Who Uses It: Google Pay, BMW, Alibaba, Toyota.
    • Special Power: Hot Reload. When using Flutter, you can save the code and see the change on your phone instantly without restarting the app.


20. Scala
File: src/020_hello.scala
Scala

object HelloWorld extends App {
  println("Hello World")
}
The Breakdown:
    • Created By: Martin Odersky (2004).
    • Type: High-level, Functional & Object-Oriented, JVM.
    • The Story: Designed to be a "better Java." It blends Object-Oriented programming (like Java) with Functional programming (like Haskell). It runs on the Java Virtual Machine.
    • Usage: Big Data Processing (Spark), Distributed Systems.
    • Who Uses It: Twitter (migrated from Ruby to Scala to handle traffic), Netflix, Airbnb.
    • Special Power: Scalability (hence the name). It powers Apache Spark, the standard tool for processing massive datasets. 


Part 2: The Functional & Academic (Languages 21–40).
These languages often originated in universities or research labs. Many focus on "Functional Programming" a paradigm where you treat code like math equations rather than a list of instructions.

21. Elixir
File: src/021_hello.exs
Elixir

IO.puts "Hello World"
The Breakdown:
    • Created By: José Valim (2011).
    • Type: Functional, Concurrent, Distributed.
    • The Story: Built on the Erlang VM (BEAM). Valim wanted the raw power and stability of Erlang but with a syntax that was actually pleasant to read (like Ruby).
    • Usage: High-traffic web systems, Real-time messaging.
    • Who Uses It: Discord (handles millions of concurrent voice chats), Pinterest, PepsiCo.
    • Special Power: Fault Tolerance. If a part of your code crashes, Elixir simply restarts that tiny part without taking down the whole system.


22. Clojure
File: src/022_hello.clj
Clojure

(println "Hello World")
The Breakdown:
    • Created By: Rich Hickey (2007).
    • Type: Functional, Lisp dialect on the JVM.
    • The Story: Hickey wanted a modern Lisp that ran on Java's massive ecosystem. It emphasizes "immutability" (data cannot be changed once created).
    • Usage: Data analysis, Banking, Backend services.
    • Who Uses It: Nubank (largest digital bank in the world), Walmart, Adobe.
    • Special Power: Code is Data. You can write code that writes its own code (Macros) more easily than in almost any other language.


23. Julia
File: src/023_hello.jl
Julia

println("Hello World")
The Breakdown:
    • Created By: Jeff Bezanson et al. (2012) at MIT.
    • Type: High-performance, Dynamic.
    • The Story: They wanted a language with the speed of C, the readability of Python, and the math prowess of MATLAB. Surprisingly, they achieved it.
    • Usage: Scientific Computing, Data Science, AI.
    • Who Uses It: NASA (modeling space missions), FAA (aircraft collision avoidance), BlackRock.
    • Special Power: Multiple Dispatch. It picks the best function to run based on the types of all arguments, making math operations incredibly fast.


24. F#
File: src/024_hello.fs
F#

printfn "Hello World"
The Breakdown:
    • Created By: Don Syme at Microsoft Research (2005).
    • Type: Functional-first, .NET.
    • The Story: Microsoft's answer to OCaml. It brings functional programming to the .NET world.
    • Usage: Financial modeling, Enterprise web backends.
    • Who Uses It: Kaggle (backend), Jet.com (e-commerce engine).
    • Special Power: Type Providers. F# can connect to an external data source (like a database or CSV) and generate types for it instantly, so you get autocomplete for your data.


25. OCaml
File: src/025_hello.ml
OCaml

print_endline "Hello World";;
The Breakdown:
    • Created By: INRIA (1996) in France.
    • Type: Functional, Static typing.
    • The Story: The "Objective Caml." It is widely loved in academia and high-frequency trading for being both very safe and very fast.
    • Usage: Financial trading systems, Compilers.
    • Who Uses It: Jane Street (famous trading firm), Facebook (built the "Flow" tool and "Hack" compiler in it).
    • Special Power: The Type System. It is so smart that if your code compiles, it is almost guaranteed to work without runtime errors.


26. Erlang
File: src/026_hello.erl
Erlang

-module(hello).
-export([start/0]).
start() ->
    io:fwrite("Hello World~n").
The Breakdown:
    • Created By: Ericsson (1986).
    • Type: Concurrent, Functional.
    • The Story: Built for telephone switches. Phones cannot go down. Erlang was designed so that you can upgrade the code while the program is running.
    • Usage: Telecommunications, Instant Messaging.
    • Who Uses It: WhatsApp (managed 900 million users with only 50 engineers), Nintendo (Switch push notifications).
    • Special Power: The "Let It Crash" philosophy. Don't handle errors; just let the process die and spawn a fresh one instantly.


27. Common Lisp
File: src/027_hello.lisp
Lisp

(format t "Hello World~%")
The Breakdown:
    • Created By: ANSI Committee (1984), roots in 1958.
    • Type: Multi-paradigm, Dynamic.
    • The Story: One of the oldest languages still in use. Lisp introduced if-then-else, garbage collection, and dynamic typing to the world.
    • Usage: AI research (historically), Complex system modeling.
    • Who Uses It: NASA (Deep Space 1 auto-navigation), Grammarly (core engine).
    • Special Power: Macros. You can redefine the syntax of the language itself to suit your needs.


28. Scheme
File: src/028_hello.scm
Scheme

(display "Hello World\n")
The Breakdown:
    • Created By: Guy Steele and Gerald Sussman (1975).
    • Type: Minimalist Lisp.
    • The Story: Created to be a cleaner, simpler Lisp. It is the standard language used to teach computer science concepts (Structure and Interpretation of Computer Programs).
    • Usage: Education, Scripting (GIMP).
    • Who Uses It: GIMP (the image editor uses it for plugins/scripts).
    • Special Power: Tail Recursion. You can call a function from itself infinitely without crashing the computer's memory.


29. Racket
File: src/029_hello.rkt
Code snippet

#lang racket
(displayln "Hello World")
The Breakdown:
    • Created By: PLT Inc. (1995).
    • Type: Lisp/Scheme dialect.
    • The Story: Originally called "PLT Scheme." It evolved into a "Programming Language for Creating Programming Languages."
    • Usage: Research, Education, Game Scripting.
    • Who Uses It: Naughty Dog (used a Racket-based language for Uncharted/The Last of Us scripting).
    • Special Power: Language-Oriented Programming. You can change the language syntax completely with just one line of code (#lang).


30. Groovy
File: src/030_hello.groovy
Groovy

println "Hello World"
The Breakdown:
    • Created By: James Strachan (2003).
    • Type: Object-Oriented, Dynamic.
    • The Story: A dynamic language for the Java platform. If Java is tedious and rigid, Groovy is loose and fun.
    • Usage: Scripting, CI/CD Pipelines, Testing.
    • Who Uses It: Jenkins (the standard for automation pipelines), Netflix, Oracle.
    • Special Power: Java Interop. It works perfectly with any Java library, but you write half as much code.


31. Elm
File: src/031_hello.elm
Elm

module Hello exposing (..)
import Html exposing (text)
main = text "Hello World"
The Breakdown:
    • Created By: Evan Czaplicki (2012).
    • Type: Functional, Compiled to JS.
    • The Story: Frustrated by runtime errors in JavaScript? Elm guarantees "No Runtime Exceptions." If it compiles, it won't crash your browser.
    • Usage: Frontend Web Development.
    • Who Uses It: NoRedInk, Prezi, IBM (parts of dashboards).
    • Special Power: The Error Messages. Elm is famous for having the friendliest compiler errors that actually tell you how to fix the bug.


32. Prolog
File: src/032_hello.plg
Prolog

:- initialization(main).
main :- write('Hello World'), nl, halt.
The Breakdown:
    • Created By: Alain Colmerauer (1972).
    • Type: Logic Programming.
    • The Story: Totally different from normal coding. You don't tell the computer how to do something; you describe facts and rules, and the computer figures out the answer.
    • Usage: AI, Natural Language Processing, Expert Systems.
    • Who Uses It: IBM Watson (parts of the reasoning engine), Java Virtual Machine (verification rules).
    • Special Power: Backtracking. It automatically tries every possibility to solve a logic puzzle.


33. Fortran
File: src/033_hello.f90
Fortran

program hello
  print *, "Hello World"
end program hello
The Breakdown:
    • Created By: John Backus at IBM (1957).
    • Type: Imperative, Compiled.
    • The Story: The first widely used high-level language. Before Fortran, you had to write machine code. Critics said it would never be as efficient as hand-coded assembly. They were wrong.
    • Usage: Supercomputing, Weather Prediction, Physics Simulations.
    • Who Uses It: NOAA (Weather forecasting), NASA, CERN.
    • Special Power: Number Crunching. It is still arguably the fastest language in the world for complex array mathematics.


34. COBOL
File: src/034_hello.cob
COBOL

       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       PROCEDURE DIVISION.
           DISPLAY 'Hello World'.
           STOP RUN.
The Breakdown:
    • Created By: CODASYL Committee (Grace Hopper involved) (1959).
    • Type: Imperative, Business-oriented.
    • The Story: Designed to be readable by managers. It uses English words for everything (ADD 1 TO x instead of x++).
    • Usage: Banking, Government, Insurance systems.
    • Who Uses It: IRS, Visa/Mastercard, and 80% of the world's daily financial transactions.
    • Special Power: Decimal Arithmetic. It handles money perfectly without the rounding errors that floating-point languages (like Python/C) have.


35. Pascal
File: src/035_hello.pas
Delphi

program Hello;
begin
  WriteLn('Hello World');
end.
The Breakdown:
    • Created By: Niklaus Wirth (1970).
    • Type: Imperative, Structured.
    • The Story: Designed to teach good programming habits. It forced you to structure your code cleanly.
    • Usage: Education, Legacy Desktop Apps (Delphi).
    • Who Uses It: Apple (The original Mac OS was written in Pascal), Skype (early versions).
    • Special Power: Compilation Speed. Turbo Pascal was famous for compiling instantly.


36. Ada
File: src/036_hello.adb
Ada

with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
    Put_Line("Hello World");
end Hello;
The Breakdown:
    • Created By: US Department of Defense (1980).
    • Type: Imperative, Object-Oriented.
    • The Story: The US military had 450 different languages. They commissioned Ada to replace them all. Named after Ada Lovelace, the first programmer.
    • Usage: Avionics, Air Traffic Control, Missiles, Trains.
    • Who Uses It: Boeing (777), European Space Agency (Ariane rockets), TGV (French high-speed trains).
    • Special Power: Safety. It checks for errors so strictly that it is very hard to write code that crashes.


37. Assembly (NASM x64)
File: src/037_hello.asm
Code snippet

section .data
    msg db "Hello World", 0xA
    len equ $ - msg
section .text
    global _start
_start:
    mov rax, 1          ; system call for write
    mov rdi, 1          ; file handle 1 is stdout
    mov rsi, msg        ; address of string to output
    mov rdx, len        ; number of bytes
    syscall             ; invoke operating system to do the write
mov rax, 60         ; system call for exit
    xor rdi, rdi        ; exit code 0
    syscall             ; invoke operating system to exit
The Breakdown:
    • Created By: Various (1940s).
    • Type: Low-level.
    • The Story: This is readable machine code. You are manually moving bytes into CPU registers (rax, rdi) and telling the CPU to execute.
    • Usage: OS Kernels, Drivers, Reverse Engineering.
    • Who Uses It: RollerCoaster Tycoon (written entirely in Assembly by one guy), BIOS developers.
    • Special Power: Absolute Control. You can do anything the hardware is capable of.


38. Visual Basic .NET
File: src/038_hello.vb
VB.Net

Module Module1
    Sub Main()
        Console.WriteLine("Hello World")
    End Sub
End Module
The Breakdown:
    • Created By: Microsoft (2001).
    • Type: Object-Oriented.
    • The Story: The evolution of the classic Visual Basic. It was the gateway drug for millions of programmers in the 90s/00s.
    • Usage: Internal Enterprise tools, Windows Desktop Apps.
    • Who Uses It: Healthcare and Manufacturing companies for internal tools.
    • Special Power: Rapid Application Development (RAD). Dragging and dropping buttons on a form is faster here than almost anywhere else.


39. Objective-C
File: src/039_hello.m
Objective-C

#import <Foundation/Foundation.h>
int main() {
    @autoreleasepool {
        NSLog(@"Hello World");
    }
    return 0;
}
The Breakdown:
    • Created By: Brad Cox and Tom Love (1984).
    • Type: Object-Oriented C.
    • The Story: They took C and glued Smalltalk-style messaging onto it. Steve Jobs licensed it for NeXT, which became macOS.
    • Usage: Legacy iOS/macOS apps.
    • Who Uses It: Apple (historically), many older iOS apps.
    • Special Power: Dynamic Runtime. You can swap out methods (functions) while the program is running (Swizzling).


40. Smalltalk
File: src/040_hello.st
Smalltalk

Transcript show: 'Hello World'; cr.
The Breakdown:
    • Created By: Alan Kay at Xerox PARC (1972).
    • Type: Pure Object-Oriented.
    • The Story: This language invented the GUI, the mouse, and Object-Oriented Programming. Steve Jobs saw Smalltalk and was inspired to make the Macintosh.
    • Usage: Educational simulations, Research.
    • Who Uses It: JP Morgan (financial risk system "Kapital").
    • Special Power: Live Coding. The environment and the code are one. You can inspect and change any object in the system while it runs.


Part 3: The Niche & Utilities (Languages 41–60).
This section covers the "Swiss Army Knives"—languages often used for specific tasks like text processing, automation, or fixing what other languages broke.

41. Tcl (Tool Command Language)
File: src/041_hello.tcl
Tcl

puts "Hello World"
The Breakdown:
    • Created By: John Ousterhout (1988).
    • Type: Scripting, Embeddable.
    • The Story: Designed to be easily embedded into C applications to give them a scripting interface. It is often paired with "Tk" (Tcl/Tk) to create simple GUIs.
    • Usage: Chip design (EDA tools), Cisco Routers.
    • Who Uses It: NASA (Mars Lander control systems), Cisco, Pixar (internal tools).
    • Special Power: "Everything is a String." Even the code itself is treated as a string, making it incredibly flexible for metaprogramming.


42. D
File: src/042_hello.d
D

import std.stdio;
void main() {
    writeln("Hello World");
}
The Breakdown:
    • Created By: Walter Bright (2001).
    • Type: Systems, Compiled.
    • The Story: Explicitly designed to be the successor to C++. It keeps the high performance of C++ but removes the decades of "cruft" and backward-compatibility headaches.
    • Usage: High-performance games, Data science.
    • Who Uses It: Facebook (parts of their backend), eBay.
    • Special Power: Compile Speed. It compiles nearly as fast as interpreted languages run, making the "edit-compile-run" loop incredibly tight.


43. Vimscript
File: src/043_hello.vim
Vim Script

echo "Hello World"
The Breakdown:
    • Created By: Bram Moolenaar (1991).
    • Type: Editor Scripting.
    • The Story: The built-in language of the Vim text editor. It exists solely to customize Vim.
    • Usage: Configuring text editors.
    • Who Uses It: Millions of developers who refuse to use a mouse.
    • Special Power: Ubiquity. If you are on a Linux server, Vim is likely the only editor installed. Knowing this language means you can customize your environment anywhere.


44. Emacs Lisp (Elisp)
File: src/044_hello.el
Lisp

(message "Hello World")
The Breakdown:
    • Created By: Richard Stallman (1985).
    • Type: Lisp dialect.
    • The Story: Emacs isn't just a text editor; it's a Lisp interpreter that happens to have text editing features. You can rewrite the editor while using it.
    • Usage: Configuring Emacs, Productivity tools (Org-mode).
    • Who Uses It: Julian Assange (used it for encryption tools), Neal Stephenson.
    • Special Power: Extensibility. People have written email clients, web browsers, and Tetris clones entirely inside Emacs using Elisp.


45. PowerShell
File: src/045_hello.ps1
PowerShell

Write-Host "Hello World"
The Breakdown:
    • Created By: Jeffrey Snover at Microsoft (2006).
    • Type: Shell / Scripting.
    • The Story: Windows needed a real command line to compete with Linux's Bash. Snover realized passing text between commands (like Bash) was messy, so PowerShell passes entire Objects.
    • Usage: System Administration, Azure Automation.
    • Who Uses It: Every Windows Sysadmin.
    • Special Power: Object Pipelines. Instead of parsing text output with regex, you can just do .Name or .ID on the output of a previous command.


46. BASIC (Bywater BASIC)
(Replaces SQL as discussed)
File: src/046_hello.bas
Basic

10 PRINT "Hello World"
20 END
The Breakdown:
    • Created By: Kemeny and Kurtz (1964).
    • Type: Imperative, Educational.
    • The Story: "Beginner's All-purpose Symbolic Instruction Code." It democratized computing. Before BASIC, only scientists programmed. After BASIC, kids programmed.
    • Usage: Education, Retro-computing.
    • Who Uses It: Bill Gates wrote the first Microsoft product (Altair BASIC) in this language.
    • Special Power: Line Numbers. The flow of control is dictated by manually numbered lines (GOTO 10), which leads to "Spaghetti Code."


47. Crystal
File: src/047_hello.cr
Crystal

puts "Hello World"
The Breakdown:
    • Created By: Ary Borenszweig (2014).
    • Type: Systems, Compiled.
    • The Story: "Fast as C, slick as Ruby." It looks almost identical to Ruby code but compiles down to a raw binary.
    • Usage: High-performance web servers, CLI tools.
    • Who Uses It: Nikola Motor Company (embedded systems).
    • Special Power: Type Inference. You rarely have to tell it "this is an integer." It figures it out, but still gives you the safety of a statically typed language.


48. Nim
File: src/048_hello.nim
Nim

echo "Hello World"
The Breakdown:
    • Created By: Andreas Rumpf (2008).
    • Type: Systems, Compiled.
    • The Story: Uses Python-like indentation but compiles to C. It allows you to write high-level code that can access hardware directly.
    • Usage: Game Development, Malware development (unfortunately, due to its small binary size and C compilation).
    • Who Uses It: Status.im (Blockchain messaging).
    • Special Power: Metaprogramming. You can write code that modifies the language's own syntax tree during compilation.


49. Awk
File: src/049_hello.awk
Awk

BEGIN { print "Hello World" }
The Breakdown:
    • Created By: Aho, Weinberger, and Kernighan (1977).
    • Type: Data-driven scripting.
    • The Story: Designed solely for processing text files. The name is just the initials of the creators.
    • Usage: Log file analysis, simple data extraction.
    • Who Uses It: Unix Sysadmins.
    • Special Power: One-liners. You can write a complete data processing program in 10 characters. awk '{print $1}' prints the first word of every line in a file.


50. Sed
File: src/050_hello.sed
Code snippet

s/^/Hello World/p
q
(Note: Sed is a stream editor, so "Hello World" is tricky. This script replaces the start of input with Hello World, prints it, and quits.)
The Breakdown:
    • Created By: Lee E. McMahon (1974).
    • Type: Stream Editor.
    • The Story: The ultimate "Find and Replace" tool. It modifies data as it flows through a pipe, without opening the file.
    • Usage: Automated text replacement in scripts.
    • Who Uses It: Everyone who uses Linux.
    • Special Power: Regex integration. It is the engine behind many massive bulk-editing tasks.


51. Zig
File: src/051_hello.zig
Code snippet

const std = @import("std");
pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello World\n", .{});
}
The Breakdown:
    • Created By: Andrew Kelley (2016).
    • Type: Systems, Low-level.
    • The Story: Designed to replace C, not C++. It removes the "hidden magic" (no hidden control flow, no hidden memory allocations).
    • Usage: Systems programming, Game Engines.
    • Who Uses It: Uber (rewrote some high-performance tools in Zig), Bun (the super-fast JS runtime).
    • Special Power: Comptime. It can run code during compilation. You can write a function that calculates a value, and only the result ends up in the final binary.


52. V (Vlang)
File: src/052_hello.v
Verilog

fn main() {
    println('Hello World')
}
The Breakdown:
    • Created By: Alexander Medvednikov (2019).
    • Type: Systems, Compiled.
    • The Story: Created to build the "Volt" mail client. It claims to compile 100x faster than C++ and be as safe as Rust.
    • Usage: Web backends, Graphics.
    • Who Uses It: Open source enthusiasts (still young).
    • Special Power: No Null, No Global Variables, No Undefined Behavior. It defaults to "Safe."


53. Haxe
File: src/053_hello.hx
Haxe

class Main {
    static function main() {
        trace("Hello World");
    }
}
The Breakdown:
    • Created By: Nicolas Cannasse (2005).
    • Type: Multi-target.
    • The Story: The "Write Once, Compile to Anything" language. Haxe code can be compiled into JavaScript, C++, C#, Java, Python, Lua, and PHP.
    • Usage: Game Development (indie).
    • Who Uses It: Motion Twin (created the hit game Dead Cells using Haxe).
    • Special Power: Transpilation. You write Haxe, and it spits out native C++ code for consoles and JavaScript code for the web from the same source.


54. CoffeeScript
File: src/054_hello.coffee
CoffeeScript

console.log "Hello World"
The Breakdown:
    • Created By: Jeremy Ashkenas (2009).
    • Type: Transpiled to JS.
    • The Story: Before ES6, JavaScript was ugly. CoffeeScript made it look like Ruby/Python. It was so influential that JavaScript eventually adopted many of its features (arrow functions, classes).
    • Usage: Legacy web apps.
    • Who Uses It: Dropbox (historically), GitHub (historically).
    • Special Power: Brevity. It saved developers from typing millions of curly braces {}.


55. Rexx
File: src/055_hello.rexx
Code snippet

SAY "Hello World"
The Breakdown:
    • Created By: Mike Cowlishaw at IBM (1979).
    • Type: Scripting.
    • The Story: The "Restructured Extended Executor." It was the main scripting language for IBM mainframes (z/OS) and OS/2.
    • Usage: Mainframe automation.
    • Who Uses It: IBM, Major Banks.
    • Special Power: Human-centric arithmetic. It processes numbers exactly as a human does (decimal), avoiding computer binary errors.


56. Icon
File: src/056_hello.icn
Code snippet

procedure main()
    write("Hello World")
end
The Breakdown:
    • Created By: Ralph Griswold (1977).
    • Type: High-level.
    • The Story: A descendant of SNOBOL. It focuses on string processing and "goal-directed execution."
    • Usage: Text analysis, Prototyping.
    • Who Uses It: Academics.
    • Special Power: Generators. Expressions in Icon can produce a sequence of results, and the program will try them one by one until it succeeds.


57. Forth
File: src/057_hello.fth
Code snippet

." Hello World" CR
The Breakdown:
    • Created By: Charles Moore (1970).
    • Type: Stack-based.
    • The Story: A very low-level language that uses a "stack" for everything. 1 2 + pushes 1, pushes 2, then adds them.
    • Usage: Boot loaders (Open Firmware), Spacecraft.
    • Who Uses It: NASA (used on the Philae lander on the Rosetta mission).
    • Special Power: Minimalism. A Forth interpreter can be written in a few kilobytes of assembly.


58. Factor
File: src/058_hello.factor
Code snippet

USE: io
"Hello World" print
The Breakdown:
    • Created By: Slava Pestov (2003).
    • Type: Stack-based, Concatenative.
    • The Story: A modern evolution of Forth. It combines the low-level stack logic with high-level object-oriented features.
    • Usage: Research, Hobbyist scripting.
    • Who Uses It: Language enthusiasts.
    • Special Power: The Listener. It has an incredibly interactive REPL where you can inspect the stack visually.


59. J
File: src/059_hello.ijs
Code snippet

'Hello World'
The Breakdown:
    • Created By: Kenneth Iverson (1990).
    • Type: Array programming.
    • The Story: The successor to APL. Iverson wanted a language that used standard ASCII characters instead of APL's weird symbols. It is extremely terse.
    • Usage: Financial analysis, Mathematical modeling.
    • Who Uses It: Quants (Quantitative Analysts).
    • Special Power: Tacit Programming. You define functions without mentioning their arguments.


60. APL
File: src/060_hello.apl
Code snippet

'Hello World'
The Breakdown:
    • Created By: Kenneth Iverson (1966).
    • Type: Array programming.
    • The Story: "A Programming Language." It is famous for using Greek letters and weird symbols (⍴, ⍳, ∊). You need a special keyboard to type it efficiently.
    • Usage: High-finance, Actuarial science.
    • Who Uses It: Morgan Stanley, Dyalog.
    • Special Power: Density. You can implement Conway's Game of Life in a single line of code. It changes how you think about data.


Part 4: The Silly (Languages 61–80).
This section marks the transition from "Useful Tools" to "Internet Culture."

61. PostScript
File: src/061_hello.ps
Code snippet

/Helvetica findfont
24 scalefont setfont
100 100 moveto
(Hello World) show
showpage
The Breakdown:
    • Created By: John Warnock (Adobe) (1982).
    • Type: Concatenative, Page Description.
    • The Story: Before PostScript, printers were dumb. You sent them "Print A." PostScript is a full Turing-complete programming language that runs inside the printer.
    • Usage: High-end Printing, PDF generation.
    • Who Uses It: Adobe, HP Printers.
    • Special Power: Vector Graphics. You aren't defining pixels; you are defining mathematical shapes that scale infinitely.


62. Mathematica (Wolfram Language)
File: src/062_hello.wls
Mathematica

Print["Hello World"]
The Breakdown:
    • Created By: Stephen Wolfram (1988).
    • Type: Symbolic.
    • The Story: It attempts to model the entire world. It knows everything from chemical elements to city populations built-in.
    • Usage: Physics, Math Research, Apple's Siri (originally).
    • Who Uses It: Apple (Siri's knowledge base), CERN.
    • Special Power: Knowledge. It knows the GDP of France in 1990 without you needing to import a database. It's built-in.


63. Gnuplot
File: src/063_hello.gp
Code snippet

print "Hello World"
The Breakdown:
    • Created By: Thomas Williams (1986).
    • Type: Command-line Graphing.
    • The Story: Scientists needed a way to visualize data on text terminals.
    • Usage: Academic papers.
    • Who Uses It: Academics worldwide.
    • Special Power: ASCII Art Graphs. It can plot complex 3D mathematical functions using only text characters.


64. Make
File: src/064_hello.mk
Makefile

all:
    @echo "Hello World"
The Breakdown:
    • Created By: Stuart Feldman (1976).
    • Type: Build Automation.
    • The Story: Feldman was tired of manually compiling files. He wrote make to check which files changed and only recompile those.
    • Usage: Compiling C/C++.
    • Who Uses It: Linux Kernel, Google (Bazel is a descendant).
    • Special Power: Dependency Graphing. It knows exactly what order to do things in.


65. CMake
File: src/065_hello.cmake
CMake

message("Hello World")
The Breakdown:
    • Created By: Kitware (2000).
    • Type: Meta-Build System.
    • The Story: Makefiles are hard to write for different operating systems. CMake writes the Makefiles for you.
    • Usage: Large C++ projects.
    • Who Uses It: Netflix, KDE, React Native.
    • Special Power: Cross-Platform generation. Write one script, generate build files for Visual Studio (Windows) and Make (Linux).


66. Bc (Basic Calculator)
File: src/066_hello.bc
Code snippet

print "Hello World\n"
quit
The Breakdown:
    • Created By: Robert Morris and Lorinda Cherry (1975).
    • Type: Arbitrary-precision calculator.
    • The Story: A standard Unix tool. It looks like a calculator but is a full language with loops and variables.
    • Usage: Shell scripts requiring math.
    • Special Power: Precision. It can calculate Pi to 10,000 decimal places in seconds.


67. M4
File: src/067_hello.m4
Code snippet

Hello World
The Breakdown:
    • Created By: Brian Kernighan and Dennis Ritchie (1977).
    • Type: Macro Processor.
    • The Story: It scans text and replaces "macros" with code. It is the engine under the hood of autoconf.
    • Usage: Generating configuration files.
    • Special Power: Invisibility. It powers the installation of almost every Linux tool, but users rarely see it.


68. PureScript
File: src/068_hello.purs
Code snippet

module Main where
import Effect.Console (log)
main = log "Hello World"
The Breakdown:
    • Created By: Phil Freeman (2013).
    • Type: Purely Functional, Compiles to JS.
    • The Story: Haskell is great, but it doesn't run in the browser. PureScript is Haskell designed specifically for the web.
    • Usage: Frontend Web Apps.
    • Special Power: No Side Effects. It is mathematically "pure."


69. Brainf*ck 
File: src/069_hello.bf
Brainfuck

++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
The Breakdown:
    • Created By: Urban Müller (1993).
    • Type: Esoteric, Minimalist.
    • The Story: Müller wanted to create a language with the smallest possible compiler (it was 240 bytes). He succeeded.
    • The Language: There are only 8 commands: + - > < [ ] . ,. You have a tape of memory and a pointer. That's it.
    • Usage: Code Golf, Mental torture.
    • Special Power: Turing Completeness. Despite having only 8 symbols, it can theoretically run any program that Python can run... it just takes a billion times longer to write.


70. ArnoldC
File: src/070_hello.arnoldc
Java

IT'S SHOWTIME
TALK TO THE HAND "Hello World"
YOU HAVE BEEN TERMINATED
The Breakdown:
    • Created By: Lauri Hartikka (2013).
    • Type: Imperative, Meme.
    • The Story: A language composed entirely of Arnold Schwarzenegger quotes.
    • Keywords: GET TO THE CHOPPER (do/while), YOU HAVE BEEN TERMINATED (end main).
    • Special Power: It is actually valid Java code under the hood.


71. LOLCODE
File: src/071_hello.lol
Plaintext

HAI 1.2
  CAN HAS STDIO?
  VISIBLE "Hello World"
KTHXBYE
The Breakdown:
    • Created By: Adam Lindsay (2007).
    • Type: Esoteric.
    • The Story: Based on the "I Can Has Cheezburger" cat memes of the mid-2000s.
    • Keywords: HAI (Start), KTHXBYE (End), IZ (If), O RLY? (Else).
    • Special Power: It’s arguably the most readable esoteric language because it reads like a chatroom from 2005.


72. Rockstar
File: src/072_hello.rock
Plaintext

Say "Hello World"
(Or the poetic version):
Plaintext

Midnight takes your heart and your soul
While your heart is as high as your soul
Put your heart without your soul into your heart
Give back your heart
The Breakdown:
    • Created By: Dylan Beattie (2018).
    • Type: Esoteric.
    • The Story: Created so recruiters could literally call people "Rockstar Developers."
    • Special Power: The code is indistinguishable from 80s Hair Metal lyrics. Variables are "common nouns," and values are assigned poetically.


73. Chef
File: src/073_hello.chef
Plaintext

Hello World Souffle.
Ingredients.
72 g haricot beans
101 eggs
108 g lard
111 cups oil
32 zucchinis
119 ml water
111 tsp salt
114 ml mustard
108 g cumin
100 g flour
33 g sugar
Method.
Put flour into the mixing bowl.
Put sugar into the mixing bowl.
Put cumin into the mixing bowl.
Put mustard into the mixing bowl.
Put salt into the mixing bowl.
Put water into the mixing bowl.
Put zucchinis into the mixing bowl.
Put oil into the mixing bowl.
Put lard into the mixing bowl.
Put eggs into the mixing bowl.
Put haricot beans into the mixing bowl.
Liquefy contents of the mixing bowl.
Pour contents of the mixing bowl into the baking dish.
Serves 1.
The Breakdown:
    • Created By: David Morgan-Mar (2002).
    • Type: Stack-based.
    • The Story: Programs must be valid cooking recipes. Variables are ingredients (dry vs liquid affects the stack).
    • Special Power: "Deliciousness." A design goal is that the recipes should actually taste good if prepared (this one probably doesn't).


74. Shakespeare (SPL)
File: src/074_hello.spl
Plaintext

The Infamous Hello World Program.
Romeo, a young man with a remarkable patience.
Juliet, a likewise young woman of remarkable grace.
Ophelia, a remarkable woman much in dispute with Hamlet.
Hamlet, the flatterer of Andersen Insulting A/S.
Act I: Hamlet's insults and flattery.
Scene I: The insulting of Romeo.
[Enter Hamlet and Romeo]
Hamlet:
 You lying stupid fatherless smelly coward!
 You are as sweet as the sum of a beautiful rose and a flower!
[Exit Hamlet]
[Enter Juliet]
Romeo:
 Speak your mind. You are as worried as the sum of yourself and the difference between my small smooth hamster and a stone. Speak your mind!
[Exit Romeo]
[Enter Ophelia]
Juliet:
 Speak your mind!
[Exit Ophelia]
(Note: This is a truncated version; the real one is much longer)12
The Breakdown:34
    • Created By: Jon Åslund and Karl Hasselström (2001).56
    • Type: Esoteric.78
    • The Story: Variables are characters. Entering/Exiting the stage manipulates the stack.910
    • Special Power: Code looks like a legiti11mate stage play.


75. Chicken
File: src/075_hello.chicken
Plaintext

chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken chicken
(Note: You need about 50 lines of the word "chicken" to print Hello World).
The Breakdown:
    • Created By: Torbjörn Söderstedt.
    • Type: Esoteric.
    • The Story: Inspired by a parody scientific paper where every word was "Chicken."
    • The Code: The number of times the word "chicken" appears on a line determines the opcode.
    • Special Power: It is the most confusing language to read aloud.


76. Whitespace
File: src/076_hello.ws
(I cannot paste the code because it is invisible. It consists entirely of Spaces, Tabs, and Newlines.)
The Breakdown:
    • Created By: Edwin Brady and Chris Morris (2003).
    • Type: Stack-based.
    • The Story: Most languages ignore whitespace. This language ignores everything except whitespace. You can hide a Whitespace program inside a normal C program's indentation.
    • Special Power: Steganography. You can hide code in plain sight.


77. Befunge
File: src/077_hello.befunge
Plaintext

>              v
v  ,,,,,"Hello"<
>48*,          v
v,,,,,,"World!"<
>25*,@
The Breakdown:
    • Created By: Chris Pressey (1993).
    • Type: Two-dimensional.
    • The Story: Most code is read left-to-right. Befunge is read in a 2D grid. Arrows (> < ^ v) change the direction of the program counter.
    • Usage: Code Golf.
    • Special Power: The playhead moves around the grid like a snake.


78. Piet
File: src/078_hello.piet
(Usually an image file. For our text-based runner, we interpret a "codel" trace or skip execution if the runner doesn't support images. For this repo, we can use a hex representation).
The Breakdown:
    • Created By: David Morgan-Mar.
    • Type: Visual.
    • The Story: Programs are bitmap images looking like abstract art (Mondrian style). The code is defined by the difference in color as you move from one pixel to the next.
    • Special Power: It’s the prettiest programming language.


79. Omgrofl
File: src/079_hello.omgrofl
Plaintext

loool
rfo
    lmao
    lmao
    lmao
    lmao
    lmao
    lmao
    lmao
    lmao
    loooooool
    tl;dr
    lmao
    loooooool
    tl;dr
    ... (and so on)
stfu
The Breakdown:
    • Created By: Juraj Borza.
    • Type: Stack-based.
    • The Story: All keywords are internet slang.
    • Keywords: loool (main), stfu (exit), lmao (increment).
    • Special Power: It feels like reading a YouTube comment section.


80. TrumpScript
File: src/080_hello.tr
Plaintext

say "Hello World"!
America is great.
The Breakdown:
    • Created By: Sam Shadwell (2016).
    • Type: Satire.
    • The Story: Created during the election.
    • Rules: No floating point numbers (only integers). Numbers must be larger than 1 million. You cannot import things from "China."
    • Special Power: If the computer thinks the code is "Fake News," it won't run.


Part 5 (Languages 81–100).
This section contains the most difficult, the most ancient, and the most ridiculous languages in existence.

81. Hodor
File: src/081_hello.hodor
Plaintext

Hodor Hodor Hodor Hodor Hodor Hodor Hodor Hodor... (repeated 100+ times)
The Breakdown:
    • Created By: Unspecified (Game of Thrones fan).
    • Type: Esoteric.
    • The Story: Every command is the word "Hodor." The logic is determined by the capitalization and punctuation of "Hodor."
    • Special Power: It is completely unreadable unless you are Bran Stark.


82. Ook!
File: src/082_hello.ook
Plaintext

Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
Ook. Ook. Ook. Ook. Ook! Ook? Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
The Breakdown:
    • Created By: David Morgan-Mar (2009).
    • Type: Esoteric (Brainfuck derivative).
    • The Story: Designed to be writable by orangutans. It is mathematically identical to Brainfuck, but the 8 commands are mapped to combinations of Ook., Ook?, and Ook!.
    • Special Power: Primate-compatible syntax.


83. Intercal
File: src/083_hello.i
Code snippet

DO ,1 <- #13
PLEASE DO ,1 SUB #1 <- #238
DO ,1 SUB #2 <- #108
DO ,1 SUB #3 <- #112
DO ,1 SUB #4 <- #0
PLEASE READ OUT ,1
PLEASE GIVE UP
The Breakdown:
    • Created By: Don Woods and James M. Lyon (1972).
    • Type: Parody.
    • The Story: The "Compiler Language With No Pronounceable Acronym." It was created to mock the rigid languages of the 70s.
    • Special Power: Politeness. If you don't use the keyword PLEASE enough times, the compiler rejects your code for being rude. If you say PLEASE too much, it rejects it for being subservient.


84. False
File: src/084_hello.f
Plaintext

"Hello World"
The Breakdown:
    • Created By: Wouter van Oortmerssen (1993).
    • Type: Stack-based, Obfuscated.
    • The Story: One of the first languages designed specifically to be as confusing as possible with a tiny compiler (1KB). It inspired Brainfuck.
    • Special Power: Density. It looks like line noise or a cat walking on a keyboard.


85. Malbolge
File: src/085_hello.mal
Plaintext

(=<`:9876Z4321UT.-Q+*)M'&%$H"!~}|Bzy?=|{z]KwZY44Eq0/{mlk**hKs_dG5[m_BA{?-Y;;Vb'rR5431M}/.zHGwEDCBA@98\6543W10/.R,+O<
The Breakdown:
    • Created By: Ben Olmstead (1998).
    • Type: "The Ninth Circle of Hell."
    • The Story: Named after the 8th circle of Hell in Dante's Inferno. It was designed to be impossible to write. It took 2 years for the first "Hello World" program to appear, and it wasn't written by a human—it was found by a computer using a beam search algorithm.
    • Special Power: Self-modifying code that encrypts itself after every instruction.


86. ZOMBIE
File: src/086_hello.zombie
Plaintext

HelloWorld is a zombie
summon
task SayHello
  say "Hello World"
animate
animate
The Breakdown:
    • Created By: Unspecified.
    • Type: Esoteric.
    • The Story: A language about necromancy. Data storage is handled by "summoning zombies" and "binding" entities to them.
    • Special Power: Syntax errors are reported as "The zombie bites you."


87. Cow
File: src/087_hello.cow
Plaintext

MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO
MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO MoO...
The Breakdown:
    • Created By: Sean Heber (2003).
    • Type: Esoteric (Brainfuck derivative).
    • The Story: Based on the "moo" sounds of cows. There are 12 variations of capitalization (moO, mOo, MOo, etc.), each corresponding to a command.
    • Special Power: Bovine logic.


88. Emojicode
File: src/088_hello.emojicode
Plaintext

🏁 🍇
  😀 🔤Hello World🔤
🍉

The Breakdown:
    • Created By: Theo Weidmann.
    • Type: Object-Oriented.
    • The Story: A fully functional, high-level language where types, classes, and methods are emojis.
    • Special Power: It’s cross-platform and actually useful, despite looking ridiculous. 🍇 is a code block, 🏁 is the main function.


89. Unlambda
File: src/089_hello.unl
Plaintext

`r```````````.H.e.l.l.o. .W.o.r.l.d
The Breakdown:
    • Created By: David Madore (1999).
    • Type: Functional (Combinator Logic).
    • The Story: It strips functional programming down to its absolute mathematical core (SKI combinator calculus). There are no variables, loops, or data structures. Only functions.
    • Special Power: It makes Haskell look like child's play.


90. GolfScript
File: src/090_hello.gs
Plaintext

"Hello World"
The Breakdown:
    • Created By: Darren Smith.
    • Type: Stack-based.
    • The Story: Designed specifically for "Code Golf" competitions (solving problems in the fewest characters possible).
    • Special Power: Brevity. It assumes everything is input and everything is output unless told otherwise.


91. Haifu
File: src/091_hello.hai
Plaintext

The world is waiting
Hello World is what we say
Beauty in the code
The Breakdown:
    • Created By: Unspecified.
    • Type: Poetic.
    • The Story: Logic is determined by the structure of Haikus (5-7-5 syllables).
    • Special Power: It forces you to be a poet to be a programmer.


92. Glass
File: src/092_hello.glass
Plaintext

{M[m(_o)O!(_n)O!(_o)O!(_l)O!(_l)O!(_e)O!(_H)O!]?}
The Breakdown:
    • Created By: Gregor Richards (2005).
    • Type: Esoteric Object-Oriented.
    • The Story: It combines a postfix notation with an object-oriented structure that is intentionally confusing.
    • Special Power: It is named "Glass" because the code is fragile and breaks easily.


93. Hexagony
File: src/093_hello.hex
Plaintext

  H ; e ;
 l ; d ;
* ; r ; o
 ; W ; l
  ; o ;
(Note: Code must be shaped like a hexagon)
The Breakdown:
    • Created By: Martin Ender.
    • Type: 2D Esoteric.
    • The Story: Like Befunge, but on a hexagonal grid. The instruction pointer has 6 directions of movement.
    • Special Power: Geometric complexity. You have to think in triangles and hexagons.


94. Dogescript
File: src/094_hello.doge
Plaintext

shh this is a comment
plz console.loge with 'Hello World'
wow
The Breakdown:
    • Created By: Zach Bruggeman (2013).
    • Type: Transpiled to JS.
    • The Story: Based on the Doge meme (wow, such code).
    • Keywords: plz (function call), very (var), wow (end block).
    • Special Power: It compiles to valid JavaScript, so you can actually run it in a browser.


95. Zsh (Z Shell)
File: src/095_hello.z
Bash

print "Hello World"
The Breakdown:
    • Created By: Paul Falstad (1990).
    • Type: Shell.
    • The Story: An extended Bourne shell with many improvements. It is now the default shell on macOS (replacing Bash).
    • Special Power: Auto-completion and themes (Oh My Zsh) that make it the favorite of developers.


96. ABC
File: src/096_hello.abc
Plaintext

WRITE "Hello World"
The Breakdown:
    • Created By: CWI Netherlands (1980s).
    • Type: Imperative.
    • The Story: The direct ancestor of Python. Guido van Rossum worked on ABC before creating Python. He liked the syntax but hated the lack of extensibility.
    • Special Power: It influenced the design of one of the world's most popular languages.


97. Vigil
File: src/097_hello.vig
Python

# (Vigil is Python-based but with consequences)
print("Hello World")
The Breakdown:
    • Created By: Munificent.
    • Type: Esoteric / Punishment.
    • The Story: "Eternal vigilance is the price of liberty."
    • Special Power: If your code throws an error (even a syntax error), Vigil deletes the source file from your hard drive. (Do not run this on important code).


98. B
File: src/098_hello.b
C

main( ) {
    putchar('H'); putchar('e'); putchar('l'); putchar('l'); putchar('o');
    putchar(' ');
    putchar('W'); putchar('o'); putchar('r'); putchar('l'); putchar('d');
    putchar('*n');
}
The Breakdown:
    • Created By: Ken Thompson and Dennis Ritchie (1969).
    • Type: Systems.
    • The Story: The predecessor to C. It was stripped down to run on tiny minicomputers with 8KB of memory.
    • Special Power: It is the missing link between assembly and C.


99. ALGOL 68
File: src/099_hello.algol
Code snippet

BEGIN
   print(("Hello World", new line))
END
The Breakdown:
    • Created By: IFIP Working Group (1968).
    • Type: Imperative.
    • The Story: The "Algorithm Language." It introduced code blocks (BEGIN / END) which eventually became curly braces {} in C. It was the standard way to publish algorithms in scientific journals for decades.
    • Special Power: Influence. Almost every modern language (C, Java, Pascal) is a descendant of the "ALGOL family."


100. I Use Arch Btw
File: src/100_hello.arch
Plaintext

i use arch btw i use arch btw i use arch btw i use arch btw i use arch btw i use arch btw i use arch btw i use arch btw
(Note: This goes on for hundreds of iterations to manipulate the pointer, similar to Brainfuck)
The Breakdown:
    • Created By: Overdesh (GitHub User).
    • Type: Esoteric / Meme.
    • The Story: The ultimate flex. The language is purely comprised of the phrase "i use arch btw".
    • Usage: Establishing dominance in Linux forums.
    • Special Power: It forces you to type the meme over and over again to get anything done.

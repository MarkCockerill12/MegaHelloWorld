# Mega Hello World: 100 Languages, One Project

Welcome to the ultimate "Hello World" collection. This repository features 100 different programming languages, ranging from the modern heavyweights to esoteric madness. Each entry provides a technical profile, historical context, and an analysis of its strengths and weaknesses.

---

## Part 1: The Modern Heavyweights (1–20)

### 1. Python

**File**: `src/001_hello_python.py`

```python
print("Hello World")
```

**Technical Profile**:

- **Developer/Origin**: Guido van Rossum (1991), CWI Netherlands.
- **Paradigm**: Multi-paradigm (Object-oriented, Imperative, Functional).
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: CPython (standard), PyPy, Jython, IronPython.

**The Story & Purpose**:
Python was designed to be a successor to the ABC language, capable of exception handling and interfacing with the Amoeba operating system. Its primary philosophy, defined in the "Zen of Python," emphasizes readability and simplicity. It has moved from a scripting tool for system administrators to the primary language for data science and machine learning.

**Key Use Cases**:

- **Data Science & AI**: TensorFlow, PyTorch, Scikit-learn.
- **Web Development**: Django, Flask, FastAPI.
- **Automation**: System scripting, web scraping (BeautifulSoup/Scrapy).
- **Companies**: Google, Instagram, Spotify, Netflix.

**Pros & Cons**:

- **Pros**: Readability is prioritized, making it easy to learn and maintain; massive ecosystem of third-party libraries; extensive community support.
- **Cons**: Execution speed is significantly lower than compiled languages; Global Interpreter Lock (GIL) limits multi-threaded performance; high memory consumption compared to C/C++.

---

### 2. JavaScript

**File**: `src/002_hello_javascript.js`

```javascript
console.log("Hello World");
```

**Technical Profile**:

- **Developer/Origin**: Brendan Eich (1995), Netscape.
- **Paradigm**: Multi-paradigm (Event-driven, Functional, Prototype-based).
- **Typing**: Dynamic, Weak.
- **Runtime/Platform**: Browser engines (V8, SpiderMonkey, JavaScriptCore), Node.js, Deno, Bun.

**The Story & Purpose**:
Initially created under the name "Mocha" and later "LiveScript," it was rebranded to JavaScript to capitalize on the hype surrounding Java. It was designed to add "glue" logic to the browser. Over time, it has evolved from a simple scripting tool to a highly optimized language capable of powering complex full-stack applications through Node.js.

**Key Use Cases**:

- **Web Frontend**: React, Vue, Angular, Svelte.
- **Server-side**: Express.js, NestJS.
- **Mobile/Desktop**: React Native, Electron.
- **Companies**: Meta, Amazon, Netflix, Twitter.

**Pros & Cons**:

- **Pros**: Ubiquitous across all web browsers; massive NPM ecosystem; asynchronous nature via Event Loop handles high concurrency well.
- **Cons**: Dynamic and weak typing can lead to subtle bugs; historical "quirks" (e.g., `NaN === NaN` is false); fragmentation across different runtimes and bundlers.

---

### 3. TypeScript

**File**: `src/003_hello_typescript.ts`

```typescript
const message: string = "Hello World";
console.log(message);
```

**Technical Profile**:

- **Developer/Origin**: Anders Hejlsberg (2012), Microsoft.
- **Paradigm**: Multi-paradigm (Object-oriented, Functional).
- **Typing**: Static (at compile time), Strong.
- **Runtime/Platform**: Transpiles to JavaScript; runs anywhere JS runs.

**The Story & Purpose**:
As JavaScript applications grew in size, Microsoft recognized the need for a better way to manage large codebases. TypeScript provides optional static typing, enabling better IDE support (autocomplete, refactoring) and catching errors early in the development cycle rather than at runtime. It is a strict syntactical superset of JavaScript.

**Key Use Cases**:

- **Enterprise Web Apps**: Large-scale projects where team collaboration is critical.
- **Library Development**: Providing type definitions for other developers.
- **Companies**: Microsoft (VS Code), Slack, Airbnb, Stripe.

**Pros & Cons**:

- **Pros**: Catch errors at compile time; superior IDE developer experience; easier to refactor large codebases.
- **Cons**: Requires a compilation step; increased complexity for simple scripts; some third-party libraries lack high-quality type definitions.

---

### 4. C

**File**: `src/004_hello_c.c`

```c
#include <stdio.h>
int main() {
    printf("Hello World\n");
    return 0;
}
```

**Technical Profile**:

- **Developer/Origin**: Dennis Ritchie (1972), Bell Labs.
- **Paradigm**: Imperative, Structural.
- **Typing**: Static, Weak.
- **Runtime/Platform**: Native (Compiles to machine code).

**The Story & Purpose**:
C was developed to rewrite the Unix operating system, which was previously written in assembly. It provides low-level access to memory and a clean, minimalist syntax that maps efficiently to machine instructions. It is the language that most modern operating systems and other programming languages are built upon.

**Key Use Cases**:

- **Operating Systems**: Linux Kernel, Windows, macOS.
- **Embedded Systems**: Microcontrollers in automotive, industrial, and consumer electronics.
- **Compilers**: Many other languages' compilers are written in C.

**Pros & Cons**:

- **Pros**: Maximum hardware efficiency; highly portable across different architectures; predictable performance with no garbage collection overhead.
- **Cons**: Manual memory management leads to leaks and security vulnerabilities (buffer overflows); lacks modern high-level features like native strings or generics; steep learning curve for beginners.

---

### 5. C++

**File**: `src/005_hello_cpp.cpp`

```cpp
#include <iostream>
int main() {
    std::cout << "Hello World" << std::endl;
    return 0;
}
```

**Technical Profile**:

- **Developer/Origin**: Bjarne Stroustrup (1985), Bell Labs.
- **Paradigm**: Multi-paradigm (Procedural, Object-oriented, Generic, Functional).
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native (Compiles to machine code).

**The Story & Purpose**:
Stroustrup wanted a language with the speed of C but the organizational power of Simula. Originally called "C with Classes," it introduced Object-Oriented Programming (OOP) to the systems level. It emphasizes "zero-overhead abstractions," meaning you only pay for the features you use.

**Key Use Cases**:

- **Game Development**: Unreal Engine, Frostbite, AAA titles.
- **High-Performance Applications**: Adobe Creative Cloud, Google Chrome, Finance (HFT).
- **Graphics**: OpenGL, Vulkan, DirectX.

**Pros & Cons**:

- **Pros**: Extremely fast and efficient; multi-paradigm flexibility; extensive control over hardware resources.
- **Cons**: One of the most complex languages to master; compatibility issues between different compiler versions; "undefined behavior" can cause cryptic crashes.

---

### 6. C#

**File**: `src/006_hello_csharp.cs`

```csharp
using System;
class Program {
    static void Main() {
        Console.WriteLine("Hello World");
    }
}
```

**Technical Profile**:

- **Developer/Origin**: Anders Hejlsberg (2000), Microsoft.
- **Paradigm**: Multi-paradigm (Object-oriented, Component-oriented, Functional).
- **Typing**: Static, Strong.
- **Runtime/Platform**: .NET (Core/Framework), Xamarin, Unity.

**The Story & Purpose**:
C# was created as a modern, object-oriented language for the .NET framework. While it bore similarities to Java, it quickly diverged by adding features like properties, events, and eventually powerful asynchronous programming (async/await). It has since moved from being Windows-only to a cross-platform powerhouse.

**Key Use Cases**:

- **Enterprise Software**: Desktop and web backend applications.
- **Game Development**: The primary language for the Unity Game Engine.
- **Mobile**: Cross-platform development via .NET MAUI/Xamarin.
- **Companies**: Microsoft, StackOverflow, Unity.

**Pros & Cons**:

- **Pros**: Excellent developer productivity and tooling (Visual Studio); high-level safety without sacrificing too much performance; versatile across desktop, web, and mobile.
- **Cons**: Garbage collection can cause minor performance spikes; historically tied to the Windows ecosystem (though this is largely resolved); larger binary sizes compared to native C++.

---

### 7. Java

**File**: `src/007_hello_java.java`

```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

**Technical Profile**:

- **Developer/Origin**: James Gosling (1995), Sun Microsystems.
- **Paradigm**: Object-oriented (Class-based), Multi-paradigm.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Java Virtual Machine (JVM).

**The Story & Purpose**:
Java was built with the "Write Once, Run Anywhere" (WORA) philosophy. By compiling code into bytecode that runs on a virtual machine (JVM), Java eliminated the need to recompile for every OS. It became the gold standard for enterprise development due to its robustness and security features.

**Key Use Cases**:

- **Enterprise Backends**: Banking, retail, and manufacturing systems.
- **Android Development**: The original language for Android apps.
- **Big Data**: Hadoop, Kafka, and Flink are written in Java.
- **Companies**: Oracle, IBM, Google, Amazon.

**Pros & Cons**:

- **Pros**: Highly portable across hardware; extremely stable and mature ecosystem; automatic memory management (Garbage Collection); rich libraries.
- **Cons**: Verbosely styled (requires more code for simple tasks); slower startup times compared to native binaries; high memory footprint.

---

### 8. Go (Golang)

**File**: `src/008_hello_go.go`

```go
package main
import "fmt"
func main() {
    fmt.Println("Hello World")
}
```

**Technical Profile**:

- **Developer/Origin**: Robert Griesemer, Rob Pike, Ken Thompson (2009), Google.
- **Paradigm**: Multi-paradigm (Imperative, Concurrent).
- **Typing**: Static, Strong.
- **Runtime/Platform**: Compiled, natively executable with a small runtime.

**The Story & Purpose**:
Google engineers who were frustrated with C++’s complexity and slow build times. It was designed to maintain the performance of C and C++ while being much simpler and safer.

**Key Use Cases**:

- **Cloud Infrastructure**: Docker, Kubernetes, Terraform are all written in Go.
- **Microservices**: High-concurrency backend services.
- **Networking**: Proxies, load balancers, and distributed systems.
- **Companies**: Google, Uber, Twitch, Dropbox.

**Pros & Cons**:

- **Pros**: Simple syntax is easy to learn; extremely fast compilation; native support for concurrency via Goroutines and Channels.
- **Cons**: Lacks advanced features like operator overloading or comprehensive generics (until recently); error handling can feel repetitive; opinionated dependency management.

---

### 9. Rust

**File**: `src/009_hello_rust.rs`

```rust
fn main() {
    println!("Hello World");
}
```

**Technical Profile**:

- **Developer/Origin**: Graydon Hoare (2010), Mozilla Research.
- **Paradigm**: Multi-paradigm (Systems, Functional, Imperative).
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native (Compiles to machine code, no runtime/GC).

**The Story & Purpose**:
Rust was born out of a desire for a systems language that ensures memory safety without a garbage collector. It introduced the concept of "ownership" and the "Borrow Checker," which prevents data races and null pointers at compile time. It is consistently the most loved language in developer surveys.

**Key Use Cases**:

- **Systems Programming**: OS development, drivers, and high-performance engines.
- **Blockchain**: Solana, Polkadot, and other high-security networks.
- **WebAssembly**: Powerful client-side code for the web.
- **Companies**: Mozilla, Meta, Discord, Amazon.

**Pros & Cons**:

- **Pros**: Memory safety without performance overhead; fearlessly concurrent (thread safety guaranteed); excellent package manager (Cargo).
- **Cons**: Very steep learning curve due to ownership rules; compilation times can be slow; strict compiler can be frustrating for beginners.

---

### 10. PHP

**File**: `src/010_hello_php.php`

```php
<?php
echo "Hello World\n";
?>
```

**Technical Profile**:

- **Developer/Origin**: Rasmus Lerdorf (1995).
- **Paradigm**: Multi-paradigm (Procedural, Object-oriented).
- **Typing**: Dynamic, Weak/Strong (depending on configuration).
- **Runtime/Platform**: Zend Engine.

**The Story & Purpose**:
PHP (Personal Home Page) started as a simple set of C macros to track visits to Lerdorf's online resume. It unintentionally became the most popular language for server-side web development. Modern PHP (v7+) has undergone a massive transformation, becoming much faster and more structured.

**Key Use Cases**:

- **CMS Platforms**: WordPress, Drupal, Joomla.
- **Web Applications**: Laravel, Symfony.
- **Companies**: Meta (originally), Wikipedia, Etsy, Slack.

**Pros & Cons**:

- **Pros**: Specifically optimized for web development; extremely easy to deploy on shared hosting; massive library of web-related tools.
- **Cons**: Historical reputation for inconsistent naming and poor security (largely fixed in modern versions); not well-suited for non-web tasks like data science or mobile.

---

### 11. Ruby

**File**: `src/011_hello_ruby.rb`

```ruby
puts "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Yukihiro "Matz" Matsumoto (1995), Japan.
- **Paradigm**: Object-oriented (Pure), Functional, Imperative.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: MRI (Matz's Ruby Interpreter), JRuby, TruffleRuby.

**The Story & Purpose**:
Matz wanted to create a language that was "more powerful than Perl, and more object-oriented than Python." Ruby focuses on developer productivity and joy. It became globally famous through the Ruby on Rails web framework, which pioneered "Convention over Configuration."

**Key Use Cases**:

- **Web Development**: Ruby on Rails.
- **Automation & DevOps**: Chef, Puppet, Homebrew.
- **Prototyping**: Fast development of MVPs.
- **Companies**: GitHub, Shopify, Airbnb, Hulu.

**Pros & Cons**:

- **Pros**: Highly expressive and readable syntax; incredible developer productivity via Rails; very welcoming and mature community.
- **Cons**: Slower execution speed compared to Python or Node.js; high memory consumption; concurrency is limited compared to Go or Elixir.

---

### 12. Swift

**File**: `src/012_hello_swift.swift`

```swift
print("Hello World")
```

**Technical Profile**:

- **Developer/Origin**: Chris Lattner (2014), Apple.
- **Paradigm**: Multi-paradigm (Object-oriented, Functional, Protocol-oriented).
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native (LLVM).

**The Story & Purpose**:
Swift was developed by Apple as a safer, faster, and more modern replacement for Objective-C. It was designed from the ground up to eliminate common programming errors (like null pointers) and to provide a "Playground" for interactive coding. It became open-source in 2015.

**Key Use Cases**:

- **Apple Platforms**: Primary language for iOS, macOS, watchOS, and tvOS.
- **Server-side Swift**: Vapor, Kitura.
- **Systems Development**: High-performance Apple-exclusive tools.

**Pros & Cons**:

- **Pros**: Extremely fast (comparable to C++); safe by design with native Optionals; modern syntax that is easy to write and read.
- **Cons**: Primarily restricted to the Apple ecosystem; ABI stability was a long-term hurdle; smaller community for server-side work.

---

### 13. Kotlin

**File**: `src/013_hello_kotlin.kt`

```kotlin
fun main() {
    println("Hello World")
}
```

**Technical Profile**:

- **Developer/Origin**: JetBrains (2011).
- **Paradigm**: Multi-paradigm (Object-oriented, Functional).
- **Typing**: Static, Strong.
- **Runtime/Platform**: JVM, JavaScript, Native (LLVM).

**The Story & Purpose**:
JetBrains, the creators of IntelliJ IDEA, wanted a language that was more concise and safer than Java but 100% interoperable with it. Kotlin reduces boilerplate code and adds features like null safety and extension functions. It was endorsed by Google as the official language for Android dev in 2017.

**Key Use Cases**:

- **Android Development**: The industry standard for mobile apps.
- **Server-side**: Modern alternative to Java for Spring Boot.
- **Multiplatform**: Sharing code between iOS, Android, and Web.
- **Companies**: Google, Netflix, Pinterest, Uber.

**Pros & Cons**:

- **Pros**: Seamless Java interoperability; significantly reduces code verbosity; built-in null safety prevents common crashes.
- **Cons**: Compilation speed can be slower than Java; smaller pool of experienced developers compared to Java; requires the JVM for most use cases.

---

### 14. Lua

**File**: `src/014_hello_lua.lua`

```lua
print("Hello World")
```

**Technical Profile**:

- **Developer/Origin**: Roberto Ierusalimschy et al. (1993), Brazil.
- **Paradigm**: Multi-paradigm (Scripting, Prototype-based).
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: Lua Interpreter, LuaJIT (Just-In-Time compiler).

**The Story & Purpose**:
Lua was designed to be a lightweight scripting language that could be easily embedded into C/C++ applications. It is famous for its simple, small footprint and high performance. It uses "tables" as its primary and only data structure, making it extremely flexible.

**Key Use Cases**:

- **Game Development**: Scripting logic in Roblox, WoW, and Civilization.
- **Embedded Systems**: Networking gear and hardware customization.
- **Configuration**: Often used as a config language for high-performance servers (e.g., Nginx).

**Pros & Cons**:

- **Pros**: Tiny footprint and lightning-fast execution (especially LuaJIT); incredibly easy to embed in C/C++; simple, minimal syntax.
- **Cons**: Very limited standard library (no built-in support for networking or complex regex); arrays start at index 1 (highly controversial among programmers).

---

### 15. Perl

**File**: `src/015_hello_perl.pl`

```perl
print "Hello World\n";
```

**Technical Profile**:

- **Developer/Origin**: Larry Wall (1987).
- **Paradigm**: Multi-paradigm (Procedural, Object-oriented, Functional).
- **Typing**: Dynamic, Weak.
- **Runtime/Platform**: Perl Interpreter.

**The Story & Purpose**:
Perl was originally created as a Unix scripting language to make report processing easier. It became the "glue" of the early web (CGI scripts) and a favorite for system administrators. Wall's philosophy ("There's more than one way to do it") led to a highly flexible but often cryptic syntax.

**Key Use Cases**:

- **System Administration**: Automation and legacy scripts.
- **Bioinformatics**: Processing massive DNA sequences.
- **Legacy Web**: Maintaining 90s/00s server infrastructure.
- **Companies**: DuckDuckGo, Booking.com, Amazon.

**Pros & Cons**:

- **Pros**: Unmatched text processing capabilities; massive CPAN library of modules; extremely powerful for quick one-off tasks.
- **Cons**: "Write-only" reputation due to dense, readable-hostile syntax; performance is lower than modern counterparts; declining popularity and developer pool.

---

### 16. R

**File**: `src/016_hello_r.r`

```r
cat("Hello World\n")
```

**Technical Profile**:

- **Developer/Origin**: Ross Ihaka and Robert Gentleman (1993), University of Auckland.
- **Paradigm**: Multi-paradigm (Functional, Imperative).
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: R Interpreter.

**The Story & Purpose**:
R is an implementation of the S programming language. It was built specifically for statisticians and data miners to perform data analysis and graphical representation. Unlike general-purpose languages, R treats data as its primary citizen.

**Key Use Cases**:

- **Statistical Modeling**: Academic and clinical research.
- **Data Visualization**: Creating publication-quality graphs.
- **Biostatistics**: Genetic mapping and clinical trial analysis.
- **Companies**: Google, Pfizer, The New York Times.

**Pros & Cons**:

- **Pros**: Best-in-class libraries for statistics (CRAN); powerful visualization tools (ggplot2); built-in support for vector and matrix operations.
- **Cons**: Not a general-purpose language (hard to build web apps or games); can be memory-intensive; inconsistent naming conventions across libraries.

---

### 17. Bash (Shell)

**File**: `src/017_hello_bash.sh`

```bash
echo "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Brian Fox (1989), Free Software Foundation.
- **Paradigm**: Imperative, Scripting.
- **Typing**: Dynamic, Weak (Strings only).
- **Runtime/Platform**: Unix/Linux/macOS shells.

**The Story & Purpose**:
Bash (Bourne Again SHell) is the standard command-line interface for Unix-like systems. It was designed to replace the original Bourne shell (sh). It is primarily used to interact with the OS and automate complex sequences of terminal commands.

**Key Use Cases**:

- **Automation**: DevOps pipelines, CI/CD, and server setup.
- **System Maintenance**: Managing files, processes, and networks.
- **Glue Code**: Connecting separate command-line tools.

**Pros & Cons**:

- **Pros**: Standard on almost all Linux/macOS systems; excellent at handling file streams and process orchestration.
- **Cons**: Syntax is brittle and prone to errors (e.g., whitespace issues); lacks complex data structures (no native objects); difficult to maintain for large programs.

---

### 18. Haskell

**File**: `src/018_hello_haskell.hs`

```haskell
main = putStrLn "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Academic Committee (1990).
- **Paradigm**: Purely Functional.
- **Typing**: Static, Strong, Inferred.
- **Runtime/Platform**: GHC (Glasgow Haskell Compiler).

**The Story & Purpose**:
Haskell was designed to serve as a common standard for purely functional language research. It is named after the logician Haskell Curry. It is lazy (only computes when needed), pure (no side effects by default), and uses monads to handle I/O and state.

**Key Use Cases**:

- **High-Assurance Systems**: Banking and security where correctness is vital.
- **Compiler Design**: Writing other programming languages.
- **Academic Research**: Testing new computer science concepts.
- **Companies**: Facebook (Spam filtering), Standard Chartered.

**Pros & Cons**:

- **Pros**: Avoids entire classes of bugs through purity; extremely concise logic; mathematically stable and predictable.
- **Cons**: Very difficult to learn due to abstract concepts (Monads, Functors); lazy evaluation can make memory issues hard to debug; smaller commercial job market.

---

### 19. Dart

**File**: `src/019_hello_dart.dart`

```dart
void main() {
  print('Hello World');
}
```

**Technical Profile**:

- **Developer/Origin**: Lars Bak and Kasper Lund (2011), Google.
- **Paradigm**: Multi-paradigm (Object-oriented, Functional).
- **Typing**: Static, Strong.
- **Runtime/Platform**: Dart VM, AOT (Ahead-of-Time) compilation for native.

**The Story & Purpose**:
Dart was originally intended to replace JavaScript in the browser. While it didn't succeed as a JS killer, it was revitalized by the Flutter UI toolkit. It is optimized for building beautiful, high-performance UIs across mobile, web, and desktop from a single codebase.

**Key Use Cases**:

- **Cross-Platform Mobile**: Creating iOS and Android apps via Flutter.
- **Desktop Apps**: Windows/macOS/Linux UI software.
- **Companies**: Google, BMW, Alibaba.

**Pros & Cons**:

- **Pros**: Optimized for UI development (Hot Reload); fast execution via AOT compilation; clean, familiar syntax for Java/C# developers.
- **Cons**: Heavily reliant on the success of Flutter; smaller ecosystem outside of UI development; requires its own VM or compilation step.

---

### 20. Scala

**File**: `src/020_hello_scala.scala`

```scala
object HelloWorld extends App {
  println("Hello World")
}
```

**Technical Profile**:

- **Developer/Origin**: Martin Odersky (2004), EPFL.
- **Paradigm**: Multi-paradigm (Object-oriented, Functional).
- **Typing**: Static, Strong.
- **Runtime/Platform**: JVM, Scala.js, Scala Native.

**The Story & Purpose**:
Scala (Scalable Language) was designed to bridge the gap between object-oriented and functional programming. It runs on the JVM and is fully compatible with Java. It gained massive popularity in the big data world due to its ability to handle complex transformations with concise code.

**Key Use Cases**:

- **Big Data Processing**: Apache Spark is built on Scala.
- **Distributed Systems**: Akka framework for concurrency.
- **Enterprise Services**: Highly scalable backend systems.
- **Companies**: Twitter, Netflix, Airbnb, Goldman Sachs.

**Pros & Cons**:

- **Pros**: Combines the best of OOP and Functional worlds; extremely powerful type system; much more concise than Java.
- **Cons**: High complexity and steep learning curve; compilation times are notoriously slow; binary compatibility between versions can be difficult to manage.

---

## Part 2: The Functional & Academic (21–40)

### 21. Elixir

**File**: `src/021_hello_elixir.exs`

```elixir
IO.puts "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: José Valim (2011), Plataformatec.
- **Paradigm**: Functional, Concurrent, Distributed.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: BEAM (Erlang Virtual Machine).

**The Story & Purpose**:
Elixir was created to bring the power and scalability of Erlang to a broader audience by providing a modern syntax (inspired by Ruby) and powerful tooling. It is designed for building distributed, fault-tolerant applications. It leverages the Actor model via Erlang processes to handle millions of simultaneous connections.

**Key Use Cases**:

- **Real-time Messaging**: Discord uses Elixir to handle millions of concurrent users.
- **E-commerce**: Massive retail systems requiring high availability.
- **Web Applications**: The Phoenix framework provides a high-performance alternative to Rails.

**Pros & Cons**:

- **Pros**: Incredible concurrency and fault tolerance; clean, modern syntax; excellent documentation and tooling (Mix, IEx).
- **Cons**: Relatively small job market compared to Java/Python; purely functional paradigm requires a mindset shift; performance for CPU-intensive mathematical tasks is lower than native languages.

---

### 22. Clojure

**File**: `src/022_hello_clojure.clj`

```clojure
(println "Hello World")
```

**Technical Profile**:

- **Developer/Origin**: Rich Hickey (2007).
- **Paradigm**: Functional, Concurrent, Logic.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: JVM, CLR, JavaScript (ClojureScript).

**The Story & Purpose**:
Clojure is a modern dialect of Lisp that runs on the Java Virtual Machine. It was designed to address the complexities of multithreaded programming by emphasizing immutability and providing software transactional memory (STM). It treats code as data and data as code.

**Key Use Cases**:

- **Financial Systems**: Handling complex concurrent transactions.
- **Data Analysis**: Working with large, nested datasets.
- **Backend Services**: Robust, maintainable microservices.
- **Companies**: Walmart, Nubank, Adobe.

**Pros & Cons**:

- **Pros**: Extremely powerful macro system; seamless Java interoperability; simplifies concurrent programming through immutability.
- **Cons**: Lisp syntax (parentheses) can be off-putting to newcomers; JVM startup times; error messages can be cryptic for those unfamiliar with the underlying Java stack.

---

### 23. Julia

**File**: `src/023_hello_julia.jl`

```julia
println("Hello World")
```

**Technical Profile**:

- **Developer/Origin**: Bezanson, Karpinski, Shah, Edelman (2012), MIT.
- **Paradigm**: Multi-paradigm (Functional, Imperative).
- **Typing**: Dynamic, Strong, Parametric.
- **Runtime/Platform**: LLVM-based JIT compilation.

**The Story & Purpose**:
Julia was created to solve the "two-language problem"—the need to prototype in a slow dynamic language (like Python) and rewrite in a fast static language (like C++) for production. It aims to be as fast as C and as easy as Python.

**Key Use Cases**:

- **Scientific Computing**: Physics, chemistry, and biology research.
- **Data Science & ML**: High-performance model training.
- **Finance**: Risk analysis and algorithmic trading.
- **Companies**: NASA, FAA, Federal Reserve.

**Pros & Cons**:

- **Pros**: Performance comparable to C/Fortran; built-in support for distributed and parallel computing; excellent math and matrix ergonomics.
- **Cons**: "Time to First Plot" (JIT overhead makes startup slow); smaller library ecosystem than Python; younger community with fewer enterprise-level resources.

---

### 24. F#

**File**: `src/024_hello_fsharp.fs`

```fsharp
printfn "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Don Syme (2005), Microsoft Research.
- **Paradigm**: Functional-first, Multi-paradigm.
- **Typing**: Static, Strong, Inferred.
- **Runtime/Platform**: .NET.

**The Story & Purpose**:
F# was developed to provide a first-class functional programming experience on the .NET platform. It is strongly influenced by ML and OCaml. It aims to reduce the "ceremony" of coding, allowing developers to focus on the problem logic rather than the plumbing.

**Key Use Cases**:

- **Finance**: Financial modeling and quantitative analysis.
- **Enterprise Web**: Safe and maintainable web services (Giraffe, Falco).
- **Data Engineering**: Reliable data pipelines.

**Pros & Cons**:

- **Pros**: Extremely concise and safe; Type Providers allow for incredible data integration; access to the entire .NET library ecosystem.
- **Cons**: Smaller community and job market than C#; functional paradigm can be difficult for long-time OOP developers; tooling support can sometimes lag behind C#.

---

### 25. OCaml

**File**: `src/025_hello_ocaml.ml`

```ocaml
print_endline "Hello World";;
```

**Technical Profile**:

- **Developer/Origin**: Xavier Leroy et al. (1996), INRIA.
- **Paradigm**: Multi-paradigm (Functional, Imperative, Object-oriented).
- **Typing**: Static, Strong, Inferred.
- **Runtime/Platform**: Native (Compiles to machine code), Bytecode.

**The Story & Purpose**:
OCaml (Objective Caml) is the main implementation of the Caml programming language. It is renowned for its powerful module system and extremely safe type system. It is favored by those who need high performance combined with the safety of functional programming.

**Key Use Cases**:

- **Compiler Construction**: Coq, Haxe, and Rust (originally) were built with OCaml.
- **Financial Trading**: Used by elite firms for high-frequency trading.
- **Static Analysis**: Tools like Facebook's Flow and Infer.

**Pros & Cons**:

- **Pros**: Highly optimized native code generation; one of the best module systems in existence; extremely stable and predictable.
- **Cons**: Historically struggled with multi-core support (though OCaml 5 addresses this); documentation can be academic and sparse; smaller third-party library ecosystem.

---

### 26. Erlang

**File**: `src/026_hello_erlang.erl`

```erlang
-module(hello).
-export([start/0]).
start() ->
    io:fwrite("Hello World~n").
```

**Technical Profile**:

- **Developer/Origin**: Joe Armstrong, Robert Virding, Mike Williams (1986), Ericsson.
- **Paradigm**: Functional, Concurrent, Distributed.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: BEAM (Erlang Virtual Machine).

**The Story & Purpose**:
Erlang was built to solve a specific problem in telephony—how to handle millions of simultaneous connections with zero downtime. It introduced the "Actor Model" of concurrency long before it became a mainstream concept.

**Key Use Cases**:

- **Telephony**: Powering massive switches and routers.
- **Messaging**: WhatsApp and WeChat core infrastructures.
- **High-Availability Services**: Online gaming backends and banking.

**Pros & Cons**:

- **Pros**: Unmatched uptime and availability; linear scalability across multiple cores and machines; real-time hot-swapping of code.
- **Cons**: Unique, unconventional syntax; purely functional nature can be difficult for many; not suitable for heavy numerical or graphical tasks.

---

### 27. Common Lisp

**File**: `src/027_hello_commonlisp.lisp`

```lisp
(format t "Hello World~%")
```

**Technical Profile**:

- **Developer/Origin**: ANSI Committee (1984).
- **Paradigm**: Multi-paradigm (Procedural, Object-oriented, Functional).
- **Typing**: Dynamic, Strong/Weak.
- **Runtime/Platform**: SBCL, CCL, ECL, and others.

**The Story & Purpose**:
Common Lisp was created to standardize the various dialects of Lisp that had emerged since 1958. It is a massive, feature-rich language that pioneered many concepts we take for granted today, such as Garbage Collection and First-class Functions. It is often cited as the ultimate language for "programmable programming."

**Key Use Cases**:

- **AI Research**: Historically the primary language for symbolic AI.
- **Complex Modeling**: Space mission planning and robotics.
- **Companies**: NASA, ITA Software (Google Flights).

**Pros & Cons**:

- **Pros**: Incredibly powerful macro system; live development (modify the system while it runs); ANSI standardized stability.
- **Cons**: "Parenthesis fatigue" for those used to C-style syntax; perceived as "old" or "academic" by the industry; many different implementations can be confusing.

---

### 28. Scheme

**File**: `src/028_hello_scheme.scm`

```scheme
(display "Hello World\n")
```

**Technical Profile**:

- **Developer/Origin**: Guy L. Steele and Gerald Jay Sussman (1975).
- **Paradigm**: Functional.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: Various (Chez Scheme, Guile, Racket).

**The Story & Purpose**:
Scheme was designed to be a minimalist dialect of Lisp. It focuses on simplicity and correctness, often used in educational settings to teach the core concepts of computer science. It was the first Lisp to use lexical scoping and to require tail-call optimization.

**Key Use Cases**:

- **Education**: Used in the classic "SICP" (Structure and Interpretation of Computer Programs) course at MIT.
- **Scripting**: Scheme-like languages used for plugins (e.g., GIMP).
- **Embedded Languages**: Guile is the official extension language for the GNU project.

**Pros & Cons**:

- **Pros**: Extremely simple and elegant specification; great for learning fundamental CS theory; fast execution for well-implemented versions.
- **Cons**: Too minimalist for many "real-world" tasks without many extensions; fragmentation between different standards (R5RS, R6RS, R7RS); smaller library ecosystem than Common Lisp.

---

### 29. Racket

**File**: `src/029_hello_racket.rkt`

```racket
#lang racket
(displayln "Hello World")
```

**Technical Profile**:

- **Developer/Origin**: PLT Inc. (1995).
- **Paradigm**: Multi-paradigm (Functional, Imperative).
- **Typing**: Dynamic (Typed Racket available).
- **Runtime/Platform**: Racket VM (formerly Racket on Chez).

**The Story & Purpose**:
Racket started as a version of Scheme (DrScheme) but evolved into a general-purpose language and a "meta-programming" platform. Its slogan is "The language-oriented programming language." It allows developers to create entirely new languages using its macro and module systems.

**Key Use Cases**:

- **Language Research**: Building and testing new DSLs (Domain Specific Languages).
- **Education**: Widely used in introductory CS courses.
- **Game Scripting**: Naughty Dog used it for internal scripting in major titles.

**Pros & Cons**:

- **Pros**: Best-in-class documentation; incredible macro system allows for total language customization; excellent IDE support (DrRacket).
- **Cons**: Larger runtime than minimalist Schemes; perception as purely educational; smaller industrial presence.

---

### 30. Groovy

**File**: `src/030_hello_groovy.groovy`

```groovy
println "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: James Strachan (2003).
- **Paradigm**: Multi-paradigm (Object-oriented, Functional).
- **Typing**: Dynamic/Static.
- **Runtime/Platform**: JVM.

**The Story & Purpose**:
Groovy was designed to be a dynamic, concise alternative to Java for the JVM. It was intended to make Java developers more productive by removing boilerplate and adding features like closures and a powerful "builders" syntax. It gained massive traction in the automation and testing space.

**Key Use Cases**:

- **Build Automation**: The primary language for Gradle build scripts.
- **CI/CD Pipelines**: Jenkinsfile scripts are written in Groovy.
- **Testing**: Spock framework provides high-quality BDD testing.

**Pros & Cons**:

- **Pros**: 100% Java interoperability; simplifies complex Java logic into few lines; very popular in the DevOps world.
- **Cons**: Dynamic nature can lead to slower performance than static Java; usage is increasingly becoming niche (limited to Gradle/Jenkins); can be "too many ways to do it" leading to inconsistent styles.

---

### 31. Elm

**File**: `src/031_hello_elm.elm`

```elm
module Hello exposing (..)
import Html exposing (text)
main = text "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Evan Czaplicki (2012).
- **Paradigm**: Purely Functional.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Compiled to JavaScript.

**The Story & Purpose**:
Elm was created specifically for browser-based GUIs. It aims to eliminate runtime exceptions and provide a highly reliable development experience. It introduced "The Elm Architecture" (Model-Update-View), which heavily influenced Redux and modern React patterns.

**Key Use Cases**:

- **Reliable Frontend Apps**: Web applications where stability is the #1 priority.
- **Learning Functional Programming**: Often cited as the best entry point to pure FP.

**Pros & Cons**:

- **Pros**: No runtime exceptions (if it compiles, it works); incredibly helpful error messages; enforces a clean, maintainable architecture.
- **Cons**: Strict and can feel restrictive (no "escape hatches"); small ecosystem compared to React/Vue; slow release cycle for new language features.

---

### 32. Prolog

**File**: `src/032_hello_prolog.plg`

```prolog
:- initialization(main).
main :- write('Hello World'), nl, halt.
```

**Technical Profile**:

- **Developer/Origin**: Alain Colmerauer and Philippe Roussel (1972), University of Marseille.
- **Paradigm**: Logic Programming.
- **Typing**: Dynamic.
- **Runtime/Platform**: Various (SWI-Prolog, GNU Prolog).

**The Story & Purpose**:
Prolog (Programmation en Logique) is the benchmark for logic programming. Instead of instructions, you provide facts (e.g., "Socrates is a man") and rules ("All men are mortal"). The computer then uses unification and backtracking to answer queries.

**Key Use Cases**:

- **Expert Systems**: Diagnosing medical or mechanical issues.
- **Lexical Analysis**: Parsing complex natural languages.
- **Semantic Web**: Reasoning about structured data.

**Pros & Cons**:

- **Pros**: Unmatched for solving symbolic, logic-based problems; declarative nature lets you describe the "what" rather than the "how."
- **Cons**: Very poor performance for general-purpose tasks; steep learning curve for those used to imperative logic; difficult to debug complex backtracking chains.

---

### 33. Fortran

**File**: `src/033_hello_fortran.f90`

```fortran
program hello
  print *, "Hello World"
end program hello
```

**Technical Profile**:

- **Developer/Origin**: John Backus (1957), IBM.
- **Paradigm**: Imperative, Structural, Array-oriented.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native.

**The Story & Purpose**:
Fortran (Formula Translation) was the first high-level programming language. It freed scientists from writing machine code and allowed them to express formulas in a readable way. It remains the gold standard for high-performance scientific and mathematical calculations.

**Key Use Cases**:

- **Supercomputing**: Weather modeling, aerospace simulations.
- **Physics & Chemistry Research**: Array-heavy mathematical algorithms.
- **Legacy Systems**: Millions of lines of proven math code in continuous use for decades.

**Pros & Cons**:

- **Pros**: Incredible performance for array and matrix math; extremely mature and verified libraries (LAPACK, BLAS); easy to parallelize.
- **Cons**: Ancient syntax (even in modern versions); lacks modern software engineering features like advanced OOP or robust string handling; difficult to find younger developers for maintenance.

---

### 34. COBOL

**File**: `src/034_hello_cobol.cob`

```cobol
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO.
       PROCEDURE DIVISION.
           DISPLAY 'Hello World'.
           STOP RUN.
```

**Technical Profile**:

- **Developer/Origin**: Grace Hopper et al. (1959), CODASYL.
- **Paradigm**: Imperative, Business-oriented.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Mainframe environments, modern compilers (GnuCOBOL).

**The Story & Purpose**:
COBOL (Common Business-Oriented Language) was designed to make business applications portable across different machines. It prioritized readability for non-programmers, resulting in a verbose, English-like syntax. It currently powers much of the global financial system.

**Key Use Cases**:

- **Banking**: Handling deposits, withdrawals, and interest.
- **Government**: Processing taxes and social benefits.
- **Insurance**: Core legacy systems for policy management.

**Pros & Cons**:

- **Pros**: Handles decimal arithmetic perfectly (vital for money); built to process massive batches of data efficiently; incredibly high "run-time" reliability.
- **Cons**: Verbose style requires 10x more lines than modern alternatives; perceived as "dead" or boring; recruitment for maintenance is difficult and expensive.

---

### 35. Pascal

**File**: `src/035_hello_pascal.pas`

```pascal
program Hello;
begin
  WriteLn('Hello World');
end.
```

**Technical Profile**:

- **Developer/Origin**: Niklaus Wirth (1970), ETH Zurich.
- **Paradigm**: Imperative, Structured.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native, Delphi.

**The Story & Purpose**:
Pascal was created as a tool for teaching programming and structured data. It was intended to move people away from the "spaghetti code" of early languages like BASIC and Fortran. It famously influenced the development of Ada and the original Apple Macintosh operating system.

**Key Use Cases**:

- **Education**: Primary teaching language in the 80s and 90s.
- **Desktop Software**: Delphi remains popular for fast Windows app development.
- **Historical Development**: Used to write early versions of Skype and Photoshop.

**Pros & Cons**:

- **Pros**: Enforces clean code habits; very fast compilation speeds; highly readable even for beginners.
- **Cons**: Perceived as a "teaching language" rather than an industrial one; modern versions (Delphi) are expensive/proprietary; smaller community than C or C++.

---

### 36. Ada

**File**: `src/036_hello_ada.adb`

```ada
with Ada.Text_IO; use Ada.Text_IO;
procedure Hello is
begin
    Put_Line("Hello World");
end Hello;
```

**Technical Profile**:

- **Developer/Origin**: Jean Ichbiah (1980), CII Honeywell Bull (for US DOD).
- **Paradigm**: Multi-paradigm (Imperative, Object-oriented).
- **Typing**: Static, Strong, Manifest.
- **Runtime/Platform**: Native.

**The Story & Purpose**:
Ada was created by the US Department of Defense to consolidate the hundreds of different languages they were using. Named after Ada Lovelace, it prioritized safety, reliability, and long-term maintenance. It is designed so that the compiler catches the vast majority of errors before the code runs.

**Key Use Cases**:

- **Aerospace**: Flight control systems in Boeing and Airbus jets.
- **Defense**: Missile systems and radar software.
- **Infrastructure**: High-speed rail control (TGV).

**Pros & Cons**:

- **Pros**: Unmatched reliability for safety-critical systems; built-in support for concurrency; extremely clear, readable syntax for logic.
- **Cons**: Perception as "over-engineered" for simple tasks; compilers and tools can be expensive; niche job market outside of aerospace/defense.

---

### 37. Assembly (NASM x64)

**File**: `src/037_hello_assembly.asm`

```nasm
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
```

**Technical Profile**:

- **Developer/Origin**: Various (Modern NASM for x86-64).
- **Paradigm**: Low-level (Imperative).
- **Typing**: None (Untyped, only raw bytes/words).
- **Runtime/Platform**: Physical Hardware (CPU).

**The Story & Purpose**:
Assembly language is a thin layer of human-readable text over raw binary machine instructions. It is specific to a CPU architecture (like x86-64 or ARM). Learning assembly is the only way to understand exactly how a computer executes code at the hardware level.

**Key Use Cases**:

- **OS Kernels**: Bootloaders and low-level hardware drivers.
- **Performance Tuning**: Manually optimizing the inner loops of high-speed code.
- **Reverse Engineering**: Analyzing malware or closed-source binaries.

**Pros & Cons**:

- **Pros**: Total control over hardware; zero overhead; fastest possible execution when written correctly.
- **Cons**: Extremely tedious to write; not portable between different CPUs; incredibly difficult to debug and maintain.

---

### 38. Visual Basic .NET

**File**: `src/038_hello_visualbasic.vb`

```vb
Module Module1
    Sub Main()
        Console.WriteLine("Hello World")
    End Sub
End Module
```

**Technical Profile**:

- **Developer/Origin**: Microsoft (2001).
- **Paradigm**: Object-oriented.
- **Typing**: Static, Strong.
- **Runtime/Platform**: .NET.

**The Story & Purpose**:
VB.NET was created as the successor to Visual Basic 6.0, transitioning it to the powerful .NET framework. It was designed to keep the "easy-to-read" English-like syntax of BASIC while providing the full modern capabilities of C#.

**Key Use Cases**:

- **Legacy Enterprise Maintenance**: Supporting internal tools built in the early 2000s.
- **Rapid Application Development**: Building simple CRUD desktop apps quickly.

**Pros & Cons**:

- **Pros**: Very easy for beginners to read; full access to everything in the .NET ecosystem; great IDE support.
- **Cons**: Declining popularity; perceived as "second-class" compared to C#; verbose syntax can make complex code cluttered.

---

### 39. Objective-C

**File**: `src/039_hello_objectivec.m`

```objectivec
#import <Foundation/Foundation.h>
int main() {
    @autoreleasepool {
        NSLog(@"Hello World");
    }
    return 0;
}
```

**Technical Profile**:

- **Developer/Origin**: Brad Cox and Tom Love (1984), Stepstone.
- **Paradigm**: Object-oriented.
- **Typing**: Static/Dynamic, Strong.
- **Runtime/Platform**: Objective-C Runtime (C-based).

**The Story & Purpose**:
Objective-C added Smalltalk-style messaging to the C language. It was chosen by Steve Jobs for NeXT computers, which eventually became the foundation of macOS and iOS. It was the sole language for Apple development until the release of Swift.

**Key Use Cases**:

- **Legacy iOS/macOS Development**: Mantaining older apps built before 2014.
- **Systems Integration**: Bridging C code with higher-level Apple APIs.

**Pros & Cons**:

- **Pros**: Incredibly dynamic runtime; proven stability over decades; seamless integration with C and C++.
- **Cons**: Unusual messaging syntax (`[object message]`); manual memory management (pre-ARC) was difficult; rapidly being replaced by Swift.

---

### 40. Smalltalk

**File**: `src/040_hello_smalltalk.st`

```smalltalk
Transcript show: 'Hello World'; cr.
```

**Technical Profile**:

- **Developer/Origin**: Alan Kay, Dan Ingalls, Adele Goldberg (1972), Xerox PARC.
- **Paradigm**: Pure Object-Oriented.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: Smalltalk VM.

**The Story & Purpose**:
Smalltalk is the language that defined modern Object-Oriented Programming. It introduced the world to the Graphical User Interface (GUI), the mouse, and "live" development environments. In Smalltalk, _everything_ is an object, and programs are built by objects sending messages to each other.

**Key Use Cases**:

- **Educational Simulations**: Teaching OOP in its purest form.
- **Finance**: Used for complex risk modeling at firms like JP Morgan.
- **Research**: Prototyping new UI/UX concepts.

**Pros & Cons**:

- **Pros**: Purest implementation of OOP; allows for "live" modifications without restarting; highly influential on almost all modern languages.
- **Cons**: Requires a proprietary VM environment; unconventional syntax; very small commercial ecosystem today.

---

### 41. Tcl

**File**: `src/041_hello_tcl.tcl`

```tcl
puts "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: John Ousterhout (1988), University of California, Berkeley.
- **Paradigm**: Multi-paradigm (Procedural, Event-driven).
- **Typing**: Dynamic, String-based (everything is a string).
- **Runtime/Platform**: Tcl Interpreter.

**The Story & Purpose**:
Tcl (Tool Command Language) was designed to be an easily embeddable command language for interactive tools. It gained fame through its association with the Tk toolkit, which made creating cross-platform GUIs incredibly simple. Its philosophy is that "everything is a string," allowing for unique flexibility in parsing and script generation.

**Key Use Cases**:

- **GUI Development**: Using the Tk toolkit for desktop apps.
- **Electronic Design Automation (EDA)**: The standard for scripting in chip design tools.
- **Testing**: The Expect framework is used to automate interactive terminal sessions.

**Pros & Cons**:

- **Pros**: Extremely easy to learn and embed; powerful cross-platform GUI support; unique string-centric logic.
- **Cons**: "Everything is a string" can lead to performance overhead; lacks modern data structures found in Python or Ruby; declining mainstream popularity.

---

### 42. D

**File**: `src/042_hello_dlang.d`

```d
import std.stdio;
void main() {
    writeln("Hello World");
}
```

**Technical Profile**:

- **Developer/Origin**: Walter Bright (2001), Digital Mars.
- **Paradigm**: Multi-paradigm (Systems, OOP, Functional, Template).
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native (LLVM/GCC/DMD).

**The Story & Purpose**:
D was created to fix the perceived frustrations of C++ while maintaining its power. It provides the low-level efficiency of C++ but adds modern features like a garbage collector (optional), powerful metaprogramming, and a simplified module system. It is often described as "C++ done right."

**Key Use Cases**:

- **High-Performance Systems**: Backend services and data processing.
- **Game Engines**: Alternative to C++ for game logic.
- **Metaprogramming**: Using "Templates" to generate code at compile-time.

**Pros & Cons**:

- **Pros**: Extremely powerful template system; performance equal to C++; faster compilation than C++.
- **Cons**: Fragmented standard library history (Phobos vs. Tango); competition from Go and Rust has limited its growth; smaller ecosystem of third-party libraries.

---

### 43. Vimscript

**File**: `src/043_hello_vimscript.vim`

```vim
echo "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Bram Moolenaar (1991).
- **Paradigm**: Imperative, Event-driven.
- **Typing**: Dynamic, Weak.
- **Runtime/Platform**: Vim/Neovim editor.

**The Story & Purpose**:
Vimscript is the language used to configure and extend the Vim text editor. It was never intended to be a general-purpose language, but as Vimmers built more complex plugins, the language grew in complexity. It provides the logic behind thousands of themes, syntax highlighters, and navigation tools.

**Key Use Cases**:

- **Vim Plugins**: Extending editor functionality.
- **Configuration**: Standardizing terminal workflow through `.vimrc`.

**Pros & Cons**:

- **Pros**: Essential for anyone who wants to fully customize the Vim experience; built-in support for text manipulation and editor state.
- **Cons**: Awkward, inconsistent syntax; performance is slow; being largely replaced by Lua in the Neovim community.

---

### 44. Emacs Lisp

**File**: `src/044_hello_emacslisp.el`

```elisp
(message "Hello World")
```

**Technical Profile**:

- **Developer/Origin**: Richard Stallman (1985).
- **Paradigm**: Lisp (Functional/Procedural).
- **Typing**: Dynamic.
- **Runtime/Platform**: Emacs editor.

**The Story & Purpose**:
Emacs Lisp (Elisp) is the soul of the GNU Emacs editor. Emacs is essentially a Lisp runtime that happens to be an editor. Almost every feature in Emacs—from the text display to the project management—is written in Elisp, allowing users to rewrite the editor while it’s running.

**Key Use Cases**:

- **Emacs Customization**: Building "Org-mode," "Magit," and other legendary tools.
- **Workflow Automation**: Scripting personal productivity within the editor.

**Pros & Cons**:

- **Pros**: Incredible extensibility; live-coding environment; massive library of existing editor logic.
- **Cons**: Dynamic scoping by default (historically); performance can lag with heavy scripts; parentheses can be daunting for non-Lisp users.

---

### 45. PowerShell

**File**: `src/045_hello_powershell.ps1`

```powershell
Write-Host "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Jeffrey Snover (2006), Microsoft.
- **Paradigm**: Imperative, Object-oriented, Pipeline.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: .NET, PowerShell Core.

**The Story & Purpose**:
Unlike Bash, which pipes text, PowerShell pipes _objects_. Developed specifically for Windows administrators, it gives direct access to the .NET framework, WMI, and COM. It has since become cross-platform (PowerShell Core), providing a powerful automation tool for Linux and macOS as well.

**Key Use Cases**:

- **Windows System Administration**: Managing Active Directory, Registry, and Services.
- **Cloud Management**: Extensive support for Azure and AWS automation.
- **DevOps**: CI/CD pipelines in enterprise environments.

**Pros & Cons**:

- **Pros**: Object-based pipeline eliminates the need for string parsing (regex/awk/sed); incredible access to the Windows OS; powerful modern syntax.
- **Cons**: Verbose command names (e.g., `Get-ChildItem` vs `ls`); startup time is slower than Bash; perceived as "Windows-only" despite being cross-platform.

---

### 46. BASIC (GW-BASIC)

**File**: `src/046_hello_basic.bas`

```basic
10 PRINT "Hello World"
20 END
```

**Technical Profile**:

- **Developer/Origin**: John G. Kemeny and Thomas E. Kurtz (1964), Dartmouth College.
- **Paradigm**: Imperative.
- **Typing**: Static (mostly).
- **Runtime/Platform**: Various Interpreters/Compilers.

**The Story & Purpose**:
BASIC (Beginner's All-purpose Symbolic Instruction Code) was the entry point for the personal computer revolution. It was designed to be easy for non-science students to use. In the 70s and 80s, almost every home computer shipped with a version of BASIC (like GW-BASIC or Commodore BASIC) in ROM.

**Key Use Cases**:

- **Education**: Primary teaching language for three decades.
- **Hobbyist Coding**: Creating simple games and tools on 8-bit hardware.

**Pros & Cons**:

- **Pros**: Extremely simple syntax; interactive environment (line-by-line execution).
- **Cons**: Encourages "spaghetti code" via `GOTO` statements; slow execution; lacks modern structures for large-scale engineering.

---

### 47. Crystal

**File**: `src/047_hello_crystal.cr`

```crystal
puts "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Ary Borenszweig et al. (2014).
- **Paradigm**: Multi-paradigm (OOP, Functional).
- **Typing**: Static (with type inference), Strong.
- **Runtime/Platform**: Native (LLVM).

**The Story & Purpose**:
Crystal’s slogan is "Fast as C, Slick as Ruby." It was designed for developers who love Ruby’s beautiful syntax but need the performance and type safety of a compiled, statically-typed language. It features an advanced type inference system that makes it feel dynamic while providing compile-time checks.

**Key Use Cases**:

- **Web Backend**: High-performance servers (Kemal framework).
- **Systems Tools**: Writing fast CLI utilities.

**Pros & Cons**:

- **Pros**: Ruby-like elegance with C-like speed; powerful macro system; null safety built into the type system.
- **Cons**: Compilation times can be slow; relatively small ecosystem compared to Ruby or Go; no native Windows support for a long time (recently improved).

---

### 48. Nim

**File**: `src/048_hello_nim.nim`

```nim
echo "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Andreas Rumpf (2008).
- **Paradigm**: Multi-paradigm (Imperative, Functional, Meta).
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native (Compiles to C, C++, or JS).

**The Story & Purpose**:
Nim is a systems language that looks like Python but performs like C. Its superpower is that it doesn't compile directly to machine code; it generates C code first, which is then compiled by a standard compiler (gcc/clang). This makes it highly portable and allows for easy integration with existing C libraries.

**Key Use Cases**:

- **Systems Programming**: OS development and drivers.
- **Game Development**: Fast logic with clean syntax.
- **Web Frontend**: Via its backend that compiles to JavaScript.

**Pros & Cons**:

- **Pros**: Python-level readability with native performance; one of the best metaprogramming (Macro) systems; zero-cost abstractions.
- **Cons**: Small community and job market; toolchain can be complex; garbage collection behavior (though configurable) can be tricky for real-time systems.

---

### 49. AWK

**File**: `src/049_hello_awk.awk`

```awk
BEGIN { print "Hello World" }
```

**Technical Profile**:

- **Developer/Origin**: Aho, Weinberger, and Kernighan (1977), Bell Labs.
- **Paradigm**: Data-driven, Scripting.
- **Typing**: Dynamic.
- **Runtime/Platform**: Unix/Linux environments.

**The Story & Purpose**:
AWK is a domain-specific language designed for text processing and data extraction. It is named after its creators (A, W, and K). It operates on a record-and-field basis, making it the perfect tool for processing CSVs, log files, and structured text directly from the command line.

**Key Use Cases**:

- **Log Analysis**: Filtering and summarizing server logs.
- **Data Transformation**: Quick cleanup of text files.
- **One-liners**: Complex data manipulation in a single terminal command.

**Pros & Cons**:

- **Pros**: Standard on all Unix systems; incredibly concise for field-based text data; no compilation required.
- **Cons**: Difficult to maintain for complex programs; inconsistent versions (awk vs nawk vs gawk); syntax can be obtuse for beginners.

---

### 50. Sed

**File**: `src/050_hello_sed.sed`

```sed
s/.*/Hello World/p
```

**Technical Profile**:

- **Developer/Origin**: Lee E. McMahon (1974), Bell Labs.
- **Paradigm**: Stream-oriented Scripting.
- **Typing**: None.
- **Runtime/Platform**: Unix/Linux environments.

**The Story & Purpose**:
Sed (Stream Editor) is a non-interactive text editor. It takes a stream of text, applies a series of transformations (using regex), and outputs the result. It is the "Swiss Army Knife" of text manipulation in shell scripts. While it can technically be used for logic, it is primarily used for search-and-replace.

**Key Use Cases**:

- **Search and Replace**: Mass editing of files in scripts.
- **Data Cleanup**: Removing whitespace or specific characters from streams.

**Pros & Cons**:

- **Pros**: Extremely fast for text transformations; ubiquitous on Unix systems.
- **Cons**: Nearly unreadable syntax for complex tasks; limited logic capabilities; heavy reliance on Regex mastery.

---

### 51. Zig

**File**: `src/051_hello_zig.zig`

```zig
const std = @import("std");
pub fn main() void {
    std.debug.print("Hello World\n", .{});
}
```

**Technical Profile**:

- **Developer/Origin**: Andrew Kelley (2016).
- **Paradigm**: Imperative, Systems.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native (LLVM).

**The Story & Purpose**:
Zig is a modern systems language designed to replace C. It omits many hidden behaviors (like hidden allocations or preprocessors) in favor of total transparency. Its "Comptime" feature allows for powerful code transformation without the complexity of traditional macros or templates.

**Key Use Cases**:

- **Systems Engineering**: Writing kernels, drivers, and low-level engines.
- **C Replacement**: Seamlessly compiling existing C projects with the Zig toolchain.
- **WebAssembly**: High-performance WASM binaries.

**Pros & Cons**:

- **Pros**: No hidden control flow; incredible C interoperability; powerful "comptime" for generic programming.
- **Cons**: Still in beta (pre-1.0); breaking changes occur frequently; smaller library ecosystem than Rust.

---

### 52. V (Vlang)

**File**: `src/052_hello_vlang.v`

```v
fn main() {
    println('Hello World')
}
```

**Technical Profile**:

- **Developer/Origin**: Alexander Medvednikov (2019).
- **Paradigm**: Imperative, Structural.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Native (Compiles to C/JS/WASM).

**The Story & Purpose**:
V is a simple language inspired by Go, but with the aim of being even faster and safer. It claims to have a compiler so fast it can compile 1.2 million lines of code per second per core. It emphasizes small binary sizes and zero dependencies.

**Key Use Cases**:

- **Fast CLI Tools**: Utilities that need to be lightweight and portable.
- **UI Development**: Native UI library in development.

**Pros & Cons**:

- **Pros**: Lightning-fast compilation; very simple, readable syntax; no garbage collector (uses Autofree).
- **Cons**: Controversial history regarding fulfilled promises; lacks the maturity of Go or Rust; relatively small community.

---

### 53. Haxe

**File**: `src/053_hello_haxe.hx`

```haxe
class Main {
    static public function main() {
        trace("Hello World");
    }
}
```

**Technical Profile**:

- **Developer/Origin**: Nicolas Cannasse (2005).
- **Paradigm**: Multi-paradigm (OOP, Functional).
- **Typing**: Static, Strong, Inferred.
- **Runtime/Platform**: Transpiles to JS, C++, C#, Java, Python, PHP, Lua.

**The Story & Purpose**:
Haxe is a "multi-platform" language. It was designed to allow developers to write code once and compile it to target almost any environment (web, mobile, desktop, console). It is particularly popular in the indie game development scene.

**Key Use Cases**:

- **Game Development**: Powering games like _Dead Cells_ and _Friday Night Funkin'_.
- **Cross-Platform Apps**: Sharing logic between frontend, backend, and mobile.

**Pros & Cons**:

- **Pros**: Unmatched platform portability; very powerful type system; mature after 15+ years.
- **Cons**: "Jack of all trades" can lead to target-specific bugs; smaller community than the platforms it targets; can be difficult to find libraries that support _every_ target.

---

### 54. CoffeeScript

**File**: `src/054_hello_coffeescript.coffee`

```coffeescript
console.log "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Jeremy Ashkenas (2009).
- **Paradigm**: Multi-paradigm, Scripting.
- **Typing**: Dynamic.
- **Runtime/Platform**: Compiled to JavaScript.

**The Story & Purpose**:
CoffeeScript was designed to make JavaScript more readable by introducing Python and Ruby-like syntax (significant whitespace, no semicolons). It was enormously popular in the early 2010s and heavily influenced the development of ES6 (modern JavaScript).

**Key Use Cases**:

- **Legacy Web Development**: Maintaining older Rails and JS apps.
- **Inspiration**: Studying the evolution of modern JS syntax.

**Pros & Cons**:

- **Pros**: Very concise; beautiful syntax; influenced many great JS features.
- **Cons**: Mostly redundant now that modern JS (ES6+) has adopted its best ideas; adds a compilation step; community has largely moved on.

---

### 55. REXX

**File**: `src/055_hello_rexx.rexx`

```rexx
/* Hello World in REXX */
say "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Mike Cowlishaw (1979), IBM.
- **Paradigm**: Scripting, Procedural.
- **Typing**: Dynamic, String-based.
- **Runtime/Platform**: Mainframes, OS/2, Unix.

**The Story & Purpose**:
REXX (Restructured Extended Executor) was designed to be a scripting language that was easy for humans to read and write. It became the de facto standard for scripting on IBM mainframes and was later used as the system-wide macro language for OS/2.

**Key Use Cases**:

- **Mainframe Automation**: Automating tasks on z/OS.
- **Embedded Scripting**: Adding macro support to enterprise applications.

**Pros & Cons**:

- **Pros**: Extremely readable (designed for non-specialists); very robust; simplifies complex system commands.
- **Cons**: Niche outside of the IBM/Mainframe world; performance is lower than modern scripting languages like Python.

---

### 56. Icon

**File**: `src/056_hello_icon.icn`

```icon
procedure main()
    write("Hello World")
end
```

**Technical Profile**:

- **Developer/Origin**: Ralph Griswold (1977), University of Arizona.
- **Paradigm**: Imperative, Goal-directed.
- **Typing**: Dynamic.
- **Runtime/Platform**: Icon Interpreter.

**The Story & Purpose**:
Icon is a high-level language focused on string manipulation and complex data structures. Its most unique feature is "Goal-directed execution," where expressions can return multiple results and the language automatically backtracks to find a successful path.

**Key Use Cases**:

- **Natural Language Processing**: Early text analysis research.
- **Data Transformation**: Researching goal-driven logic.

**Pros & Cons**:

- **Pros**: Unique backtracking logic simplifies complex search problems; excellent string-handling.
- **Cons**: Niche academic language; performance isn't suitable for modern high-load systems.

---

### 57. Forth

**File**: `src/057_hello_forth.fth`

```forth
: HELLO ( -- )  ." Hello World" CR ;
HELLO
```

**Technical Profile**:

- **Developer/Origin**: Charles H. Moore (1970).
- **Paradigm**: Stack-oriented, Concatenative.
- **Typing**: None.
- **Runtime/Platform**: Native, Virtual Machine.

**The Story & Purpose**:
Forth is built around a data stack and RPN (Reverse Polish Notation). You define "words" (functions) by combining existing ones. It is incredibly lightweight and can be implemented in just a few hundred bytes of code, making it a favorite for bootloaders and space-constrained hardware.

**Key Use Cases**:

- **Embedded Systems**: Space probes (Voyager, Galileo) and hardware testing.
- **Bootloaders**: Minimal environments where every byte counts.
- **Industrial Control**: Real-time robotics.

**Pros & Cons**:

- **Pros**: Tiny footprint; extremely fast; "Interactive" hardware control.
- **Cons**: RPN syntax is difficult for most programmers; no type safety; "write-only" reputation due to stack manipulation complexity.

---

### 58. Factor

**File**: `src/058_hello_factor.factor`

```factor
"Hello World" print
```

**Technical Profile**:

- **Developer/Origin**: Slava Pestov (2003).
- **Paradigm**: Concatenative, Functional, OOP.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: Native.

**The Story & Purpose**:
Factor is a modern, feature-rich concatenative language. It takes the stack-based ideas of Forth but adds a garbage collector, an object system, and a powerful library ecosystem. It is designed to be highly productive while maintaining the unique power of stack-based programming.

**Key Use Cases**:

- **Research**: Studying concatenative paradigms.
- **Personal Projects**: Developers looking for a highly expressive, unique environment.

**Pros & Cons**:

- **Pros**: Much easier to use than Forth; high-level features like GC and Unicode support; great interactive environment.
- **Cons**: Stack-based logic remains a hurdle for many; niche community; smaller library selection.

---

### 59. J

**File**: `src/059_hello_j.ijs`

```j
echo 'Hello World'
```

**Technical Profile**:

- **Developer/Origin**: Kenneth E. Iverson and Roger Hui (1990).
- **Paradigm**: Array Programming, Functional.
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: J Interpreter.

**The Story & Purpose**:
J is a successor to APL. It maintains APL's incredible power for mathematical and array operations but uses standard ASCII characters instead of special symbols. It is extremely dense—programs that would take 100 lines in Java can often be written in a single line of J.

**Key Use Cases**:

- **Financial Analysis**: Complex operations on massive insurance or market data.
- **Mathematical Modeling**: High-level statistical research.

**Pros & Cons**:

- **Pros**: Unmatched density and power for array operations; mathematically elegant.
- **Cons**: Extremely cryptic syntax ("Tacoless" programming); steep learning curve.

---

### 60. APL

**File**: `src/060_hello_apl.apl`

```apl
'Hello World'
```

**Technical Profile**:

- **Developer/Origin**: Kenneth E. Iverson (1966), IBM.
- **Paradigm**: Array Programming.
- **Typing**: Dynamic.
- **Runtime/Platform**: Mainframes, Dyalog APL.

**The Story & Purpose**:
APL (A Programming Language) is famous for its unique character set. It treats multi-dimensional arrays as its primary data structure. It was designed to accurately express mathematical notation in a computer language. Many APL programmers use special keyboards or keymaps to enter its symbols.

**Key Use Cases**:

- **Finance**: Used by firms like Morgan Stanley for complex calculations.
- **Mathematics**: Teaching high-level array theory.

**Pros & Cons**:

- **Pros**: Can express complex matrix math in seconds; extremely elegant for those who speak its "language."
- **Cons**: Requires special symbols/keyboards; essentially unreadable to the uninitiated; difficult to integrate with modern web/app stacks.

---

## Part 4: The Esoteric (61–80)

### 61. PostScript

**File**: `src/061_hello_postscript.ps`

```postscript
/Helvetica findfont 72 scalefont setfont
100 100 moveto
(Hello World) show
showpage
```

**Technical Profile**:

- **Developer/Origin**: John Warnock and Charles Geschke (1982), Adobe.
- **Paradigm**: Stack-oriented, Page Description.
- **Typing**: Dynamic.
- **Runtime/Platform**: Printers, Ghostscript.

**The Story & Purpose**:
PostScript is a Turing-complete language designed specifically for imaging and printing. It was the foundation of the desktop publishing revolution. When you print a document, your computer often sends a PostScript program to the printer, which then executes the code to render the graphics and text on the page.

**Key Use Cases**:

- **Printing**: High-quality document rendering.
- **Graphic Design**: Creating scalable vector graphics (EPS format).

**Pros & Cons**:

- **Pros**: Incredible precision for layout and typography; industry standard for professional printing.
- **Cons**: Stack-based logic is difficult for many; difficult to debug without specialized viewers; being largely superseded by PDF (though PDF is derived from it).

---

### 62. Mathematica (Wolfram Language)

**File**: `src/062_hello_mathematica.wls`

```wolfram
Print["Hello World"]
```

**Technical Profile**:

- **Developer/Origin**: Stephen Wolfram (1988), Wolfram Research.
- **Paradigm**: Multi-paradigm (Logic, Functional, Symbolic).
- **Typing**: Dynamic, Strong.
- **Runtime/Platform**: Wolfram Engine.

**The Story & Purpose**:
Wolfram Language is a highly advanced symbolic language. It is unique because it includes a massive built-in knowledge base (Wolfram|Alpha), allowing you to call functions for real-world data (like "current weather in London" or "GDP of Japan") directly in your code.

**Key Use Cases**:

- **Scientific Research**: Complex mathematical modeling and simulations.
- **Data Science**: High-level data visualization and analysis.
- **Education**: Primary tool for university-level mathematics.

**Pros & Cons**:

- **Pros**: Unmatched built-in knowledge base and high-level functions; beautiful notebook interface.
- **Cons**: Proprietary and expensive (though free versions exist for Raspberry Pi); steep learning curve for symbolic logic.

---

### 63. Gnuplot

**File**: `src/063_hello_gnuplot.gp`

```gnuplot
print "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Thomas Williams and Colin Kelley (1986).
- **Paradigm**: Command-driven Scripting.
- **Typing**: Dynamic.
- **Runtime/Platform**: Gnuplot.

**The Story & Purpose**:
Gnuplot is a portable command-line driven graphing utility. It was created to help scientists and students visualize mathematical functions and data interactively. It is famously used as the plotting backend for Octave and other analytical tools.

**Key Use Cases**:

- **Academic Research**: Creating high-quality graphs for papers.
- **Server-side Graphing**: Generating plots from data streams in Realtime.

**Pros & Cons**:

- **Pros**: Extremely fast and lightweight; supports a massive variety of output formats (SVG, PNG, PDF, TeX).
- **Cons**: Awkward syntax for complex layouts; not a general-purpose language; 3D plotting can be tricky.

---

### 4. Make

**File**: `src/064_hello_make.mk`

```make
hello:
@echo "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Stuart Feldman (1976), Bell Labs.
- **Paradigm**: Declarative, Logic-based.
- **Typing**: None.
- **Runtime/Platform**: Unix/Linux/macOS (GNU Make).

**The Story & Purpose**:
Make is a build automation tool that automatically determines which parts of a large program need to be recompiled. It uses a `Makefile` to define dependencies. Feldman received an ACM Software System Award for Make, which remains the backbone of C/C++ development environments today.

**Key Use Cases**:

- **Build Pipelines**: Automating the compilation of software.
- **Task Runner**: A simple way to group common terminal commands.

**Pros & Cons**:

- **Pros**: Ubiquitous on all systems; handles file dependencies perfectly; zero configuration required for simple tasks.
- **Cons**: "Tab-gate" (requires literal tabs, not spaces); brittle syntax can be difficult to debug; complex logic is hard to express.

---

### 65. CMake

**File**: `src/065_hello_cmake.cmake`

```cmake
message("Hello World")
```

**Technical Profile**:

- **Developer/Origin**: Ken Martin and Bill Hoffman (2000), Kitware.
- **Paradigm**: Declarative (Scripting).
- **Typing**: None.
- **Runtime/Platform**: Cross-platform.

**The Story & Purpose**:
CMake stands for "Cross-platform Make." It was created to generate native build files (like Makefiles or Visual Studio projects) from a single configuration. It has become the de facto standard for modern C++ project management.

**Key Use Cases**:

- **C/C++ Project Management**: Organizing large, cross-platform codebases.
- **Dependency Management**: Finding and linking external libraries.

**Pros & Cons**:

- **Pros**: Truly cross-platform; great for managing complex dependency chains; huge industry adoption.
- **Cons**: Syntax is widely considered messy and difficult; steep learning curve; "boilerplate" heavy for small projects.

---

### 66. bc

**File**: `src/066_hello_bc.bc`

```bc
print "Hello World\n"
quit
```

**Technical Profile**:

- **Developer/Origin**: Robert Morris and Lorinda Cherry (1975), Bell Labs.
- **Paradigm**: Imperative.
- **Typing**: Static (Numbers only).
- **Runtime/Platform**: Unix/Linux environments.

**The Story & Purpose**:
bc (Basic Calculator) is an arbitrary-precision mathematical scripting language. It is often used in shell scripts when Bash's built-in integer math isn't enough. It allows for calculations with hundreds of digits of precision.

**Key Use Cases**:

- **Shell Scripting**: Performing high-precision math in terminal tools.
- **Quick Math**: Portable command-line calculator.

**Pros & Cons**:

- **Pros**: Extremely lightweight; standard on Unix; arbitrary precision.
- **Cons**: Limited to mathematical tasks; unusual syntax for modern developers.

---

### 67. m4

**File**: `src/067_hello_m4.m4`

```m4
Hello World
```

**Technical Profile**:

- **Developer/Origin**: Brian Kernighan and Dennis Ritchie (1977), Bell Labs.
- **Paradigm**: Macro Processor.
- **Typing**: None.
- **Runtime/Platform**: Unix/Linux.

**The Story & Purpose**:
m4 is a general-purpose macro processor. It was designed to provide a better way to generate code for other languages (like C or Fortran). It is most famously used as a core component of the GNU Autoconf system, which helps make software portable between different Unix systems.

**Key Use Cases**:

- **Code Generation**: Generating boilerplate for compilers or build systems.
- **Autoconf**: Powering the `./configure` scripts used in many open-source projects.

**Pros & Cons**:

- **Pros**: Extremely powerful for text expansion; very lightweight.
- **Cons**: Syntax is incredibly cryptic and dangerous (e.g., matching quotes can be a nightmare); "write-once, never-read" reputation.

---

### 68. PureScript

**File**: `src/068_hello_purs.purs`

```purescript
module Main where
import Effect.Console (log)
main = log "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Phil Freeman (2013).
- **Paradigm**: Purely Functional.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Compiled to JavaScript.

**The Story & Purpose**:
PureScript brings the power and safety of Haskell to the web browser. It is a strictly typed, purely functional language that compiles to human-readable JavaScript. It aims to eliminate runtime errors through a robust type system, similar to Elm but with more advanced features (like Row Polymorphism).

**Key Use Cases**:

- **Reliable Web Apps**: Applications where data correctness and safety are paramount.
- **Functional Research**: Bringing advanced FP concepts to the frontend.

**Pros & Cons**:

- **Pros**: Haskell-like power on the web; no runtime exceptions; very powerful type system.
- **Cons**: Steep learning curve (Monads, ADTs); small ecosystem compared to TypeScript; build times can be slow.

---

### 69. Brainfuck

**File**: `src/069_hello_brainfuck.bf`

```python
# python3 -c 'print("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.")'
```

**Technical Profile**:

- **Developer/Origin**: Urban Müller (1993).
- **Paradigm**: Esoteric, Minimalist.
- **Typing**: None.
- **Runtime/Platform**: Minimalist Virtual Machine (Data pointer and 8 commands).

**The Story & Purpose**:
Brainfuck was created to be the smallest possible Turing-complete compiler. The entire language consists of only 8 characters: `>`, `<`, `+`, `-`, `.`, `,`, `[`, and `]`. It is a pure challenge for programmers—a way to prove that you can write logic using the absolute bare minimum set of operations.

**Key Use Cases**:

- **Coding Challenges**: Proving mastery of low-level memory logic.
- **Academic Research**: Studying the limits of Turing completeness.

**Pros & Cons**:

- **Pros**: The ultimate minimalist language; pure intellectual puzzle.
- **Cons**: Explicitly designed to be difficult to read and write; zero practical utility; mentally taxing.

---

### 70. ArnoldC

**File**: `src/070_hello_arnoldc.arnoldc`

```arnoldc
IT'S SHOWTIME
TALK TO THE HAND "Hello World"
YOU HAVE BEEN TERMINATED
```

**Technical Profile**:

- **Developer/Origin**: Lauri Hartikka (2014).
- **Paradigm**: Imperative, Joke-based.
- **Typing**: Dynamic.
- **Runtime/Platform**: JVM.

**The Story & Purpose**:
ArnoldC is an esoteric language where the commands are replaced by famous quotes from Arnold Schwarzenegger movies. For example, `IT'S SHOWTIME` starts the program, and `TALK TO THE HAND` prints to the console. It was created purely for humor and to celebrate 80s action cinema.

**Key Use Cases**:

- **Fun & Education**: Introducing people to programming concepts in a hilarious way.
- **Memes**: It’s the ultimate "macho" programming language.

**Pros & Cons**:

- **Pros**: Hilarious; strangely readable for fans of Arnold's movies.
- **Cons**: Extremely verbose; limited functionality; not suitable for professional work.

### 71. LOLCODE

**File**: `src/071_hello_lolcode.lol`

```lolcode
HAI 1.2
    VISIBLE "Hello World"
KTHXBYE
```

**Technical Profile**:

- **Developer/Origin**: Adam Lindsay (2007).
- **Paradigm**: Esoteric, Meme-based.
- **Typing**: Dynamic.
- **Runtime/Platform**: Various Interpreters (LCI, PLOL).

**The Story & Purpose**:
LOLCODE is an esoteric programming language inspired by lolspeak, the language of the "lolcat" internet meme. It was created to see if a functional language could be built using only the vocabulary of cat memes. Commands include `HAI` (start), `KTHXBYE` (end), and `VISIBLE` (print).

**Key Use Cases**:

- **Humor & Community**: A fun way for developers to engage with internet culture.
- **Education**: Teaching basic block structure using funny terms.

**Pros & Cons**:

- **Pros**: Highly memorable; brings a smile to programmers' faces.
- **Cons**: Extremely silly; zero practical utility; difficult to manage complex logic.

---

### 72. Rockstar

**File**: `src/072_hello_rockstar.rock`

```rockstar
Say "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Dylan Beattie (2018).
- **Paradigm**: Esoteric, Narrative.
- **Typing**: Dynamic.
- **Runtime/Platform**: Rockstar Interpreter (transpiles to JS/Python/C#).

**The Story & Purpose**:
Rockstar was designed to create programs that look like 80s power ballads. Its purpose is to confuse project managers and recruitment bots who search for "Rockstar Developers." In Rockstar, you don't write code; you write lyrics. Variables are often poetic descriptions, and math is performed through lyrical comparisons.

**Key Use Cases**:

- **Fun**: Writing "lyrical" solutions to coding problems.
- **Confusing Recruitment Bots**: Literally becoming a "Rockstar Developer."

**Pros & Cons**:

- **Pros**: Unique and creative; technically Turing-complete.
- **Cons**: Very verbose; purely a "joke" language.

---

### 73. Chef

**File**: `src/073_hello_chef.chef`

```chef
cat << 'EOF'
Hello World Souffle.

Ingredients.
72 g H
101 g e
108 g l
108 g l
111 g o
32 g space
87 g W
111 g o
114 g r
108 g l
100 g d
33 g !

Method.
Put H into mixing bowl.
Put e into mixing bowl.
Put l into mixing bowl.
Put l into mixing bowl.
Put o into mixing bowl.
Put space into mixing bowl.
Put W into mixing bowl.
Put o into mixing bowl.
Put r into mixing bowl.
Put l into mixing bowl.
Put d into mixing bowl.
Put ! into mixing bowl.
Liquefy contents of the mixing bowl.
Pour contents of the mixing bowl into the baking dish.

Serves 1.
EOF
```

**Technical Profile**:

- **Developer/Origin**: David Morgan-Mar (2002).
- **Paradigm**: Esoteric, Recipe-based.
- **Typing**: Stack-based (Values are ingredients).
- **Runtime/Platform**: Chef Interpreter.

**The Story & Purpose**:
Chef programs are designed to look like cooking recipes. Variables are ingredients (e.g., "72g of sugar"), and the stack is a mixing bowl. The primary design goal was that the code should not only be a valid program but also reasonably plausible as a recipe.

**Key Use Cases**:

- **Puzzle Solving**: Can you write code that actually sounds like a good meal?
- **Artistic Programming**: Merging culinary arts with computer science.

**Pros & Cons**:

- **Pros**: Highly creative; incredibly fun to read.
- **Cons**: Extremely verbose; requires constant mental mapping between food and data.

---

### 74. Shakespeare (SPL)

**File**: `src/074_hello_shakespeare.spl`

```bash
cat << 'EOF'
The Infamous Hello World Program.

Romeo, a young man with a remarkable patience.
Juliet, a likewise young woman of remarkable grace.

                    Act I: Hamlet's Speeches.
                    Scene I: The Setup.
[Enter Romeo and Juliet]
Romeo: You are as beautiful as the sun! (sets Juliet to 72)
Juliet: Speak your mind. (prints out the character in Juliet)
...
[Exit Romeo]
EOF
```

**Technical Profile**:

- **Developer/Origin**: Adam Lindsay (2007).
- **Paradigm**: Esoteric, Play-based.
- **Typing**: Variable-based (Characters represent values).
- **Runtime/Platform**: SPL to C Transpiler.

**The Story & Purpose**:
The Shakespeare Programming Language (SPL) makes your code look like a Shakespearean play. Characters on stage are variables, and their values are modified through insults and compliments. It was designed to be as "un-program-like" as possible by using the language of 16th-century drama.

**Key Use Cases**:

- **Theater/Arts**: A fun crossover for fans of literature.
- **Education**: Demonstrating that syntax can be anything you imagine.

**Pros & Cons**:

- **Pros**: The most "literary" language ever created; hilariously dramatic.
- **Cons**: Massive file sizes for simple tasks; extremely difficult to debug "emotional" variables.

---

### 75. Chicken

**File**: `src/075_hello_chicken.chicken`

```python
# python3 -c 'print("chicken " * 500)'
```

**Technical Profile**:

- **Developer/Origin**: Dylan Beattie (2018).
- **Paradigm**: Esoteric, Minimalist.
- **Typing**: None.
- **Runtime/Platform**: Chicken Interpreter.

**The Story & Purpose**:
Chicken is a language where the only valid keyword is the word "chicken." The number of "chickens" on each line corresponds to a different opcode in its virtual machine. It was inspired by a parody scientific presentation that consisted entirely of the word "Chicken."

**Key Use Cases**:

- **Satire**: Poking fun at overly complex language specifications.
- **Challenge**: Trying to count hundreds of "chickens" without going insane.

**Pros & Cons**:

- **Pros**: Purely satirical; easy to "spell."
- **Cons**: Impossible for a human to read without a counter; zero practical value.

---

### 76. Whitespace

**File**: `src/076_hello_whitespace.ws`

```python
# python3 -c 'print("\t\n\t\n \t\t  \t \n\t\n \t\t\t\t  \n\t\n \t\t\t\t\t  \n\t\n \t\t\t\t\t  \n\t\n \t\t\t\t\t\t\t\n\t\n \t \t \n\t\n \t\t \t\t\t \n\t\n \t\t\t\t\t\t\t\n\t\n \t\t\t\t\t\t\n\t\n \t\t\t\t\t  \n\t\n \t\t\t\t  \n\t\n \t \t! \n\t\n\n\n")'
```

**Technical Profile**:

- **Developer/Origin**: Edwin Brady and Chris Morris (2003).
- **Paradigm**: Esoteric, Invisible.
- **Typing**: Stack-based.
- **Runtime/Platform**: Whitespace Interpreter.

**The Story & Purpose**:
Whitespace is a language that ignores all non-whitespace characters. Space, Tab, and Newline are the only valid commands. It was designed to demonstrate that the choice of "tokens" is arbitrary. A Whitespace program can be hidden inside the indentation of another language's source code.

**Key Use Cases**:

- **Steganography**: Hiding code in plain sight inside text files.
- **April Fools Jokes**: Giving a "blank" file to a confused developer.

**Pros & Cons**:

- **Pros**: Truly invisible; unique stack-based logic.
- **Cons**: Requires a specialized editor/viewer to even see the code; incredibly hard to debug.

---

### 77. Befunge

**File**: `src/077_hello_befunge.befunge`

```befunge
 >              v
@,,,,,,,,,,,,"Hello World" <
```

**Technical Profile**:

- **Developer/Origin**: Chris Pressey (1993).
- **Paradigm**: Esoteric, Two-dimensional.
- **Typing**: None.
- **Runtime/Platform**: Befunge-93/98 Interpreter.

**The Story & Purpose**:
Befunge is a unique two-dimensional language. The instruction pointer moves across a grid of code. Commands can change the pointer’s direction (up, down, left, right), allowing for loops and logic to be expressed through physical layout. It was designed to be as difficult to compile as possible.

**Key Use Cases**:

- **Visual Logic**: Building code that looks like a maze.
- **Puzzle Games**: Designing levels that are also valid programs.

**Pros & Cons**:

- **Pros**: Fascinating visual flow; pure creativity in layout.
- **Cons**: Extremely difficult to mentally trace long programs; non-linear flow makes it very hard to read.

---

### 78. Piet

**File**: `src/078_hello_piet.piet`

**Note**: This is an image file.

**Technical Profile**:

- **Developer/Origin**: David Morgan-Mar (2001).
- **Paradigm**: Esoteric, Graphical.
- **Typing**: Color-based.
- **Runtime/Platform**: Piet Interpreter (reads PNG/GIF files).

**The Story & Purpose**:
Named after the abstract artist Piet Mondrian, Piet code consists of bitmaps that look like abstract art. Logic is determined by the "hue" and "lightness" transitions between adjacent pixels. A program in Piet is literally a work of art.

**Key Use Cases**:

- **Artistic Synthesis**: Creating beautiful images that are also functional software.
- **Mystery**: Sharing code that looks like a 1x1 pixel or a complex canvas.

**Pros & Cons**:

- **Pros**: The most beautiful programming language; unique graphical logic.
- **Cons**: Requires image editing tools to write; extremely difficult to implement complex algorithms.

---

### 79. Omcrofl

**File**: `src/079_hello_omgrofl.omgrofl`

```omgrofl
lol n00b iiz 72
rofl n00b
...
stfu
```

**Technical Profile**:

- **Developer/Origin**: Juraj Borza (2006).
- **Paradigm**: Esoteric, L33t-speak.
- **Typing**: Variable-based.
- **Runtime/Platform**: Omgrofl Interpreter.

**The Story & Purpose**:
Omcrofl (Oh My God, ROFL) is a language based on 2000s "Internet Slang." Variables must be named after L33t terms (like `n00b` or `pwned`), and the control flow uses phrases like `w00t` and `stfu`. It captures the "gamer" culture of the early web.

**Key Use Cases**:

- **Retro Charm**: A time capsule of early 2000s internet culture.

**Pros & Cons**:

- **Pros**: Nostalgic and funny for those who grew up in that era.
- **Cons**: Highly specific slang; limited functionality.

---

### 80. TrumpScript

**File**: `src/080_hello_trumpscript.tr`

```trumpscript
say "Hello World"
America is great.
```

**Technical Profile**:

- **Developer/Origin**: Sam Shadwell et al. (2016), Rice University.
- **Paradigm**: Esoteric, Political Satire.
- **Typing**: Strong (it only likes large numbers).
- **Runtime/Platform**: Python-based interpreter.

**The Story & Purpose**:
Created during the 2016 election, TrumpScript is a satirical language based on Donald Trump's rhetoric. It has unique rules: no floating-point numbers (only whole integers, because "we only make whole deals"), no import statements (all code must be "homegrown"), and every program must end with "America is great."

**Key Use Cases**:

- **Political Satire**: A coding-based commentary on political style.
- **Social Commentary**: Demonstrating how language rules can reflect ideology.

**Pros & Cons**:

- **Pros**: Extremely topical and funny rule set.
- **Cons**: Crashing is frequent (it doesn't like losing); purposefully restrictive rules make it almost impossible to use for anything useful.

---

## Part 5: The Difficult & Ridiculous (81–100)

### 81. Hodor

**File**: `src/081_hello_hodor.hodor`

```python
# python3 -c 'print("Hodor! " * 20)'
```

**Technical Profile**:

- **Developer/Origin**: Various (inspired by Game of Thrones).
- **Paradigm**: Esoteric, Minimalist.
- **Typing**: None.
- **Runtime/Platform**: Hodor Interpreter.

**The Story & Purpose**:
Hodor is a language inspired by the character Hodor from _Game of Thrones_. Similar to the Chicken language, the only valid word is "Hodor" (though it can be "hodor", "HODOR", or "Hodor!"). The specific combination and punctuation determine the logic. It’s a tribute to a character who only ever said one word.

**Key Use Cases**:

- **Fan Art**: A digital tribute to George R. R. Martin's universe.
- **Comedy**: Writing code that literally says nothing but "Hodor."

**Pros & Cons**:

- **Pros**: Fun for fans of the show; very simple vocabulary.
- **Cons**: Completely unreadable logic; zero practical use.

---

### 82. Ook!

**File**: `src/082_hello_ook.ook`

```python
# python3 -c 'print("Ook. Ook? " * 50)'
```

**Technical Profile**:

- **Developer/Origin**: David Morgan-Mar (2002).
- **Paradigm**: Esoteric, Minimalist.
- **Typing**: None.
- **Runtime/Platform**: Ook! Interpreter (equivalent to Brainfuck).

**The Story & Purpose**:
Ook! is a joke language designed for orangutans. It is a one-to-one mapping of Brainfuck, but replacing the 8 punctuation marks with combinations of "Ook.", "Ook?", and "Ook!". The goal was to create a language that an orangutan could understand (according to Terry Pratchett's _Discworld_ logic).

**Key Use Cases**:

- **Pratchett Tributes**: Celebrating the Librarian of Unseen University.
- **Brainfuck Variants**: A slightly more "vocal" version of minimalist logic.

**Pros & Cons**:

- **Pros**: Funny concept; directly compatible with Brainfuck logic.
- **Cons**: Even more verbose than Brainfuck; repetitive to type.

---

### 83. INTERCAL

**File**: `src/083_hello_intercal.i`

```intercal
DO ,1 <- #13
PLEASE DO ,1 SUB #1 <- #238
PLEASE DO ,1 SUB #2 <- #108
...
PLEASE GIVE UP
```

**Technical Profile**:

- **Developer/Origin**: Don Woods and James M. Lyon (1972).
- **Paradigm**: Esoteric, Parody.
- **Typing**: Static (Bits).
- **Runtime/Platform**: C-INTERCAL.

**The Story & Purpose**:
INTERCAL (Compiler Language With No Pronounceable Acronym) was created to parody the languages of the 60s (like Fortran and COBOL). It is intentionally designed to be frustrating. For example, you must use the word `PLEASE` occasionally—if you don't use it enough, the compiler thinks you're rude and fails; if you use it too much, it thinks you're groveling and also fails.

**Key Use Cases**:

- **Historical Parody**: Understanding the "anti-design" philosophy of the 70s.
- **Masochism**: Programmers who enjoy fighting their compiler.

**Pros & Cons**:

- **Pros**: The original joke language; historically significant.
- **Cons**: Intentionally illogical; nearly impossible to learn; syntax is a headache by design.

---

### 84. False

**File**: `src/084_hello_false.f`

```false
"Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Wouter van Oortmerssen (1993).
- **Paradigm**: Esoteric, Stack-oriented.
- **Typing**: None.
- **Runtime/Platform**: False Interpreter.

**The Story & Purpose**:
False was the inspiration for Brainfuck. It aimed to be a functional, extremely minimalist stack-based language with a tiny compiler (only 1KB!). It uses single-character commands and is designed for extreme density.

**Key Use Cases**:

- **Inspiration**: Studying the direct ancestor of Brainfuck.
- **Density**: Writing complex logic in a handful of characters.

**Pros & Cons**:

- **Pros**: Incredibly compact; fast execution for its size.
- **Cons**: Obscure syntax (mostly punctuation); very hard to read.

---

### 85. Malbolge

**File**: `src/085_hello_malbolge.mal`

```bash
# Generation Command:
# python3 -c 'print("(=<`#9]~6ZY327Uv4-Qsqpnmjgfedcba`_^]\\[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9876543210/.-,+*)(\x27&%$# \"! \x1f\x1e\x1d\x1c\x1b\x1a\x19\x18\x17\x16\x15\x14\x13\x12\x11\x10\x0f\x0e\x0d\x0c\x0b\x0a\x09\x08\x07\x06\x05\x04\x03\x02\x01\x00")'
```

**Technical Profile**:

- **Developer/Origin**: Ben Olmstead (1998).
- **Paradigm**: Esoteric, Self-modifying.
- **Typing**: None.
- **Runtime/Platform**: Malbolge Interpreter.

**The Story & Purpose**:
Named after the eighth circle of Hell in Dante's _Inferno_, Malbolge was designed to be impossible to write. It is self-modifying, meaning every time a command is executed, it changes into a different command. The first "Hello World" program wasn't even written by a human—it was found by an evolutionary algorithm searching through random code.

**Key Use Cases**:

- **Cryptography**: Using its logic for obfuscation research.
- **Computational Limits**: Testing if an AI or algorithm can solve its code.

**Pros & Cons**:

- **Pros**: The most difficult language in human history; a true legend in computer science.
- **Cons**: Humanly impossible to write; code appears as gibberish; zero practical utility.

---

### 86. Zombie

**File**: `src/086_hello_zombie.zombie`

```zombie
summon
    shambler Hello
    say "Hello World"
animate
```

**Technical Profile**:

- **Developer/Origin**: David Morgan-Mar.
- **Paradigm**: Esoteric, Necromancy-based.
- **Typing**: Entity-based.
- **Runtime/Platform**: Zombie Interpreter.

**The Story & Purpose**:
In Zombie, your variables are "shamblers" or "ghosts" that you must "summon" and "animate." The language is designed to handle "undead" entities. If you don't manage your zombies correctly, they can "eat" your data or "haunt" your loops.

**Key Use Cases**:

- **Horror Fans**: Creating code with a spooky theme.
- **Creative Logic**: Managing resources as if they were fragile, dangerous entities.

**Pros & Cons**:

- **Pros**: Very atmospheric and creative syntax.
- **Cons**: Verbose; limited mathematical powers.

---

### 87. Cow

**File**: `src/087_hello_cow.cow`

```python
# python3 -c 'print("MoO " * 300)'
```

**Technical Profile**:

- **Developer/Origin**: Sean Heber (2003).
- **Paradigm**: Esoteric, Minimalist.
- **Typing**: None.
- **Runtime/Platform**: Cow Interpreter.

**The Story & Purpose**:
Cow is a language where every command is a variation of the word "moo" (e.g., `moO`, `mOo`, `MOo`, `mOO`). It is based on Brainfuck but adds more commands and state variables. It was created to see how much bovine humor one could fit into a Turing-complete language.

**Key Use Cases**:

- **Farm-themed Coding**: A lighthearted challenge for livestock enthusiasts.
- **Esoteric Research**: Advancing the logic of Brainfuck-like languages.

**Pros & Cons**:

- **Pros**: Simple and rhythmic syntax.
- **Cons**: Extremely repetitive; impossible to distinguish commands visually without a specialized highlighter.

---

### 88. Emojicode

**File**: `src/088_hello_emojicode.emojicode`

```emojicode
?? ??
  ?? ??Hello World??
??
```

**Technical Profile**:

- **Developer/Origin**: Theo Johansen (2014).
- **Paradigm**: Object-oriented, Esoteric.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Emojicode Real-Time Engine (ERT).

**The Story & Purpose**:
Emojicode is a high-level language where all keywords are emojis. Unlike most esoteric languages, it is actually quite powerful, featuring a full object-oriented system, optionals, and generics. It was designed to bring the expressiveness of emojis to the rigid world of programming.

**Key Use Cases**:

- **Mobile Development (Thematic)**: Writing logic using familiar icons.
- **Modern Education**: Making code feel more approachable for the "Emoji Generation."

**Pros & Cons**:

- **Pros**: Visually vibrant; surprisingly robust and feature-rich.
- **Cons**: Typing requires an emoji picker or constant copy-pasting; can be visually overwhelming for large projects.

---

### 89. Unlambda

**File**: `src/089_hello_unlambda.unl`

```unlambda
`r``..`..`..`..`..`..`..`..`..`..`..`..`..i
```

**Technical Profile**:

- **Developer/Origin**: David Madore (1999).
- **Paradigm**: Esoteric, Functional.
- **Typing**: None.
- **Runtime/Platform**: Unlambda Interpreter.

**The Story & Purpose**:
Unlambda is a functional programming language that is purposefully difficult. It has no variables and no lambda abstraction. Instead, it uses combinatory logic. It was designed to be as "anti-readable" as possible while remaining functional.

**Key Use Cases**:

- **Logic Theory**: Studying SKI combinators in a practical (if painful) way.
- **Mental Gymnastics**: Reconstructing fundamental logic from tiny building blocks.

**Pros & Cons**:

- **Pros**: Pure functional logic; no "hidden" state.
- **Cons**: Extremely difficult to mentally model; code appears as a string of backticks and single characters.

---

### 90. GolfScript

**File**: `src/090_hello_golfscript.gs`

```golfscript
"Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Darren Smith (2007).
- **Paradigm**: Esoteric, Stack-oriented.
- **Typing**: Dynamic.
- **Runtime/Platform**: GolfScript Interpreter.

**The Story & Purpose**:
GolfScript was designed explicitly for "Code Golfing"—the practice of writing programs in the fewest number of bytes possible. It uses single-character commands for almost everything. A program that solves a complex mathematical problem can often be written in just 10-20 characters.

**Key Use Cases**:

- **Code Golfing**: Competing in size-based challenges.
- **One-liners**: Writing incredibly dense terminal utilities.

**Pros & Cons**:

- **Pros**: The king of density; powerful stack operations.
- **Cons**: Practically impossible for a human to read without line-by-line documentation; very fragile syntax.

---

### 91. Haifu

**File**: `src/091_hello_haifu.hai`

```haifu
The sky is blue.
The sun is shining bright.
Hello World today.
```

**Technical Profile**:

- **Developer/Origin**: Various (Esoteric paradigm).
- **Paradigm**: Esoteric, Haiku-based.
- **Typing**: None.
- **Runtime/Platform**: Haifu Interpreter.

**The Story & Purpose**:
Haifu is an esoteric language where the source code must be a valid Haiku (5-7-5 syllable structure). The logic is derived from the "meaning" of the words and the structure of the poem. It was created to demonstrate that programming can be a form of poetry.

**Key Use Cases**:

- **Creative Writing**: Writing code that is literally a poem.
- **Academic Challenges**: Solving logic problems within strict syllable limits.

**Pros & Cons**:

- **Pros**: Beautiful and artistic.
- **Cons**: Extremely restrictive; impossible to write complex logic; syllable counting is technically difficult for an interpreter.

---

### 92. Glass

**File**: `src/092_hello_glass.glass`

```glass
{M [f (Hello World) o] m}
```

**Technical Profile**:

- **Developer/Origin**: Gregor Richards (2005).
- **Paradigm**: Esoteric, Object-oriented, Stack-based.
- **Typing**: Dynamic.
- **Runtime/Platform**: Glass Interpreter.

**The Story & Purpose**:
Glass is an esoteric language that combines object-oriented principles with a stack-based architecture. It is notoriously complex because every action requires a heavy amount of "hand-shaking" between objects and the stack. It was designed to be highly structured yet completely unreadable.

**Key Use Cases**:

- **Esoteric Research**: Studying the intersection of OOP and stack logic.

**Pros & Cons**:

- **Pros**: Technically robust for an esoteric language.
- **Cons**: Over-engineered by design; extremely verbose.

---

### 93. Hexagony

**File**: `src/093_hello_hexagony.hex`

```hexagony
  H ; e ; l ;
 l ; o ; W ; o ;
r ; l ; d ; ! ; @
```

**Technical Profile**:

- **Developer/Origin**: Martin Ender (2015).
- **Paradigm**: Esoteric, Two-dimensional.
- **Typing**: None.
- **Runtime/Platform**: Hexagony Interpreter.

**The Story & Purpose**:
Hexagony is a two-dimensional language where the code is laid out in a hexagonal grid. The instruction pointer moves in six possible directions. It is a more complex, hexagonal version of Befunge.

**Key Use Cases**:

- **Visual Puzzles**: Designing compact hexagonal logic.

**Pros & Cons**:

- **Pros**: Visually beautiful; extremely clever layout.
- **Cons**: Mentally exhausting to trace; very difficult to debug.

---

### 94. Dogescript

**File**: `src/094_hello_dogescript.doge`

```dogescript
shrobe console
plz console.loge with 'Hello World'
```

**Technical Profile**:

- **Developer/Origin**: Various.
- **Paradigm**: Esoteric, Meme-based.
- **Typing**: Dynamic.
- **Runtime/Platform**: Compiles to JavaScript.

**The Story & Purpose**:
Dogescript is a language that compiles to JavaScript, using the broken English ("much wow", "plz", "very") of the Doge meme. It was one of the first meme-languages to gain significant GitHub traction.

**Key Use Cases**:

- **Meme Development**: Writing JS with more "wow."
- **Intro to Transpilers**: A simple way to see how one language turns into another.

**Pros & Cons**:

- **Pros**: Much fun; very wow; easy to read for internet natives.
- **Cons**: Redundant (just JS with different keywords); limited life span of memes.

---

### 95. Zsh (Shell)

**File**: `src/095_hello_zsh.z`

```zsh
echo "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Paul Falstad (1990).
- **Paradigm**: Imperative, Shell.
- **Typing**: Dynamic.
- **Runtime/Platform**: Zsh.

**The Story & Purpose**:
Zsh (Z Shell) is an extended version of the Bourne Shell (sh) with many improvements, including better tab-completion and "globbing." It is now the default shell for macOS. It is highly compatible with Bash but adds many "power-user" features.

**Key Use Cases**:

- **Terminal Workflow**: Default interactive shell for developers.
- **Advanced Scripting**: Handling complex file patterns and completions.

**Pros & Cons**:

- **Pros**: Superior interactive features; highly customizable; compatible with Bash.
- **Cons**: Minor syntax differences with Bash can cause portability issues.

---

### 96. ABC

**File**: `src/096_hello_abc.abc`

```abc
WRITE "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Leo Geurts, Lambert Meertens, Steven Pemberton (1980s), CWI.
  ABC was designed to be a replacement for BASIC—easy for non-programmers to use but much more structured. It is most famous for being the direct predecessor to Python. Guido van Rossum worked on ABC and took many of its ideas (like indentation for blocks) to create Python.
- **Typing**: Static.
- **Runtime/Platform**: ABC Interpreter.

**The Story & Purpose**:
ABC was designed to be a replacement for BASIC—easy for non-programmers to use but much more structured. It is most famous for being the direct predecessor to Python. Guido van Rossum worked on ABC and took many of its ideas (like indentation for blocks) to create Python.

**Key Use Cases**:

- **Educational History**: Understanding the origins of Python.
- **Research**: Studying 80s ergonomic programming.

**Pros & Cons**:

- **Pros**: Clean and simple; very readable.
- **Cons**: High memory usage for the era; largely extinct now.

---

### 97. Vigil

**File**: `src/097_hello_vigil.vig`

```vigil
say "Hello World"
```

**Technical Profile**:

- **Developer/Origin**: Various (Joke paradigm).
- **Paradigm**: Moral Imperative.
- **Typing**: Strict.
- **Runtime/Platform**: Vigil Interpreter (Python-based).

**The Story & Purpose**:
Vigil is an esoteric language with a strict moral code. If your code contains an error or fails an assertion, Vigil "punishes" you by deleting your source file. It is the ultimate "high-stakes" programming language.

**Key Use Cases**:

- **Extreme Programming**: Testing your confidence in your code.
- **Humor**: The final boss of "strict" compilers.

**Pros & Cons**:

- **Pros**: Enforces 100% correctness by threat of deletion.
- **Cons**: Will literally delete your work if you make a typo; purely a joke.

---

### 98. B

**File**: `src/098_hello_b.b`

```b
main() {
  putchar('hell');
  putchar('o wo');
  putchar('rld\n');
}
```

**Technical Profile**:

- **Developer/Origin**: Ken Thompson and Dennis Ritchie (1969), Bell Labs.
- **Paradigm**: Imperative.
- **Typing**: Typeless (everything is a word).
- **Runtime/Platform**: PDP-7, PDP-11.

**The Story & Purpose**:
B was the transition between BCPL and C. It was used to develop early versions of the Unix operating system. It was "typeless" because it was designed for machines where everything was a single word. It introduced the `++` and `--` operators.

**Key Use Cases**:

- **Operating System History**: A must-study for systems researchers.

**Pros & Cons**:

- **Pros**: Influenced C; extremely fast for its time.
- **Cons**: Typelessness led to many errors on newer hardware; replaced by C almost immediately.

---

### 99. Algol 68

**File**: `src/099_hello_algol68.algol`

```algol
BEGIN
  print(("Hello World", newline))
END
```

**Technical Profile**:

- **Developer/Origin**: Adriaan van Wijngaarden et al. (1968), IFIP.
  Algol 68 was designed to be a rigorous, mathematically sound successor to Algol 60. It was extremely advanced, featuring operator overloading, user-defined types, and concurrency—concepts that wouldn't become mainstream for decades. It was unfortunately too complex for most compilers of the era.
- **Typing**: Static, Strong.
- **Runtime/Platform**: Various Mainframes.

**The Story & Purpose**:
Algol 68 was designed to be a rigorous, mathematically sound successor to Algol 60. It was extremely advanced, featuring operator overloading, user-defined types, and concurrency—concepts that wouldn't become mainstream for decades. It was unfortunately too complex for most compilers of the era.

**Key Use Cases**:

- **CS Theory**: Influenced almost all modern block-structured languages.
- **Academic Research**: Testing advanced type systems in the 70s.

**Pros & Cons**:

- **Pros**: Mathematically perfect specification; years ahead of its time.
- **Cons**: Extremely difficult to implement; considered "too complex" by the industry at the time.

---

### 100. I Use Arch Btw

**File**: `src/100_hello_i_use_arch_btw.arch`

```python
# python3 -c 'print("I use arch btw\n" * 1000)'
```

**Technical Profile**:

- **Developer/Origin**: The Internet (Memes).
- **Paradigm**: Esoteric, Linux-based.
- **Typing**: Strong.
- **Runtime/Platform**: Bash/Python script.

**The Story & Purpose**:
This is the final language in the collection, dedicated to the meme that Arch Linux users always feel the need to tell everyone they use Arch. It is a performance-art language that simply outputs the meme phrase repeatedly, reflecting the obsessive nature of the Linux community.

**Key Use Cases**:

- **Flexing**: Proving you installed Arch.
- **Memes**: The perfect conclusion to a 100-language repository.

**Pros & Cons**:

- **Pros**: 100% accurate to the meme.
- **Cons**: Verbose; annoying after the first three lines; zero utility.

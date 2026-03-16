-module(hello).
-export([main/1]).

main(_Args) ->
    io:fwrite("Hello World~n").

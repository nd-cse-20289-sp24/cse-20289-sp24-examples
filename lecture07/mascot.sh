#!/bin/sh

# Display appropriate cowsay based on operating system

case $(uname) in
    Darwin|*BSD)
    	cowsay -f daemon "$@"
    ;;
    Linux)
    	cowsay -f tux "$@"
    ;;
    *)
    	cowsay "$@"
    ;;
esac

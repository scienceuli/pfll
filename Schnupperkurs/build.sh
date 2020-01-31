#!/bin/bash

# Theme
theme=black

# Transition
transition="slide"

# Show Controls
controls="true"

# Display progress
progress="true"

# Input
input="slides.md"

# Output
output="index.html"

# Revealjs URL
revealjsurl="https://revealjs.com"

# Build
function build() {
	echo "Building slides to $output"
	pandoc -t revealjs \
	-V theme=$theme \
	-V transition=$transition \
	-V controls=$controls \
	-V progress=$progress \
	-V revealjs-url=$revealjsurl \
	-s $input -o $output
}

build

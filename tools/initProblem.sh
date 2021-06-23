#!/bin/bash
# requires bash4 support

LANGUAGES=(
    "C++=cpp"
    "Python3=py"
    "Java=java"
    "JavaScript=js"
    "Kotlin=kt"
    "Go=go"
    "Swift=swift"
    "Lua=lua"
)

parent_path="."
if [ ${PWD##*/} == "tools" ]; then 
    parent_path=".."
fi
q_path="$parent_path/problems/Q$1"

echo -e "Initialize problem $1 to path $q_path ."

# create folder
mkdir -p $q_path

# check markdown exists
md_path="$q_path/Q$1.md"
md_init=0
if [ ! -f $md_path ]; then
    md_init=1
    echo -e "# Q$1 {title} [link]()\n" > $md_path
    echo -e "| language   | file                           | runtime(ms) | memory(MB) |" >> $md_path
    echo -e "| ---------- | ------------------------------ | ----------- | ---------- |" >> $md_path
else
    echo "File $md_path already exists! SKIP"
fi

# write to markdown and create language files
for language in "${LANGUAGES[@]}"; do
    name="${language%%=*}"
    ext="${language##*=}"
    echo -e "Initialize for language $name with extension .$ext"

    if [ $md_init == 1 ]; then
        printf "| %-10s | %-30s | -           | -          |\n" $name "[Q$1.$ext](./Q$1.$ext)" >> $md_path
    fi 
    
    touch "$q_path/Q$1.$ext"
done
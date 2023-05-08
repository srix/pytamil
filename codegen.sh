#! /bin/bash

echo “${BASH_SOURCE:-$0}”

path=`readlink -f “${BASH_SOURCE:-$0}”`

DIR_PATH=`dirname $path`

echo ‘The absolute path is’ $path
echo ‘---------------------------------------------’
echo ‘The Directory Path is’ $DIR_PATH
echo $DIR_PATH/தமிழ்/codegen/


RESOURCE_PATH="$DIR_PATH/pytamil/தமிழ்/resources"
CODEGEN_PATH="$DIR_PATH/pytamil/தமிழ்/codegen"

# cd ./pytamil/தமிழ்/resources/
antlr4 -Dlanguage=Python3 $RESOURCE_PATH/மாத்திரை.g4 -o $CODEGEN_PATH
antlr4 -Dlanguage=Python3 $RESOURCE_PATH/வெண்பா.g4 -o $CODEGEN_PATH
antlr4 -Dlanguage=Python3 $RESOURCE_PATH/ஆசிரியப்பா.g4 -o $CODEGEN_PATH
antlr4 -Dlanguage=Python3 $RESOURCE_PATH/சீர்.g4 -o $CODEGEN_PATH
# antlr4 -Dlanguage=Python3 $RESOURCE_PATH/கலிப்பா.g4 -o $CODEGEN_PATH

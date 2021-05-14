#! /bin/bash

# bash showtree.sh [workspace folder] [grammar file basename] [grammar]
# bash showtree.sh /home/srix/workspace/pytamil வெண்பா.g4 வெண்பா 


shopt -s expand_aliases

WORKSPACE=$1
CURRENT_FILE_BASENAME=$2
ANTLR4_PATH="$WORKSPACE/tools/antlr-4.9.2-complete.jar" 
GRAMMAR_LIB_FOLDER="$WORKSPACE/pytamil/தமிழ்/resources"
GRAMMAR_FILE="$WORKSPACE/pytamil/தமிழ்/resources/$CURRENT_FILE_BASENAME"

# TEMPDIR="$WORKSPACE/tools/tempdir/"
TEMPDIR=$(mktemp -d -t showtree-$(date +%Y-%m-%d-%H-%M-%S)-XXXXXXXXXX)
GRAMMAR=$3
INPUT_TEXT="$WORKSPACE/pytamil/debug/வெண்பா-input.txt"


export CLASSPATH=".:$ANTLR4_PATH:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "$ANTLR4_PATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'

antlr4 -lib $GRAMMAR_LIB_FOLDER -o $TEMPDIR $GRAMMAR_FILE
cd $TEMPDIR

javac $GRAMMAR*.java 
grun $GRAMMAR $GRAMMAR -gui $INPUT_TEXT

rm -rf $TEMPDIR
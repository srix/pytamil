#!/usr/bin/env bash
# Regenerate the ANTLR parsers under pytamil/தமிழ்/codegen/ from the grammars in
# pytamil/தமிழ்/resources/. Requires Java. The jar version must match the
# antlr4-python3-runtime pin in requirements.txt.
set -euo pipefail

ANTLR_VERSION=4.13.2
DIR_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ANTLR_JAR="$DIR_PATH/tools/antlr-$ANTLR_VERSION-complete.jar"
RESOURCE_PATH="$DIR_PATH/pytamil/தமிழ்/resources"
CODEGEN_PATH="$DIR_PATH/pytamil/தமிழ்/codegen"

# Run from inside resources/ with relative paths so the "Generated from ..." header in
# every generated file is machine-independent. -lib lets `import சீர்;` resolve.
cd "$RESOURCE_PATH"
for grammar in மாத்திரை வெண்பா ஆசிரியப்பா சீர் புணர்ச்சிவிதிகள் சொல்; do
    echo "antlr4 $ANTLR_VERSION -> $grammar"
    java -jar "$ANTLR_JAR" -Dlanguage=Python3 -lib . -o "$CODEGEN_PATH" "$grammar.g4"
done

# கலிப்பா.g4 is a placeholder and does not compile yet; see specs/ roadmap.

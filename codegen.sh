#!/usr/bin/env bash
# Regenerate the ANTLR parsers under pytamil/தமிழ்/codegen/ from the grammars in
# pytamil/தமிழ்/resources/. Requires Java. The jar version must match the
# antlr4-python3-runtime pin in requirements.txt.
set -euo pipefail

DIR_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ANTLR_JAR="$DIR_PATH/tools/antlr-4.9.2-complete.jar"
RESOURCE_PATH="$DIR_PATH/pytamil/தமிழ்/resources"
CODEGEN_PATH="$DIR_PATH/pytamil/தமிழ்/codegen"

# -lib lets `import சீர்;` in வெண்பா.g4 / ஆசிரியப்பா.g4 resolve regardless of cwd.
for grammar in மாத்திரை வெண்பா ஆசிரியப்பா சீர் புணர்ச்சிவிதிகள் சொல்; do
    echo "antlr4 -> $grammar"
    java -jar "$ANTLR_JAR" -Dlanguage=Python3 -lib "$RESOURCE_PATH" \
        "$RESOURCE_PATH/$grammar.g4" -o "$CODEGEN_PATH"
done

# கலிப்பா.g4 is a placeholder and does not compile yet; see specs/ roadmap.

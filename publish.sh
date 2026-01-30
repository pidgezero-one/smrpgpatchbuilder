#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./release.sh patch
#   ./release.sh minor
#   ./release.sh major
#   ./release.sh 1.2.3

BUMP="${1:-patch}"
PYPROJECT="pyproject.toml"

if [[ ! -f "$PYPROJECT" ]]; then
  echo "ERROR: $PYPROJECT not found in current directory."
  exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: Not inside a git repository."
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "WARNING: Working tree is not clean (you have uncommitted changes)."
  echo "         This script will 'git add .' and commit them."
  echo
fi

# Extract current version from [project] section in a macOS-awk compatible way
CURRENT_VERSION="$(
  awk '
    BEGIN { in_project=0 }
    /^[[:space:]]*\[project\][[:space:]]*$/ { in_project=1; next }
    in_project && /^[[:space:]]*\[/ { in_project=0 }  # next table starts -> leave [project]
    in_project && /^[[:space:]]*version[[:space:]]*=[[:space:]]*"[0-9]+\.[0-9]+\.[0-9]+"/ {
      match($0, /"[0-9]+\.[0-9]+\.[0-9]+"/)
      v = substr($0, RSTART + 1, RLENGTH - 2)
      print v
      exit
    }
  ' "$PYPROJECT"
)"

if [[ -z "${CURRENT_VERSION:-}" ]]; then
  echo "ERROR: Could not find [project] version like: version = \"1.2.3\" in $PYPROJECT"
  exit 1
fi

# Compute new version
NEW_VERSION=""
if [[ "$BUMP" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  NEW_VERSION="$BUMP"
else
  IFS='.' read -r MA MI PA <<< "$CURRENT_VERSION"
  case "$BUMP" in
    patch) ((PA+=1)) ;;
    minor) ((MI+=1)); PA=0 ;;
    major) ((MA+=1)); MI=0; PA=0 ;;
    *)
      echo "ERROR: bump must be patch|minor|major|X.Y.Z (got: $BUMP)"
      exit 1
      ;;
  esac
  NEW_VERSION="${MA}.${MI}.${PA}"
fi

# Ensure tag doesn't already exist
if git rev-parse "v${NEW_VERSION}" >/dev/null 2>&1; then
  echo "ERROR: git tag v${NEW_VERSION} already exists."
  exit 1
fi

echo "Bumping version: ${CURRENT_VERSION} -> ${NEW_VERSION}"

# Edit pyproject.toml in-place: only update version inside [project]
NEW_VERSION="$NEW_VERSION" perl -0777 -i -pe '
  my $new = $ENV{NEW_VERSION} // die "NEW_VERSION not set\n";

  # Replace version inside the [project] table only.
  # This is a conservative multiline match: [project] ... version = "x.y.z"
  if (s/(\[project\][\s\S]*?\n\s*version\s*=\s*")(\d+\.\d+\.\d+)(")/$1$new$3/m) {
    # ok
  } else {
    die "version line not found under [project]\n";
  }
' "$PYPROJECT"

# rm -rf dist/
rm -rf dist/

# python -m build
python3 -m build

# git add .
git add .

# git commit -m "<version number>"
git commit -m "${NEW_VERSION}"

# git push
git push

# git tag v<version number>
git tag "v${NEW_VERSION}"

# git push origin v<version number>
git push origin "v${NEW_VERSION}"

# Twine upload (won't prompt if TWINE_USERNAME/TWINE_PASSWORD are set)
python3 -m twine upload dist/*

echo "Done: released ${NEW_VERSION}"

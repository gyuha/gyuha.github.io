#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DOCS_DIR="$ROOT_DIR/docs"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

if [ ! -d "$DOCS_DIR" ]; then
  echo "docs directory not found: $DOCS_DIR" >&2
  exit 1
fi

cp -R "$DOCS_DIR"/. "$TMP_DIR"/

paths=(
  "CNAME"
  "favicon.ico"
  "index.html"
  "index.json"
  "index.xml"
  "sitemap.xml"
  "assets"
  "categories"
  "css"
  "images"
  "img"
  "js"
  "page"
  "post"
  "search"
  "superpowers"
  "tags"
  "vendor"
  "video"
)

for path in "${paths[@]}"; do
  rm -rf "$ROOT_DIR/$path"
  if [ -e "$TMP_DIR/$path" ]; then
    cp -R "$TMP_DIR/$path" "$ROOT_DIR/$path"
  fi
done

echo "Mirrored docs output to repository root."

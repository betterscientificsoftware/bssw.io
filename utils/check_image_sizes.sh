#!/bin/bash
#
# Flag image files that are too large for the image service behind the bssw.io
# site.  The free Cloudinary account used by the site ignores files larger
# than 10 MB, and the only symptom is that the image does not show up on the
# site (see issue #2316).
#
# Run as:
#
#   ./utils/check_image_sizes.sh [-m|--max-bytes <n>] [-f|--fail] <file>...
#
# Each file larger than the limit is reported.  By default this only warns and
# exits 0; with --fail, it exits 1 if any file is over the limit.  Files that
# do not exist (e.g. deleted in a PR) are skipped.  When run under GitHub
# Actions, each oversized file is also reported as an annotation on the PR.
#

usage_str="Usage: check_image_sizes.sh [-m|--max-bytes <n>] [-f|--fail] <file>..."

# 10 MB, counted in decimal (a little under 10 MiB) so that borderline files
# are flagged rather than missed.
max_bytes=10000000
fail_on_oversize=0
files=()

while (( "$#" )); do
  case "$1" in
    -m|--max-bytes)
      if [[ ! "$2" =~ ^[0-9]+$ ]] ; then
        echo "Error: $1 requires a whole number of bytes, got '$2'" >&2
        echo "${usage_str}"
        exit 2
      fi
      max_bytes=$2
      shift 2
      ;;
    -f|--fail)
      fail_on_oversize=1
      shift
      ;;
    -h|--help)
      echo "${usage_str}"
      exit 0
      ;;
    --)
      shift
      files+=("$@")
      break
      ;;
    -*) # unsupported flags
      echo "Error: Unsupported flag $1" >&2
      echo "${usage_str}"
      exit 2
      ;;
    *)
      files+=("$1")
      shift
      ;;
  esac
done

if [[ "${fail_on_oversize}" == "1" ]] ; then
  annotation=error
else
  annotation=warning
fi

num_checked=0
num_oversize=0

for file in "${files[@]}" ; do
  if [[ ! -f "${file}" ]] ; then
    echo "Skipping missing file: ${file}"
    continue
  fi
  num_checked=$((num_checked+1))
  size=$(wc -c < "${file}")
  size=$((size+0))
  if (( size > max_bytes )) ; then
    num_oversize=$((num_oversize+1))
    msg="${file} is ${size} bytes, over the ${max_bytes} byte limit for images on the bssw.io site. It will not show up on the site; please reduce its size."
    echo "Too large: ${msg}"
    if [[ "${GITHUB_ACTIONS}" == "true" ]] ; then
      echo "::${annotation} file=${file},title=Image too large::${msg}"
    fi
    if [[ -n "${GITHUB_STEP_SUMMARY}" ]] ; then
      if (( num_oversize == 1 )) ; then
        echo "| Image over the ${max_bytes} byte limit | Size (bytes) |" >> "${GITHUB_STEP_SUMMARY}"
        echo "| --- | ---: |" >> "${GITHUB_STEP_SUMMARY}"
      fi
      echo "| \`${file}\` | ${size} |" >> "${GITHUB_STEP_SUMMARY}"
    fi
  fi
done

if (( num_oversize == 0 )) ; then
  echo "CHECK_IMAGE_SIZES: ALL PASSED (${num_checked} file(s) checked)"
  exit 0
fi

echo "CHECK_IMAGE_SIZES: ${num_oversize} of ${num_checked} file(s) over the ${max_bytes} byte limit"
if [[ "${fail_on_oversize}" == "1" ]] ; then
  exit 1
fi
exit 0

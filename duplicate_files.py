"""
/a/b/foo --> "potato"
/a/b/bar --> "carrot"
/a/c/baz --> "potato"
/a/c/quux --> "rutabega"
/a/d/xyzzy --> "carrot"
/e/f/asdf --> "potato"

def find_duplicate_files("/a") --> [["b/foo", "c/baz"], ["b/bar", "d/xyzzy"]]
"""

def find_duplicate_files(path):
    # Traverse the path for the files
    # Figure out if file is a duplicate
    

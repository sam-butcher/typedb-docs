## this filegroup exposes all .md files that are placed under the sub-directories of the root directory (where this BUILD file is located at)
## given the directory structure below, test-1.md and test-2.md are INCLUDED. test-0.md is EXCLUDED.
## root_directory:
##      test-0.md
##      sub-directory:
##          test-1.md
##          sub-sub-dir:
##              test-2.md

filegroup(
    name = "content",
    srcs = glob(
        ["*/**/*.md"],
        exclude=[
	    "bazel-*/**/*.md",
        ".runfiles/**/*.md"
        ]
    ),
    visibility = ["//visibility:public"]
)

filegroup(
    name = "template",
    srcs = glob(
        ["*/**/*.yml"],
        exclude=[
            "bazel-bin/**/*.yml",
            "bazel-out/**/*.yml",
            "bazel-docs/**/*.yml",
            ".runfiles/**/*.yml"
        ]
    ),
    visibility = ["//visibility:public"]
)

# CI targets that are not declared in any BUILD file, but are called externally
filegroup(
    name = "ci",
    data = [
        "@typedb_dependencies//tool/unuseddeps:unused-deps",
        "@typedb_dependencies//tool/release:docs",
    ],
)

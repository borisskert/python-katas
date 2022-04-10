import subprocess
import sys


def run_tests():
    result = subprocess.run(['python', '-m', 'unittest'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    errors = result.stderr.decode('utf-8')

    if "FAILED" in errors:
        print(errors)
        sys.exit(1)

    output = result.stdout.decode('utf-8')

    lines = output.split("\n")

    failed_lines = list(filter(has_failed, lines))

    if len(failed_lines) > 0:
        error_output = "\n".join(failed_lines)
        print(error_output)
        sys.exit(1)

    success_output = "\n".join(lines)
    print(success_output)
    sys.exit(0)


def has_failed(line):
    return "<FAILED::>" in line


if __name__ == "__main__":
    run_tests()

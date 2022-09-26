import subprocess

from db.path import file_path


def delete():
    subprocess.run(['rm', file_path])


if __name__ == '__main__':
    delete()

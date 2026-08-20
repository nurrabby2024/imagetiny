"""Minimal example for ImageTiny."""

from imagetiny import imagetiny


def main():
 runner = imagetiny({"name": "ImageTiny", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()
"""Python GPT Chatbot."""
import codecs
import re
from pathlib import Path

from setuptools import setup


def read(filename):
    """Read a text file."""
    file_path = Path(__file__).parent / filename
    return codecs.open(file_path, encoding="utf-8").read()


def find_meta(meta):
    """Extract __meta__ from META_FILE."""
    re_str = r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta)
    meta_match = re.search(re_str, META_FILE, re.M)
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError(f"Unable to find __{meta}__ string.")


PACKAGE_NAME = "chatbot"
META_FILE = read(Path(__file__).parent / PACKAGE_NAME / "__init__.py")

setup(
    name="Chatbot",
    version=find_meta("version"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    description="Python GPT Chatbot",
    url="https://github.com/DoranTech/chatbot",
    long_description=read("README.md"),
    packages=["chatbot"],
    install_requires=["openai"],
    python_requires=">=3.12",
    entry_points={"console_scripts": ["chatbot=chatbot.__main__:main"]},
)

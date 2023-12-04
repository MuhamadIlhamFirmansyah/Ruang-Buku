from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_desciption = f.read()

REPO_NAME = "Ruang Buku"
AUTHOR_USER_NAME = "Muhamad Ilham Firmansyah"
SRC_REPO = "src"
LIST_OF_REQUIRETMENT = ['streamlit', 'numpy']

setup(
    name=SRC_REPO,
    Version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description=long_desciption,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="entbappy73@gmail.com",
    packages=[SRC_REPO],
    python_requires=">=3.10.5",
    install_requires=LIST_OF_REQUIRETMENT
)

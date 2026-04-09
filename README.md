# Static Site Generator

A static site generator built in Python that converts Markdown files into a fully functional HTML website. It supports inline markdown (bold, italic, code, links, images) and block-level markdown (headings, paragraphs, quotes, code blocks, lists), and can deploy to GitHub Pages.

## What It Does

- Converts Markdown files into HTML pages using a template
- Supports bold, italic, inline code, links, and images
- Supports headings, paragraphs, blockquotes, code blocks, ordered and unordered lists
- Recursively generates pages from a `content/` directory into a `docs/` directory
- Copies static assets (CSS, images) into the output directory
- Configurable base path for GitHub Pages deployment

## Installation

Clone the project to your local machine:

```bash
git clone https://github.com/dimknife63/static-site.git
cd static-site
```

## Usage

### Run Tests

```bash
./test.sh
```

### Run Locally

```bash
./main.sh
```

Then open your browser and go to:

```
http://localhost:8888/
```

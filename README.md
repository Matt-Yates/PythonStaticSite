# PythonStaticSite

A lightweight static site generator written in Python. It takes Markdown content and an HTML template, and builds a ready-to-serve static website.

## How It Works

1. Content is written in Markdown and stored in the `content/` directory.
2. The `template.html` file defines the overall page layout.
3. The Python source in `src/` processes the content and template, generating HTML pages into a `public/` output directory.
4. Static assets (CSS, images, etc.) from the `static/` directory are copied directly into `public/`.

## Project Structure

```
PythonStaticSite/
├── content/        # Markdown content files
├── docs/           # Project documentation
├── src/            # Python source code
├── static/         # Static assets (CSS, images, etc.)
├── template.html   # HTML template used for page generation
├── build.sh        # Script to build the site
├── main.sh         # Script to run the generator
└── test.sh         # Script to run tests
```

## Usage

### Configuration

The generator accepts a single command-line argument to set the `basepath` of the site. This ensures that internal links and assets function correctly even when the site is hosted in a subdirectory (like GitHub Pages).

| Argument | Description | Default |
| :--- | :--- | :--- |
| `basepath` | The root URL path for all internal links and assets. | `/` |

### Usage

#### Local Development
For local testing, run the generator without any arguments. This builds the site with absolute paths starting from the root `/`.

#### Production / GitHub Pages
When deploying to GitHub Pages (e.g., `https://username.github.io/repo-name/`), provide your repository name as the `basepath`. This ensures that all internal links (`href`) and assets (`src`) are correctly rewritten to include the subdirectory.

```bash
python3 src/main.py "/repo-name/" 
```

## Requirements

- Python 3

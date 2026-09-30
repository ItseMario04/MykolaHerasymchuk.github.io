Massively by HTML5 UP
html5up.net | @ajlkn
Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)


This is Massively, a text-heavy, article-oriented design built around a huge background
image (with a new parallax implementation I'm testing) and scroll effects (powered by
Scrollex). A *slight* departure from all the one-pagers I've been doing lately, but one
that fulfills a few user requests and makes use of some new techniques I've been wanting
to try out. Enjoy it :)

Demo images* courtesy of Unsplash, a radtastic collection of CC0 (public domain) images
you can use for pretty much whatever.

(* = not included)

AJ
aj@lkn.io | @ajlkn


Notebook HTML exports:

Install the exporter once with:
	python -m pip install -r requirements-notebooks.txt

The VS Code folder-open task watches Python_code and exports each .ipynb file to
an HTML file with the same name. It preserves saved outputs and does not execute
notebook cells. To export all notebooks manually, run:
	python scripts/notebook_export.py

For a page, use a download link to the .ipynb and an iframe whose src points to
the matching .html file in Python_code. Keep both files in that folder.

Credits:

	Demo Images:
		Unsplash (unsplash.com)

	Icons:
		Font Awesome (fontawesome.io)

	Other:
		jQuery (jquery.com)
		Scrollex (github.com/ajlkn/jquery.scrollex)
		Responsive Tools (github.com/ajlkn/responsive-tools)
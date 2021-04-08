all: run_script command_line

run_script:
	python ../examples/example.py
	python assert_isfile.py mygraph
	rm mygraph

command_line:
	nx2tikz --input ../examples/example.py --output out.tex --format tikz
	python assert_isfile.py out.tex
	rm out.tex
	nx2tikz --input ../examples/example.py --output out --format pdf
	python assert_isfile.py out.pdf
	rm out.pdf
	nx2tikz --input ../examples/example.py --output out --format tex
	python assert_isfile.py out
	rm out

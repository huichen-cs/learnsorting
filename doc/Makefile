all: exercise.pdf

%.pdf: %.ps
	ps2pdf \
		-dPDFSETTINGS=/prepress \
		-dSubsetFonts=true \
		-dEmbedAllFonts=true \
		-dMaxSubsetPct=100 \
		-dCompatibilityLevel=1.4 $<

%.ps: %.dvi
	dvips $<

%.dvi: %.tex
	latex $<
#	bibtex $(basename $<)
	latex $<
	latex $<

hgid:
	hg identify --id > revision.tex

gitid:
	git rev-parse HEAD > revision.tex

clean:
	${RM} *.out *.snm *.aux *.nav *.toc *.dvi *.log *.ps *.vrb *.bbl *.blg


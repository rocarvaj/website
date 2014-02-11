# Converts all .md files in the current path into HTML
# using Markdown
##
# Rodolfo Carvajal, 2014

HTMLS := $(patsubst %.md,%.html,$(wildcard *.md))

all: $(HTMLS)

%.html: %.md
	./md/Markdown.pl $< > %.tmp
	mv %.tmp $@
